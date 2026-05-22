---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasource-rasterdatasource-withtilesourceandlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSource.withTileSourceAndListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-class</li>
<li class="self-crumb">RasterDataSource.withTileSourceAndListener factory constructor</li>
</ol>
<div class="self-name">RasterDataSource.withTileSourceAndListener</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/RasterDataSource-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>RasterDataSource.withTileSourceAndListener constructor</h1></div>
<section class="multi-line-signature">
RasterDataSource.withTileSourceAndListener(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-explore-mapview-mapcontext-class context, </li>
<li>String name, </li>
<li>/sdk-for-flutter-explore-mapview-datasource-rastertilesource-class tileSource, </li>
<li>/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcelistener-class listener, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a RasterDataSource instance with the provided raster tile source and registers
a listener.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>context</code> The map context to associate the data source with.</p>
</li>
<li>
<p><code>name</code> The unique name of the data source.</p>
</li>
<li>
<p><code>tileSource</code> The raster tile source.</p>
</li>
<li>
<p><code>listener</code> The initial listener to be registered for receiving state notifications.
Due to the asynchronous nature of the data source initialization, the listeners
registered later might miss some notifications. This listener is guaranteed to
receive all notifications.
The state notifications can occur on an arbitrary thread.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RasterDataSource.withTileSourceAndListener(MapContext context, String name, RasterTileSource tileSource, RasterDataSourceListener listener) =&gt; $prototype.withTileSourceAndListener(context, name, tileSource, listener);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-class</li>
<li class="self-crumb">RasterDataSource.withTileSourceAndListener factory constructor</li>
</ol>
<h5>RasterDataSource class</h5>
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
