---
title: "accessPoints property - Place class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-place-accesspoints"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/Place-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">accessPoints</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="name">accessPoints</span>

</div>

<div class="section desc markdown">

The access points to the place, such as the points on a road or in a parking lot. A place can have multiple access points. For example, a large warehouse can have multiple entrances, while the center of the warehouse may not be directly reachable. Note that access points are meant to be reachable by vehicles. For routes it is recommended to navigate to one of the available access points (if any), whereas the `sideOfStreetHint` should be set to the geographic coordinates of the place. The list is empty when no access points are known or when the place is directly reachable. A place can have multiple access points. For example, a large warehouse can have multiple entrances, while the center of the warehouse may not be directly reachable. Note that access points are meant to be reachable by vehicles. For routes it is recommended to navigate to one of the available access points (if any), whereas the `sideOfStreetHint` should be set to the geographic coordinates of the place. The list is empty when no access points are known or when the place is directly reachable. Gets the access points to the place, such as the points on a road or in a parking lot.

</div>

## Implementation

``` dart
List<GeoCoordinates> get accessPoints;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

