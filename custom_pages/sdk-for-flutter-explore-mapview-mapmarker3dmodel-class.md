---
title: "MapMarker3DModel class abstract"
slug: "sdk-for-flutter-explore-mapview-mapmarker3dmodel-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3DModel-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapMarker3DModel-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapMarker3DModel/MapMarker3DModel.html">MapMarker3DModel</a></li>
<li><a href="mapview/MapMarker3DModel/MapMarker3DModel.fromMesh.html">fromMesh</a></li>
<li><a href="mapview/MapMarker3DModel/MapMarker3DModel.fromMeshWithTextureFilePath.html">fromMeshWithTextureFilePath</a></li>
<li><a href="mapview/MapMarker3DModel/MapMarker3DModel.fromMeshWithTextureFilePathAndColor.html">fromMeshWithTextureFilePathAndColor</a></li>
<li><a href="mapview/MapMarker3DModel/MapMarker3DModel.withTextureFilePath.html">withTextureFilePath</a></li>
<li><a href="mapview/MapMarker3DModel/MapMarker3DModel.withTextureFilePathAndColor.html">withTextureFilePathAndColor</a></li>
<li class="section-title inherited">
<a href="mapview/MapMarker3DModel-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapMarker3DModel/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MapMarker3DModel/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapview/MapMarker3DModel-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapMarker3DModel/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapMarker3DModel/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapMarker3DModel-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapMarker3DModel/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapMarker3DModel class</li>
</ol>
<div class="self-name">MapMarker3DModel</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapMarker3DModel-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapMarker3DModel class abstract</h1></div>
<section class="desc markdown">
<p>Represents a 3D model that can be used by a /sdk-for-flutter-explore-mapview-mapmarker3d-class to be shown on the map.</p>
<p>Geometry of 3D marker can be provided in form of a Wavefront OBJ file as specified in
<a href="http://www.martinreddy.net/gfx/3d/OBJ.spec">http://www.martinreddy.net/gfx/3d/OBJ.spec</a> or as mesh built via /sdk-for-flutter-explore-mapview-meshbuilder-class.</p>
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
<p>A 3D mesh can be specified programatically using /sdk-for-flutter-explore-mapview-meshbuilder-class and passed to
<code>MapMarker3DModel</code> constructor. This method supports creating a mesh from
quads and triangles. Textured geometry is also supported, the mesh faces
need to have texture coordinates and a texture file needs to be passed
along with the mesh to <code>MapMarker3DModel</code> constructor.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapMarker3DModel">
/sdk-for-flutter-explore-mapview-mapmarker3dmodel-mapmarker3dmodel(String geometryFilePath)
</dt>
<dd>
          Creates a new 3D model from path to .obj file.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMarker3DModel.fromMesh">
/sdk-for-flutter-explore-mapview-mapmarker3dmodel-mapmarker3dmodel-frommesh(/sdk-for-flutter-explore-mapview-mesh-class mesh)
</dt>
<dd>
          Creates a new 3D model from a mesh.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMarker3DModel.fromMeshWithTextureFilePath">
/sdk-for-flutter-explore-mapview-mapmarker3dmodel-mapmarker3dmodel-frommeshwithtexturefilepath(/sdk-for-flutter-explore-mapview-mesh-class mesh, String textureFilePath)
</dt>
<dd>
          Creates a new 3D model from mesh and texture.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMarker3DModel.fromMeshWithTextureFilePathAndColor">
/sdk-for-flutter-explore-mapview-mapmarker3dmodel-mapmarker3dmodel-frommeshwithtexturefilepathandcolor(/sdk-for-flutter-explore-mapview-mesh-class mesh, String textureFilePath, Color color)
</dt>
<dd>
          Creates a new 3D model from mesh, texture and color.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMarker3DModel.withTextureFilePath">
/sdk-for-flutter-explore-mapview-mapmarker3dmodel-mapmarker3dmodel-withtexturefilepath(String geometryFilePath, String textureFilePath)
</dt>
<dd>
          Creates a new 3D model from path to .obj file and texture.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMarker3DModel.withTextureFilePathAndColor">
/sdk-for-flutter-explore-mapview-mapmarker3dmodel-mapmarker3dmodel-withtexturefilepathandcolor(String geometryFilePath, String textureFilePath, Color color)
</dt>
<dd>
          Creates a new 3D model from path to .obj file, texture and color.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-mapmarker3dmodel-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-mapmarker3dmodel-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-mapmarker3dmodel-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-mapmarker3dmodel-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-explore-mapview-mapmarker3dmodel-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapMarker3DModel class</li>
</ol>
<h5>mapview library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
