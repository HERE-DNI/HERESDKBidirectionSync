---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapviewbase-viewtogeocoordinates"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- viewToGeoCoordinates.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapViewBase-class.html">/sdk-for-flutter-explore-mapview-mapviewbase-class</a></li>
<li class="self-crumb">viewToGeoCoordinates abstract method</li>
</ol>
<div class="self-name">viewToGeoCoordinates</div>
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
<div class="main-content" data-above-sidebar="mapview/MapViewBase-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>viewToGeoCoordinates abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>?
viewToGeoCoordinates(<wbr/><ol class="parameter-list single-line"> <li><a href="../../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a> viewCoordinates</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Converts view coordinates (in pixels) to geographical coordinates.</p>
<p>An optional altitude component of the resulting geographical coordinate is not set.</p>
<p>If the view coordinates specify a point above a horizon, then the result
is geographical coordinates of the point on a horizon below the specified
view coordinates.</p>
<p>The fog effect is ignored for the calculation, meaning that for the view point
within the area covered by the fog, the result is geographical coordinates
that would be displayed at the specified point if the fog effect was
not applied.</p>
<p>If the render surface is not attached, it will return <code>null</code>.</p>
<ul>
<li><code>viewCoordinates</code> Point inside the view to convert.</li>
</ul>
<p>Returns <a href="../../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>. The geographical coordinates under specified view point or <code>null</code> if there is no render surface attached.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoCoordinates? viewToGeoCoordinates(Point2D viewCoordinates);</code></pre>
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
<li><a href="../../mapview/MapViewBase-class.html">/sdk-for-flutter-explore-mapview-mapviewbase-class</a></li>
<li class="self-crumb">viewToGeoCoordinates abstract method</li>
</ol>
<h5>MapViewBase class</h5>
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
