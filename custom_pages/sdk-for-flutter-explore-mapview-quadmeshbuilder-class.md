---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-quadmeshbuilder-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- QuadMeshBuilder-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/QuadMeshBuilder-class.html#constructors">Constructors</a></li>
<li><a href="mapview/QuadMeshBuilder/QuadMeshBuilder.html">QuadMeshBuilder</a></li>
<li class="section-title inherited">
<a href="mapview/QuadMeshBuilder-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MeshBuilder/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/QuadMeshBuilder-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/build.html">build</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/quad.html">quad</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/toString.html">toString</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/triangle.html">triangle</a></li>
<li><a href="mapview/QuadMeshBuilder/withTextureCoordinates.html">withTextureCoordinates</a></li>
<li class="section-title inherited"><a href="mapview/QuadMeshBuilder-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">QuadMeshBuilder class</li>
</ol>
<div class="self-name">QuadMeshBuilder</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/QuadMeshBuilder-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>QuadMeshBuilder class abstract</h1></div>
<section class="desc markdown">
<p>Builder for a single quad.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li><a href="../mapview/MeshBuilder-class.html">/sdk-for-flutter-explore-mapview-meshbuilder-class</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="QuadMeshBuilder">
<a href="../mapview/QuadMeshBuilder/QuadMeshBuilder.html">/sdk-for-flutter-explore-mapview-quadmeshbuilder-quadmeshbuilder</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview/MeshBuilder/hashCode.html">/sdk-for-flutter-explore-mapview-meshbuilder-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MeshBuilder/runtimeType.html">/sdk-for-flutter-explore-mapview-meshbuilder-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="build">
<a href="../mapview/MeshBuilder/build.html">/sdk-for-flutter-explore-mapview-meshbuilder-build</a>(<wbr/>)
    → <a href="../mapview/Mesh-class.html">/sdk-for-flutter-explore-mapview-mesh-class</a>?

</dt>
<dd class="inherited">
  Returns <a href="../mapview/Mesh-class.html">/sdk-for-flutter-explore-mapview-mesh-class</a>. mesh containing added geometry or 'null' if no geometry was added.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MeshBuilder/noSuchMethod.html">/sdk-for-flutter-explore-mapview-meshbuilder-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="quad">
<a href="../mapview/MeshBuilder/quad.html">/sdk-for-flutter-explore-mapview-meshbuilder-quad</a>(<wbr/><a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> a, <a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> b, <a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> c, <a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> d)
    → <a href="../mapview/QuadMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-quadmeshbuilder-class</a>
</dt>
<dd class="inherited">
  Adds a quad.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MeshBuilder/toString.html">/sdk-for-flutter-explore-mapview-meshbuilder-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="triangle">
<a href="../mapview/MeshBuilder/triangle.html">/sdk-for-flutter-explore-mapview-meshbuilder-triangle</a>(<wbr/><a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> a, <a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> b, <a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> c)
    → <a href="../mapview/TriangleMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-trianglemeshbuilder-class</a>
</dt>
<dd class="inherited">
  Adds a triangle.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="withTextureCoordinates">
<a href="../mapview/QuadMeshBuilder/withTextureCoordinates.html">/sdk-for-flutter-explore-mapview-quadmeshbuilder-withtexturecoordinates</a>(<wbr/><a href="../core/Anchor2D-class.html">/sdk-for-flutter-explore-core-anchor2d-class</a> a, <a href="../core/Anchor2D-class.html">/sdk-for-flutter-explore-core-anchor2d-class</a> b, <a href="../core/Anchor2D-class.html">/sdk-for-flutter-explore-core-anchor2d-class</a> c, <a href="../core/Anchor2D-class.html">/sdk-for-flutter-explore-core-anchor2d-class</a> d)
    → <a href="../mapview/MeshBuilder-class.html">/sdk-for-flutter-explore-mapview-meshbuilder-class</a>
</dt>
<dd>
  Adds texture coordinates to a quad.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../mapview/MeshBuilder/operator_equals.html">/sdk-for-flutter-explore-mapview-meshbuilder-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">QuadMeshBuilder class</li>
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
</HTMLBlock>
