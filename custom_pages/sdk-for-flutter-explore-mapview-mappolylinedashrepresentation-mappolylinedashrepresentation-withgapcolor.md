---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-mappolylinedashrepresentation-withgapcolor"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapPolylineDashRepresentation.withGapColor.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapPolylineDashRepresentation-class.html">/sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-class</a></li>
<li class="self-crumb">MapPolylineDashRepresentation.withGapColor factory constructor</li>
</ol>
<div class="self-name">MapPolylineDashRepresentation.withGapColor</div>
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
<h1>MapPolylineDashRepresentation.withGapColor constructor</h1></div>
<section class="multi-line-signature">
MapPolylineDashRepresentation.withGapColor(<wbr/><ol class="parameter-list"> <li><a href="../../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> lineWidth, </li>
<li><a href="../../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> dashLength, </li>
<li><a href="../../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> gapLength, </li>
<li>Color dashColor, </li>
<li>Color gapColor, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a representation for a dashed line with both dash and the gap being colored.</p>
<p>At map measures smaller than the smallest map measure in the <code>lineWidth</code>,
<code>dashLength</code> and <code>gapLength</code>, the value used for rendering is constant
and equal to the value given for the smallest map measure in the
respective <a href="../../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> object.</p>
<p>At map measures bigger than the biggest map measure in the <code>lineWidth</code>,
<code>dashLength</code> and <code>gapLength</code>, the value used for rendering is constant
and equal to the value given for the biggest map measure in the
respective <a href="../../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> object.</p>
<p>At map measures between two nearest given map measures, the values are
linearly interpolated between values given for these map measures.</p>
<p>For <a href="../../mapview/MapMeasureKind.html">/sdk-for-flutter-explore-mapview-mapmeasurekind</a> only <a href="../../mapview/MapMeasureKind.html">/sdk-for-flutter-explore-mapview-mapmeasurekind</a> is supported.</p>
<p>For <a href="../../mapview/RenderSizeUnit.html">/sdk-for-flutter-explore-mapview-rendersizeunit</a> only <a href="../../mapview/RenderSizeUnit.html">/sdk-for-flutter-explore-mapview-rendersizeunit</a> is supported.</p>
<p>All sizes must not be 0 (<a href="../../mapview/MapMeasureDependentRenderSize/sizes.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-sizes</a> with all values set to 0.0).</p>
<ul>
<li>
<p><code>lineWidth</code> The width of the polyline depending on the map measure.</p>
</li>
<li>
<p><code>dashLength</code> The dash length of the polyline depending on the map measure.</p>
</li>
<li>
<p><code>gapLength</code> The gap length of the polyline depending on the map measure.</p>
</li>
<li>
<p><code>dashColor</code> The color of the dashes.</p>
</li>
<li>
<p><code>gapColor</code> The color of the gaps.</p>
</li>
</ul>
<p>Throws <a href="../../mapview/MapPolylineRepresentationInstantiationException-class.html">/sdk-for-flutter-explore-mapview-mappolylinerepresentationinstantiationexception-class</a>. In case of invalid input parameters.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolylineDashRepresentation.withGapColor(MapMeasureDependentRenderSize lineWidth, MapMeasureDependentRenderSize dashLength, MapMeasureDependentRenderSize gapLength, ui.Color dashColor, ui.Color gapColor) =&gt; $prototype.withGapColor(lineWidth, dashLength, gapLength, dashColor, gapColor);</code></pre>
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
<li class="self-crumb">MapPolylineDashRepresentation.withGapColor factory constructor</li>
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
