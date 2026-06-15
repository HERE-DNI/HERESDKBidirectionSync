---
title: "lookAtPointWithGeoOrientationAndMeasure static method"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatpointwithgeoorientationandmeasure"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtPointWithGeoOrientationAndMeasure.html -->


<div>
<h1>lookAtPointWithGeoOrientationAndMeasure static method</h1></div>

<a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>
lookAtPointWithGeoOrientationAndMeasure(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a> target, </li>
<li><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a> orientation, </li>
<li><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> measure</li>
</ol>)

      

    

<p>Creates an update to position the map camera to look at the given target with the given
orientation and map measure.</p>
<p>Any target or orientation sub-element value that is not finite will be excluded from the update.
If the map measure is not valid, the current map camera distance to the target point is preserved.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>target</code> The look-at target position in geodetic coordinates.</p>
</li>
<li>
<p><code>orientation</code> Geodetic orientation at look-at target.</p>
</li>
<li>
<p><code>measure</code> The desired map measure.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookAtPointWithGeoOrientationAndMeasure(GeoCoordinatesUpdate target, GeoOrientationUpdate orientation, MapMeasure measure) =&gt; $prototype.lookAtPointWithGeoOrientationAndMeasure(target, orientation, measure);</code></pre>

 



</div>
`
}</HTMLBlock>
