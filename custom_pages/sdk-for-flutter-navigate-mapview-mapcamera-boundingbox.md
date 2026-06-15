---
title: "boundingBox property"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-boundingbox"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- boundingBox.html -->


<div>
<h1>boundingBox property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>?
boundingBox


<p>Currently visible map area encompassed in a GeoBox.
Note that this bounding box is always rectangular, and its sides are always
parallel to the latitude and longitude. If the camera is rotated, the returned
bounding box will be a circumscribed rectangle that is larger than the
visible map area. Similarly, when the map is tilted (for example, if
the map is tilted by 45 degrees), the visible map area represents
a trapezoidal area in the world. Resulting value will then be a larger
circumscribed rectangle that contains this trapezoid area.
Because on this, corners of the resulting bounding box may be located
outside of the currently visible area.</p>
<p>When the map area does not fully fill the viewport, <code>null</code> is returned.
Gets the current visible map area encompassed in a GeoBox.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoBox? get boundingBox;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
