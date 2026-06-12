---
title: "MapMarker3D.fromImage constructor"
slug: "sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d-fromimage"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3D.fromImage.html -->


<div>
<h1>MapMarker3D.fromImage constructor</h1></div>

MapMarker3D.fromImage(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a> at, </li>
<li><a href="/sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a> image, </li>
<li>double scale, </li>
<li><a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a> unit, </li>
</ol>)
    

<p>Creates a flat marker from provided map image.</p>
<p>Such map marker is a flat 3D marker of rectangular shape textured with given image.
Aspect ratio of the flat marker is determined by aspect ratio of the image.</p>
<p>Only bitmap images are supported, using a <a href="/sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a> created from SVG data
will result in distorted rendering of the flat marker.</p>
<p>Altitude component of the coordinates, if set, controls 3D marker's elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
<p>Size of the rendered flat marker can be specified in either world or screen coordinate space.</p>
<p>For <a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.pixels</a>, the flat marker will cover <code>MapMarker3D.fromImage.scale</code> * image's width pixels
horizontally and <code>MapMarker3D.fromImage.scale</code> * image's height pixels vertically. The size of the flat marker
remains constant on the screen.</p>
<p>For <a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.densityIndependentPixels</a> the flat marker will cover <code>MapMarker3D.fromImage.scale</code> *
image's width density independent pixels horizontally and <code>MapMarker3D.fromImage.scale</code> * image's height
density independent pixels vertically. The size of the flat marker remains constant on
the screen.</p>
<p>For <a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.meters</a> the flat marker will cover <code>MapMarker3D.fromImage.scale</code> * image's width meters
horizontally and <code>MapMarker3D.fromImage.scale</code> * image's height meters vertically. Unlike with pixels or
density independent pixels the size of the flat marker will grow and shrink together
with regular map content like streets or buildings.</p>
<ul>
<li>
<p><code>at</code> The geographical coordinates where the flat marker is placed corresponding to center of the
provided map image.</p>
</li>
<li>
<p><code>image</code> The MapImage containing the texture data of the flat marker. SVG images are not supported.</p>
</li>
<li>
<p><code>scale</code> Scale factor applied to the dimensions of the image.</p>
</li>
<li>
<p><code>unit</code> Determines whether the size of the flat marker is represented in world or in screen space.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMarker3D.fromImage(GeoCoordinates at, MapImage image, double scale, RenderSizeUnit unit) =&gt; $prototype.fromImage(at, image, scale, unit);</code></pre>

 



</div>
`
}</HTMLBlock>
