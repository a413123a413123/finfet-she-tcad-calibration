(function(){
 var rows=[].slice.call(document.querySelectorAll('.row'));
 var F={ch:new Set(),cite:new Set(),acc:new Set(),meth:new Set(),src:new Set(),flag:new Set()};
 var q='';
 var cnt=document.getElementById('cnt');

 function apply(){
  var n=0;
  rows.forEach(function(r){
   var d=r.dataset,ok=true,k;
   for(k in F){ if(F[k].size && !F[k].has(d[k])) ok=false; }
   if(ok && q && d.q.indexOf(q)<0) ok=false;
   r.classList.toggle('hide',!ok);
   if(ok) n++;
  });
  cnt.textContent=n+' / '+rows.length+' 篇';
 }

 document.querySelectorAll('.chip[data-k]').forEach(function(b){
  b.addEventListener('click',function(){
   var on=b.getAttribute('aria-pressed')==='true';
   b.setAttribute('aria-pressed',on?'false':'true');
   var s=F[b.dataset.k];
   if(on){ s.delete(b.dataset.v); } else { s.add(b.dataset.v); }
   apply();
  });
 });

 document.getElementById('q').addEventListener('input',function(ev){
  q=ev.target.value.toLowerCase().trim(); apply();
 });

 document.getElementById('reset').addEventListener('click',function(){
  for(var k in F){ F[k].clear(); }
  document.querySelectorAll('.chip[data-k]').forEach(function(b){b.setAttribute('aria-pressed','false');});
  document.getElementById('q').value=''; q=''; apply();
 });

 rows.forEach(function(r){
  var hd=r.querySelector('.hd');
  hd.addEventListener('click',function(){
   var o=r.classList.toggle('open');
   hd.setAttribute('aria-expanded',o?'true':'false');
  });
 });

 var allOpen=false;
 var ta=document.getElementById('toggleAll');
 ta.addEventListener('click',function(){
  allOpen=!allOpen;
  rows.forEach(function(r){
   if(r.classList.contains('hide')) return;
   r.classList.toggle('open',allOpen);
   r.querySelector('.hd').setAttribute('aria-expanded',allOpen?'true':'false');
  });
  ta.textContent=allOpen?'全部收合':'全部展開';
 });

 var list=document.getElementById('list');
 document.getElementById('sort').addEventListener('change',function(ev){
  var m=ev.target.value,a=rows.slice();
  if(m==='yr'){ a.sort(function(x,y){return (+y.dataset.yr)-(+x.dataset.yr);}); }
  else if(m==='cite'){ a.sort(function(x,y){
    var c=x.dataset.cite.localeCompare(y.dataset.cite);
    return c!==0?c:(x.dataset.ord-y.dataset.ord);}); }
  else { a.sort(function(x,y){return x.dataset.ord-y.dataset.ord;}); }
  a.forEach(function(r){list.appendChild(r);});
 });

 document.querySelectorAll('a[data-goto]').forEach(function(a){
  a.addEventListener('click',function(ev){
   ev.preventDefault();
   var r=document.querySelector('.row[data-id="'+a.dataset.goto+'"]');
   if(!r) return;
   r.classList.remove('hide');
   r.classList.add('open');
   r.querySelector('.hd').setAttribute('aria-expanded','true');
   r.scrollIntoView({block:'center',behavior:'smooth'});
  });
 });
})();
