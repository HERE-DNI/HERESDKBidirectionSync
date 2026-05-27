---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-meshbuilder-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MeshBuilder-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MeshBuilder-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MeshBuilder/MeshBuilder.html">MeshBuilder</a></li>
<li class="section-title inherited">
<a href="mapview/MeshBuilder-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MeshBuilder/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/MeshBuilder-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MeshBuilder/build.html">build</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MeshBuilder/quad.html">quad</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/toString.html">toString</a></li>
<li><a href="mapview/MeshBuilder/triangle.html">triangle</a></li>
<li class="section-title inherited"><a href="mapview/MeshBuilder-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MeshBuilder class</li>
</ol>
<div class="self-name">MeshBuilder</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MeshBuilder-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MeshBuilder class abstract</h1></div>
<section class="desc markdown">
<p>Builder for meshes.</p>
<p>Such meshes can contain different kinds of primitives, like quads or
triangles. Both primitives support adding texture coordinates that are mapped to the
corners of the primitives. See <a href="../mapview/TriangleMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-trianglemeshbuilder-class</a> and <a href="../mapview/QuadMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-quadmeshbuilder-class</a> for more details.</p>
<p>Note: Normals cannot be set as they are not necessary when using the <a href="../mapview/MeshBuilder-class.html">/sdk-for-flutter-explore-mapview-meshbuilder-class</a>.</p>
<p>Example how to build a cube using <a href="../mapview/QuadMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-quadmeshbuilder-class</a></p>
<pre class="language-dart"><code>Mesh? cube = MeshBuilder()
      .quad(Point3D(0.5, 0.5, 0.5),
            Point3D(-0.5, 0.5, 0.5),
            Point3D(0.5, -0.5, 0.5),
            Point3D(-0.5, -0.5, 0.5))
      .quad(Point3D(-0.5, 0.5, -0.5),
            Point3D(0.5, 0.5, -0.5),
            Point3D(-0.5, -0.5, -0.5),
            Point3D(0.5, -0.5, -0.5))
      .quad(Point3D(0.5, 0.5, -0.5),
            Point3D(0.5, 0.5, 0.5),
            Point3D(0.5, -0.5, -0.5),
            Point3D(0.5, -0.5, 0.5))
      .quad(Point3D(-0.5, 0.5, 0.5),
            Point3D(-0.5, 0.5, -0.5),
            Point3D(-0.5, -0.5, 0.5),
            Point3D(-0.5, -0.5, -0.5))
      .quad(Point3D(-0.5, 0.5, 0.5),
            Point3D(0.5, 0.5, 0.5),
            Point3D(-0.5, 0.5, -0.5),
            Point3D(0.5, 0.5, -0.5))
      .quad(Point3D(0.5, -0.5, 0.5),
            Point3D(-0.5, -0.5, 0.5),
            Point3D(0.5, -0.5, -0.5),
            Point3D(-0.5, -0.5, -0.5))
      .build();
</code></pre>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implementers</dt>
<dd><ul class="comma-separated clazz-relationships">
<li><a href="../mapview/QuadMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-quadmeshbuilder-class</a></li>
<li><a href="../mapview/TriangleMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-trianglemeshbuilder-class</a></li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MeshBuilder">
<a href="../mapview/MeshBuilder/MeshBuilder.html">/sdk-for-flutter-explore-mapview-meshbuilder-meshbuilder</a>()
</dt>
<dd>
          Constructs an instance of MeshBuilder.
            <div class="constructor-modifier features">factory</div>
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
<dt class="callable" id="build">
<a href="../mapview/MeshBuilder/build.html">/sdk-for-flutter-explore-mapview-meshbuilder-build</a>(<wbr/>)
    → <a href="../mapview/Mesh-class.html">/sdk-for-flutter-explore-mapview-mesh-class</a>?

</dt>
<dd>
  Returns <a href="../mapview/Mesh-class.html">/sdk-for-flutter-explore-mapview-mesh-class</a>. mesh containing added geometry or 'null' if no geometry was added.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MeshBuilder/noSuchMethod.html">/sdk-for-flutter-explore-mapview-meshbuilder-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="quad">
<a href="../mapview/MeshBuilder/quad.html">/sdk-for-flutter-explore-mapview-meshbuilder-quad</a>(<wbr/><a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> a, <a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> b, <a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> c, <a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> d)
    → <a href="../mapview/QuadMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-quadmeshbuilder-class</a>
</dt>
<dd>
  Adds a quad.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MeshBuilder/toString.html">/sdk-for-flutter-explore-mapview-meshbuilder-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="triangle">
<a href="../mapview/MeshBuilder/triangle.html">/sdk-for-flutter-explore-mapview-meshbuilder-triangle</a>(<wbr/><a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> a, <a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> b, <a href="../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> c)
    → <a href="../mapview/TriangleMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-trianglemeshbuilder-class</a>
</dt>
<dd>
  Adds a triangle.
  

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
<li class="self-crumb">MeshBuilder class</li>
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
