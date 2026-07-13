---
title: "opacity property - MapMarker3D class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker3d-opacity"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- opacity.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker3D-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">opacity</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">double</span> <span class="name">opacity</span>

</div>

<div class="section desc markdown">

The opacity factor adjusting the opacity of a 3D marker. The factor is applied to the alpha channel of the resulting texture of the marker. Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the specified fill color specified in <a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a>. Returns an opacity factor which specifies the translucency of a 3D map marker.

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

The opacity factor adjusting the opacity of a 3D marker. The factor is applied to the alpha channel of the resulting texture of the marker. Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the specified fill color specified in <a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a>. Sets an opacity factor which specifies the translucency of a 3D map marker.

Provided value is clamped to the \[0.0, 1.0\] range.

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
