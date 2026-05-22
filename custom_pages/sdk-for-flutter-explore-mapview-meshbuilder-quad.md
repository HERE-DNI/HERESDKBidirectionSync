---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-meshbuilder-quad"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- quad.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-meshbuilder-class</li>
<li class="self-crumb">quad abstract method</li>
</ol>
<div class="self-name">quad</div>
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
<h1>quad abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-mapview-quadmeshbuilder-class
quad(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-explore-core-point3d-class a, </li>
<li>/sdk-for-flutter-explore-core-point3d-class b, </li>
<li>/sdk-for-flutter-explore-core-point3d-class c, </li>
<li>/sdk-for-flutter-explore-core-point3d-class d, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Adds a quad.</p>
<p>Internally, this will be transformed into triangles abc and bdc.</p>
<p>Triangle visibility is determined via back-face culling. Front-facing triangles are expected to have
counter-clockwise winding.</p>
<ul>
<li>
<p><code>a</code> First vertex of quad.</p>
</li>
<li>
<p><code>b</code> Second vertex of the quad.</p>
</li>
<li>
<p><code>c</code> Third vertex of the quad.</p>
</li>
<li>
<p><code>d</code> Fourth vertex of the quad.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-explore-mapview-quadmeshbuilder-class. A /sdk-for-flutter-explore-mapview-quadmeshbuilder-class instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">QuadMeshBuilder quad(Point3D a, Point3D b, Point3D c, Point3D d);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-meshbuilder-class</li>
<li class="self-crumb">quad abstract method</li>
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



</div>
`
}</HTMLBlock>
