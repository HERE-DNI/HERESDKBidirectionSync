---
title: "MapMarker3DModel class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmarker3dmodel-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3DModel-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapMarker3DModel-class-sidebar.html">

<div>

# <span class="kind-class">MapMarker3DModel</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents a 3D model that can be used by a <a href="sdk-for-flutter-explore-mapview-mapmarker3d-class">MapMarker3D</a> to be shown on the map.

Geometry of 3D marker can be provided in form of a Wavefront OBJ file as specified in <http://www.martinreddy.net/gfx/3d/OBJ.spec> or as mesh built via <a href="sdk-for-flutter-explore-mapview-meshbuilder-class">MeshBuilder</a>.

# 1. Creating `MapMarker3DModel` from OBJ file

For OBJ files, HERE SDK only supports the following set of features of the OBJ specification:

- Triangle Meshes
- Following vertex attributes must be present:
  - Vertex Position
  - Vertex Normal
  - Texture Coordinates
  - Geometry must be indexed (contain an Index Buffer)
  - Face element

HERE SDK does not support:

- Multi Texturing
- Materials (mtllib \[external .mtl file name\] )
  - Lines
  - Higher Order Surfaces
  - Vendor specific extensions

For supported texture formats, HERE SDK allows the following formats to be specified: JPG, PNG, GPU compressed texture formats: ECT1 (OpenGL only), YUV, ASTC, KTX.

# 2. Creating `MapMarker3DModel` programatically

A 3D mesh can be specified programatically using <a href="sdk-for-flutter-explore-mapview-meshbuilder-class">MeshBuilder</a> and passed to `MapMarker3DModel` constructor. This method supports creating a mesh from quads and triangles. Textured geometry is also supported, the mesh faces need to have texture coordinates and a texture file needs to be passed along with the mesh to `MapMarker3DModel` constructor.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-mapmarker3dmodel">MapMarker3DModel</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-geometryFilePath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">geometryFilePath</span></span>)</span>  
Creates a new 3D model from path to .obj file.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-mapmarker3dmodel-frommesh">MapMarker3DModel.fromMesh</a></span><span class="signature">(<span id="sdk-for-flutter-explore-fromMesh-param-mesh" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mesh-class">Mesh</a></span> <span class="parameter-name">mesh</span></span>)</span>  
Creates a new 3D model from a mesh.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-mapmarker3dmodel-frommeshwithtexturefilepath">MapMarker3DModel.fromMeshWithTextureFilePath</a></span><span class="signature">(<span id="sdk-for-flutter-explore-fromMeshWithTextureFilePath-param-mesh" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mesh-class">Mesh</a></span> <span class="parameter-name">mesh</span>, </span><span id="sdk-for-flutter-explore-fromMeshWithTextureFilePath-param-textureFilePath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">textureFilePath</span></span>)</span>  
Creates a new 3D model from mesh and texture.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-mapmarker3dmodel-frommeshwithtexturefilepathandcolor">MapMarker3DModel.fromMeshWithTextureFilePathAndColor</a></span><span class="signature">(<span id="sdk-for-flutter-explore-fromMeshWithTextureFilePathAndColor-param-mesh" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mesh-class">Mesh</a></span> <span class="parameter-name">mesh</span>, </span><span id="sdk-for-flutter-explore-fromMeshWithTextureFilePathAndColor-param-textureFilePath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">textureFilePath</span>, </span><span id="sdk-for-flutter-explore-fromMeshWithTextureFilePathAndColor-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span></span>)</span>  
Creates a new 3D model from mesh, texture and color.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-mapmarker3dmodel-withtexturefilepath">MapMarker3DModel.withTextureFilePath</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withTextureFilePath-param-geometryFilePath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">geometryFilePath</span>, </span><span id="sdk-for-flutter-explore-withTextureFilePath-param-textureFilePath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">textureFilePath</span></span>)</span>  
Creates a new 3D model from path to .obj file and texture.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-mapmarker3dmodel-withtexturefilepathandcolor">MapMarker3DModel.withTextureFilePathAndColor</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withTextureFilePathAndColor-param-geometryFilePath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">geometryFilePath</span>, </span><span id="sdk-for-flutter-explore-withTextureFilePathAndColor-param-textureFilePath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">textureFilePath</span>, </span><span id="sdk-for-flutter-explore-withTextureFilePathAndColor-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span></span>)</span>  
Creates a new 3D model from path to .obj file, texture and color.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
