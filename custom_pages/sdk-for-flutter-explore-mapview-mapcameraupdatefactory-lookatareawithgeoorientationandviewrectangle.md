---
title: "lookAtAreaWithGeoOrientationAndViewRectangle static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatareawithgeoorientationandviewrectangle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtAreaWithGeoOrientationAndViewRectangle.html -->


<div>
<h1>lookAtAreaWithGeoOrientationAndViewRectangle static method</h1></div>

<a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>
lookAtAreaWithGeoOrientationAndViewRectangle(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a> target, </li>
<li><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a> orientation, </li>
<li><a href="sdk-for-flutter-explore-core-rectangle2d-class">Rectangle2D</a> viewRectangle</li>
</ol>)

      

    

<p>Create an update to look at the given geo-box and fit it inside the given rectangle.</p>
<p>If geoBox is not valid, no update will be applied to the map camera.</p>
<p>If the <code>MapCameraUpdateFactory.lookAtAreaWithGeoOrientationAndViewRectangle.viewRectangle</code> parameter is invalid, fully or partially outside the map view,
then the entire map viewport will be used as <code>MapCameraUpdateFactory.lookAtAreaWithGeoOrientationAndViewRectangle.viewRectangle</code>. Thus, no padding will be applied.
A <code>MapCameraUpdateFactory.lookAtAreaWithGeoOrientationAndViewRectangle.viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
coordinates (x, y) are invalid, when they are negative.</p>
<p>All <code>MapCameraUpdateFactory.lookAtAreaWithGeoOrientationAndViewRectangle.viewRectangle</code> values need to be finite to be considered as valid.</p>
<p>In cases where it is not possible to find a solution for the given parameters,
the resulting MapCameraUpdate will not change the map camera.</p>
<p>The altitude of the target points is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>target</code> Geodetic box that should be visible inside the given view rectangle.</p>
</li>
<li>
<p><code>orientation</code> Geodetic orientation at the target point.</p>
</li>
<li>
<p><code>viewRectangle</code> View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookAtAreaWithGeoOrientationAndViewRectangle(GeoBox target, GeoOrientationUpdate orientation, Rectangle2D viewRectangle) =&gt; $prototype.lookAtAreaWithGeoOrientationAndViewRectangle(target, orientation, viewRectangle);</code></pre>

 



</div>
`
}</HTMLBlock>
