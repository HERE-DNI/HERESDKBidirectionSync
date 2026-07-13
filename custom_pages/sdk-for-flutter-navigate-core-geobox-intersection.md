---
title: "intersection method - GeoBox class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-geobox-intersection"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- intersection.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoBox-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">intersection</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span>\></span></span> <span class="name">intersection</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-intersection-param-geoBox" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span> <span class="parameter-name">geoBox</span></span>

)

</div>

<div class="section desc markdown">

Computes the intersection with the passed <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>.

The altitude values are ignored. Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `geoBox` Another geo box to check intersection with.

Returns `List<GeoBox>`. It will be empty if there is no overlap.

Otherwise, 1 or more geo boxes covering common area by this and passed <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>.

</div>

## Implementation

``` dart
List<GeoBox> intersection(GeoBox geoBox) => $prototype.intersection(this, geoBox);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
