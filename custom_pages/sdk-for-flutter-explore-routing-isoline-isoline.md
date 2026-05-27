---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-isoline-isoline"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- Isoline.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/Isoline-class.html">/sdk-for-flutter-explore-routing-isoline-class</a></li>
<li class="self-crumb">Isoline factory constructor</li>
</ol>
<div class="self-name">Isoline</div>
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
<div class="main-content" data-above-sidebar="routing/Isoline-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>Isoline constructor</h1></div>
<section class="multi-line-signature">
Isoline(<wbr/><ol class="parameter-list"> <li><a href="../../routing/IsolineRangeType.html">/sdk-for-flutter-explore-routing-isolinerangetype</a> rangeType, </li>
<li>double rangeValue, </li>
<li><a href="../../routing/MapMatchedCoordinates-class.html">/sdk-for-flutter-explore-routing-mapmatchedcoordinates-class</a> center, </li>
<li>List&lt;<wbr/><a href="../../core/GeoPolygon-class.html">/sdk-for-flutter-explore-core-geopolygon-class</a>&gt; polygons, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Constructs an isoline instance.</p>
<p>This instance is provided by the
<a href="../../routing/CalculateIsolineCallback.html">/sdk-for-flutter-explore-routing-calculateisolinecallback</a>.</p>
<ul>
<li>
<p><code>rangeType</code> Specifies the range type of the provided <code>Isoline.Isoline().rangeValue</code> list.</p>
</li>
<li>
<p><code>rangeValue</code> A list of range values. At least one value must be set.</p>
</li>
<li>
<p><code>center</code> The center of the isoline.</p>
</li>
<li>
<p><code>polygons</code> A list of polygons that belong to this isoline. At least one value must be set.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory Isoline(IsolineRangeType rangeType, double rangeValue, MapMatchedCoordinates center, List&lt;GeoPolygon&gt; polygons) =&gt; $prototype.make(rangeType, rangeValue, center, polygons);</code></pre>
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
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/Isoline-class.html">/sdk-for-flutter-explore-routing-isoline-class</a></li>
<li class="self-crumb">Isoline factory constructor</li>
</ol>
<h5>Isoline class</h5>
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
