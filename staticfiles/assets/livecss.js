var livecss={pollFrequency:1e3,outstandingRequests:{},filesLastModified:{},watchTimers:{},watchAll:function(){this.unwatchAll();var e=setInterval(this.proxy(function(){for(var e=document.getElementsByTagName("link"),t=["screen","handheld","all",""],n=0;n<e.length;n++){var s=(e[n].getAttribute("media")||"").toLowerCase();"stylesheet"==e[n].getAttribute("rel")&&0<=livecss.indexOf(t,s)&&this.isLocalLink(e[n])&&this.refreshLinkElement(e[n])}}),this.pollFrequency);this.watchTimers.all=e},watch:function(e){var t=e.getAttribute("href");this.unwatch(t),this.watchTimers[t]=setInterval(this.proxy(function(){var e=this.linkElementWithHref(t);this.refreshLinkElement(e)}),this.pollFrequency)},unwatchAll:function(){for(var e in this.watchTimers)this.unwatch(e)},unwatch:function(e){null!=this.watchTimers[e]&&(clearInterval(this.watchTimers[e]),delete this.watchTimers[e],delete this.outstandingRequests[e])},linkElementWithHref:function(e){for(var t=document.getElementsByTagName("link"),n=0;n<t.length;n++)if(t[n].href==e)return t[n]},replaceLinkElement:function(e,t){var n=e.parentNode,s=e.nextSibling,i=this.addCacheBust(e.href),r=document.createElement("link");r.href=i,r.setAttribute("rel","stylesheet"),s?n.insertBefore(r,s):n.appendChild(r);var a=setInterval(this.proxy(function(){this.isCssElementLoaded(r)&&("undefined"!=typeof console&&console.log("CSS refreshed:",this.removeCacheBust(i)),clearInterval(a),delete this.outstandingRequests[this.removeCacheBust(i)],n.removeChild(e))}),100)},refreshLinkElement:function(n){var s,i,r=this.removeCacheBust(n.getAttribute("href"));this.outstandingRequests[r]||(s=new XMLHttpRequest,this.outstandingRequests[r]=s,i=this.addCacheBust(r),s.onreadystatechange=this.proxy(function(e){var t;4==s.readyState&&(delete this.outstandingRequests[r],200!=s.status&&304!=s.status||(t=Date.parse(s.getResponseHeader("Last-Modified")),(!this.filesLastModified[r]||this.filesLastModified[r]<t)&&(this.filesLastModified[r]=t,this.replaceLinkElement(n,i))))}),s.open("HEAD",i),s.send(null))},isCssElementLoaded:function(e){try{return e.sheet&&0<e.sheet.cssRules.length}catch(e){}return!1},isLocalLink:function(e){var t=e.href,e=new RegExp("^/|^"+document.location.protocol+"//"+document.location.host);return 0==t.search(e)},addCacheBust:function(e){return this.removeCacheBust(e)+"?cache_bust="+(new Date).getTime()},removeCacheBust:function(e){return e.replace(/\?cache_bust=[^&]+/,"")},proxy:function(e){var t=this;return function(){return e.apply(t,[])}},indexOf:function(e,t){for(var n=0;n<e.length;n++)if(e[n]==t)return n;return-1},addEventListener:function(e,t,n){e.attachEvent?e.attachEvent("on"+t,n):e.addEventListener(t,n,!1)}};0<=window.location.search.toString().indexOf("startlivecss=true")&&livecss.addEventListener(window,"load",function(){livecss.watchAll()});