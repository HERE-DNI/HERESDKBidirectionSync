---
title: "setMarker3dModel abstract method"
slug: "sdk-for-flutter-explore-mapview-locationindicator-setmarker3dmodel"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setMarker3dModel.html -->


<div>
<h1>setMarker3dModel abstract method</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.27.0. Please use the setMarker3dModelWithRenderSizeUnit instead.")</li>
</ol>
</div>
void
setMarker3dModel(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-class">MapMarker3DModel</a> model, </li>
<li>double scale, </li>
<li><a href="sdk-for-flutter-explore-mapview-locationindicatormarkertype">LocationIndicatorMarkerType</a> type</li>
</ol>)

      

    

<p>Sets the MapMarker3DModel asset to be displayed as location indicator for a specified type.</p>
<p>The 3D model should be oriented with y axis up and thus standing on the x/z plane where the
z axis is the depth. The direction in which the location indicator is pointing is the
positive z axis. Please note that only MapMarker3DModel created from *.obj files are
supported. Models created from Mesh will be ignored.</p>
<ul>
<li>
<p><code>model</code> The MapMarker3DModel object to be displayed for the specified type. Only models
created from obj files are supported. Those created from mesh will be ignored.</p>
</li>
<li>
<p><code>scale</code> The scaling which will be applied to the marker model. As the size of the
location marker should be aligned on devices with different resolutions the
scale factor is applied relative to the ppi value and thus differs from the
scale which is passed to <a href="sdk-for-flutter-explore-mapview-mapmarker3d-class">MapMarker3D</a> objects.
Meter is used for the unit of the map marker 3d model coordinate system.
For historical reason, the scale factor is internally devided by 6.
To display a unit qube of 1x1x1 meter as is, please use a scale value of 6.0.</p>
</li>
<li>
<p><code>type</code> The type of location marker for which the marker 3d model should be replaced.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.27.0. Please use the setMarker3dModelWithRenderSizeUnit instead.")

void setMarker3dModel(MapMarker3DModel model, double scale, LocationIndicatorMarkerType type);</code></pre>

 



</div>
`
}</HTMLBlock>
