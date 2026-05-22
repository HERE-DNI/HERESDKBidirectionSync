---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-datasource-polygontilesource-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolygonTileSource-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">PolygonTileSource class</li>
</ol>
<div class="self-name">PolygonTileSource</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/PolygonTileSource-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PolygonTileSource class abstract</h1></div>
<section class="desc markdown">
<p>A source of geodetic polygon tiles.</p>
<p>Polygons provided by an implementation must be clipped to the boundaries of the requested tile.
The implementations must be thread-safe.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-explore-mapview-datasource-tilesource-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PolygonTileSource">
/sdk-for-flutter-explore-mapview-datasource-polygontilesource-polygontilesource(/sdk-for-flutter-explore-mapview-datasource-tilesourcedataversion-class getDataVersionLambda(/sdk-for-flutter-explore-mapview-datasource-tilekey-class), void addListenerLambda(/sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class), void removeListenerLambda(/sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class), /sdk-for-flutter-explore-mapview-datasource-tilesourceloadtilerequesthandle-class? loadTileLambda(/sdk-for-flutter-explore-mapview-datasource-tilekey-class, /sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-class), /sdk-for-flutter-explore-mapview-datasource-tilingscheme tilingSchemeGetLambda(), List&lt;<wbr/>int&gt; storageLevelsGetLambda())
</dt>
<dd>
          A source of geodetic polygon tiles.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-datasource-tilesource-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-datasource-tilesource-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="storageLevels">
/sdk-for-flutter-explore-mapview-datasource-tilesource-storagelevels
→ List&lt;<wbr/>int&gt;
</dt>
<dd class="inherited">
  The storage levels available for this data source. Supported range [0, 31].
At least one level must be available for this to be used as a source of data.
Gets the storage levels available for this data source. Supported range [0, 31].
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="tilingScheme">
/sdk-for-flutter-explore-mapview-datasource-tilesource-tilingscheme
→ /sdk-for-flutter-explore-mapview-datasource-tilingscheme
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
/sdk-for-flutter-explore-mapview-datasource-tilesource-addlistener(<wbr/>/sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class listener)
    → void

</dt>
<dd class="inherited">
  Adds a listener for receiving state notifications.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="getDataVersion">
/sdk-for-flutter-explore-mapview-datasource-tilesource-getdataversion(<wbr/>/sdk-for-flutter-explore-mapview-datasource-tilekey-class tileKey)
    → /sdk-for-flutter-explore-mapview-datasource-tilesourcedataversion-class

</dt>
<dd class="inherited">
  Gets the current data version of a tile.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="loadTile">
/sdk-for-flutter-explore-mapview-datasource-polygontilesource-loadtile(<wbr/>/sdk-for-flutter-explore-mapview-datasource-tilekey-class tileKey, /sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-class completionHandler)
    → /sdk-for-flutter-explore-mapview-datasource-tilesourceloadtilerequesthandle-class?

</dt>
<dd>
  Load data of a tile.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-datasource-tilesource-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="removeListener">
/sdk-for-flutter-explore-mapview-datasource-tilesource-removelistener(<wbr/>/sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class listener)
    → void

</dt>
<dd class="inherited">
  Removes a listener from receiving state notifications.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-datasource-tilesource-tostring(<wbr/>)
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
/sdk-for-flutter-explore-mapview-datasource-tilesource-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">PolygonTileSource class</li>
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



</div>
`
}</HTMLBlock>
