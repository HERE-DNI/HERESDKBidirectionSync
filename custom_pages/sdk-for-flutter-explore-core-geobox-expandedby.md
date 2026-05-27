---
title: "Implementation"
slug: "sdk-for-flutter-explore-core-geobox-expandedby"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- expandedBy.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li><a href="../../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a></li>
<li class="self-crumb">expandedBy method</li>
</ol>
<div class="self-name">expandedBy</div>
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
<div class="main-content" data-above-sidebar="core/GeoBox-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>expandedBy method</h1></div>
<section class="multi-line-signature">
<a href="../../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>
expandedBy(<wbr/><ol class="parameter-list"> <li>double southMeters, </li>
<li>double westMeters, </li>
<li>double northMeters, </li>
<li>double eastMeters, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates a <code>GeoBox</code> which is expanded by a fixed distance.</p>
<p>Throws an InstantiationError if it is not possible to create a valid
<code>GeoBox</code> with the given arguments.</p>
<ul>
<li>
<p><code>southMeters</code> Distance in the south direction in meters to expand the <code>GeoBox</code>.</p>
</li>
<li>
<p><code>westMeters</code> Distance in the west direction in meters to expand the <code>GeoBox</code>.</p>
</li>
<li>
<p><code>northMeters</code> Distance in the north direction in meters to expand the <code>GeoBox</code>.</p>
</li>
<li>
<p><code>eastMeters</code> Distance in the east direction in meters to expand the <code>GeoBox</code>.</p>
</li>
</ul>
<p>Returns <a href="../../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>. The expanded <code>GeoBox</code>.</p>
<p>Throws <a href="../../core.errors/InstantiationException-class.html">/sdk-for-flutter-explore-core-errors-instantiationexception-class</a>. Instantiation error.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoBox expandedBy(double southMeters, double westMeters, double northMeters, double eastMeters) =&gt; $prototype.expandedBy(this, southMeters, westMeters, northMeters, eastMeters);</code></pre>
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
<li><a href="../../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a></li>
<li class="self-crumb">expandedBy method</li>
</ol>
<h5>GeoBox class</h5>
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
