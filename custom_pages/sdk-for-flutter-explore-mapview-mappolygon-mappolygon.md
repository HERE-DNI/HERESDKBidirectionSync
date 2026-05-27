---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mappolygon-mappolygon"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapPolygon.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapPolygon-class.html">/sdk-for-flutter-explore-mapview-mappolygon-class</a></li>
<li class="self-crumb">MapPolygon factory constructor</li>
</ol>
<div class="self-name">MapPolygon</div>
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
<div class="main-content" data-above-sidebar="mapview/MapPolygon-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapPolygon constructor</h1></div>
<section class="multi-line-signature">
MapPolygon(<wbr/><ol class="parameter-list single-line"> <li><a href="../../core/GeoPolygon-class.html">/sdk-for-flutter-explore-core-geopolygon-class</a> geometry, </li>
<li>Color color</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.</p>
<p>The winding order of the vertices can be in clockwise or counter-clockwise order.
It is recomended to provide the outer boundary ordered clockwise and closed.</p>
<p>Note:</p>
<ul>
<li>
<p>The polygon shape should not cover more than half of the globe,
otherwise unexpected results may occur.</p>
</li>
<li>
<p>Polygons which are self-intersecting are not supported and may lead to render
artifacts.</p>
</li>
<li>
<p>The inner boundaries (holes) specified in the GeoPolygon are ignored.</p>
</li>
<li>
<p><code>geometry</code> The list of vertices representing the outer boundary of polygon.</p>
</li>
<li>
<p><code>color</code> The fill color for the polygon</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolygon(GeoPolygon geometry, ui.Color color) =&gt; $prototype.$init(geometry, color);</code></pre>
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
<li><a href="../../mapview/MapPolygon-class.html">/sdk-for-flutter-explore-mapview-mappolygon-class</a></li>
<li class="self-crumb">MapPolygon factory constructor</li>
</ol>
<h5>MapPolygon class</h5>
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
