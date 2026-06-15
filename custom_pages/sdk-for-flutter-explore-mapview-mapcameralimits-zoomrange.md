---
title: "zoomRange property"
slug: "sdk-for-flutter-explore-mapview-mapcameralimits-zoomrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- zoomRange.html -->


<div>
<h1>zoomRange property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-explore-mapview-mapmeasurerange-class">MapMeasureRange</a>
zoomRange


<p>The zoom range that can be applied to the camera.
Gets the currently set camera zoom range.</p>
<p>By default, a <a href="sdk-for-flutter-explore-mapview-mapcameralimits-minzoomlevel">MapCameraLimits.minZoomLevel</a>-<a href="sdk-for-flutter-explore-mapview-mapcameralimits-maxzoomlevel">MapCameraLimits.maxZoomLevel</a> zoom range is set during initialization.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMeasureRange get zoomRange;</code></pre>

</section>
<section id="setter">

void
zoomRange=(<a href="sdk-for-flutter-explore-mapview-mapmeasurerange-class">MapMeasureRange</a> value)


<p>The zoom range that can be applied to the camera.
Sets a new camera zoom range.</p>
<p>The supported values fall inside <a href="sdk-for-flutter-explore-mapview-mapcameralimits-minzoomlevel">MapCameraLimits.minZoomLevel</a>-<a href="sdk-for-flutter-explore-mapview-mapcameralimits-maxzoomlevel">MapCameraLimits.maxZoomLevel</a> range.
Values outside the supported zoom range are ignored.</p>
<p>If the current camera zoom exceeds the limit range, it will immediately be set to minimum or maximum, depending on which is closest.</p>
<p>This new limit range becomes active during the next rendering loop.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set zoomRange(MapMeasureRange value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
