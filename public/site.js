document.addEventListener('click',function(e){var b=e.target.closest('.copy-command');if(!b)return;var code=document.getElementById(b.dataset.copy);if(!code)return;navigator.clipboard.writeText(code.textContent).then(function(){var n=b.parentElement.querySelector('.copy-note');if(n){n.textContent=document.documentElement.lang.indexOf('pt')===0?'Copiado.':'Copied.';setTimeout(function(){n.textContent=''},2500)}})});

/* Hero demo: stepped, looping playback in the manner of the research animation —
   auto-plays while visible, pausable, step-selectable, stops offscreen,
   reduced-motion starts paused on the final frame. Purely illustrative; no data involved. */
(function(){
var demo=document.querySelector('[data-memory-demo]');if(!demo)return;
var ids=['u1','a1','fact','u2','a2','chip'],msgs={};
ids.forEach(function(k){msgs[k]=demo.querySelector('[data-demo-msg="'+k+'"]')});
var cards={1:demo.querySelector('[data-demo-card="1"]'),2:demo.querySelector('[data-demo-card="2"]'),3:demo.querySelector('[data-demo-card="3"]')};
var steps=[].slice.call(demo.querySelectorAll('[data-demo-step]'));
var playBtn=demo.querySelector('[data-demo-play]');
var phases=[{s:1,m:['u1']},{s:2,m:['u1','a1','fact']},{s:3,m:['u1','a1','fact','u2']},{s:3,m:['u1','a1','fact','u2','chip']},{s:3,m:['u1','a1','fact','u2','chip','a2']}];
var hold=[2400,2400,1600,1000,5600];
var i=0,timer=null,userPaused=false,visible=true;
var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function apply(n){i=n;var p=phases[n];demo.dataset.stage=p.s;
ids.forEach(function(k){if(msgs[k])msgs[k].classList.toggle('shown',p.m.indexOf(k)>-1)});
[1,2,3].forEach(function(s){if(cards[s])cards[s].classList.toggle('active',p.s===s)});
steps.forEach(function(b){b.setAttribute('aria-pressed',String(+b.getAttribute('data-demo-step')===p.s))})}
function stop(){if(timer){clearTimeout(timer);timer=null}}
function tick(){timer=setTimeout(function(){apply((i+1)%phases.length);tick()},hold[i])}
function playing(){return !!timer}
function ui(){if(!playBtn)return;var on=playing();demo.classList.toggle('is-playing',on);
var g=playBtn.querySelector('[data-demo-icon]');if(g)g.textContent=on?'\u2161':'\u25B6';
var t=playBtn.getAttribute(on?'data-pause':'data-play');
var l=playBtn.querySelector('[data-demo-label]');if(l)l.textContent=t;
playBtn.setAttribute('aria-label',t);
playBtn.setAttribute('aria-pressed',String(!on))}
function maybeRun(){stop();if(!userPaused&&visible&&!document.hidden)tick();ui()}
if(playBtn){playBtn.hidden=false;playBtn.addEventListener('click',function(){userPaused=playing();if(userPaused)stop();else maybeRun();ui()})}
steps.forEach(function(b){b.addEventListener('click',function(){userPaused=true;stop();apply(+b.getAttribute('data-demo-step')===1?0:(+b.getAttribute('data-demo-step')===2?1:4));ui()})});
if('IntersectionObserver' in window){new IntersectionObserver(function(es){visible=es[0].isIntersecting;maybeRun()},{threshold:.25}).observe(demo)}
document.addEventListener('visibilitychange',maybeRun);
if(reduce){userPaused=true;apply(4);ui()}else{apply(0);maybeRun()}
})();

/* Value page: two small planning models. Simple arithmetic on the visitor's own numbers;
   mirrors the memorysafe.ca simulator's middle (50%) and 30% what-if scenarios. */
(function(){
var root=document.querySelector('[data-value]');if(!root)return;
var lang=document.documentElement.lang||'en-CA';
var hoursWord=root.getAttribute('data-hours')||'hrs';
var nf=new Intl.NumberFormat(lang,{maximumFractionDigits:0});
var cf=new Intl.NumberFormat(lang,{style:'currency',currency:'CAD',maximumFractionDigits:0});
function num(key){var el=root.querySelector('[data-v="'+key+'"]');var n=el?parseFloat(el.value):0;return isFinite(n)&&n>0?n:0}
function put(key,text){var el=root.querySelector('[data-vo="'+key+'"]');if(el)el.textContent=text}
function calc(){
var lost=num('people')*num('minutes')*52/60;
put('lost',nf.format(Math.round(lost))+' '+hoursWord);
put('returned',nf.format(Math.round(lost*.5))+' '+hoursWord);
put('value',cf.format(Math.round(lost*.5*num('rate'))));
var avoided=num('runs')*num('mins')*365*.3/60;
put('avoided',nf.format(Math.round(avoided))+' '+hoursWord);
put('gross',cf.format(Math.round(avoided*num('cost'))));
}
root.addEventListener('input',calc);
var tabs=[].slice.call(root.querySelectorAll('[data-value-tab]'));
tabs.forEach(function(b){b.addEventListener('click',function(){
tabs.forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});
[].slice.call(root.querySelectorAll('[data-value-panel]')).forEach(function(pn){pn.hidden=pn.getAttribute('data-value-panel')!==b.getAttribute('data-value-tab')})})});
calc();
})();
