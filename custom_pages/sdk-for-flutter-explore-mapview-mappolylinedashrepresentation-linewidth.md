---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-linewidth"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- lineWidth.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapPolylineDashRepresentation-class.html">/sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-class</a></li>
<li class="self-crumb">lineWidth property</li>
</ol>
<div class="self-name">lineWidth</div>
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
<div class="main-content" data-above-sidebar="mapview/MapPolylineDashRepresentation-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>lineWidth property</h1></div>
<section id="getter">
<section class="multi-line-signature">
<a href="../../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a>
lineWidth
</section>
<section class="desc markdown">
<p>The width of the polyline depending on the map measure.
At map measures smaller than smallest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the smallest
map measure in the <code>lineWidth</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the biggest
map measure in the <code>lineWidth</code>.</p>
<p>At map measures between two nearest given map measures, the values are
linearly interpolated between values given for these map measures.
Gets the map measure dependent polyline width.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMeasureDependentRenderSize get lineWidth;</code></pre>
</section>
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
<li><a href="../../mapview/MapPolylineDashRepresentation-class.html">/sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-class</a></li>
<li class="self-crumb">lineWidth property</li>
</ol>
<h5>MapPolylineDashRepresentation class</h5>
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
