---
title: "PolygonPrefetcher class - prefetcher library - Dart API"
slug: "sdk-for-flutter-navigate-prefetcher-polygonprefetcher-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolygonPrefetcher-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="prefetcher/prefetcher-library-sidebar.html" data-below-sidebar="prefetcher/PolygonPrefetcher-class-sidebar.html">

<div>

# <span class="kind-class">PolygonPrefetcher</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Supports downloading of map data - in advance - into the cache to optimize temporary offline use cases that rely on cached map data.

Please note, this class puts data in the map cache, which has its own size constraints, and extensive usage may start evicting old cached data. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-polygonprefetcher-polygonprefetcher">PolygonPrefetcher</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a PolygonPrefetcher instance for a given <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-polygonprefetcher-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-polygonprefetcher-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-polygonprefetcher-estimatemapdatasize">estimateMapDataSize</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-estimateMapDataSize-param-geoPolygon" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">geoPolygon</span>, </span><span id="sdk-for-flutter-navigate-estimateMapDataSize-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-prefetcher-mapdatasizelistener-class">MapDataSizeListener</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Estimates map data size for the area bounded by geo polygon.

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-polygonprefetcher-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-polygonprefetcher-prefetch">prefetch</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-prefetch-param-geoPolygon" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">geoPolygon</span>, </span><span id="sdk-for-flutter-navigate-prefetch-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-class">PrefetchStatusListener</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Prefetches map data for an area bounded by geo polygon.

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-polygonprefetcher-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-polygonprefetcher-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
