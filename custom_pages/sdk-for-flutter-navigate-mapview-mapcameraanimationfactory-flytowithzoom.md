---
title: "flyToWithZoom static method"
slug: "sdk-for-flutter-navigate-mapview-mapcameraanimationfactory-flytowithzoom"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- flyToWithZoom.html -->


<div>
<h1>flyToWithZoom static method</h1></div>

<a href="/sdk-for-flutter-navigate-mapview-mapcameraanimation-class">MapCameraAnimation</a>
flyToWithZoom(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a> target, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> zoom, </li>
<li>double bowFactor, </li>
<li>Duration duration, </li>
</ol>)

      

    

<p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.</p>
<p>The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom.</p>
<p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>target</code> The coordinates of the camera destination point.
Any target sub-element value that is not finite will be set to the current camera target sub-element value.
Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</li>
<li>
<p><code>zoom</code> The zoom at the end of the animation.</p>
</li>
<li>
<p><code>bowFactor</code> A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.</p>
</li>
</ul>
<p>The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
curve is relative to the travel distance between current camera target and destination target.</p>
<p>A bow factor of 0 does not affect the camera's zoom over time.</p>
<p>Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.</p>
<p>The bow factor is clamped to [-1, +1].</p>
<p>Note that the lowest possible camera distance to earth is 0 meters and that the animation
curve will not go below this value.</p>
<p>Note that currently, bow factor is ignored and assumed to be 1 if either start or end
of animation has a non zero tilt.</p>
<ul>
<li><code>duration</code> Duration of the flight. Negative duration results in no camera change when applied.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-mapview-mapcameraanimation-class">MapCameraAnimation</a>. MapCameraAnimation instance</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraAnimation flyToWithZoom(GeoCoordinatesUpdate target, MapMeasure zoom, double bowFactor, Duration duration) =&gt; $prototype.flyToWithZoom(target, zoom, bowFactor, duration);</code></pre>

 



</div>
`
}</HTMLBlock>
