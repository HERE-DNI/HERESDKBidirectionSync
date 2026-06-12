---
title: "MapMarker.withAnchor constructor"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-mapmarker-withanchor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker.withAnchor.html -->


<div>
<h1>MapMarker.withAnchor constructor</h1></div>

MapMarker.withAnchor(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> coordinates, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a> image, </li>
<li><a href="/sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a> anchor</li>
</ol>)
    

<p>Creates an instance of a marker at given coordinates, represented by specified image,
with anchor point specifying how the image is positioned relative to the marker's coordinates.</p>
<p>The anchor is a way of specifying position offset relative to image's dimensions on the screen.
For example, (0, 0) places the top-left corner of the image at the marker's coordinates.
(1, 1) would place the bottom-right corner of the image at the marker's coordinates.
(0.5, 0.5) which is the default value would center the image at the marker's coordinates.
Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
centered horizontally with its bottom edge above the marker's coordinates at the distance
in pixels that is equal to the height of the image.</p>
<ul>
<li>
<p><code>coordinates</code> The marker's geographical coordinates.</p>
</li>
<li>
<p><code>image</code> The image to draw on the map.</p>
</li>
<li>
<p><code>anchor</code> The anchor point for the marker image which specifies the position offset relative
to the marker's coordinates.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMarker.withAnchor(GeoCoordinates coordinates, MapImage image, Anchor2D anchor) =&gt; $prototype.withAnchor(coordinates, image, anchor);</code></pre>

 



</div>
`
}</HTMLBlock>
