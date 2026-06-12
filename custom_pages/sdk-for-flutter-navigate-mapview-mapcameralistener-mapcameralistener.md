---
title: "MapCameraListener constructor"
slug: "sdk-for-flutter-navigate-mapview-mapcameralistener-mapcameralistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraListener.html -->


<div>
<h1>MapCameraListener constructor</h1></div>

MapCameraListener(<ol class="parameter-list single-line"> <li>void onMapCameraUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-mapcamerastate-class">MapCameraState</a></li>
</ol>)</li>
</ol>)
    

<p>Abstract class for objects that want to get updates whenever the map is redrawn after
camera parameters change.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapCameraListener(
  void Function(MapCameraState) onMapCameraUpdatedLambda,

) =&gt; MapCameraListener$Lambdas(
  onMapCameraUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
