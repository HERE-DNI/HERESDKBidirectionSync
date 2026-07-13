---
title: "envelopeGeoBoxes method - GeoBox class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-geobox-envelopegeoboxes"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoBox-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">envelopeGeoBoxes</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>?</span> <span class="name">envelopeGeoBoxes</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-envelopeGeoBoxes-param-geoBoxes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span>\></span></span> <span class="parameter-name">geoBoxes</span></span>

)

</div>

<div class="section desc markdown">

Envelopes the list of `GeoBox` areas by returning the smallest `GeoBox` covering all specified `GeoBox` objects.

- `geoBoxes` List of `GeoBox` objects.

Returns <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox?</a>. `GeoBox` covering all `GeoBox` areas, or `null` if input is empty.

</div>

## Implementation

``` dart
static GeoBox? envelopeGeoBoxes(List<GeoBox> geoBoxes) => $prototype.envelopeGeoBoxes(geoBoxes);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

