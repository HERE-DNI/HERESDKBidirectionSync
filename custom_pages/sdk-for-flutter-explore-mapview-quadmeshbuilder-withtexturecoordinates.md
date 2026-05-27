---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-quadmeshbuilder-withtexturecoordinates"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- withTextureCoordinates.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/QuadMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-quadmeshbuilder-class</a></li>
<li class="self-crumb">withTextureCoordinates abstract method</li>
</ol>
<div class="self-name">withTextureCoordinates</div>
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
<div class="main-content" data-above-sidebar="mapview/QuadMeshBuilder-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>withTextureCoordinates abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../mapview/MeshBuilder-class.html">/sdk-for-flutter-explore-mapview-meshbuilder-class</a>
withTextureCoordinates(<wbr/><ol class="parameter-list"> <li><a href="../../core/Anchor2D-class.html">/sdk-for-flutter-explore-core-anchor2d-class</a> a, </li>
<li><a href="../../core/Anchor2D-class.html">/sdk-for-flutter-explore-core-anchor2d-class</a> b, </li>
<li><a href="../../core/Anchor2D-class.html">/sdk-for-flutter-explore-core-anchor2d-class</a> c, </li>
<li><a href="../../core/Anchor2D-class.html">/sdk-for-flutter-explore-core-anchor2d-class</a> d, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Adds texture coordinates to a quad.</p>
<p>Coordinates are specified as <code>&lt;u,v&gt;</code> with <code>&lt;0,0&gt;</code>
representing the bottom-left and <code>&lt;1,1&gt;</code> upper-right corner.</p>
<ul>
<li>
<p><code>a</code> Texture coordinate for vertex a. See <a href="../../mapview/MeshBuilder/quad.html">/sdk-for-flutter-explore-mapview-meshbuilder-quad</a></p>
</li>
<li>
<p><code>b</code> Texture coordinate for vertex b. See <a href="../../mapview/MeshBuilder/quad.html">/sdk-for-flutter-explore-mapview-meshbuilder-quad</a></p>
</li>
<li>
<p><code>c</code> Texture coordinate for vertex c. See <a href="../../mapview/MeshBuilder/quad.html">/sdk-for-flutter-explore-mapview-meshbuilder-quad</a></p>
</li>
<li>
<p><code>d</code> Texture coordinate for vertex d. See <a href="../../mapview/MeshBuilder/quad.html">/sdk-for-flutter-explore-mapview-meshbuilder-quad</a></p>
</li>
</ul>
<p>Returns <a href="../../mapview/MeshBuilder-class.html">/sdk-for-flutter-explore-mapview-meshbuilder-class</a>. A <a href="../../mapview/MeshBuilder-class.html">/sdk-for-flutter-explore-mapview-meshbuilder-class</a> instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MeshBuilder withTextureCoordinates(Anchor2D a, Anchor2D b, Anchor2D c, Anchor2D d);</code></pre>
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
<li><a href="../../mapview/QuadMeshBuilder-class.html">/sdk-for-flutter-explore-mapview-quadmeshbuilder-class</a></li>
<li class="self-crumb">withTextureCoordinates abstract method</li>
</ol>
<h5>QuadMeshBuilder class</h5>
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
