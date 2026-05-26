---
title: "MapLayerVisibilityRange constructor"
slug: "sdk-for-flutter-explore-mapview-maplayervisibilityrange-maplayervisibilityrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapLayerVisibilityRange.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-maplayervisibilityrange-class</li>
<li class="self-crumb">MapLayerVisibilityRange const constructor</li>
</ol>
<div class="self-name">MapLayerVisibilityRange</div>
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
<div class="main-content" data-above-sidebar="mapview/MapLayerVisibilityRange-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapLayerVisibilityRange constructor</h1></div>
<section class="multi-line-signature">
      const
      MapLayerVisibilityRange(<wbr/><ol class="parameter-list single-line"> <li>double minimumZoomLevel, </li>
<li>double maximumZoomLevel</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>minimumZoomLevel</code> Minimum zoom level on which the layer will be visible. The value must be greater than or equal to the <code>MapCameraLimits.MIN_ZOOM_LEVEL</code>.</li>
<li><code>maximumZoomLevel</code> Minimum zoom level from which the layer will not be visible. The value must be less than or equal to the <code>MapCameraLimits.MAX_ZOOM_LEVEL</code>.
Note that the map layer is not visible at the maximum zoom level.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">const MapLayerVisibilityRange(this.minimumZoomLevel, this.maximumZoomLevel);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-maplayervisibilityrange-class</li>
<li class="self-crumb">MapLayerVisibilityRange const constructor</li>
</ol>
<h5>MapLayerVisibilityRange class</h5>
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
`
}</HTMLBlock>
