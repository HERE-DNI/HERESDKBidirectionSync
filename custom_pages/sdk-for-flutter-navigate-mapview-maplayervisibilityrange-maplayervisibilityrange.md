---
title: "MapLayerVisibilityRange constructor"
slug: "sdk-for-flutter-navigate-mapview-maplayervisibilityrange-maplayervisibilityrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapLayerVisibilityRange.html -->


<div>
<h1>MapLayerVisibilityRange constructor</h1></div>

      const
      MapLayerVisibilityRange(<ol class="parameter-list single-line"> <li>double minimumZoomLevel, </li>
<li>double maximumZoomLevel</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>minimumZoomLevel</code> Minimum zoom level on which the layer will be visible. The value must be greater than or equal to the <code>MapCameraLimits.MIN_ZOOM_LEVEL</code>.</li>
<li><code>maximumZoomLevel</code> Minimum zoom level from which the layer will not be visible. The value must be less than or equal to the <code>MapCameraLimits.MAX_ZOOM_LEVEL</code>.
Note that the map layer is not visible at the maximum zoom level.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">const MapLayerVisibilityRange(this.minimumZoomLevel, this.maximumZoomLevel);</code></pre>

 



</div>
`
}</HTMLBlock>
