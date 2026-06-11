---
title: "MapMarker3DModel"
slug: "sdk-for-ios-navigate-api-reference-classes-mapmarker3dmodel"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapMarker3DModel"></a>
<a title="MapMarker3DModel Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

        MapMarker3DModel Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapMarker3DModel</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapMarker3DModel</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarker3DModel</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarker3DModel</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a 3D model that can be used by a <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3d">MapMarker3D</a></code> to be shown on the map.
Geometry of 3D marker can be provided in form of a Wavefront OBJ file as specified in
<a href="http://www.martinreddy.net/gfx/3d/OBJ.spec">http://www.martinreddy.net/gfx/3d/OBJ.spec</a> or as mesh built via <code><a href="sdk-for-ios-navigate-api-reference-classes-meshbuilder">MeshBuilder</a></code>.</p>
<h1 class="heading" id="1-creating-code-mapmarker3dmodel-code-from-obj-file">1. Creating <code>MapMarker3DModel</code> from OBJ file</h1>
<p>For OBJ files, HERE SDK only supports the following set of features of the OBJ specification:</p>
<ul>
<li>Triangle Meshes</li>
<li>Following vertex attributes must be present:

<ul>
<li>Vertex Position</li>
<li>Vertex Normal</li>
<li>Texture Coordinates</li>
<li>Geometry must be indexed (contain an Index Buffer)</li>
<li>Face element</li>
</ul></li>
</ul>
<p>HERE SDK does not support:</p>
<ul>
<li>Multi Texturing</li>
<li>Materials (mtllib [external .mtl file name] )

<ul>
<li>Lines</li>
<li>Higher Order Surfaces</li>
<li>Vendor specific extensions</li>
</ul></li>
</ul>
<p>For supported texture formats, HERE SDK allows the following formats to be specified:
JPG, PNG, GPU compressed texture formats: ECT1 (OpenGL only), YUV, ASTC, KTX.</p>
<h1 class="heading" id="2-creating-code-mapmarker3dmodel-code-programatically">2. Creating <code>MapMarker3DModel</code> programatically</h1>
<p>A 3D mesh can be specified programatically using <code><a href="sdk-for-ios-navigate-api-reference-classes-meshbuilder">MeshBuilder</a></code> and passed to
<code>MapMarker3DModel</code> constructor. This method supports creating a mesh from
quads and triangles. Textured geometry is also supported, the mesh faces
need to have texture coordinates and a texture file needs to be passed
along with the mesh to <code>MapMarker3DModel</code> constructor.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarker3DModelC18InstantiationErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InstantiationError"></a>
<a class="token" href="#/s:7heresdk16MapMarker3DModelC18InstantiationErrora">InstantiationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Thrown when a problem occurs while trying to create <code>MapMarker3DModel</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">InstantiationError</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3dmodel-instantiationerrorcode">InstantiationErrorCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarker3DModelC16geometryFilePath07texturefG05colorACSS_SSSo7UIColorCtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(geometryFilePath:textureFilePath:color:)"></a>
<a class="token" href="#/s:7heresdk16MapMarker3DModelC16geometryFilePath07texturefG05colorACSS_SSSo7UIColorCtcfc">init(geometryFilePath:<wbr/>textureFilePath:<wbr/>color:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new 3D model from path to .obj file, texture and color.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">geometryFilePath</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">textureFilePath</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">color</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geometryFilePath</em>
</code>
</td>
<td>
<div>
<p>Absolute path to obj file.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>textureFilePath</em>
</code>
</td>
<td>
<div>
<p>Absolute path to texture file.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>color</em>
</code>
</td>
<td>
<div>
<p>Color to be blend with texture.
This color is multiplied with color of texture.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarker3DModelC4mesh15textureFilePath5colorAcA4MeshC_SSSo7UIColorCtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(mesh:textureFilePath:color:)"></a>
<a class="token" href="#/s:7heresdk16MapMarker3DModelC4mesh15textureFilePath5colorAcA4MeshC_SSSo7UIColorCtKcfc">init(mesh:<wbr/>textureFilePath:<wbr/>color:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new 3D model from mesh, texture and color.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapMarker3DModel.html#/s:7heresdk16MapMarker3DModelC18InstantiationErrora">MapMarker3DModel.InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">mesh</span><span class="p">:</span> <span class="kt"><a href="../Maps.html#/s:7heresdk4MeshC">Mesh</a></span><span class="p">,</span> <span class="nv">textureFilePath</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">color</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mesh</em>
</code>
</td>
<td>
<div>
<p>Mesh containing the 3d geometry together with texture coordinates.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>textureFilePath</em>
</code>
</td>
<td>
<div>
<p>Absolute path to texture file.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>color</em>
</code>
</td>
<td>
<div>
<p>Color to be blend with texture.
This color is multiplied with color of texture.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarker3DModelC16geometryFilePath07texturefG0ACSS_SStcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(geometryFilePath:textureFilePath:)"></a>
<a class="token" href="#/s:7heresdk16MapMarker3DModelC16geometryFilePath07texturefG0ACSS_SStcfc">init(geometryFilePath:<wbr/>textureFilePath:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new 3D model from path to .obj file and texture.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">geometryFilePath</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">textureFilePath</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geometryFilePath</em>
</code>
</td>
<td>
<div>
<p>Absolute path to obj file.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>textureFilePath</em>
</code>
</td>
<td>
<div>
<p>Absolute path to texture file.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarker3DModelC4mesh15textureFilePathAcA4MeshC_SStKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(mesh:textureFilePath:)"></a>
<a class="token" href="#/s:7heresdk16MapMarker3DModelC4mesh15textureFilePathAcA4MeshC_SStKcfc">init(mesh:<wbr/>textureFilePath:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new 3D model from mesh and texture.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapMarker3DModel.html#/s:7heresdk16MapMarker3DModelC18InstantiationErrora">MapMarker3DModel.InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">mesh</span><span class="p">:</span> <span class="kt"><a href="../Maps.html#/s:7heresdk4MeshC">Mesh</a></span><span class="p">,</span> <span class="nv">textureFilePath</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mesh</em>
</code>
</td>
<td>
<div>
<p>Mesh containing the 3d geometry together with texture coordinates.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>textureFilePath</em>
</code>
</td>
<td>
<div>
<p>Absolute path to texture file.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarker3DModelC16geometryFilePathACSS_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(geometryFilePath:)"></a>
<a class="token" href="#/s:7heresdk16MapMarker3DModelC16geometryFilePathACSS_tcfc">init(geometryFilePath:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new 3D model from path to .obj file.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">geometryFilePath</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geometryFilePath</em>
</code>
</td>
<td>
<div>
<p>Absolute path to obj file.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarker3DModelC4meshAcA4MeshC_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(mesh:)"></a>
<a class="token" href="#/s:7heresdk16MapMarker3DModelC4meshAcA4MeshC_tcfc">init(mesh:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new 3D model from a mesh.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">mesh</span><span class="p">:</span> <span class="kt"><a href="../Maps.html#/s:7heresdk4MeshC">Mesh</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mesh</em>
</code>
</td>
<td>
<div>
<p>Mesh containing the 3d geometry 3D data.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarker3DModelC22InstantiationErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a class="token" href="#/s:7heresdk16MapMarker3DModelC22InstantiationErrorCodeO">InstantiationErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the reason for a failure to create <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3dmodel">MapMarker3DModel</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapmarker3dmodel-instantiationerrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3dmodel">MapMarker3DModel</a></span><span class="o">.</span><span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
}</HTMLBlock>
