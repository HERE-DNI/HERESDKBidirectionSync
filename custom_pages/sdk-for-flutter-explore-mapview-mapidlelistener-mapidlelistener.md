---
title: "MapIdleListener constructor"
slug: "sdk-for-flutter-explore-mapview-mapidlelistener-mapidlelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapIdleListener.html -->


<div>
<h1>MapIdleListener constructor</h1></div>

MapIdleListener(<ol class="parameter-list single-line"> <li>void onMapBusyLambda(), </li>
<li>void onMapIdleLambda()</li>
</ol>)
    

<p>Used to detect when the map becomes idle or busy.</p>
<p>Map is considered busy when its state changes (for example as a result of camera manipulation)
and/or when it requires a redraw (for example, as a result of map data being downloaded).</p>
<p>Map is considered idle when current state is fully rendered and no further
redraws are necessary.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapIdleListener(
  void Function() onMapBusyLambda,
  void Function() onMapIdleLambda,

) =&gt; MapIdleListener$Lambdas(
  onMapBusyLambda,
  onMapIdleLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
