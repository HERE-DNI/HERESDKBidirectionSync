---
title: "setCustomStyle method - Venue class - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue-control-venue-setcustomstyle"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/Venue-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setCustomStyle</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setCustomStyle</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setCustomStyle-param-geometries" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a></span>\></span></span> <span class="parameter-name">geometries</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setCustomStyle-param-style" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-style-venuegeometrystyle-class">VenueGeometryStyle</a>?</span> <span class="parameter-name">style</span>, </span>
3.  <span id="sdk-for-flutter-navigate-setCustomStyle-param-labelStyle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-style-venuelabelstyle-class">VenueLabelStyle</a>?</span> <span class="parameter-name">labelStyle</span></span>

)

</div>

<div class="section desc markdown">

Sets a custom style for geometries and related labels.

- `geometries` The list of geometries to apply the new style.

- `style` The style for geometries, or `null` to reset the style to default.

- `labelStyle` The style for geometry labels, or `null` to reset the label style to default.

</div>

## Implementation

``` dart
void setCustomStyle(List<VenueGeometry> geometries, VenueGeometryStyle? style, VenueLabelStyle? labelStyle);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

