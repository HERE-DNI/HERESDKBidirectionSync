---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-mappolylinedashimagerepresentation"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapPolylineDashImageRepresentation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapPolylineDashImageRepresentation-class.html">/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-class</a></li>
<li class="self-crumb">MapPolylineDashImageRepresentation factory constructor</li>
</ol>
<div class="self-name">MapPolylineDashImageRepresentation</div>
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
<div class="main-content" data-above-sidebar="mapview/MapPolylineDashImageRepresentation-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapPolylineDashImageRepresentation constructor</h1></div>
<section class="multi-line-signature">
MapPolylineDashImageRepresentation(<wbr/><ol class="parameter-list"> <li><a href="../../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> dashLength, </li>
<li><a href="../../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> gapLength, </li>
<li><a href="../../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> dashWidth, </li>
<li><a href="../../mapview/MapImage-class.html">/sdk-for-flutter-explore-mapview-mapimage-class</a> image, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a simple dash pattern in which the lengths of a dash and gap can be different.</p>
<p>Dashes are rendered as image.</p>
<p>This allows for patterns like <code>'  —  —  —  —'</code> or <code>' ——— ——— ———'</code>.</p>
<p>For <a href="../../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> supplied for <code>dashLength</code>, <code>gapLength</code> and <code>dashWidth</code>,
only <a href="../../mapview/MapMeasureKind.html">/sdk-for-flutter-explore-mapview-mapmeasurekind</a> is supported for <a href="../../mapview/MapMeasureDependentRenderSize/measureKind.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-measurekind</a>
and only <a href="../../mapview/RenderSizeUnit.html">/sdk-for-flutter-explore-mapview-rendersizeunit</a> is supported for <a href="../../mapview/MapMeasureDependentRenderSize/sizeUnit.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-sizeunit</a>.</p>
<p>Only map measure values in range [3-19] are supported.</p>
<p>The value of the keys in <a href="../../mapview/MapMeasureDependentRenderSize/sizes.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-sizes</a> is truncated to integer values,
hence only a single value can be provided per zoom level.</p>
<p>The values are interpolated linearly between zoom levels.</p>
<ul>
<li>
<p><code>dashLength</code> The map measure dependent length of a dash, to which image width is stretched.</p>
</li>
<li>
<p><code>gapLength</code> The map measure dependent length of a gap between dash images.</p>
</li>
<li>
<p><code>dashWidth</code> The map measure dependent width of a dash, to which image height is stretched.</p>
</li>
<li>
<p><code>image</code> Image to be rendered in place of dash space. It is stretched to match <code>dashWidth</code> and <code>dashLength</code>.</p>
</li>
</ul>
<p>Throws <a href="../../mapview/MapPolylineRepresentationInstantiationException-class.html">/sdk-for-flutter-explore-mapview-mappolylinerepresentationinstantiationexception-class</a>. In case of invalid input parameters.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolylineDashImageRepresentation(MapMeasureDependentRenderSize dashLength, MapMeasureDependentRenderSize gapLength, MapMeasureDependentRenderSize dashWidth, MapImage image) =&gt; $prototype.$init(dashLength, gapLength, dashWidth, image);</code></pre>
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
<li><a href="../../mapview/MapPolylineDashImageRepresentation-class.html">/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-class</a></li>
<li class="self-crumb">MapPolylineDashImageRepresentation factory constructor</li>
</ol>
<h5>MapPolylineDashImageRepresentation class</h5>
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
