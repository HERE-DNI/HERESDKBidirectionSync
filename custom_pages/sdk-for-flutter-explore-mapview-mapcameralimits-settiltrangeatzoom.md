---
title: "setTiltRangeAtZoom abstract method"
slug: "sdk-for-flutter-explore-mapview-mapcameralimits-settiltrangeatzoom"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setTiltRangeAtZoom.html -->


<div>
<h1>setTiltRangeAtZoom abstract method</h1></div>

void
setTiltRangeAtZoom(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> zoom, </li>
<li><a href="/sdk-for-flutter-explore-core-anglerange-class">AngleRange</a> tiltRange</li>
</ol>)

      

    

<p>Sets tilt ranges that can be set on the camera at given zoom.</p>
<p>The resulting camera tilt at a zoom is an interpolated value of the ranges set for closest matching zoom values.
When no tilt range is specified for <a href="/sdk-for-flutter-explore-mapview-mapcameralimits-minzoomlevel">MapCameraLimits.minZoomLevel</a>, the tilt range set through <a href="/sdk-for-flutter-explore-mapview-mapcameralimits-tiltrange">MapCameraLimits.tiltRange</a> is used for interpolation.</p>
<p>Zoom or tilt values outside the supported zoom and tilt range are ignored.
By default, the maximum tilt range for all zoom values is set during initialization.</p>
<ul>
<li>
<p><code>zoom</code> Zoom at which the range is set.</p>
</li>
<li>
<p><code>tiltRange</code> Tilt range.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setTiltRangeAtZoom(MapMeasure zoom, AngleRange tiltRange);</code></pre>

 



</div>
`
}</HTMLBlock>
