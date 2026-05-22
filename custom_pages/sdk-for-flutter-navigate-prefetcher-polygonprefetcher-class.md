---
title: "Untitled"
slug: "sdk-for-flutter-navigate-prefetcher-polygonprefetcher-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolygonPrefetcher-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li class="self-crumb">PolygonPrefetcher class</li>
</ol>
<div class="self-name">PolygonPrefetcher</div>
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
<div class="main-content" data-above-sidebar="prefetcher/prefetcher-library-sidebar.html" data-below-sidebar="prefetcher/PolygonPrefetcher-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PolygonPrefetcher class abstract</h1></div>
<section class="desc markdown">
<p>Supports downloading of map data - in advance - into the cache to optimize temporary offline
use cases that rely on cached map data.</p>
<p>Please note, this class puts data in the map cache, which has its own size constraints,
and extensive usage may start evicting old cached data.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PolygonPrefetcher">
/sdk-for-flutter-navigate-prefetcher-polygonprefetcher-polygonprefetcher(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
</dt>
<dd>
          Creates a PolygonPrefetcher instance for a given /sdk-for-flutter-navigate-core-engine-sdknativeengine-class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-prefetcher-polygonprefetcher-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-prefetcher-polygonprefetcher-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="estimateMapDataSize">
/sdk-for-flutter-navigate-prefetcher-polygonprefetcher-estimatemapdatasize(<wbr/>/sdk-for-flutter-navigate-core-geopolygon-class geoPolygon, /sdk-for-flutter-navigate-prefetcher-mapdatasizelistener-class callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Estimates map data size for the area bounded by geo polygon.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-prefetcher-polygonprefetcher-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="prefetch">
/sdk-for-flutter-navigate-prefetcher-polygonprefetcher-prefetch(<wbr/>/sdk-for-flutter-navigate-core-geopolygon-class geoPolygon, /sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-class callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Prefetches map data for an area bounded by geo polygon.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-prefetcher-polygonprefetcher-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-prefetcher-polygonprefetcher-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li class="self-crumb">PolygonPrefetcher class</li>
</ol>
<h5>prefetcher library</h5>
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
