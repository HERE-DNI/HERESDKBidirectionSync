---
title: "lookAtAreaWithGeoOrientationAndViewRectangle abstract method"
slug: "sdk-for-flutter-explore-mapview-mapcamera-lookatareawithgeoorientationandviewrectangle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtAreaWithGeoOrientationAndViewRectangle.html -->


<div>
<h1>lookAtAreaWithGeoOrientationAndViewRectangle abstract method</h1></div>

void
lookAtAreaWithGeoOrientationAndViewRectangle(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a> target, </li>
<li><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a> orientation, </li>
<li><a href="sdk-for-flutter-explore-core-rectangle2d-class">Rectangle2D</a> viewRectangle</li>
</ol>)

      

    

<p>Makes the camera look at the specified geodetic area and pass a rectangle which specifies
where the area should appear inside of the map view.</p>
<p>The supplied orientation is the orientation of the camera looking
at the target, so the resulting camera state will have the
same orientation as the one supplied to this method. Please note that
the resulting orientation might deviate from the provided orientation.
This is particularly the case if a large geobox on world level and a
view rectangle which is relatively small was passed to the method.</p>
<p>The altitude of the target points is ignored.</p>
<ul>
<li>
<p><code>target</code> Geodetic area which will be shown in the viewRectangle.</p>
</li>
<li>
<p><code>orientation</code> Desired orientation of the camera.</p>
</li>
<li>
<p><code>viewRectangle</code> The view rectangle in viewport pixel coordinates inside which the geographical target
area is displayed.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void lookAtAreaWithGeoOrientationAndViewRectangle(GeoBox target, GeoOrientationUpdate orientation, Rectangle2D viewRectangle);</code></pre>

 



</div>
`
}</HTMLBlock>
