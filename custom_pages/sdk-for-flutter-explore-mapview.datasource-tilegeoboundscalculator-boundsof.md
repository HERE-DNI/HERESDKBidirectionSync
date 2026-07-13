---
title: "boundsOf method - TileGeoBoundsCalculator class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-tilegeoboundscalculator-boundsof"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- boundsOf.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/TileGeoBoundsCalculator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">boundsOf</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="name">boundsOf</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-boundsOf-param-tileKey" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a></span> <span class="parameter-name">tileKey</span></span>

)

</div>

<div class="section desc markdown">

Computes the geodetic bounds (as <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>) for a tile identified by <a href="sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a>.

- `tileKey` <a href="sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a> to compute geodetic bounds for. The geodetic bounds would be calculated relative to the tiling scheme provided at this <a href="sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-class">TileGeoBoundsCalculator</a> instance creation.

Returns <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>. The geodetic bounds of tile identified by given <a href="sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a>.

</div>

## Implementation

``` dart
GeoBox boundsOf(TileKey tileKey);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
