---
title: "lookAtPoints static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtPoints.html -->


<div>
<h1>lookAtPoints static method</h1></div>

<a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>
lookAtPoints(<ol class="parameter-list"> <li>List&lt;<a href="/sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>&gt; points, </li>
<li><a href="/sdk-for-flutter-explore-core-rectangle2d-class">Rectangle2D</a> viewRectangle, </li>
<li><a href="/sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a> orientation, </li>
<li><a href="/sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> measureLimit, </li>
</ol>)

      

    

<p>Create an update to look at the given geo locations and fit them inside the given rectangle,
in accordance with a map measure limit.</p>
<p>If the provided <code>MapCameraUpdateFactory.lookAtPoints.points</code> list is empty, no update will be applied to the camera.</p>
<p>If the <code>MapCameraUpdateFactory.lookAtPoints.viewRectangle</code> parameter is invalid, fully or partially outside the map view,
then the entire map viewport will be used as <code>MapCameraUpdateFactory.lookAtPoints.viewRectangle</code>. Thus, no padding will be applied.
A <code>MapCameraUpdateFactory.lookAtPoints.viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
coordinates (x, y) are invalid, when they are negative.</p>
<p>All <code>MapCameraUpdateFactory.lookAtPoints.viewRectangle</code> values need to be finite to be considered as valid.
If measure limit is not valid, no update will be applied to the map camera.</p>
<p>The altitude of the target points is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>points</code> Array of points in geodetic space that should be visible inside the given view rectangle.</p>
</li>
<li>
<p><code>viewRectangle</code> View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.</p>
</li>
<li>
<p><code>orientation</code> Geodetic orientation at the new calculated target point.</p>
</li>
<li>
<p><code>measureLimit</code> Map measure limit:</p>
</li>
<li>
<p>as distance: the minimum distance from map camera to earth surface at the center of the view rectangle in meters.
The map camera should not be positioned closer to the center of view rectangle than this.</p>
</li>
<li>
<p>as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the center of view rectangle in meters. This is not the zoom level for
the calculated lookAt target point. Can be used to not zoom closer than a given level.</p>
</li>
<li>
<p>as scale: the minimum scale for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the center of view rectangle in meters. This is not the scale for
the calculated lookAt target point.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookAtPoints(List&lt;GeoCoordinates&gt; points, Rectangle2D viewRectangle, GeoOrientationUpdate orientation, MapMeasure measureLimit) =&gt; $prototype.lookAtPoints(points, viewRectangle, orientation, measureLimit);</code></pre>

 



</div>
`
}</HTMLBlock>
