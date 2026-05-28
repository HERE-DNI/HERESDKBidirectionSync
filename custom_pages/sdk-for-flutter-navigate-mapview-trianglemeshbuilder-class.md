---
title: "TriangleMeshBuilder class abstract"
slug: "sdk-for-flutter-navigate-mapview-trianglemeshbuilder-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TriangleMeshBuilder-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/TriangleMeshBuilder-class.html#constructors">Constructors</a></li>
<li><a href="mapview/TriangleMeshBuilder/TriangleMeshBuilder.html">TriangleMeshBuilder</a></li>
<li class="section-title inherited">
<a href="mapview/TriangleMeshBuilder-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MeshBuilder/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/TriangleMeshBuilder-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/build.html">build</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/quad.html">quad</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/toString.html">toString</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/triangle.html">triangle</a></li>
<li><a href="mapview/TriangleMeshBuilder/withTextureCoordinates.html">withTextureCoordinates</a></li>
<li class="section-title inherited"><a href="mapview/TriangleMeshBuilder-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MeshBuilder/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">TriangleMeshBuilder class</li>
</ol>
<div class="self-name">TriangleMeshBuilder</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/TriangleMeshBuilder-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TriangleMeshBuilder class abstract</h1></div>
<section class="desc markdown">
<p>Builder for a single triangle.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-mapview-meshbuilder-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TriangleMeshBuilder">
/sdk-for-flutter-navigate-mapview-trianglemeshbuilder-trianglemeshbuilder()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-meshbuilder-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-meshbuilder-runtimetype
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
/sdk-for-flutter-navigate-mapview-meshbuilder-build(<wbr/>)
    → /sdk-for-flutter-navigate-mapview-mesh-class?

</dt>
<dd class="inherited">
  Returns /sdk-for-flutter-navigate-mapview-mesh-class. mesh containing added geometry or 'null' if no geometry was added.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-meshbuilder-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="quad">
/sdk-for-flutter-navigate-mapview-meshbuilder-quad(<wbr/>/sdk-for-flutter-navigate-core-point3d-class a, /sdk-for-flutter-navigate-core-point3d-class b, /sdk-for-flutter-navigate-core-point3d-class c, /sdk-for-flutter-navigate-core-point3d-class d)
    → /sdk-for-flutter-navigate-mapview-quadmeshbuilder-class

</dt>
<dd class="inherited">
  Adds a quad.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-meshbuilder-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="triangle">
/sdk-for-flutter-navigate-mapview-meshbuilder-triangle(<wbr/>/sdk-for-flutter-navigate-core-point3d-class a, /sdk-for-flutter-navigate-core-point3d-class b, /sdk-for-flutter-navigate-core-point3d-class c)
    → /sdk-for-flutter-navigate-mapview-trianglemeshbuilder-class

</dt>
<dd class="inherited">
  Adds a triangle.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="withTextureCoordinates">
/sdk-for-flutter-navigate-mapview-trianglemeshbuilder-withtexturecoordinates(<wbr/>/sdk-for-flutter-navigate-core-anchor2d-class a, /sdk-for-flutter-navigate-core-anchor2d-class b, /sdk-for-flutter-navigate-core-anchor2d-class c)
    → /sdk-for-flutter-navigate-mapview-meshbuilder-class

</dt>
<dd>
  Adds texture coordinates to a triangle.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-mapview-meshbuilder-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">TriangleMeshBuilder class</li>
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
