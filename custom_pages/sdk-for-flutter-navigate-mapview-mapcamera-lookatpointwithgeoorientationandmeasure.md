---
title: "lookAtPointWithGeoOrientationAndMeasure abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-lookatpointwithgeoorientationandmeasure"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtPointWithGeoOrientationAndMeasure.html -->


<div>
<h1>lookAtPointWithGeoOrientationAndMeasure abstract method</h1></div>

void
lookAtPointWithGeoOrientationAndMeasure(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> target, </li>
<li><a href="/sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a> orientation, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> zoom</li>
</ol>)

      

    

<p>Makes the camera look at the geodetic target with the given zoom and orientation.</p>
<p>The supplied orientation is the orientation of the camera looking
at the target, so the resulting camera state will have the
same orientation as the one supplied to this method.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>target</code> Geodetic coordinates at which the camera will point.</p>
</li>
<li>
<p><code>orientation</code> Desired orientation of the camera.</p>
</li>
<li>
<p><code>zoom</code> The zoom level which can be provided as distance to the target point, scale or
zoom level.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void lookAtPointWithGeoOrientationAndMeasure(GeoCoordinates target, GeoOrientationUpdate orientation, MapMeasure zoom);</code></pre>

 



</div>
`
}</HTMLBlock>
