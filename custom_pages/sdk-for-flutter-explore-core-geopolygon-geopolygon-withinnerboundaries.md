---
title: "Implementation"
slug: "sdk-for-flutter-explore-core-geopolygon-geopolygon-withinnerboundaries"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- GeoPolygon.withInnerBoundaries.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li><a href="../../core/GeoPolygon-class.html">/sdk-for-flutter-explore-core-geopolygon-class</a></li>
<li class="self-crumb">GeoPolygon.withInnerBoundaries factory constructor</li>
</ol>
<div class="self-name">GeoPolygon.withInnerBoundaries</div>
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
<div class="main-content" data-above-sidebar="core/GeoPolygon-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>GeoPolygon.withInnerBoundaries constructor</h1></div>
<section class="multi-line-signature">
GeoPolygon.withInnerBoundaries(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>&gt; vertices, </li>
<li>List&lt;<wbr/>List&lt;<wbr/><a href="../../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>&gt;&gt; innerBoundaries</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Constructs an instance of this class from the provided vertices and inner boundaries (holes).</p>
<p>Throws InstantiationError if the number of vertices is less than three.</p>
<ul>
<li>
<p><code>vertices</code> List of vertices representing the polygon outer boundary in clockwise order.</p>
</li>
<li>
<p><code>innerBoundaries</code> List of polygon inner boundaries (holes), each in counterclockwise order.</p>
</li>
</ul>
<p>Throws <a href="../../core.errors/InstantiationException-class.html">/sdk-for-flutter-explore-core-errors-instantiationexception-class</a>. Instantiation error.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory GeoPolygon.withInnerBoundaries(List&lt;GeoCoordinates&gt; vertices, List&lt;List&lt;GeoCoordinates&gt;&gt; innerBoundaries) =&gt; $prototype.withInnerBoundaries(vertices, innerBoundaries);</code></pre>
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
<li><a href="../../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li><a href="../../core/GeoPolygon-class.html">/sdk-for-flutter-explore-core-geopolygon-class</a></li>
<li class="self-crumb">GeoPolygon.withInnerBoundaries factory constructor</li>
</ol>
<h5>GeoPolygon class</h5>
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
