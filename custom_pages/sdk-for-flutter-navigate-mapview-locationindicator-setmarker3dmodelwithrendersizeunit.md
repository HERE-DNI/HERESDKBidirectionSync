---
title: "setMarker3dModelWithRenderSizeUnit abstract method"
slug: "sdk-for-flutter-navigate-mapview-locationindicator-setmarker3dmodelwithrendersizeunit"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setMarker3dModelWithRenderSizeUnit.html -->


<div>
<h1>setMarker3dModelWithRenderSizeUnit abstract method</h1></div>

void
setMarker3dModelWithRenderSizeUnit(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a> model, </li>
<li>double scale, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-locationindicatormarkertype">LocationIndicatorMarkerType</a> type, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a> renderSizeUnit, </li>
</ol>)

      

    

<p>Sets the <a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a> asset to be displayed as location indicator for a specified type.</p>
<p>The 3D model should be oriented with y axis up and thus standing on the x/z plane where the
z axis is the depth. The direction in which the location indicator is pointing is the
positive z axis. Please note that only <a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a> created from <code>obj</code> files are
supported. Models created from Mesh will be ignored.</p>
<ul>
<li>
<p><code>model</code> The <a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a> object to be displayed for the specified type. Only models
created from <code>obj</code> files are supported. Those created from mesh will be ignored.</p>
</li>
<li>
<p><code>scale</code> A scale factor applied to the marker model.</p>
</li>
<li>
<p><code>type</code> The type of location marker for which the marker 3d model should be replaced.</p>
</li>
<li>
<p><code>renderSizeUnit</code> The <a href="/sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a> specifying how the vertex coordinates of the
3D model are being interpreted. It specifies whether the 3D model is placed in world or
screen coordinate space.</p>
</li>
</ul>
<p><a href="/sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.meters</a> will make the 3D model use world
coordinate space, meaning that it will change size together with the map
when it is zoomed in and out. A simple 10 by 10 by 10 (in model space) cube
will have a size of 10 by 10 by 10 meters in world space.</p>
<p><a href="/sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.pixels</a> makes the 3D model use screen coordinate space,
meaning that it will have constant size on the screen regardless
of how the map zoom changes. A simple 10 by 10 (in model space) rectangle
will have a size of 10 by 10 pixels on the screen.</p>
<p><a href="/sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.densityIndependentPixels</a> is similar to pixels,
but the resulting size will take into account the pixel density of the
display, meaning that physical size on the screen will be approximately
the same regardless of the size or resolution of the display.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setMarker3dModelWithRenderSizeUnit(MapMarker3DModel model, double scale, LocationIndicatorMarkerType type, RenderSizeUnit renderSizeUnit);</code></pre>

 



</div>
`
}</HTMLBlock>
