/* Pageview-only configuration. No cookies or local storage. */
'use strict';
window.goatcounter = {
  path: location.pathname,
  title: document.title,
  referrer: '',
  no_session: true,
  no_events: true,
  no_onload: navigator.doNotTrack === '1' || navigator.globalPrivacyControl === true
};
