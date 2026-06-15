---
title: "lookAtTargetAndPoints static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookattargetandpoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtTargetAndPoints.html -->


<div>
<h1>lookAtTargetAndPoints static method</h1></div>

<a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>
lookAtTargetAndPoints(<ol class="parameter-list"> <li><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a> target, </li>
<li><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a> orientation, </li>
<li>List&lt;<a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>&gt; points, </li>
<li><a href="sdk-for-flutter-explore-core-rectangle2d-class">Rectangle2D</a> viewRectangle, </li>
<li><a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> minMeasure, </li>
<li><a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> maxMeasure, </li>
</ol>)

      

    

<p>Creates an update to position the camera to look at the given target with the given
orientation and obeying map measure limits, so that the given geo locations are inside the given rectangle.</p>
<p>Such position update can possibly not be found.</p>
<p>Any target or orientation sub-element value that is not finite will be excluded from the update.</p>
<p>If the provided <code>MapCameraUpdateFactory.lookAtTargetAndPoints.points</code> list is empty, no update will be applied to the map camera.</p>
<p>If the <code>MapCameraUpdateFactory.lookAtTargetAndPoints.viewRectangle</code> parameter is invalid, fully or partially outside the map view,
then the entire map viewport will be used as <code>MapCameraUpdateFactory.lookAtTargetAndPoints.viewRectangle</code>. Thus, no padding will be applied.
A <code>MapCameraUpdateFactory.lookAtTargetAndPoints.viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
coordinates (x, y) are invalid, when they are negative.</p>
<p>If map measures are not valid, no update will be applied to the map camera.</p>
<p>The altitude of the target points is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>target</code> The look-at target position in geodetic coordinates.</p>
</li>
<li>
<p><code>orientation</code> Geodetic orientation at look-at target.</p>
</li>
<li>
<p><code>points</code> Array of points in geodetic space that should be visible inside the given view rectangle.</p>
</li>
<li>
<p><code>viewRectangle</code> View rectangle in viewport pixel coordinates inside which the geographical points are displayed.</p>
</li>
<li>
<p><code>minMeasure</code> Minimum map measure:</p>
</li>
<li>
<p>as distance: the minimum distance from map camera to earth surface at the look-at target in meters.
The map camera should not be positioned closer to target than this.</p>
</li>
<li>
<p>as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the look-at target in meters.
Can be used to not zoom closer than a given level.</p>
</li>
<li>
<p>as scale: the minimum scale for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the look-at target in meters.</p>
</li>
<li>
<p><code>maxMeasure</code> Maximum map measure:</p>
</li>
<li>
<p>as distance: the maximum distance from map camera to earth surface at the look-at target in meters.
The map camera should not be positioned further from target than this.</p>
</li>
<li>
<p>as zoom level: the minimum zoom level for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the look-at target in meters.
Can be used to not zoom further than a given level.</p>
</li>
<li>
<p>as scale: the maximum scale for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the look-at target in meters.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookAtTargetAndPoints(GeoCoordinatesUpdate target, GeoOrientationUpdate orientation, List&lt;GeoCoordinates&gt; points, Rectangle2D viewRectangle, MapMeasure minMeasure, MapMeasure maxMeasure) =&gt; $prototype.lookAtTargetAndPoints(target, orientation, points, viewRectangle, minMeasure, maxMeasure);</code></pre>

 



</div>
`
}</HTMLBlock>
