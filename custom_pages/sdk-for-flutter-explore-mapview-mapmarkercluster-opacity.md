---
title: "opacity property - MapMarkerCluster class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmarkercluster-opacity"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarkerCluster-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">opacity</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">double</span> <span class="name">opacity</span>

</div>

<div class="section desc markdown">

Opacity is the factor which is applied to the alpha channel of the image used for marker cluster. Gets the current opacity of the marker cluster image.

</div>

## Implementation

``` dart
double get opacity;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">opacity=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-opacity-param-value" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Opacity is the factor which is applied to the alpha channel of the image used for marker cluster. Sets the opacity of the marker cluster image.

Provided value is clamped in range \[0.0, 1.0\]. Default value is 1.0 which means marker cluster is displayed with the default opacity of the image.

Marker clusters with opacity value set to 0.0 are still on the map and are considered for picking.

Markers part of cluster will use their respective opacity when not displayed as a cluster icon.

</div>

## Implementation

``` dart
set opacity(double value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

