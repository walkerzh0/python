(function(_){var ba,ha,la,ma,ra,sa,z,xa,ya,Aa,Ha,La,Na,Ua,Va,Xa,Ya,ab,bb,cb,eb,jb,lb,nb,ob,pb,qb,rb,tb,sb,ub,wb,vb,xb,yb,zb,Ab,Db,Eb,Kb,Jb,Ib,Nb,Pb,Qb,Rb,Tb,Ub,Xb,Yb,Wb,Vb,Zb,cc,dc,ec,fc,hc,ic,mc,kc,nc,rc,uc,tc,wc,xc,yc,Bc,Dc,Ec,Hc,Ic,Kc,Lc,Mc,Oc,ea,Pc,fa;ba=function(a){return function(){return _.aa[a].apply(this,arguments)}};_.ca=function(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}};_.da=function(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];return b?b.call(a):{next:_.ca(a)}};ha=function(a,b){a.prototype=ea(b.prototype);a.prototype.constructor=a;if(fa)fa(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.S=b.prototype};la=function(a,b){if(b){var c=_.ia;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];e in c||(c[e]={});c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&null!=b&&(0,_.ka)(c,a,{configurable:!0,writable:!0,value:b})}};ma=function(a,b){this.b=a;(0,_.ka)(this,"description",{configurable:!0,writable:!0,value:b})};_.l=function(a){return void 0!==a};_.m=function(a){return"string"==typeof a};_.r=function(a,b,c){a=a.split(".");c=c||_.q;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)!a.length&&_.l(b)?c[d]=b:c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}};_.na=function(){};_.oa=function(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";else if("function"==b&&"undefined"==typeof a.call)return"object";return b};_.pa=function(a){return"array"==_.oa(a)};_.qa=function(a){return"function"==_.oa(a)};ra=function(a,b,c){return a.call.apply(a.bind,arguments)};sa=function(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}};_.v=function(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?_.v=ra:_.v=sa;return _.v.apply(null,arguments)};_.w=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}};_.x=function(a,b){function c(){}c.prototype=b.prototype;a.S=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.nc=function(a,c,f){for(var d=Array(arguments.length-2),e=2;e<arguments.length;e++)d[e-2]=arguments[e];return b.prototype[c].apply(a,d)}};_.ua=function(a,b){b=(0,_.ta)(a,b);var c;(c=0<=b)&&Array.prototype.splice.call(a,b,1);return c};_.va=function(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]};z=function(a){return-1!=wa.indexOf(a)};xa=function(){return z("iPhone")&&!z("iPod")&&!z("iPad")};ya=function(a){ya[" "](a);return a};_.za=function(a,b){try{return ya(a[b]),!0}catch(c){}return!1};Aa=function(){var a=_.q.document;return a?a.documentMode:void 0};_.A=function(){};_.B=function(a,b,c){a.b=null;b||(b=[]);a.B=void 0;a.o=-1;a.g=b;a:{if(b=a.g.length){--b;var d=a.g[b];if(!(null===d||"object"!=typeof d||_.pa(d)||Ba&&d instanceof Uint8Array)){a.v=b-a.o;a.l=d;break a}}a.v=Number.MAX_VALUE}a.A={};if(c)for(b=0;b<c.length;b++)if(d=c[b],d<a.v)d+=a.o,a.g[d]=a.g[d]||Ca;else{var e=a.v+a.o;a.g[e]||(a.l=a.g[e]={});a.l[d]=a.l[d]||Ca}};_.Da=function(a,b){if(b<a.v){b+=a.o;var c=a.g[b];return c===Ca?a.g[b]=[]:c}if(a.l)return c=a.l[b],c===Ca?a.l[b]=[]:c};_.C=function(a,b,c){a=_.Da(a,b);return null==a?c:a};_.D=function(a,b){a=_.Da(a,b);a=null==a?a:!!a;return null==a?!1:a};_.E=function(a,b,c){a.b||(a.b={});if(!a.b[c]){var d=_.Da(a,c);d&&(a.b[c]=new b(d))}return a.b[c]};_.Ea=function(a,b,c){a.b||(a.b={});if(!a.b[c]){for(var d=_.Da(a,c),e=[],f=0;f<d.length;f++)e[f]=new b(d[f]);a.b[c]=e}b=a.b[c];b==Ca&&(b=a.b[c]=[]);return b};_.Fa=function(a){if(a.b)for(var b in a.b){var c=a.b[b];if(_.pa(c))for(var d=0;d<c.length;d++)c[d]&&_.Fa(c[d]);else c&&_.Fa(c)}return a.g};Ha=function(a){_.B(this,a,Ga)};_.Ia=function(a){_.B(this,a,null)};_.Ka=function(a){_.B(this,a,Ja)};La=function(a){_.B(this,a,null)};_.Ma=function(a){_.B(this,a,null)};Na=function(a){return _.Ea(a,_.Ka,1)};_.Oa=function(a,b){var c=/[?&]adurl=([^&]+)/.exec(a);if(!c||!/[?&]ae=1(&|$)/.test(a)||/[?&]dsh=1(&|$)/.test(a))return null;try{return{Fa:a+(b?"":"&act=1"),M:decodeURIComponent(c[1]),Va:c.index}}catch(d){return null}};_.F=function(){this.l="";this.o=Pa};_.Qa=function(a){if(a instanceof _.F&&a.constructor===_.F&&a.o===Pa)return a.l;_.oa(a);return"type_error:SafeUrl"};_.Ta=function(a){if(a instanceof _.F)return a;a="object"==typeof a&&a.g?a.b():String(a);Ra.test(a)||(a="about:invalid#zClosurez");return _.Sa(a)};_.Sa=function(a){var b=new _.F;b.l=a;return b};Ua=function(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}};Va=function(a,b,c,d,e){c="&"+b+"="+c;var f=a.indexOf("&"+d+"=");c=0>f?a+c:a.substring(0,f)+c+a.substring(f);return 2E3<c.length?_.l(e)?Va(a,b,e,d,void 0):a:c};_.Wa=function(a,b){this.b=_.l(a)?a:0;this.g=_.l(b)?b:0};Xa=function(a){try{return!!a&&null!=a.location.href&&_.za(a,"foo")}catch(b){return!1}};Ya=function(a,b){if(a)for(var c in a)Object.prototype.hasOwnProperty.call(a,c)&&b.call(void 0,a[c],c,a)};_.Za=function(a){a.preventDefault?a.preventDefault():a.returnValue=!1};ab=function(a){return a?a.passive&&$a()?a:a.capture||!1:!1};_.G=function(a,b,c,d){a.addEventListener&&a.addEventListener(b,c,ab(d))};bb=function(a,b,c){a.removeEventListener&&a.removeEventListener(b,c,ab(void 0))};_.db=function(a,b,c){cb(a,b,void 0===c?null:c)};cb=function(a,b,c){a.google_image_requests||(a.google_image_requests=[]);var d=a.document.createElement("img");if(c){var e=function(a){c&&c(a);bb(d,"load",e);bb(d,"error",e)};_.G(d,"load",e);_.G(d,"error",e)}d.src=b;a.google_image_requests.push(d)};eb=function(a,b){for(var c in a)Object.prototype.hasOwnProperty.call(a,c)&&b.call(void 0,a[c],c,a)};_.gb=function(a,b,c,d,e,f,g){if(!g)a:{if(1===a.nodeType)try{if(1==a.nodeType){c:{try{var k=a.getBoundingClientRect()}catch(t){var n={left:0,top:0,right:0,bottom:0};break c}if(_.fb&&a.ownerDocument.body){var p=a.ownerDocument;k.left-=p.documentElement.clientLeft+p.body.clientLeft;k.top-=p.documentElement.clientTop+p.body.clientTop}n=k}g=new _.Wa(n.left,n.top)}else{var u=a.changedTouches?a.changedTouches[0]:a;g=new _.Wa(u.clientX,u.clientY)}break a}catch(t){}g=new _.Wa(0,0)}if(document.createEvent)n=document.createEvent("MouseEvents"),n.initMouseEvent("click",!0,!0,null,0,g.b,g.g,g.b,g.g,c,f,d,e,b,null);else return!1;if(a.dispatchEvent)a.dispatchEvent(n);else return!1;return!0};_.ib=function(a,b,c){c=void 0===c?_.H:c;switch(a){case 2:return c.getElementsByClassName(b);case 3:return c.getElementsByTagName(b)}return[]};_.I=function(a,b,c){c=void 0===c?_.H:c;switch(a){case 1:if(c.getElementById)return c.getElementById(b);break;case 2:case 3:if(a=_.ib(a,b,c),0<a.length)return a[0]}return null};jb=function(a,b){a&&eb(b,function(b,d){a.style[d]=b})};lb=function(a,b,c,d){b=c(d,b);if(!(b instanceof Array))return a;(0,_.kb)(b,function(b){if(2!==b.length&&3!==b.length)return a;a=Va(a,b[0],b[1],"adurl",b[2])});return a};nb=function(a,b,c){c=void 0===c?{}:c;this.error=a;this.context=b.context;this.line=b.line||-1;this.msg=b.message||"";this.file=b.file||"";this.id=b.id||"jserror";this.meta=c};ob=function(a,b){this.b=a;this.g=b};pb=function(a,b){this.url=a;this.Ja=!!b;this.depth=null};qb=function(){this.l="&";this.o=_.l(void 0)?void 0:"trn";this.v=!1;this.g={};this.A=0;this.b=[]};rb=function(a,b){var c={};c[a]=b;return[c]};tb=function(a,b,c,d,e){var f=[];Ya(a,function(a,k){(a=sb(a,b,c,d,e))&&f.push(k+"="+a)});return f.join(b)};sb=function(a,b,c,d,e){if(null==a)return"";b=b||"&";c=c||",$";"string"==typeof c&&(c=c.split(""));if(a instanceof Array){if(d=d||0,d<c.length){for(var f=[],g=0;g<a.length;g++)f.push(sb(a[g],b,c,d+1,e));return f.join(c[d])}}else if("object"==typeof a)return e=e||0,2>e?encodeURIComponent(tb(a,b,c,d,e+1)):"...";return encodeURIComponent(String(a))};ub=function(a,b,c,d){a.b.push(b);a.g[b]=rb(c,d)};wb=function(a,b,c){b=b+"//pagead2.googlesyndication.com"+c;var d=vb(a)-c.length;if(0>d)return"";a.b.sort(function(a,b){return a-b});c=null;for(var e="",f=0;f<a.b.length;f++)for(var g=a.b[f],k=a.g[g],n=0;n<k.length;n++){if(!d){c=null==c?g:c;break}var p=tb(k[n],a.l,",$");if(p){p=e+p;if(d>=p.length){d-=p.length;b+=p;e=a.l;break}else a.v&&(e=d,p[e-1]==a.l&&--e,b+=p.substr(0,e),e=a.l,d=0);c=null==c?g:c}}f="";a.o&&null!=c&&(f=e+a.o+"="+c);return b+f};vb=function(a){if(!a.o)return 4E3;var b=1,c;for(c in a.g)b=c.length>b?c.length:b;return 4E3-a.o.length-b-a.l.length-1};xb=function(a,b,c,d,e,f){if((d?a.g:Math.random())<(e||.01))try{if(c instanceof qb)var g=c;else g=new qb,Ya(c,function(a,b){var c=g,d=c.A++;a=rb(b,a);c.b.push(d);c.g[d]=a});var k=wb(g,a.b,"/pagead/gen_204?id="+b+"&");k&&("undefined"===typeof f?_.db(_.q,k):_.db(_.q,k,f))}catch(n){}};yb=function(){var a=_.q.performance;return a&&a.now&&a.timing?Math.floor(a.now()+a.timing.navigationStart):(0,_.J)()};zb=function(){var a=void 0===a?_.q:a;return(a=a.performance)&&a.now?a.now():null};Ab=function(a,b,c){this.label=a;this.type=b;this.value=c;this.duration=0;this.uniqueId=this.label+"_"+this.type+"_"+Math.random();this.slotId=void 0};Db=function(){var a=Bb;this.events=[];this.g=a||_.q;var b=null;a&&(a.google_js_reporting_queue=a.google_js_reporting_queue||[],this.events=a.google_js_reporting_queue,b=a.google_measure_js_timing);this.b=Cb()||(null!=b?b:1>Math.random())};Eb=function(a){a&&K&&Cb()&&(K.clearMarks("goog_"+a.uniqueId+"_start"),K.clearMarks("goog_"+a.uniqueId+"_end"))};_.Hb=function(){var a=Fb;this.l=Gb;this.o=this.g;this.b=void 0===a?null:a};Kb=function(a,b,c,d){try{if(a.b&&a.b.b){var e=a.b.start(b.toString(),3);var f=c();a.b.end(e)}else f=c()}catch(g){c=!0;try{Eb(e),c=(d||a.o).call(a,b,new Ib(Jb(g),g.fileName,g.lineNumber),void 0,void 0)}catch(k){a.g(217,k)}if(!c)throw g;}return f};_.Mb=function(a,b,c){var d=Lb;return function(e){for(var f=[],g=0;g<arguments.length;++g)f[g]=arguments[g];return Kb(d,a,function(){return b.apply(c,f)})}};Jb=function(a){var b=a.toString();a.name&&-1==b.indexOf(a.name)&&(b+=": "+a.name);a.message&&-1==b.indexOf(a.message)&&(b+=": "+a.message);if(a.stack){a=a.stack;var c=b;try{-1==a.indexOf(c)&&(a=c+"\n"+a);for(var d;a!=d;)d=a,a=a.replace(/((https?:\/..*\/)[^\/:]*:\d+(?:.|\n)*)\2/,"$1");b=a.replace(/\n */g,"\n")}catch(e){b=c}}return b};Ib=function(a,b,c){nb.call(this,Error(a),{message:a,file:void 0===b?"":b,line:void 0===c?-1:c})};Nb=function(){if(!Bb.google_measure_js_timing){var a=Fb;a.b=!1;a.events!=a.g.google_js_reporting_queue&&(Cb()&&(0,_.kb)(a.events,Eb),a.events.length=0)}};_.Ob=function(a,b,c){xb(Gb,a,b,"jserror"!=a,c,void 0)};Pb=function(a,b,c){this.b=a;this.B=b;this.l=c;this.C=[];this.o=[];this.G={};this.g={};this.D=this.v=!1;this.A=-1};Qb=function(a,b,c){var d=b=b.getAttribute("data-original-click-url");if(d)for(var e=0;e<a.C.length;e++)d=lb(d,b,a.C[e],c);return d};Rb=function(a,b){b=void 0===b?Date.now():b;return b-a.A>_.C(a.b,39,0)};Tb=function(a,b){-1===b.href.indexOf("dbm/clk")&&(/[?&]ae=1(&|$)/.test(b.href)||_.D(a.b,38))&&Kb(Lb,446,function(){var c=Date.now(),d;if(d=Rb(a,c)){d=b.href;var e=_.Oa(d,!0);if(e){var f=e.Va;var g=e.Fa;g=g.slice(0,f)+"&act=1&ri=1"+g.slice(f);d=navigator.sendBeacon?navigator.sendBeacon(g,"")?{ua:e.M,ra:!0}:{ua:d.slice(0,f)+"&ri=2"+d.slice(f),ra:!1}:{ua:d.slice(0,f)+"&ri=16"+d.slice(f),ra:!1}}else d={ua:d,ra:!1};e=d;d=e.ra;e=e.ua;e=e instanceof _.F||!Sb.test(e)?e:_.Sa(e);e=e instanceof _.F?e:_.Ta(e);b.href=_.Qa(e)}d&&(a.A=c)},void 0)};Ub=function(a,b,c,d){if(0!=a.o.length&&(d.preventDefault?!d.defaultPrevented:!1!==d.returnValue)){var e=1==d.which&&!d.ctrlKey&&"_blank"!=b.target&&"_new"!=b.target;e&&_.Za(d);for(var f=[],g={},k=0;k<a.o.length;g={ma:g.ma},k++)if(g.ma=a.o[k](c),g.ma){var n=new Promise(function(a){return function(b){_.db(_.L,a.ma,b)}}(g));f.push(n)}c=Promise.all(f);f=new Promise(function(a){window.setTimeout(a,2E3)});e&&Promise.race([c,f]).then((0,_.v)(Pb.prototype.N,a,b,d))}};Xb=function(a,b,c){var d=_.Ea(a.B,_.Ia,23),e=!1;d=_.da(d);for(var f=d.next();!f.done;f=d.next())if(f=f.value,"use_async_for_js_click_handler"===_.C(f,1,"")&&"True"===_.C(f,2,"")){e=!0;break}e&&a.l?(_.Za(c),Vb(a,b,c).then(function(c){c||Tb(a,b)})):Wb(a,b,c)||Tb(a,b)};Yb=function(a,b,c,d){a.g[d]||(a.g[d]={});a.g[d][c]||(a.g[d][c]=[]);_.G(b,d,(0,_.v)(a.J,a,b,c,d))};Wb=function(a,b,c){var d=b.href;if(a.l){var e=Date.now(),f=Rb(a,e);if(a.l.Ia(b,c,a.b,a.D,f))return f&&(a.A=e),!0}else if(_.q.googdlu&&(_.q.googdlu.tryOpenPlayStore&&_.q.googdlu.tryOpenPlayStore(c,d,_.C(a.b,15,""))||_.q.googdlu.tryOpenItunesStore&&_.q.googdlu.tryOpenItunesStore(c,d,_.C(a.b,15,""),_.D(a.b,42),_.D(a.b,43),_.C(a.B,7,""),_.C(a.B,8,""))))return!0;return _.D(a.b,31)&&_.D(a.b,30)&&_.C(a.b,28,"")&&_.q.googdlu&&_.q.googdlu.tryOpenAppUrl?(_.q.googdlu.tryOpenAppUrl(c,d,_.C(a.b,32,""),_.C(a.b,28,"")),!0):!1};Vb=function(a,b,c){return a.l?a.l.eb(b,c,a.b):new Promise(function(a){a(!1)})};Zb=function(a){if(a.classList)return a.classList;a=a.className;return _.m(a)&&a.match(/\S+/g)||[]};_.$b=function(a,b){a.classList?a.classList.add(b):(a.classList?a.classList.contains(b):0<=(0,_.ta)(Zb(a),b))||(a.className+=0<a.className.length?" "+b:b)};_.bc=function(a,b){if(a.classList)a.classList.remove(b);else if(a.classList?a.classList.contains(b):0<=(0,_.ta)(Zb(a),b))a.className=ac(Zb(a),function(a){return a!=b}).join(" ")};cc=function(a){_.q.setTimeout(function(){throw a;},0)};dc=function(){var a=_.q.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!z("Presto")&&(a=function(){var a=document.createElement("IFRAME");a.style.display="none";a.src="";document.documentElement.appendChild(a);var b=a.contentWindow;a=b.document;a.open();a.write("");a.close();var c="callImmediate"+Math.random(),d="file:"==b.location.protocol?"*":b.location.protocol+"//"+b.location.host;a=(0,_.v)(function(a){if(("*"==d||a.origin==d)&&a.data==c)this.port1.onmessage()},this);b.addEventListener("message",a,!1);this.port1={};this.port2={postMessage:function(){b.postMessage(c,d)}}});if("undefined"!==typeof a&&!z("Trident")&&!z("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(_.l(c.next)){c=c.next;var a=c.Ga;c.Ga=null;a()}};return function(a){d.next={Ga:a};d=d.next;b.port2.postMessage(0)}}return"undefined"!==typeof document&&"onreadystatechange"in document.createElement("SCRIPT")?function(a){var b=document.createElement("SCRIPT");b.onreadystatechange=function(){b.onreadystatechange=null;b.parentNode.removeChild(b);b=null;a();a=null};document.documentElement.appendChild(b)}:function(a){_.q.setTimeout(a,0)}};ec=function(a,b){this.l=a;this.o=b;this.g=0;this.b=null};fc=function(){this.g=this.b=null};hc=function(){var a=gc,b=null;a.b&&(b=a.b,a.b=a.b.next,a.b||(a.g=null),b.next=null);return b};ic=function(){this.next=this.g=this.b=null};mc=function(a){jc||kc();lc||(jc(),lc=!0);gc.add(a,void 0)};kc=function(){if(_.q.Promise&&_.q.Promise.resolve){var a=_.q.Promise.resolve(void 0);jc=function(){a.then(nc)}}else jc=function(){var a=nc;!_.qa(_.q.setImmediate)||_.q.Window&&_.q.Window.prototype&&!z("Edge")&&_.q.Window.prototype.setImmediate==_.q.setImmediate?(oc||(oc=dc()),oc(a)):_.q.setImmediate(a)}};nc=function(){for(var a;a=hc();){try{a.b.call(a.g)}catch(c){cc(c)}var b=pc;b.o(a);100>b.g&&(b.g++,a.next=b.b,b.b=a)}lc=!1};_.N=function(){this.o=this.o;this.l=this.l};_.qc=function(a){_.N.call(this);this.B=1;this.v=[];this.A=0;this.b=[];this.g={};this.D=!!a};rc=function(a,b,c){mc(function(){a.apply(b,c)})};uc=function(a,b,c,d,e){this.v=new _.qc;this.g=a;this.g[0]=[b];this.o=[];this.l=new Pb(c,d,e);this.b=c;b=_.C(this.b,22,"");c=_.C(this.b,23,"");b&&c&&e&&(e.canOpenIntents([{url:b,id:b,F:c}],(0,_.v)(this.Ma,this))||e.canOpenURLs(b,(0,_.v)(this.Ma,this)));(e=_.I(1,"common_15click_anchor"))?(a[20]=[e],tc(this,20)):(e=_.va(_.ib(2,"common_15click_anchor")),0<e.length&&(a[20]=e,tc(this,20)))};_.vc=function(a,b,c){a=a.getElementsByAdPiece(b);if(c)for(b=0;b<a.length;b++){var d=a[b].getAttribute(c);if(d)return d}return null};tc=function(a,b){if(a.g[b]&&a.ya(b)){a.o.push(b);var c=a.l;a=a.g[b];for(var d=0;d<a.length;d++){var e=a[d];e.href&&e.setAttribute("data-original-click-url",e.href);Yb(c,e,b,"mousedown");Yb(c,e,b,"click")}c.G[b]=!0}};wc=function(a,b){a=a.getElementsByAdPiece(b);for(b=0;b<a.length;b++)if(!a[b].href)return!1;return!0};xc=function(a){this.B=new _.qc;this.v=null;this.l=[];this.b=a;this.o=[];this.A=!1;this.g=null};yc=function(a){a=new xc(new Ha(a));_.r("adSlot",a,void 0);return a};_.zc=function(){var a=_.q.adSlot;return a?a:(Lb.g(536,Error("no adslot"),void 0,void 0),yc(null))};Bc=function(a,b,c){uc.call(this,a,b,c,_.zc().b,_.zc().g);for(a=0;a<Ac.length;a++)tc(this,Ac[a])};Dc=function(a,b){var c=O,d={};if(!b)return null;d[0]=[b];eb(Cc,function(a){c[a]&&(d[a]=_.va(_.ib(2,c[a],b)))});return new Bc(d,b,a)};Ec=function(a){_.D(a,19)&&(0,_.kb)(_.Da(a,20),function(a){_.db(_.L,a,void 0)})};Hc=function(a,b,c){b.gqid=Fc;b.qqid=Gc;b.com=a;_.Ob("glaurung",b,c)};Ic=function(a,b){var c=_.E(b,La,16);c&&_.D(c,12)&&_.D(b,5)&&jb(a,{backgroundColor:"transparent",backgroundImage:"none"})};Kc=function(a,b,c){var d=a.b,e=_.E(d,La,16);if(e&&_.D(e,1)){e=O;for(var f in e)delete e[f];O[1]="title-link";O[2]="url-link";O[3]="body-link";O[4]="button-link";O[8]="favicon-link";O[6]="image-link";O[26]="price";O[23]="reviews";O[43]="rating-stars";O[44]="reviews-count";O[24]="app-store";O[25]="promo-headline";O[33]="app-icon";O[16]="image-gallery";O[40]="image-gallery-image-link";O[36]="logo-link";O[37]="advertiser-link";O[38]="call-to-action-link";O[39]="video";O[42]="logo";O[50]="badge-box";O[9]="ad-background";_.I(2,"app-store-link",b)&&(O[24]="app-store-link");_.I(2,"app-icon-link",b)&&(O[33]="app-icon-link");_.I(2,"promo-headline-link",b)&&(O[25]="promo-headline-link")}f=_.I(1,"adunit",b);e=_.I(1,"ads",b);if(!f||!e)return 1;var g={};0==_.C(d,32,0)?(g.width=_.C(d,2,0)+"px",g.height=_.C(d,3,0)+"px",g.position="absolute",g.top="0",g.left="0"):(g.width="100%",g.height="100%");g.overflow="hidden";jb(f,g);Ic(f,d);Ic(e,d);try{c(e,a)}catch(p){return _.D(d,13)&&(Jc=p),2}c=0;d=Na(d);for(f=0;f<d.length;f++){g=d[f];var k="taw"+_.C(g,2,0);e=_.I(1,k,b);if(!e)return 3;e=Dc(g,e);if(!e)return 1;_.L.registerAd?_.L.registerAd(e,k):c=4;_.D(g,11)&&_.L.initAppPromo&&_.L.initAppPromo(e,a);Ec(g);if(_.D(g,19)&&(g=_.Da(g,33),0<g.length))for(k=0;k<g.length;k++){var n=(0,_.v)(Bc.prototype.A,e,g[k]);e.l.o.push(n)}a.za(e)}return c};Lc=function(a,b,c){var d=[];d[0]=[c];d[15]=[b];(b=_.I(1,"abgc"))&&(d[27]=[b]);(b=_.I(1,"cbc"))&&(d[28]=[b]);uc.call(this,d,c,a,_.zc().b,_.zc().g);tc(this,15)};Mc=function(a,b){var c={};c[0]=[b];uc.call(this,c,b,a,_.zc().b,_.zc().g)};Oc=function(a,b,c){uc.call(this,a,b,c,_.zc().b,_.zc().g);for(a=0;a<Nc.length;a++)tc(this,Nc[a]);this.listen(4,"mouseover",(0,_.v)(this.H,this,0,"onhoverbg",!1));this.listen(4,"mouseout",(0,_.v)(this.H,this,0,"onhoverbg",!0))};_.aa=[];ea="function"==typeof Object.create?Object.create:function(a){function b(){}b.prototype=a;return new b};if("function"==typeof Object.setPrototypeOf)Pc=Object.setPrototypeOf;else{var Qc;a:{var Rc={Ua:!0},Sc={};try{Sc.__proto__=Rc;Qc=Sc.Ua;break a}catch(a){}Qc=!1}Pc=Qc?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}fa=Pc;_.ia="undefined"!=typeof window&&window===this?this:"undefined"!=typeof global&&null!=global?global:this;_.ka="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){a!=Array.prototype&&a!=Object.prototype&&(a[b]=c.value)};la("Promise",function(a){function b(a){this.g=0;this.l=void 0;this.b=[];var b=this.o();try{a(b.resolve,b.reject)}catch(n){b.reject(n)}}function c(){this.b=null}function d(a){return a instanceof b?a:new b(function(b){b(a)})}if(a)return a;c.prototype.g=function(a){if(null==this.b){this.b=[];var b=this;this.l(function(){b.v()})}this.b.push(a)};var e=_.ia.setTimeout;c.prototype.l=function(a){e(a,0)};c.prototype.v=function(){for(;this.b&&this.b.length;){var a=this.b;this.b=[];for(var b=0;b<a.length;++b){var c=a[b];a[b]=null;try{c()}catch(p){this.o(p)}}}this.b=null};c.prototype.o=function(a){this.l(function(){throw a;})};b.prototype.o=function(){function a(a){return function(d){c||(c=!0,a.call(b,d))}}var b=this,c=!1;return{resolve:a(this.G),reject:a(this.v)}};b.prototype.G=function(a){if(a===this)this.v(new TypeError("A Promise cannot resolve to itself"));else if(a instanceof b)this.J(a);else{a:switch(typeof a){case "object":var c=null!=a;break a;case "function":c=!0;break a;default:c=!1}c?this.D(a):this.A(a)}};b.prototype.D=function(a){var b=void 0;try{b=a.then}catch(n){this.v(n);return}"function"==typeof b?this.N(b,a):this.A(a)};b.prototype.v=function(a){this.B(2,a)};b.prototype.A=function(a){this.B(1,a)};b.prototype.B=function(a,b){if(0!=this.g)throw Error("Cannot settle("+a+", "+b+"): Promise already settled in state"+this.g);this.g=a;this.l=b;this.C()};b.prototype.C=function(){if(null!=this.b){for(var a=0;a<this.b.length;++a)f.g(this.b[a]);this.b=null}};var f=new c;b.prototype.J=function(a){var b=this.o();a.ta(b.resolve,b.reject)};b.prototype.N=function(a,b){var c=this.o();try{a.call(b,c.resolve,c.reject)}catch(p){c.reject(p)}};b.prototype.then=function(a,c){function d(a,b){return"function"==typeof a?function(b){try{e(a(b))}catch(M){f(M)}}:b}var e,f,g=new b(function(a,b){e=a;f=b});this.ta(d(a,e),d(c,f));return g};b.prototype.catch=function(a){return this.then(void 0,a)};b.prototype.ta=function(a,b){function c(){switch(d.g){case 1:a(d.l);break;case 2:b(d.l);break;default:throw Error("Unexpected state: "+d.g);}}var d=this;null==this.b?f.g(c):this.b.push(c)};b.resolve=d;b.reject=function(a){return new b(function(b,c){c(a)})};b.race=function(a){return new b(function(b,c){for(var e=_.da(a),f=e.next();!f.done;f=e.next())d(f.value).ta(b,c)})};b.all=function(a){var c=_.da(a),e=c.next();return e.done?d([]):new b(function(a,b){function f(b){return function(c){g[b]=c;k--;0==k&&a(g)}}var g=[],k=0;do g.push(void 0),k++,d(e.value).ta(f(g.length-1),b),e=c.next();while(!e.done)})};return b});ma.prototype.toString=function(){return this.b};_.Tc=function(){function a(c){if(this instanceof a)throw new TypeError("Symbol is not a constructor");return new ma("jscomp_symbol_"+(c||"")+"_"+b++,c)}var b=0;return a}();_.q=this;_.J=Date.now||function(){return+new Date};var ac;_.ta=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if(_.m(a))return _.m(b)&&1==b.length?a.indexOf(b,0):-1;for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1};_.kb=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=_.m(a)?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)};ac=Array.prototype.filter?function(a,b){return Array.prototype.filter.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=[],e=0,f=_.m(a)?a.split(""):a,g=0;g<c;g++)if(g in f){var k=f[g];b.call(void 0,k,g,a)&&(d[e++]=k)}return d};_.Uc=Array.prototype.some?function(a,b){return Array.prototype.some.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=_.m(a)?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a))return!0;return!1};_.Vc=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};var wa;a:{var Wc=_.q.navigator;if(Wc){var Xc=Wc.userAgent;if(Xc){wa=Xc;break a}}wa=""};ya[" "]=_.na;var Yc,Zc,ad,ed;Yc=z("Opera");_.fb=z("Trident")||z("MSIE");Zc=z("Edge");_.$c=z("Gecko")&&!(-1!=wa.toLowerCase().indexOf("webkit")&&!z("Edge"))&&!(z("Trident")||z("MSIE"))&&!z("Edge");ad=-1!=wa.toLowerCase().indexOf("webkit")&&!z("Edge");_.bd=z("Android");_.cd=xa();_.dd=z("iPad");a:{var fd="",gd=function(){var a=wa;if(_.$c)return/rv:([^\);]+)(\)|;)/.exec(a);if(Zc)return/Edge\/([\d\.]+)/.exec(a);if(_.fb)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(ad)return/WebKit\/(\S+)/.exec(a);if(Yc)return/(?:Version)[ \/]?(\S+)/.exec(a)}();gd&&(fd=gd?gd[1]:"");if(_.fb){var hd=Aa();if(null!=hd&&hd>parseFloat(fd)){ed=String(hd);break a}}ed=fd}_.id=ed;var kd=_.q.document;_.jd=kd&&_.fb?Aa()||("CSS1Compat"==kd.compatMode?parseInt(_.id,10):5):void 0;_.ld=xa()||z("iPod");_.md=z("iPad");_.nd=z("Android")&&!((z("Chrome")||z("CriOS"))&&!z("Edge")||z("Firefox")||z("FxiOS")||z("Opera")||z("Silk"));var Ba="function"==typeof Uint8Array,Ca=[];_.x(Ha,_.A);_.x(_.Ia,_.A);_.x(_.Ka,_.A);_.x(La,_.A);_.x(_.Ma,_.A);var Ga=[1,23],Ja=[20,33];_.Ka.prototype.getType=function(){return _.C(this,1,0)};_.F.prototype.g=!0;_.F.prototype.b=function(){return this.l};var Ra=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i,Pa={};_.Sa("about:blank");var Sb=/^((market|itms|intent|itms-appss):\/\/)/i;_.od=Ua(function(){var a=document.createElement("div");a.innerHTML="<div><div></div></div>";var b=a.firstChild.firstChild;a.innerHTML="";return!b.parentElement});var Cc;Cc={Jb:0,ic:1,jc:45,kc:46,Xb:48,URL:2,Cb:3,ub:4,hc:5,bc:7,Pb:8,Ab:9,Rb:6,Ub:34,Kb:13,vb:14,Qb:15,Sb:16,Tb:40,fc:47,mc:29,Gb:30,gc:49,Yb:17,Db:18,Ib:19,Hb:20,dc:23,yb:24,ac:25,$b:26,zb:27,Zb:28,VIDEO:39,lc:31,Fb:32,xb:33,Lb:35,Vb:36,wb:37,Eb:38,Wb:42,cc:43,ec:44,Bb:50,Mb:1E3,Nb:1001,Ob:1002};_.pd=[16,47,49,18,27,28,39];_.H=document;_.L=window;_.Wa.prototype.ceil=function(){this.b=Math.ceil(this.b);this.g=Math.ceil(this.g);return this};_.Wa.prototype.floor=function(){this.b=Math.floor(this.b);this.g=Math.floor(this.g);return this};_.Wa.prototype.round=function(){this.b=Math.round(this.b);this.g=Math.round(this.g);return this};var $a=Ua(function(){var a=!1;try{var b=Object.defineProperty({},"passive",{get:function(){a=!0}});_.q.addEventListener("test",null,b)}catch(c){}return a});var qd=!!window.google_async_iframe_id,rd=qd&&window.parent||window;var sd=/^https?:\/\/(\w|-)+\.cdn\.ampproject\.(net|org)(\?|\/|$)/;var td=null;var K=_.q.performance,ud=!!(K&&K.mark&&K.measure&&K.clearMarks),Cb=Ua(function(){var a;if(a=ud){var b;if(null===td){td="";try{a="";try{a=_.q.top.location.hash}catch(c){a=_.q.location.hash}a&&(td=(b=a.match(/\bdeid=([\d,]+)/))?b[1]:"")}catch(c){}}b=td;a=!!b.indexOf&&0<=b.indexOf("1337")}return a});Db.prototype.start=function(a,b){if(!this.b)return null;var c=zb()||yb();a=new Ab(a,b,c);b="goog_"+a.uniqueId+"_start";K&&Cb()&&K.mark(b);return a};Db.prototype.end=function(a){if(this.b&&"number"==typeof a.value){var b=zb()||yb();a.duration=b-a.value;b="goog_"+a.uniqueId+"_end";K&&Cb()&&K.mark(b);this.b&&this.events.push(a)}};_.Hb.prototype.pinger=ba(0);_.Hb.prototype.g=function(a,b,c,d,e){e=e||"jserror";try{var f=new qb;f.v=!0;ub(f,1,"context",a);b.error&&b.meta&&b.id||(b=new Ib(Jb(b),b.fileName,b.lineNumber));b.msg&&ub(f,2,"msg",b.msg.substring(0,512));b.file&&ub(f,3,"file",b.file);0<b.line&&ub(f,4,"line",b.line);var g=b.meta||{};if(d)try{d(g)}catch(zd){}b=[g];f.b.push(5);f.g[5]=b;d=_.q;b=[];g=null;do{var k=d;if(Xa(k)){var n=k.location.href;g=k.document&&k.document.referrer||null}else n=g,g=null;b.push(new pb(n||""));try{d=k.parent}catch(zd){d=null}}while(d&&k!=d);n=0;for(var p=b.length-1;n<=p;++n)b[n].depth=p-n;k=_.q;if(k.location&&k.location.ancestorOrigins&&k.location.ancestorOrigins.length==b.length-1)for(p=1;p<b.length;++p){var u=b[p];u.url||(u.url=k.location.ancestorOrigins[p-1]||"",u.Ja=!0)}var t=new pb(_.q.location.href,!1);k=null;var y=b.length-1;for(u=y;0<=u;--u){var P=b[u];!k&&sd.test(P.url)&&(k=P);if(P.url&&!P.Ja){t=P;break}}P=null;var sc=b.length&&b[y].url;0!=t.depth&&sc&&(P=b[y]);var M=new ob(t,P);M.g&&ub(f,6,"top",M.g.url||"");ub(f,7,"url",M.b.url||"");xb(this.l,e,f,!1,c)}catch(zd){try{xb(this.l,e,{context:"ecmserr",rctx:a,msg:Jb(zd),url:M&&M.b.url},!1,c)}catch(Ck){}}return!0};ha(Ib,nb);var Gb,Lb;if(qd&&!Xa(rd)){var vd="."+_.H.domain;try{for(;2<vd.split(".").length&&!Xa(rd);)_.H.domain=vd=vd.substr(vd.indexOf(".")+1),rd=window.parent}catch(a){}Xa(rd)||(rd=window)}var Bb=rd,Fb=new Db;Gb=new function(){var a=void 0===a?_.L:a;this.b="http:"===a.location.protocol?"http:":"https:";this.g=Math.random()};Lb=new _.Hb;"complete"==Bb.document.readyState?Nb():Fb.b&&_.G(Bb,"load",function(){Nb()});Pb.prototype.N=function(a,b){this.v=!0;var c=!1;b.target&&(c=_.gb(b.target,b.button,b.ctrlKey,b.shiftKey,b.metaKey,b.altKey,new _.Wa(b.x,b.y)));!a.href||c||Wb(this,a,b)||(Tb(this,a),_.L.top.location=a.href)};Pb.prototype.J=function(a,b,c,d){if(this.v)this.v=!1;else{d||(d=_.L.event);this.g[c][b].forEach(function(a){a(d)});if(a.href){var e=Qb(this,a,d.type);e&&(a.href=e)}"click"==c&&(Ub(this,a,b,d),(d.preventDefault?d.defaultPrevented:!1===d.returnValue)||Xb(this,a,d))}};var oc;ec.prototype.get=function(){if(0<this.g){this.g--;var a=this.b;this.b=a.next;a.next=null}else a=this.l();return a};var pc=new ec(function(){return new ic},function(a){a.reset()});fc.prototype.add=function(a,b){var c=pc.get();c.set(a,b);this.g?this.g.next=c:this.b=c;this.g=c};ic.prototype.set=function(a,b){this.b=a;this.g=b;this.next=null};ic.prototype.reset=function(){this.next=this.g=this.b=null};var jc,lc=!1,gc=new fc;_.N.prototype.o=!1;_.N.prototype.Ba=ba(1);_.N.prototype.L=ba(3);_.x(_.qc,_.N);_.qc.prototype.subscribe=function(a,b,c){var d=this.g[a];d||(d=this.g[a]=[]);var e=this.B;this.b[e]=a;this.b[e+1]=b;this.b[e+2]=c;this.B=e+3;d.push(e);return e};_.qc.prototype.G=function(a){var b=this.b[a];b&&(b=this.g[b],0!=this.A?(this.v.push(a),this.b[a+1]=_.na):(b&&_.ua(b,a),delete this.b[a],delete this.b[a+1],delete this.b[a+2]))};_.qc.prototype.C=function(a,b){var c=this.g[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.D)for(e=0;e<c.length;e++){var g=c[e];rc(this.b[g+1],this.b[g+2],d)}else{this.A++;try{for(e=0,f=c.length;e<f;e++)g=c[e],this.b[g+1].apply(this.b[g+2],d)}finally{if(this.A--,0<this.v.length&&0==this.A)for(;c=this.v.pop();)this.G(c)}}}};_.qc.prototype.L=ba(2);_.h=uc.prototype;_.h.Ma=function(a,b){b=(a=_.C(this.b,22,""))&&b?b[a]:!1;this.l.D=!!b;this.H(0,"app_installed",!b)};_.h.navigationAdPieces=function(){return this.o};_.h.ya=function(){return!0};_.h.has=function(a){return(a=this.g[a])&&0<a.length};_.h.listen=function(a,b,c){var d=this.g[a];if(d){var e=this.l;c=_.w(c,a,this);var f=("click"==b||"mousedown"==b)&&e.G[a];e.g[b]||(e.g[b]={});e.g[b][a]||(e.g[b][a]=[]);e.g[b][a].push(c);if(!f)for(a=0;a<d.length;a++)_.G(d[a],b,c)}};_.h.H=function(a,b,c){if(b){a=this.getElementsByAdPiece(a);for(var d=0;d<a.length;d++)c?_.bc(a[d],b):_.$b(a[d],b)}};_.h.getElementsByAdPiece=function(a){return this.g[a]?this.g[a]:[]};_.h.creativeConversionUrl=function(){return _.C(this.b,6,"")};_.h.redirectUrl=function(){return _.C(this.b,8,"")};_.h.getIndex=function(){return _.C(this.b,2,0)};_.h.listenOnObject=function(a,b){this.v.subscribe(a,b)};_.h.fireOnObject=function(a,b){this.v.C(a,b)};_.h=xc.prototype;_.h.forEachAd=function(a){(0,_.kb)(this.l,a)};_.h.za=function(a){this.l.push(a)};_.h.Za=function(a){if(a=_.I(1,a))this.v=a;if(0==this.l.length)_.q.css=null;else{for(a=0;a<this.o.length;++a)this.o[a]();this.A=!0}};_.h.listenOnObject=function(a,b){this.B.subscribe(a,b)};_.h.fireOnObject=function(a,b){this.B.C(a,b)};_.h.registerFinalizeCallback=function(a){this.A?a():this.o.push(a)};_.h.getSerializedAdSlotData=function(){return _.Fa(this.b)};_.h.getAdsLength=function(){return this.l.length};_.h.getAd=function(a){return 0<=a&&a<this.l.length&&this.l[a].getIndex()==a?this.l[a]:null};_.h.getContainer=function(){return this.v};_.h.openSystemBrowser=function(a){return this.g?(this.g.openSystemBrowser(a,{useFirstPackage:!0,useRunningProcess:!0}),!0):!1};_.h.openAttribution=function(a){return this.g?(this.g.openSystemBrowser(a,{useFirstPackage:!0,useRunningProcess:!0,useCustomTabs:!0}),!0):!1};ha(Bc,uc);Bc.prototype.ya=function(a){return wc(this,a)||4==a};Bc.prototype.A=function(a,b){return this.ya(b)?a:""};var Ac=[1,2,3,4,8,6,40,24,33,25,36,37,38,9];var Fc="UNKNOWN",Gc="UNKNOWN",Jc=null,Q={},O=(Q[1]="ad-title",Q[2]="ad-url",Q[3]="ad-body",Q[4]="ad-button",Q[8]="ad-favicon",Q[6]="ad-image",Q[26]="ad-price",Q[23]="ad-reviews",Q[43]="ad-rating-stars",Q[44]="ad-reviews-count",Q[24]="ad-app-store-image",Q[25]="ad-promo-headline",Q[33]="ad-app-icon",Q[16]="ad-image-gallery",Q[40]="ad-image-gallery-image",Q[36]="ad-logo",Q[37]="ad-advertiser",Q[38]="ad-call-to-action",Q[39]="ad-video",Q[42]="ad-logo-wrapper",Q[9]="ad-background",Q);ha(Lc,uc);ha(Mc,uc);ha(Oc,uc);Oc.prototype.ya=function(a){return wc(this,a)||4==a};var R={},wd=(R[1]="rhtitle",R[45]="rhtitleline1",R[46]="rhtitleline2",R[48]="rhlongtitle",R[3]="rhbody",R[2]="rhurl",R[4]="rhbutton",R[8]="rhfavicon",R[14]="rhaddress",R[6]="rhimage",R[34]="rhimagetemplate",R[49]="rh-scrollflow",R[16]="rhimagegallery",R[47]="rhreviewgallery",R[29]="rhviewimagegallery",R[30]="rhcloseimagegalleryview",R[31]="rhtrydemobutton",R[32]="rhclosetrydemoview",R[39]="rhvideo",R[9]="rhbackground",R[13]="rh-icore-empty",R[5]="rhsitelink",R[7]="rhradlink",R[17]="rh-multiframe",R[18]="rh-box-breadcrumbs",R[23]="rhstarratings",R[24]="rhstoreicon",R[25]="rhpromotext",R[26]="rhprice",R[27]="abgc",R[28]="cbc",R[35]="rhdemocountdowntimer",R[36]="rhlogo",R[1001]="rhoverlap-imagegallery",R[1002]="rhoverlap-trydemo",R),Nc=[1,45,46,48,2,4,5,7,8,3,9,6,14,15,34,26,24,36];xc.prototype.forEachAd=xc.prototype.forEachAd;xc.prototype.addAd=xc.prototype.za;xc.prototype.finalize=xc.prototype.Za;_.r("buildAdSlot",yc,void 0);_.r("buildGlaurungAds",function(a,b,c){var d=(new Date).getTime(),e=1,f=!1;Jc=null;try{f=_.D(a.b,13),Fc=_.C(a.b,8,""),Gc=_.C(a.b,7,""),e=Kc(a,b,c)}catch(g){f&&(Jc=g),e=1}a=(new Date).getTime();b={};b.r=e;b.d=a-d;Hc("bridge",b);return e},void 0);_.r("glaurungError",function(){return Jc},void 0);_.r("glaurungBridge.log",Hc,void 0);_.r("glaurungBridge.getAdPieceClassName",function(a){return O[a]},void 0);_.r("buildImageAd",function(a,b){if(0>b||b>=Na(a.b).length)a=null;else{a=Na(a.b)[b];b=_.I(1,"google_image_div");var c=_.I(1,"aw0");a=b&&c?new Lc(a,c,b):null}return a},void 0);_.r("buildRichmediaAd",function(a,b){return 0>b||b>=Na(a.b).length?null:new Mc(Na(a.b)[b],_.H.body)},void 0);_.r("buildTextAd",function(a,b){var c=a.b;if(!(0>b||b>=Na(c).length)){if(0>b||b>=Na(a.b).length)var d=null;else{d=Na(a.b)[b];var e=_.I(1,"taw"+b);if(e){var f={0:[e]},g;for(g in Cc){var k=Cc[g],n=wd[k];n&&(f[k]=_.va(_.ib(2,n,e)))}d=new Oc(f,e,d)}else d=null}d&&(_.L.registerAd&&_.L.registerAd(d,"taw"+b),a.za(d),_.D(Na(c)[b],11)&&_.L.initAppPromo&&_.L.initAppPromo(d,a))}},void 0);})(window.hydra=window.hydra||{});
