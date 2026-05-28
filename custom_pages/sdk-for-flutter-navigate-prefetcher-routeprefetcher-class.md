---
title: "RoutePrefetcher class abstract"
slug: "sdk-for-flutter-navigate-prefetcher-routeprefetcher-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoutePrefetcher-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="prefetcher/RoutePrefetcher-class.html#constructors">Constructors</a></li>
<li><a href="prefetcher/RoutePrefetcher/RoutePrefetcher.html">RoutePrefetcher</a></li>
<li class="section-title">
<a href="prefetcher/RoutePrefetcher-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="prefetcher/RoutePrefetcher/hashCode.html">hashCode</a></li>
<li><a href="prefetcher/RoutePrefetcher/prefetchCorridorLengthMeters.html">prefetchCorridorLengthMeters</a></li>
<li class="inherited"><a href="prefetcher/RoutePrefetcher/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="prefetcher/RoutePrefetcher-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="prefetcher/RoutePrefetcher/noSuchMethod.html">noSuchMethod</a></li>
<li><a class="deprecated" href="prefetcher/RoutePrefetcher/prefetchAroundLocationWithRadius.html">prefetchAroundLocationWithRadius</a></li>
<li><a href="prefetcher/RoutePrefetcher/prefetchAroundRouteOnIntervals.html">prefetchAroundRouteOnIntervals</a></li>
<li><a href="prefetcher/RoutePrefetcher/prefetchGeoCorridor.html">prefetchGeoCorridor</a></li>
<li><a href="prefetcher/RoutePrefetcher/stopPrefetchAroundRoute.html">stopPrefetchAroundRoute</a></li>
<li class="inherited"><a href="prefetcher/RoutePrefetcher/toString.html">toString</a></li>
<li class="section-title inherited"><a href="prefetcher/RoutePrefetcher-class.html#operators">Operators</a></li>
<li class="inherited"><a href="prefetcher/RoutePrefetcher/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li class="self-crumb">RoutePrefetcher class</li>
</ol>
<div class="self-name">RoutePrefetcher</div>
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
<div class="main-content" data-above-sidebar="prefetcher/prefetcher-library-sidebar.html" data-below-sidebar="prefetcher/RoutePrefetcher-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RoutePrefetcher class abstract</h1></div>
<section class="desc markdown">
<p>Supports downloading of map data - in advance - into the cache to optimize temporary offline
use cases that rely on cached map data.</p>
<p>This allows scenarios such as navigation to work in a
specific area reliably even though the network might be offline at that time.
Please note, this class puts data in the map cache, which has its own size constraints,
and extensive usage may start evicting old cached data.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RoutePrefetcher">
/sdk-for-flutter-navigate-prefetcher-routeprefetcher-routeprefetcher(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
</dt>
<dd>
          Creates a RoutePrefetcher instance for a given /sdk-for-flutter-navigate-core-engine-sdknativeengine-class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-prefetcher-routeprefetcher-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="prefetchCorridorLengthMeters">
/sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetchcorridorlengthmeters
↔ int
</dt>
<dd>
  The length of the corridor along the route in front of the car which will be used to prefetch data.
Upper limit for length is 50000 meters, when the requested length is greater than upper limit, then 50000 meters set.
Lower limit for length is 1000 meters, when the requested length is less than lower limit, then 1000 meters set.
The route corridor has a default length of 10 km and a width of 5 km.
Gets the length of the corridor along the route in front of the car which will be used to prefetch data.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-prefetcher-routeprefetcher-runtimetype
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
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-prefetcher-routeprefetcher-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="prefetchAroundLocationWithRadius">
/sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetcharoundlocationwithradius(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class currentLocation, double? radiusInMeters)
    → void

</dt>
<dd>
  Prefetches map data within a user-defined circular area around a given location.
  

</dd>
<dt class="callable" id="prefetchAroundRouteOnIntervals">
/sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetcharoundrouteonintervals(<wbr/>/sdk-for-flutter-navigate-navigation-navigatorinterface-class navigator)
    → void

</dt>
<dd>
  Prefetches map data within a corridor along the route, that is currently set for the
provided /sdk-for-flutter-navigate-navigation-navigatorinterface-class instance.
  

</dd>
<dt class="callable" id="prefetchGeoCorridor">
/sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetchgeocorridor(<wbr/>/sdk-for-flutter-navigate-core-geocorridor-class corridor, /sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-class callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Prefetch tiles for a given geo-corridor.
  

</dd>
<dt class="callable" id="stopPrefetchAroundRoute">
/sdk-for-flutter-navigate-prefetcher-routeprefetcher-stopprefetcharoundroute(<wbr/>)
    → void

</dt>
<dd>
  Stops listening /sdk-for-flutter-navigate-navigation-navigatorinterface-class passed to /sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetcharoundrouteonintervals
for route progress events and stops prefetching data along the current route.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-prefetcher-routeprefetcher-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-prefetcher-routeprefetcher-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">RoutePrefetcher class</li>
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
</div></div>
</div>
`
}</HTMLBlock>
