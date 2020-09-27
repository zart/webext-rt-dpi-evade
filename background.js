function evade_dpi(details) {
  if (!details.url.includes("?")) // do internal redirect when no query
    return { redirectUrl: details.url + "?" }
}
const filter = { urls: ["http://*/*.js"] }
const blocking = ["blocking"]

if (typeof chrome !== 'undefined')
  chrome.webRequest.onBeforeRequest.addListener(evade_dpi, filter, blocking)

if (typeof browser !== 'undefined')
  browser.webRequest.onBeforeRequest.addListener(evade_dpi, filter, blocking)
