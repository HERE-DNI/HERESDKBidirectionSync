---
title: "expandedBy method - GeoBox class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-geobox-expandedby"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoBox-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">expandedBy</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="name">expandedBy</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-expandedBy-param-southMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">southMeters</span>, </span>
2.  <span id="sdk-for-flutter-explore-expandedBy-param-westMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">westMeters</span>, </span>
3.  <span id="sdk-for-flutter-explore-expandedBy-param-northMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">northMeters</span>, </span>
4.  <span id="sdk-for-flutter-explore-expandedBy-param-eastMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">eastMeters</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a `GeoBox` which is expanded by a fixed distance.

Throws an InstantiationError if it is not possible to create a valid `GeoBox` with the given arguments.

- `southMeters` Distance in the south direction in meters to expand the `GeoBox`.

- `westMeters` Distance in the west direction in meters to expand the `GeoBox`.

- `northMeters` Distance in the north direction in meters to expand the `GeoBox`.

- `eastMeters` Distance in the east direction in meters to expand the `GeoBox`.

Returns <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>. The expanded `GeoBox`.

Throws <a href="sdk-for-flutter-explore-core-errors-instantiationexception-class">InstantiationException</a>. Instantiation error.

</div>

## Implementation

``` dart
GeoBox expandedBy(double southMeters, double westMeters, double northMeters, double eastMeters) => $prototype.expandedBy(this, southMeters, westMeters, northMeters, eastMeters);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

