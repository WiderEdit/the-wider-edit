import { chromium, webkit } from 'playwright';
import assert from 'node:assert/strict';
import { mkdir, writeFile } from 'node:fs/promises';

const base='https://wideredit.github.io/the-wider-edit/';
const paths=['ru/','de/','ru/business/','de/business/'];
const results=[];
await mkdir('layout-report',{recursive:true});
let failed=false;

async function geometry(page) {
  return page.locator('.story-card').evaluateAll(cards=>cards.map(card=>{
    const frame=card.querySelector('.story-image');
    const img=frame.querySelector('img');
    const rect=frame.getBoundingClientRect();
    const title=card.querySelector('h2').getBoundingClientRect();
    const group=card.closest('.latest,.article-list');
    const anchor=group.matches('.latest')?group.querySelector(':scope > .eyebrow'):group.previousElementSibling;
    return {width:rect.width,height:rect.height,titleOffset:title.top-rect.top,
      leadGap:card===group.querySelector('.story-card')&&anchor?rect.top-anchor.getBoundingClientRect().bottom:null,
      textGap:title.top-rect.bottom,naturalWidth:img.naturalWidth,
      overflow:document.documentElement.scrollWidth-document.documentElement.clientWidth};
  }));
}

for(const [engine,type] of [['chromium',chromium],['webkit',webkit]]) {
  const browser=await type.launch();
  for(const path of paths) {
    const label=engine+'-'+path.replaceAll('/','-');
    const context=await browser.newContext({viewport:{width:390,height:844},deviceScaleFactor:1,isMobile:true,hasTouch:true});
    const page=await context.newPage();
    let release;
    const gate=new Promise(resolve=>{release=resolve;});
    const pending=[];
    await page.route('**/*',async route=>{
      const req=route.request(), host=new URL(req.url()).hostname;
      if(host==='gc.zgo.at'||host.endsWith('.goatcounter.com'))return route.abort();
      if(req.resourceType()==='image') { pending.push(req.url());await gate; }
      return route.continue();
    });
    try {
      const response=await page.goto(base+path,{waitUntil:'domcontentloaded',timeout:45000});
      assert(response?.ok(),'Published page returned '+response?.status());
      await page.locator('.story-card').first().waitFor({state:'attached'});
      await page.locator('.story-card').first().scrollIntoViewIfNeeded();
      // Stylesheet load is render-blocking; wait for the actual square wrapper rule.
      await page.waitForFunction(()=>getComputedStyle(document.querySelector('.story-image')).position==='relative');
      if(path==='ru/'||path==='de/') {
        assert.equal(await page.locator('.hero-art').count(),0,'Decorative hero returned');
        assert.equal(await page.locator('.latest .story-card').count(),1,'Homepage needs exactly one newest story');
        assert(await page.locator('.new-badge').isVisible(),'New story badge is missing');
        assert(await page.locator('.home-hero').evaluate(el=>el.nextElementSibling?.matches('.latest')), 'Newest story must follow signature intro');
      }
      const before=await geometry(page);
      assert(before.length>0,'No story cards found');
      for(const g of before) {
        assert(Math.abs(g.width-g.height)<3,'Non-square reserved thumbnail '+JSON.stringify(g));
        assert(g.textGap>=0&&g.textGap<140,'Excess gap before title '+JSON.stringify(g));
        assert(g.leadGap===null||(g.leadGap>=0&&g.leadGap<160),'Excess gap above thumbnail '+JSON.stringify(g));
        assert(g.overflow<=2,'Horizontal overflow');
        assert.equal(g.naturalWidth,0,'Before-load sample must precede image decoding');
      }
      release();
      // Scroll each lazy image into view before waiting for it to decode.
      for(const img of await page.locator('.story-card img').all()) {
        await img.scrollIntoViewIfNeeded();
        await img.evaluate(el=>el.decode());
      }
      const after=await geometry(page);
      for(let i=0;i<before.length;i++) {
        assert(after[i].naturalWidth>0,'Image failed to load');
        assert(Math.abs(before[i].height-after[i].height)<3,'Height changed after decode');
        assert(Math.abs(before[i].titleOffset-after[i].titleOffset)<3,'Title shifted after decode');
        assert(after[i].overflow<=2,'Horizontal overflow after decode');
      }
      results.push({engine,path,status:'pass',before,after});
      console.log('PASS',label);
    } catch(error) {
      failed=true; release();
      results.push({engine,path,status:'fail',error:String(error),pendingImages:pending});
      await page.screenshot({path:'layout-report/'+label+'.png',fullPage:true}).catch(()=>{});
      console.error('FAIL',label,String(error));
    } finally {release();await context.close();}
  }
  await browser.close();
}
await writeFile('layout-report/results.json',JSON.stringify(results,null,2));
if(failed)process.exitCode=1;
