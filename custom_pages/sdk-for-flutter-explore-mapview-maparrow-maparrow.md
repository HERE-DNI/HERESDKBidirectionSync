---
title: "MapArrow constructor"
slug: "sdk-for-flutter-explore-mapview-maparrow-maparrow"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapArrow.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-maparrow-class</li>
<li class="self-crumb">MapArrow factory constructor</li>
</ol>
<div class="self-name">MapArrow</div>
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
<div class="main-content" data-above-sidebar="mapview/MapArrow-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapArrow constructor</h1></div>
<section class="multi-line-signature">
MapArrow(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-core-geopolyline-class geometry, </li>
<li>double widthInPixels, </li>
<li>Color color</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new <code>MapArrow</code> instance.</p>
<p>Altitude component of <code>GeoPolyline</code>'s vertices is ignored.</p>
<ul>
<li>
<p><code>geometry</code> The geometry of the arrow tail. The last coordinate in the list defines the position where the
head of the arrow is located.</p>
</li>
<li>
<p><code>widthInPixels</code> The width of the arrow tail in pixel. Negative values are clamped to 0. The tip is scaled accordingly.</p>
</li>
<li>
<p><code>color</code> The color of the arrow. The alpha channel is ignored, the color is
interpreted as fully opaque.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapArrow(GeoPolyline geometry, double widthInPixels, ui.Color color) =&gt; $prototype.$init(geometry, widthInPixels, color);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-maparrow-class</li>
<li class="self-crumb">MapArrow factory constructor</li>
</ol>
<h5>MapArrow class</h5>
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
