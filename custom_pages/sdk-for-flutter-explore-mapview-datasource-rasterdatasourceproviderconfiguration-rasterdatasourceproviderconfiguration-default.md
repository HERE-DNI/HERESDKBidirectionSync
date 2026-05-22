---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-rasterdatasourceproviderconfiguration-default"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSourceProviderConfiguration.Default.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-class</li>
<li class="self-crumb">RasterDataSourceProviderConfiguration.Default constructor</li>
</ol>
<div class="self-name">RasterDataSourceProviderConfiguration.Default</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/RasterDataSourceProviderConfiguration-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>RasterDataSourceProviderConfiguration.Default constructor</h1></div>
<section class="multi-line-signature">
RasterDataSourceProviderConfiguration.Default(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback urlProvider, </li>
<li>/sdk-for-flutter-explore-mapview-datasource-tilingscheme tilingScheme, </li>
<li>List&lt;<wbr/>int&gt; storageLevels, </li>
<li>bool hasAlphaChannel, </li>
<li>Map&lt;<wbr/>String, String&gt;? headers, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>urlProvider</code> Provides a function that generates URLs based on tile coordinates and storage level.</li>
<li><code>tilingScheme</code> The tiling scheme used by this source.</li>
<li><code>storageLevels</code> The storage levels available for this data source. Supported range [0, 31].
At least one level must be available for this provider to be used as a source of data.
At storage level zero, the whole world is represented by one tile. At storage level 1
the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme).
The tiling process continues in this fashion until sufficient granularity has been
achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds
to the storage level.
Depending on the available storage levels and the given camera zoom level, the
appropriate z value of the tile key will be determined.</li>
<li><code>hasAlphaChannel</code> A flag indicating whether the image content contains an alpha channel for transparency. Default value is <code>false</code>.</li>
<li><code>headers</code> The optional name-value pairs specifying HTTP headers that are passed with each tile request.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RasterDataSourceProviderConfiguration.Default(this.urlProvider, this.tilingScheme, this.storageLevels, this.hasAlphaChannel, this.headers);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-class</li>
<li class="self-crumb">RasterDataSourceProviderConfiguration.Default constructor</li>
</ol>
<h5>RasterDataSourceProviderConfiguration class</h5>
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
