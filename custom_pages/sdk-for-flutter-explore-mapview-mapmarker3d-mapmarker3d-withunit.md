---
title: "MapMarker3D.withUnit constructor"
slug: "sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d-withunit"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3D.withUnit.html -->


<div>
<h1>MapMarker3D.withUnit constructor</h1></div>

MapMarker3D.withUnit(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a> at, </li>
<li><a href="/sdk-for-flutter-explore-mapview-mapmarker3dmodel-class">MapMarker3DModel</a> model, </li>
<li>double scale, </li>
<li><a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a> unit, </li>
</ol>)
    

<p>Creates a new 3D marker at given world coordinates, using the supplied 3D model.</p>
<p>The unit specifies how the 3D geometry of the model is interpreted (meters for world space,
pixels or density independent pixels for screen space), while scale determines its relative size.</p>
<p>For <a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.pixels</a> one unit of the 3D marker model will cover <code>MapMarker3D.withUnit.scale</code> pixels.
The size of the 3D marker remains constant on the screen.</p>
<p>For <a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.densityIndependentPixels</a> one unit of the 3D marker model will
cover <code>MapMarker3D.withUnit.scale</code> density independent pixels. The size of the 3D marker remains constant on
the screen.</p>
<p>For <a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.meters</a> one unit of the 3D marker model will cover <code>MapMarker3D.withUnit.scale</code> meters
in the real world. Unlike with pixels or density-independent pixels the size of the
3D marker will grow and shrink together with regular map content like streets or buildings.</p>
<p>The origin of the 3D model's local coordinate system is placed at the specified
geographical coordinates.</p>
<p>Altitude component of the coordinates, if set, controls 3D marker's elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
<ul>
<li>
<p><code>at</code> The geographical coordinates where the 3D marker is placed corresponding to origin of the
3D model's local coordinate system.</p>
</li>
<li>
<p><code>model</code> The 3D model used to render the 3D marker.</p>
</li>
<li>
<p><code>scale</code> Scale factor to apply to the 3D model.</p>
</li>
<li>
<p><code>unit</code> Determines the unit of the model vertices and whether the size of the 3D marker
is expressed in world or screen space.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMarker3D.withUnit(GeoCoordinates at, MapMarker3DModel model, double scale, RenderSizeUnit unit) =&gt; $prototype.withUnit(at, model, scale, unit);</code></pre>

 



</div>
`
}</HTMLBlock>
