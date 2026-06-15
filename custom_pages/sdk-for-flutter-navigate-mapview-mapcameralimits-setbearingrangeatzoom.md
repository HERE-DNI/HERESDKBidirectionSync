---
title: "setBearingRangeAtZoom abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapcameralimits-setbearingrangeatzoom"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setBearingRangeAtZoom.html -->


<div>
<h1>setBearingRangeAtZoom abstract method</h1></div>

void
setBearingRangeAtZoom(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> zoom, </li>
<li><a href="sdk-for-flutter-navigate-core-anglerange-class">AngleRange</a> bearingRange</li>
</ol>)

      

    

<p>Sets the bearing range within which the camera can rotate at a given zoom.</p>
<p>The resulting camera bearing at a zoom is an interpolated value of the ranges set for closest matching zoom values.
When no bearing range is specified for <a href="sdk-for-flutter-navigate-mapview-mapcameralimits-minzoomlevel">MapCameraLimits.minZoomLevel</a>, the bearing range set through
<a href="sdk-for-flutter-navigate-mapview-mapcameralimits-bearingrange">MapCameraLimits.bearingRange</a> is used for interpolation.</p>
<p>Zoom values outside the supported zoom range are ignored.
By default, the maximum bearing range for all zoom values is set during initialization.</p>
<ul>
<li>
<p><code>zoom</code> Zoom at which the range is set.</p>
</li>
<li>
<p><code>bearingRange</code> Bearing range.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setBearingRangeAtZoom(MapMeasure zoom, AngleRange bearingRange);</code></pre>

 



</div>
`
}</HTMLBlock>
