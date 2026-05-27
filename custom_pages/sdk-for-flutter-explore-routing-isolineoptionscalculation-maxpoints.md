---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-isolineoptionscalculation-maxpoints"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- maxPoints.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/IsolineOptionsCalculation-class.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-class</a></li>
<li class="self-crumb">maxPoints property</li>
</ol>
<div class="self-name">maxPoints</div>
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
<div class="main-content" data-above-sidebar="routing/IsolineOptionsCalculation-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>maxPoints property</h1></div>
<section class="multi-line-signature">
        
        int?
        maxPoints
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Limits the number of points in the resulting isoline polygon. If the
isoline consists of multiple polygons, the sum of points from all
polygons is considered. Note that this parameter does not affect the calculation,
but the shape of the polygon. Look at <a href="../../routing/IsolineCalculationMode.html">/sdk-for-flutter-explore-routing-isolinecalculationmode</a> parameter
to optimize performance.
A higher value will result in a more accurate polygon shape. Rendering a polygon
with a high number of points can negatively impact rendering performance.
The minimum allowed value is 30, lower values will be ignored.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? maxPoints;</code></pre>
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
<li><a href="../../routing/IsolineOptionsCalculation-class.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-class</a></li>
<li class="self-crumb">maxPoints property</li>
</ol>
<h5>IsolineOptionsCalculation class</h5>
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
