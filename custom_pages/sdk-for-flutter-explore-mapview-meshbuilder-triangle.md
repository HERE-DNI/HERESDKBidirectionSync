---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-meshbuilder-triangle"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- triangle.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MeshBuilder-class.html">/sdk-for-flutter-explore-mapview-meshbuilder-class</a></li>
<li class="self-crumb">triangle abstract method</li>
</ol>
<div class="self-name">triangle</div>
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
<div class="main-content" data-above-sidebar="mapview/MeshBuilder-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>triangle abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../mapview/TriangleMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-trianglemeshbuilder-class</a>
triangle(<wbr/><ol class="parameter-list single-line"> <li><a href="../../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> a, </li>
<li><a href="../../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> b, </li>
<li><a href="../../core/Point3D-class.html">/sdk-for-flutter-explore-core-point3d-class</a> c</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Adds a triangle.</p>
<p>Triangle visibility is determined via back-face culling. Front-facing
triangles are expected to have counter-clockwise winding.</p>
<ul>
<li>
<p><code>a</code> First vertex of the triangle.</p>
</li>
<li>
<p><code>b</code> Second vertex of the triangle.</p>
</li>
<li>
<p><code>c</code> Third vertex of the triangle.</p>
</li>
</ul>
<p>Returns <a href="../../mapview/TriangleMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-trianglemeshbuilder-class</a>. A <a href="../../mapview/TriangleMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-trianglemeshbuilder-class</a> instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TriangleMeshBuilder triangle(Point3D a, Point3D b, Point3D c);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MeshBuilder-class.html">/sdk-for-flutter-explore-mapview-meshbuilder-class</a></li>
<li class="self-crumb">triangle abstract method</li>
</ol>
<h5>MeshBuilder class</h5>
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
