---
title: "isDepthCheckEnabled property - MapMarker3D class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker3d-isdepthcheckenabled"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isDepthCheckEnabled.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker3D-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">isDepthCheckEnabled</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">isDepthCheckEnabled</span>

</div>

<div class="section desc markdown">

Determines whether the depth of the 3D marker's vertices is considered during rendering. If set to `false`, the 3D marker will always appear in front of any other map objects. If set to `true` the 3D marker might be occluded by other map objects like extruded buildings.

By default depth check is set to `false`.

Use the altitude of the <a href="sdk-for-flutter-navigate-mapview-mapmarker3d-coordinates">MapMarker3D.coordinates</a> to position the 3D marker sufficiently high above the surface. Setting depth check to `true` will fix visual glitches where components of the marker 3D model unexpectedly shine through. Returns `true` if depth check is enabled.

</div>

## Implementation

``` dart
bool get isDepthCheckEnabled;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">isDepthCheckEnabled=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-isDepthCheckEnabled-param-value" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Determines whether the depth of the 3D marker's vertices is considered during rendering. If set to `false`, the 3D marker will always appear in front of any other map objects. If set to `true` the 3D marker might be occluded by other map objects like extruded buildings.

By default depth check is set to `false`.

Use the altitude of the <a href="sdk-for-flutter-navigate-mapview-mapmarker3d-coordinates">MapMarker3D.coordinates</a> to position the 3D marker sufficiently high above the surface. Setting depth check to `true` will fix visual glitches where components of the marker 3D model unexpectedly shine through. Set whether the depth of the 3D marker's vertices is considered during rendering.

</div>

## Implementation

``` dart
set isDepthCheckEnabled(bool value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
