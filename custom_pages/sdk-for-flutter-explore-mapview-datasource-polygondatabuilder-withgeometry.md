---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-datasource-polygondatabuilder-withgeometry"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- withGeometry.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li><a href="../../mapview.datasource/PolygonDataBuilder-class.html">/sdk-for-flutter-explore-mapview-datasource-polygondatabuilder-class</a></li>
<li class="self-crumb">withGeometry abstract method</li>
</ol>
<div class="self-name">withGeometry</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/PolygonDataBuilder-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>withGeometry abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../mapview.datasource/PolygonDataBuilder-class.html">/sdk-for-flutter-explore-mapview-datasource-polygondatabuilder-class</a>
withGeometry(<wbr/><ol class="parameter-list single-line"> <li><a href="../../core/GeoPolygon-class.html">/sdk-for-flutter-explore-core-geopolygon-class</a> geometry</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Configures the builder with geometry for the polygon to be created.</p>
<ul>
<li><code>geometry</code> Geometry of the polygon.
The outer boundary has to be ordered clockwise and closed.
Any inner boundary has to be ordered counterclockwise and closed.
Altitude of boundary vertices is ignored.
The visual behaviour for self-intersecting outer boundary is undefined.</li>
</ul>
<p>Returns <a href="../../mapview.datasource/PolygonDataBuilder-class.html">/sdk-for-flutter-explore-mapview-datasource-polygondatabuilder-class</a>. The builder.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">PolygonDataBuilder withGeometry(GeoPolygon geometry);</code></pre>
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
<li><a href="../../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li><a href="../../mapview.datasource/PolygonDataBuilder-class.html">/sdk-for-flutter-explore-mapview-datasource-polygondatabuilder-class</a></li>
<li class="self-crumb">withGeometry abstract method</li>
</ol>
<h5>PolygonDataBuilder class</h5>
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
