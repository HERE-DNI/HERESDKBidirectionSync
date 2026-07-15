---
title: "setIndoorMarkersFor method - IndoorRouteStyle class - venue.routing library - Dart API"
slug: "sdk-for-flutter-navigate-venue-routing-indoorroutestyle-setindoormarkersfor"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.routing/IndoorRouteStyle-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setIndoorMarkersFor</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setIndoorMarkersFor</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setIndoorMarkersFor-param-feature" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a></span> <span class="parameter-name">feature</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setIndoorMarkersFor-param-upMarker" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>?</span> <span class="parameter-name">upMarker</span>, </span>
3.  <span id="sdk-for-flutter-navigate-setIndoorMarkersFor-param-downMarker" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>?</span> <span class="parameter-name">downMarker</span>, </span>
4.  <span id="sdk-for-flutter-navigate-setIndoorMarkersFor-param-exitMarker" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>?</span> <span class="parameter-name">exitMarker</span>, </span>

)

</div>

<div class="section desc markdown">

Sets map markers for the given indoor feature.

- `feature` An indoor feature.

- `upMarker` A <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a> to go up.

- `downMarker` A <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a> to go down.

- `exitMarker` A <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a> to exit the indoor feature.

</div>

## Implementation

``` dart
void setIndoorMarkersFor(IndoorLevelChangeFeatures feature, MapMarker? upMarker, MapMarker? downMarker, MapMarker? exitMarker);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

