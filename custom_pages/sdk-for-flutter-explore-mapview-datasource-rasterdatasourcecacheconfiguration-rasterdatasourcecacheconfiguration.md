---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-rasterdatasourcecacheconfiguration"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- RasterDataSourceCacheConfiguration.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li><a href="../../mapview.datasource/RasterDataSourceCacheConfiguration-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-class</a></li>
<li class="self-crumb">RasterDataSourceCacheConfiguration constructor</li>
</ol>
<div class="self-name">RasterDataSourceCacheConfiguration</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/RasterDataSourceCacheConfiguration-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>RasterDataSourceCacheConfiguration constructor</h1></div>
<section class="multi-line-signature">
RasterDataSourceCacheConfiguration(<wbr/><ol class="parameter-list single-line"> <li>String path, </li>
<li>int diskSize</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Constructs a Cache object from the provided path and cache size.</p>
<ul>
<li><code>path</code> The path to the directory to use for the cache. By default, the map gets initialized with a
data path which can be fetched from <code>SDKOptions.cachePath</code>. The cache will be relative to this path,
unless an absolute path is provided. The cache can be stored in an internal/external storage as long
as the app has read/write permissions.
Empty string means the data path will be used for caching.
If the provided path, either as absolute path or as relative path is invalid,
then caching will be disabled.
There is no contraint regarding the existence of the path. If the path does not exist
but is valid, it will be created.</li>
<li><code>diskSize</code> The maximum size to use on disk for the cache, in bytes. Default is 32 MiB.
This cache is independent from the map cache as defined via <code>SDKOptions</code>.
Its size is only limited by the total device storage capacity.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RasterDataSourceCacheConfiguration(this.path, this.diskSize);</code></pre>
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
<li><a href="../../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li><a href="../../mapview.datasource/RasterDataSourceCacheConfiguration-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-class</a></li>
<li class="self-crumb">RasterDataSourceCacheConfiguration constructor</li>
</ol>
<h5>RasterDataSourceCacheConfiguration class</h5>
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
