---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mappolyline-progress"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- progress.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapPolyline-class.html">/sdk-for-flutter-explore-mapview-mappolyline-class</a></li>
<li class="self-crumb">progress property</li>
</ol>
<div class="self-name">progress</div>
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
<div class="main-content" data-above-sidebar="mapview/MapPolyline-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>progress property</h1></div>
<section id="getter">
<section class="multi-line-signature">
double
progress
</section>
<section class="desc markdown">
<p>The progress from the polyline's starting point, as a ratio of its total length clamped to
the range [0, 1].
Gets the progress of the polyline, 0 by default.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double get progress;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
progress=(<wbr/>double value)
</section>
<section class="desc markdown">
<p>The progress from the polyline's starting point, as a ratio of its total length clamped to
the range [0, 1].
Sets the progress of the polyline from its starting point as a ratio of its total length
clamped to the range [0; 1].</p>
<p>As the progress varies, the equivalent part of the
polyline gets covered by the progress color and progress outline color. The rest of the
polyline until its end point retains the line color and outline color along with an
optional dash pattern.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set progress(double value);</code></pre>
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
<li><a href="../../mapview/MapPolyline-class.html">/sdk-for-flutter-explore-mapview-mappolyline-class</a></li>
<li class="self-crumb">progress property</li>
</ol>
<h5>MapPolyline class</h5>
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
