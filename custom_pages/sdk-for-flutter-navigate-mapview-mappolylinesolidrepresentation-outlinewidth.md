---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-outlinewidth"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- outlineWidth.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-class</li>
<li class="self-crumb">outlineWidth property</li>
</ol>
<div class="self-name">outlineWidth</div>
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
<h1>outlineWidth property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class
outlineWidth
</section>
<section class="desc markdown">
<p>The width of the outline on one side of the polyline depending on the map measure.
The total width of the polyline is <code>line width + 2 * outline width</code>.</p>
<p>At map measures smaller than smallest map measure in the <code>outlineWidth</code>,
outline width is constant and equal to the width given for the smallest
map measure in the <code>outlineWidth</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>outlineWidth</code>,
outline width is constant and equal to the width given for the biggest
map measure in the <code>outlineWidth</code>.</p>
<p>At map measures between two nearest given map measures, the values are
linearly interpolated between values given for these map measures.
Gets the map measure dependent polyline outline width.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMeasureDependentRenderSize get outlineWidth;</code></pre>
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-class</li>
<li class="self-crumb">outlineWidth property</li>
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
