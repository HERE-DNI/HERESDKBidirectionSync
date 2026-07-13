---
title: "RoutePrefetcher class - prefetcher library - Dart API"
slug: "sdk-for-flutter-navigate-prefetcher-routeprefetcher-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoutePrefetcher-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="prefetcher/prefetcher-library-sidebar.html" data-below-sidebar="prefetcher/RoutePrefetcher-class-sidebar.html">

<div>

# <span class="kind-class">RoutePrefetcher</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Supports downloading of map data - in advance - into the cache to optimize temporary offline use cases that rely on cached map data.

This allows scenarios such as navigation to work in a specific area reliably even though the network might be offline at that time. Please note, this class puts data in the map cache, which has its own size constraints, and extensive usage may start evicting old cached data. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-routeprefetcher">RoutePrefetcher</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a RoutePrefetcher instance for a given <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetchcorridorlengthmeters">prefetchCorridorLengthMeters</a></span> <span class="signature">↔ int</span>  
The length of the corridor along the route in front of the car which will be used to prefetch data. Upper limit for length is 50000 meters, when the requested length is greater than upper limit, then 50000 meters set. Lower limit for length is 1000 meters, when the requested length is less than lower limit, then 1000 meters set. The route corridor has a default length of 10 km and a width of 5 km. Gets the length of the corridor along the route in front of the car which will be used to prefetch data.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name deprecated"><a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetcharoundlocationwithradius" class="deprecated">prefetchAroundLocationWithRadius</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-prefetchAroundLocationWithRadius-param-currentLocation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">currentLocation</span>, </span><span id="sdk-for-flutter-navigate-prefetchAroundLocationWithRadius-param-radiusInMeters" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">radiusInMeters</span></span>) <span class="returntype parameter">→ void</span> </span>  
Prefetches map data within a user-defined circular area around a given location.

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetcharoundrouteonintervals">prefetchAroundRouteOnIntervals</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-prefetchAroundRouteOnIntervals-param-navigator" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a></span> <span class="parameter-name">navigator</span></span>) <span class="returntype parameter">→ void</span> </span>  
Prefetches map data within a corridor along the route, that is currently set for the provided <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> instance.

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetchgeocorridor">prefetchGeoCorridor</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-prefetchGeoCorridor-param-corridor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocorridor-class">GeoCorridor</a></span> <span class="parameter-name">corridor</span>, </span><span id="sdk-for-flutter-navigate-prefetchGeoCorridor-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-class">PrefetchStatusListener</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Prefetch tiles for a given geo-corridor.

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-stopprefetcharoundroute">stopPrefetchAroundRoute</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Stops listening <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> passed to <a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetcharoundrouteonintervals">RoutePrefetcher.prefetchAroundRouteOnIntervals</a> for route progress events and stops prefetching data along the current route.

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
