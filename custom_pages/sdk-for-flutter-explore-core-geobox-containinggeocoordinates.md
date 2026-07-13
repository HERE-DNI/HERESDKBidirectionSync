---
title: "containingGeoCoordinates method - GeoBox class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-geobox-containinggeocoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- containingGeoCoordinates.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoBox-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">containingGeoCoordinates</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>?</span> <span class="name">containingGeoCoordinates</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-containingGeoCoordinates-param-geoCoordinates" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">geoCoordinates</span></span>

)

</div>

<div class="section desc markdown">

Creates a `GeoBox` which encompases all coordinates from the list.

The provided list must contain at least two points. The altitude values of the input coordinates are not considered for the result.

- `geoCoordinates` List of coordinates to encompass inside bounding box.

Returns <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox?</a>. `GeoBox` containing all supplied coordinates, or `null` if less than two coordinates were provided.

</div>

## Implementation

``` dart
static GeoBox? containingGeoCoordinates(List<GeoCoordinates> geoCoordinates) => $prototype.containingGeoCoordinates(geoCoordinates);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
