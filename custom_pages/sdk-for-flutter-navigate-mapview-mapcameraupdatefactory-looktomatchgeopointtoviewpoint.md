---
title: "lookToMatchGeoPointToViewPoint static method"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-looktomatchgeopointtoviewpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookToMatchGeoPointToViewPoint.html -->


<div>
<h1>lookToMatchGeoPointToViewPoint static method</h1></div>

<a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>
lookToMatchGeoPointToViewPoint(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> geoPoint, </li>
<li><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a> viewPoint</li>
</ol>)

      

    

<p>Creates an update to position the map camera to look at the map
with the given geo point located at the given view point.</p>
<p>Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
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
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookToMatchGeoPointToViewPoint(GeoCoordinates geoPoint, Point2D viewPoint) =&gt; $prototype.lookToMatchGeoPointToViewPoint(geoPoint, viewPoint);</code></pre>

 



</div>
`
}</HTMLBlock>
