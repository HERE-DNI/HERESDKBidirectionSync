---
title: "getIndoorMarkerFor method - IndoorRouteStyle class - venue.routing library - Dart API"
slug: "sdk-for-flutter-navigate-venue-routing-indoorroutestyle-getindoormarkerfor"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.routing/IndoorRouteStyle-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getIndoorMarkerFor</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>?</span> <span class="name">getIndoorMarkerFor</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getIndoorMarkerFor-param-feature" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a></span> <span class="parameter-name">feature</span>, </span>
2.  <span id="sdk-for-flutter-navigate-getIndoorMarkerFor-param-deltaZ" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">deltaZ</span></span>

)

</div>

<div class="section desc markdown">

Returns a <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a> for a given indoor feature and the number of levels to change.

By default, no map markers are provided.

- `feature` An indoor feature.

- `deltaZ` A number of levels to change, positive for up, negative for down. In the case of 0, the method returns an exit map marker.

Returns <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker?</a>. The result <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>, if it was set.

</div>

## Implementation

``` dart
MapMarker? getIndoorMarkerFor(IndoorLevelChangeFeatures feature, int deltaZ);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

