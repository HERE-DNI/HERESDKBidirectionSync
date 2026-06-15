---
title: "MapImageOverlay.withAnchor constructor"
slug: "sdk-for-flutter-explore-mapview-mapimageoverlay-mapimageoverlay-withanchor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapImageOverlay.withAnchor.html -->


<div>
<h1>MapImageOverlay.withAnchor constructor</h1></div>

MapImageOverlay.withAnchor(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a> viewCoordinates, </li>
<li><a href="sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a> image, </li>
<li><a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a> anchor</li>
</ol>)
    

<p>Creates an instance of an overlay at given view coordinates, represented by specified image,
with anchor point specifying how the image is positioned relative to the overlay's view coordinates.</p>
<p>The anchor is a way of specifying position offset relative to image's dimensions on the view.
For example, (0, 0) places the top-left corner of the image at the overlay's view coordinates.
(1, 1) would place the bottom-right corner of the image at the overlay's view coordinates.
(0.5, 0.5) which is the default value would center the image at the overlay's view coordinates.</p>
<p>Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
centered horizontally with its bottom edge above the overlay's view coordinates at the distance
in pixels that is equal to the height of the image.</p>
<ul>
<li>
<p><code>viewCoordinates</code> The overlay's view coordinates in pixels.</p>
</li>
<li>
<p><code>image</code> The image to draw on the map.</p>
</li>
<li>
<p><code>anchor</code> The anchor point for the overlay image which specifies the position offset relative
to the overlay's view coordinates.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapImageOverlay.withAnchor(Point2D viewCoordinates, MapImage image, Anchor2D anchor) =&gt; $prototype.withAnchor(viewCoordinates, image, anchor);</code></pre>

 



</div>
`
}</HTMLBlock>
