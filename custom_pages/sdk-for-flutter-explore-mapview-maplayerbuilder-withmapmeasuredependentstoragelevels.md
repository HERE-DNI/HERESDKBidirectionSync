---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-maplayerbuilder-withmapmeasuredependentstoragelevels"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- withMapMeasureDependentStorageLevels.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapLayerBuilder-class.html">/sdk-for-flutter-explore-mapview-maplayerbuilder-class</a></li>
<li class="self-crumb">withMapMeasureDependentStorageLevels abstract method</li>
</ol>
<div class="self-name">withMapMeasureDependentStorageLevels</div>
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
<div class="main-content" data-above-sidebar="mapview/MapLayerBuilder-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>withMapMeasureDependentStorageLevels abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../mapview/MapLayerBuilder-class.html">/sdk-for-flutter-explore-mapview-maplayerbuilder-class</a>
withMapMeasureDependentStorageLevels(<wbr/><ol class="parameter-list single-line"> <li><a href="../../mapview/MapLayerMapMeasureDependentStorageLevels-class.html">/sdk-for-flutter-explore-mapview-maplayermapmeasuredependentstoragelevels-class</a> mapLayerMapMeasureDependentStorageLevels</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Applies a mapping from the map measure to the storage level.</p>
<p>This mapping is used by the layer to request data
for the specified storage level corresponding to the map measure from the datasource.
This can be used for example to fine-tune the resolution of raster layers.
Note: When the map camera is significantly tilted, the storage level is further reduced for data towards the horizon.
Note: Mappings that request higher storage levels will lead to an increased number
of requests to the raster tile service.
Providing the map measure to storage level mapping is optional. If not provided, the default mapping will
use a storage level that is for raster layers one and for others three levels lower than the zoom level,
corresponding to an offset of -1 and -3.</p>
<ul>
<li><code>mapLayerMapMeasureDependentStorageLevels</code> The map measure to storage level mapping that should be applied for the layer.</li>
</ul>
<p>Returns <a href="../../mapview/MapLayerBuilder-class.html">/sdk-for-flutter-explore-mapview-maplayerbuilder-class</a>. This class instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapLayerBuilder withMapMeasureDependentStorageLevels(MapLayerMapMeasureDependentStorageLevels mapLayerMapMeasureDependentStorageLevels);</code></pre>
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
<li><a href="../../mapview/MapLayerBuilder-class.html">/sdk-for-flutter-explore-mapview-maplayerbuilder-class</a></li>
<li class="self-crumb">withMapMeasureDependentStorageLevels abstract method</li>
</ol>
<h5>MapLayerBuilder class</h5>
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
