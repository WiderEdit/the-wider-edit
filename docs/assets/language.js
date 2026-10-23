'use strict';
const language=(navigator.language||'ru').toLowerCase().startsWith('de')?'de':'ru';
location.replace(new URL(language+'/',location.href).href);
