---
title: "pause abstract method"
slug: "sdk-for-flutter-explore-mapview-heremapcontroller-pause"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- pause.html -->


<div>
<h1>pause abstract method</h1></div>

void
pause()

      

    

<p>Pauses the map widget.</p>
<p>A paused map widget stops rendering updates until it gets resumed. It is recommended to not schedule
any map updates while in the paused state as they are cached in-memory and will pile-up until the
map widget gets resumed.</p>
<p>By default, the map widget gets automatically paused and resumed based on platform specific
events (e.g. client application going into background/foreground). Once this method gets called,
the automatic behavior gets disabled.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void pause();</code></pre>

 



</div>
`
}</HTMLBlock>
