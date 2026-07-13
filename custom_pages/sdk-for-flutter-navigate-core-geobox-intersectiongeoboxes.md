---
title: "intersectionGeoBoxes method - GeoBox class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-geobox-intersectiongeoboxes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- intersectionGeoBoxes.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoBox-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">intersectionGeoBoxes</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span>\></span></span> <span class="name">intersectionGeoBoxes</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-intersectionGeoBoxes-param-geoBoxes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span>\></span></span> <span class="parameter-name">geoBoxes</span></span>

)

</div>

<div class="section desc markdown">

Computes intersection of list of <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a> instances.

The altitude values are ignored. Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `geoBoxes` List of <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a> instances.

Returns `List<GeoBox>`. It will be empty if there is no overlap between all the passed <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a> instances.

Otherwise, 1 or more geo boxes covering common area by all the passed <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a> instances.

</div>

## Implementation

``` dart
static List<GeoBox> intersectionGeoBoxes(List<GeoBox> geoBoxes) => $prototype.intersectionGeoBoxes(geoBoxes);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
