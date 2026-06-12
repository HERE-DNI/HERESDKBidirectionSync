---
title: "MapMarker3DModel class abstract"
slug: "sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3DModel-class.html -->


<div>
<h1>MapMarker3DModel class abstract</h1></div>

<p>Represents a 3D model that can be used by a <a href="/sdk-for-flutter-navigate-mapview-mapmarker3d-class">MapMarker3D</a> to be shown on the map.</p>
<p>Geometry of 3D marker can be provided in form of a Wavefront OBJ file as specified in
<a href="http://www.martinreddy.net/gfx/3d/OBJ.spec">http://www.martinreddy.net/gfx/3d/OBJ.spec</a> or as mesh built via <a href="/sdk-for-flutter-navigate-mapview-meshbuilder-class">MeshBuilder</a>.</p>
<h1 id="1-creating-mapmarker3dmodel-from-obj-file">1. Creating MapMarker3DModel from OBJ file</h1>
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
</ul>
</li>
</ul>
<p>HERE SDK does not support:</p>
<ul>
<li>Multi Texturing</li>
<li>Materials (mtllib [external .mtl file name] )
<ul>
<li>Lines</li>
<li>Higher Order Surfaces</li>
<li>Vendor specific extensions</li>
</ul>
</li>
</ul>
<p>For supported texture formats, HERE SDK allows the following formats to be specified:
JPG, PNG, GPU compressed texture formats: ECT1 (OpenGL only), YUV, ASTC, KTX.</p>
<h1 id="2-creating-mapmarker3dmodel-programatically">2. Creating MapMarker3DModel programatically</h1>
<p>A 3D mesh can be specified programatically using <a href="/sdk-for-flutter-navigate-mapview-meshbuilder-class">MeshBuilder</a> and passed to
<code>MapMarker3DModel</code> constructor. This method supports creating a mesh from
quads and triangles. Textured geometry is also supported, the mesh faces
need to have texture coordinates and a texture file needs to be passed
along with the mesh to <code>MapMarker3DModel</code> constructor.</p>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-mapmarker3dmodel">MapMarker3DModel</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-mapmarker3dmodel-frommesh">MapMarker3DModel.fromMesh</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-mapmarker3dmodel-frommeshwithtexturefilepath">MapMarker3DModel.fromMeshWithTextureFilePath</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-mapmarker3dmodel-frommeshwithtexturefilepathandcolor">MapMarker3DModel.fromMeshWithTextureFilePathAndColor</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-mapmarker3dmodel-withtexturefilepath">MapMarker3DModel.withTextureFilePath</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-mapmarker3dmodel-withtexturefilepathandcolor">MapMarker3DModel.withTextureFilePathAndColor</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
