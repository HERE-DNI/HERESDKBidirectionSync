---
title: "opacity property - MapMarker class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-opacity"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- opacity.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">opacity</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">double</span> <span class="name">opacity</span>

</div>

<div class="section desc markdown">

Opacity, the factor applied to the alpha channel of the marker image. Gets the current opacity of the marker image. Value is in the range of \[0.0, 1.0\]. Default value is 1.0.

</div>

## Implementation

``` dart
double get opacity;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">opacity=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-opacity-param-value" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Opacity, the factor applied to the alpha channel of the marker image. Sets the opacity of the marker image.

Provided value is clamped to the range of \[0.0, 1.0\]. Default value is 1.0, which means marker is displayed with the default opacity of the image.

Markers with opacity value set to 0.0 are still on the map and are considered for picking.

</div>

## Implementation

``` dart
set opacity(double value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
