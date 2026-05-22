---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-mappolylinesolidrepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineSolidRepresentation.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-class</li>
<li class="self-crumb">MapPolylineSolidRepresentation factory constructor</li>
</ol>
<div class="self-name">MapPolylineSolidRepresentation</div>
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
<h1>MapPolylineSolidRepresentation constructor</h1></div>
<section class="multi-line-signature">
MapPolylineSolidRepresentation(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class lineWidth, </li>
<li>Color color, </li>
<li>/sdk-for-flutter-navigate-mapview-linecap capShape</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a representation for a solid line without outline.</p>
<p>At map measures smaller than smallest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the smallest
map measure in the <code>lineWidth</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the biggest
map measure in the <code>lineWidth</code>.</p>
<p>At map measures between two nearest given map measures line width is
linearly interpolated between width values given for these map measures.</p>
<p>For /sdk-for-flutter-navigate-mapview-mapmeasurekind only /sdk-for-flutter-navigate-mapview-mapmeasurekind is supported.</p>
<p>For /sdk-for-flutter-navigate-mapview-rendersizeunit only /sdk-for-flutter-navigate-mapview-rendersizeunit is supported.</p>
<p><code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).</p>
<ul>
<li>
<p><code>lineWidth</code> The width of the polyline depending on the map measure.</p>
</li>
<li>
<p><code>color</code> The color of the polyline.</p>
</li>
<li>
<p><code>capShape</code> The cap shape applied to both ends of the polyline.</p>
</li>
</ul>
<p>Throws /sdk-for-flutter-navigate-mapview-mappolylinerepresentationinstantiationexception-class. In case of invalid input parameters.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolylineSolidRepresentation(MapMeasureDependentRenderSize lineWidth, ui.Color color, LineCap capShape) =&gt; $prototype.$init(lineWidth, color, capShape);</code></pre>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-class</li>
<li class="self-crumb">MapPolylineSolidRepresentation factory constructor</li>
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



</div>
`
}</HTMLBlock>
