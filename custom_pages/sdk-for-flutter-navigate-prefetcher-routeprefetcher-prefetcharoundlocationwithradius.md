---
title: "prefetchAroundLocationWithRadius method - RoutePrefetcher class - prefetcher library - Dart API"
slug: "sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetcharoundlocationwithradius"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- prefetchAroundLocationWithRadius.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="prefetcher/RoutePrefetcher-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">prefetchAroundLocationWithRadius</span> abstract method

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.27.0. Please use \[PolygonPrefetcher.prefetch\] instead.")

</div>

<span class="returntype">void</span> <span class="name deprecated">prefetchAroundLocationWithRadius</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-prefetchAroundLocationWithRadius-param-currentLocation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">currentLocation</span>, </span>
2.  <span id="sdk-for-flutter-navigate-prefetchAroundLocationWithRadius-param-radiusInMeters" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">radiusInMeters</span></span>

)

</div>

<div class="section desc markdown">

Prefetches map data within a user-defined circular area around a given location.

The radius, specified in meters, must be between 1 km and 50 km. If `null` is passed as the radius, a default value of 2 km is used. It is recommended to call this method once before starting navigation to ensure a smooth experience.

To control list of map content features for area prefetch, use <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>.

- `currentLocation` The center of the circle to prefetch data within.

- `radiusInMeters` The radius of the circle to prefetch data within.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.27.0. Please use [PolygonPrefetcher.prefetch] instead.")

void prefetchAroundLocationWithRadius(GeoCoordinates currentLocation, double? radiusInMeters);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
