---
title: "tiltRange property"
slug: "sdk-for-flutter-explore-mapview-mapcameralimits-tiltrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- tiltRange.html -->


<div>
<h1>tiltRange property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a>
tiltRange


<p>The tilt range that can be applied to the camera.
Gets the current tilt range.</p>
<p>By default, a <a href="sdk-for-flutter-explore-mapview-mapcameralimits-mintilt">MapCameraLimits.minTilt</a>-<a href="sdk-for-flutter-explore-mapview-mapcameralimits-maxtilt">MapCameraLimits.maxTilt</a> tilt range is set during initialization.</p>
<p>This range might not be yet active if no rendering loop has been executed since the last call to set the range.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">AngleRange get tiltRange;</code></pre>

</section>
<section id="setter">

void
tiltRange=(<a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a> value)


<p>The tilt range that can be applied to the camera.
Sets a new tilt limit range.</p>
<p>The supported values fall inside <a href="sdk-for-flutter-explore-mapview-mapcameralimits-mintilt">MapCameraLimits.minTilt</a>-<a href="sdk-for-flutter-explore-mapview-mapcameralimits-maxtilt">MapCameraLimits.maxTilt</a> range.
Values outside the supported range are ignored.</p>
<p>If the current camera tilt exceeds the new limit range, it will immediately be set to minimum or maximum,
depending on which is closest.</p>
<p>This new limit range becomes active during the next rendering loop.</p>
<p>All previously set tilt ranges are cleared and the new tilt range is applied for all zoom values.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set tiltRange(AngleRange value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
