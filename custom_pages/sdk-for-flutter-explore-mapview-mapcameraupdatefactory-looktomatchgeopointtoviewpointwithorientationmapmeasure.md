---
title: "lookToMatchGeoPointToViewPointWithOrientationMapMeasure static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-looktomatchgeopointtoviewpointwithorientationmapmeasure"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookToMatchGeoPointToViewPointWithOrientationMapMeasure.html -->


<div>
<h1>lookToMatchGeoPointToViewPointWithOrientationMapMeasure static method</h1></div>

<a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>
lookToMatchGeoPointToViewPointWithOrientationMapMeasure(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a> geoPoint, </li>
<li><a href="/sdk-for-flutter-explore-core-point2d-class">Point2D</a> viewPoint, </li>
<li><a href="/sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a> orientation, </li>
<li><a href="/sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> measure, </li>
</ol>)

      

    

<p>Creates an update to position the map camera to look at the map with the given
orientation and map measure and with the given geo point located at the given view point.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<p>Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>geoPoint</code> The geo point that will be matched to the given view point.
Note: the geo point will differ from the look at target of the camera. After this update the camera
will still look at the principal point and therefore the look at target will be different from the geo
point, since the geo point will correspond to the given view point and the look at target
will correspond to the principal point. Look at target and the geo point will be identical only
if the given view point is identical to the principal point.</p>
</li>
<li>
<p><code>viewPoint</code> View point coordinates in pixels.</p>
</li>
<li>
<p><code>orientation</code> Geodetic orientation at look-at target.</p>
</li>
<li>
<p><code>measure</code> The desired map measure.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookToMatchGeoPointToViewPointWithOrientationMapMeasure(GeoCoordinates geoPoint, Point2D viewPoint, GeoOrientationUpdate orientation, MapMeasure measure) =&gt; $prototype.lookToMatchGeoPointToViewPointWithOrientationMapMeasure(geoPoint, viewPoint, orientation, measure);</code></pre>

 



</div>
`
}</HTMLBlock>
