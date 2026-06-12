---
title: "lookAtAreaWithViewRectangle static method"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatareawithviewrectangle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtAreaWithViewRectangle.html -->


<div>
<h1>lookAtAreaWithViewRectangle static method</h1></div>

<a href="/sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>
lookAtAreaWithViewRectangle(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geobox-class">GeoBox</a> target, </li>
<li><a href="/sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a> viewRectangle</li>
</ol>)

      

    

<p>Creates an update to look at the given geo-box and fit it inside the given rectangle,
preserving current orientation and zooming at the center of view rectangle.</p>
<p>If geoBox is not valid, no update will be applied to the map camera.</p>
<p>If the <code>MapCameraUpdateFactory.lookAtAreaWithViewRectangle.viewRectangle</code> parameter is invalid, fully or partially outside the map view,
then the entire map viewport will be used as <code>MapCameraUpdateFactory.lookAtAreaWithViewRectangle.viewRectangle</code>. Thus, no padding will be applied.
A <code>MapCameraUpdateFactory.lookAtAreaWithViewRectangle.viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
coordinates (x, y) are invalid, when they are negative.</p>
<p>In cases where it is not possible to find a solution for the given parameters,
the resulting MapCameraUpdate will not change the map camera.</p>
<p>The altitude of the target points is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<ul>
<li>
<p><code>target</code> Geodetic box that should be visible inside the given view rectangle.</p>
</li>
<li>
<p><code>viewRectangle</code> View rectangle in viewport pixel coordinates.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate lookAtAreaWithViewRectangle(GeoBox target, Rectangle2D viewRectangle) =&gt; $prototype.lookAtAreaWithViewRectangle(target, viewRectangle);</code></pre>

 



</div>
`
}</HTMLBlock>
