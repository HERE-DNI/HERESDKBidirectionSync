---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-datasource-linetilesource-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- LineTileSource-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/LineTileSource-class.html#constructors">Constructors</a></li>
<li><a href="mapview.datasource/LineTileSource/LineTileSource.html">LineTileSource</a></li>
<li class="section-title inherited">
<a href="mapview.datasource/LineTileSource-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview.datasource/TileSource/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview.datasource/TileSource/runtimeType.html">runtimeType</a></li>
<li class="inherited"><a href="mapview.datasource/TileSource/storageLevels.html">storageLevels</a></li>
<li class="inherited"><a href="mapview.datasource/TileSource/tilingScheme.html">tilingScheme</a></li>
<li class="section-title"><a href="mapview.datasource/LineTileSource-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview.datasource/TileSource/addListener.html">addListener</a></li>
<li class="inherited"><a href="mapview.datasource/TileSource/getDataVersion.html">getDataVersion</a></li>
<li><a href="mapview.datasource/LineTileSource/loadTile.html">loadTile</a></li>
<li class="inherited"><a href="mapview.datasource/TileSource/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview.datasource/TileSource/removeListener.html">removeListener</a></li>
<li class="inherited"><a href="mapview.datasource/TileSource/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview.datasource/LineTileSource-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview.datasource/TileSource/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li class="self-crumb">LineTileSource class</li>
</ol>
<div class="self-name">LineTileSource</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/LineTileSource-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>LineTileSource class abstract</h1></div>
<section class="desc markdown">
<p>A source of geodetic line tiles.</p>
<p>Lines provided by an implementation must be clipped to the boundaries of the requested tile.
The implementations must be thread-safe.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li><a href="../mapview.datasource/TileSource-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesource-class</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="LineTileSource">
<a href="../mapview.datasource/LineTileSource/LineTileSource.html">/sdk-for-flutter-explore-mapview-datasource-linetilesource-linetilesource</a>(<a href="../mapview.datasource/TileSourceDataVersion-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesourcedataversion-class</a> getDataVersionLambda(<a href="../mapview.datasource/TileKey-class.html">/sdk-for-flutter-explore-mapview-datasource-tilekey-class</a>), void addListenerLambda(<a href="../mapview.datasource/TileSourceListener-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class</a>), void removeListenerLambda(<a href="../mapview.datasource/TileSourceListener-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class</a>), <a href="../mapview.datasource/TileSourceLoadTileRequestHandle-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesourceloadtilerequesthandle-class</a>? loadTileLambda(<a href="../mapview.datasource/TileKey-class.html">/sdk-for-flutter-explore-mapview-datasource-tilekey-class</a>, <a href="../mapview.datasource/LineTileSourceLoadResultHandler-class.html">/sdk-for-flutter-explore-mapview-datasource-linetilesourceloadresulthandler-class</a>), <a href="../mapview.datasource/TilingScheme.html">/sdk-for-flutter-explore-mapview-datasource-tilingscheme</a> tilingSchemeGetLambda(), List&lt;<wbr/>int&gt; storageLevelsGetLambda())
</dt>
<dd>
          A source of geodetic line tiles.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview.datasource/TileSource/hashCode.html">/sdk-for-flutter-explore-mapview-datasource-tilesource-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview.datasource/TileSource/runtimeType.html">/sdk-for-flutter-explore-mapview-datasource-tilesource-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="storageLevels">
<a href="../mapview.datasource/TileSource/storageLevels.html">/sdk-for-flutter-explore-mapview-datasource-tilesource-storagelevels</a>
→ List&lt;<wbr/>int&gt;
</dt>
<dd class="inherited">
  The storage levels available for this data source. Supported range [0, 31].
At least one level must be available for this to be used as a source of data.
Gets the storage levels available for this data source. Supported range [0, 31].
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="tilingScheme">
<a href="../mapview.datasource/TileSource/tilingScheme.html">/sdk-for-flutter-explore-mapview-datasource-tilesource-tilingscheme</a>
→ <a href="../mapview.datasource/TilingScheme.html">/sdk-for-flutter-explore-mapview-datasource-tilingscheme</a>
</dt>
<dd class="inherited">
  The tiling scheme used by this source.
Gets the tiling scheme used by this source.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="addListener">
<a href="../mapview.datasource/TileSource/addListener.html">/sdk-for-flutter-explore-mapview-datasource-tilesource-addlistener</a>(<wbr/><a href="../mapview.datasource/TileSourceListener-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class</a> listener)
    → void

</dt>
<dd class="inherited">
  Adds a listener for receiving state notifications.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="getDataVersion">
<a href="../mapview.datasource/TileSource/getDataVersion.html">/sdk-for-flutter-explore-mapview-datasource-tilesource-getdataversion</a>(<wbr/><a href="../mapview.datasource/TileKey-class.html">/sdk-for-flutter-explore-mapview-datasource-tilekey-class</a> tileKey)
    → <a href="../mapview.datasource/TileSourceDataVersion-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesourcedataversion-class</a>
</dt>
<dd class="inherited">
  Gets the current data version of a tile.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="loadTile">
<a href="../mapview.datasource/LineTileSource/loadTile.html">/sdk-for-flutter-explore-mapview-datasource-linetilesource-loadtile</a>(<wbr/><a href="../mapview.datasource/TileKey-class.html">/sdk-for-flutter-explore-mapview-datasource-tilekey-class</a> tileKey, <a href="../mapview.datasource/LineTileSourceLoadResultHandler-class.html">/sdk-for-flutter-explore-mapview-datasource-linetilesourceloadresulthandler-class</a> completionHandler)
    → <a href="../mapview.datasource/TileSourceLoadTileRequestHandle-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesourceloadtilerequesthandle-class</a>?

</dt>
<dd>
  Load data of a tile.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview.datasource/TileSource/noSuchMethod.html">/sdk-for-flutter-explore-mapview-datasource-tilesource-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="removeListener">
<a href="../mapview.datasource/TileSource/removeListener.html">/sdk-for-flutter-explore-mapview-datasource-tilesource-removelistener</a>(<wbr/><a href="../mapview.datasource/TileSourceListener-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class</a> listener)
    → void

</dt>
<dd class="inherited">
  Removes a listener from receiving state notifications.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview.datasource/TileSource/toString.html">/sdk-for-flutter-explore-mapview-datasource-tilesource-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../mapview.datasource/TileSource/operator_equals.html">/sdk-for-flutter-explore-mapview-datasource-tilesource-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li class="self-crumb">LineTileSource class</li>
</ol>
<h5>mapview.datasource library</h5>
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
