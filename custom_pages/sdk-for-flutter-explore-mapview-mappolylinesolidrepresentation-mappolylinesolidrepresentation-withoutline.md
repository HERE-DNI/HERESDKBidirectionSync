---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-mappolylinesolidrepresentation-withoutline"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapPolylineSolidRepresentation.withOutline.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapPolylineSolidRepresentation-class.html">/sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-class</a></li>
<li class="self-crumb">MapPolylineSolidRepresentation.withOutline factory constructor</li>
</ol>
<div class="self-name">MapPolylineSolidRepresentation.withOutline</div>
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
<div class="main-content" data-above-sidebar="mapview/MapPolylineSolidRepresentation-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapPolylineSolidRepresentation.withOutline constructor</h1></div>
<section class="multi-line-signature">
MapPolylineSolidRepresentation.withOutline(<wbr/><ol class="parameter-list"> <li><a href="../../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> lineWidth, </li>
<li>Color color, </li>
<li><a href="../../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> outlineWidth, </li>
<li>Color outlineColor, </li>
<li><a href="../../mapview/LineCap.html">/sdk-for-flutter-explore-mapview-linecap</a> capShape, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a representation for a solid line with outline.</p>
<p>The total width of the polyline is <code>line width + 2 * outline width</code>.</p>
<p>At map measures smaller than smallest map measure in the <code>lineWidth</code>
and <code>outlineWidth</code>, the value is constant and equal to the width given for
the smallest map measure in the <code>lineWidth</code> and <code>outlineWidth</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
and <code>outlineWidth</code>, the value is constant and equal to the width given for
the biggest map measure in the <code>lineWidth</code> and <code>outlineWidth</code>.</p>
<p>At map measures between two nearest given map measure is
linearly interpolated between width values given for these map measures.</p>
<p>For <a href="../../mapview/MapMeasureKind.html">/sdk-for-flutter-explore-mapview-mapmeasurekind</a> only <a href="../../mapview/MapMeasureKind.html">/sdk-for-flutter-explore-mapview-mapmeasurekind</a> is supported.</p>
<p>For <a href="../../mapview/RenderSizeUnit.html">/sdk-for-flutter-explore-mapview-rendersizeunit</a> only <a href="../../mapview/RenderSizeUnit.html">/sdk-for-flutter-explore-mapview-rendersizeunit</a> is supported.</p>
<p><code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).</p>
<ul>
<li>
<p><code>lineWidth</code> The width of the polyline depending on the map measure.</p>
</li>
<li>
<p><code>color</code> The color of the polyline.</p>
</li>
<li>
<p><code>outlineWidth</code> The width of the outline on one side of the polyline depending on
the map measure.</p>
</li>
<li>
<p><code>outlineColor</code> The outline color of the polyline.</p>
</li>
<li>
<p><code>capShape</code> The cap shape applied to both ends of the polyline.</p>
</li>
</ul>
<p>Throws <a href="../../mapview/MapPolylineRepresentationInstantiationException-class.html">/sdk-for-flutter-explore-mapview-mappolylinerepresentationinstantiationexception-class</a>. In case of invalid input parameters.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolylineSolidRepresentation.withOutline(MapMeasureDependentRenderSize lineWidth, ui.Color color, MapMeasureDependentRenderSize outlineWidth, ui.Color outlineColor, LineCap capShape) =&gt; $prototype.withOutline(lineWidth, color, outlineWidth, outlineColor, capShape);</code></pre>
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
<li><a href="../../mapview/MapPolylineSolidRepresentation-class.html">/sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-class</a></li>
<li class="self-crumb">MapPolylineSolidRepresentation.withOutline factory constructor</li>
</ol>
<h5>MapPolylineSolidRepresentation class</h5>
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
