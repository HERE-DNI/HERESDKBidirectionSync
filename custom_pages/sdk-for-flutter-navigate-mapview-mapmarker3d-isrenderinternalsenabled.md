---
title: "isRenderInternalsEnabled property - MapMarker3D class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker3d-isrenderinternalsenabled"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isRenderInternalsEnabled.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker3D-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">isRenderInternalsEnabled</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">isRenderInternalsEnabled</span>

</div>

<div class="section desc markdown">

Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons. Default value is `false`. Can be used with translucent 3D marker.

Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two passes: first pass with front-face, second pass with back-face culling enabled. With this flag enabled for 3D marker with depth check disabled rendering is performed in a single pass with back-face culling disabled. Returns a flag indicating whether to render internal geometry of a 3D marker occluded by its front facing polygons. Default value is `false`.

</div>

## Implementation

``` dart
bool get isRenderInternalsEnabled;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">isRenderInternalsEnabled=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-isRenderInternalsEnabled-param-value" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons. Default value is `false`. Can be used with translucent 3D marker.

Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two passes: first pass with front-face, second pass with back-face culling enabled. With this flag enabled for 3D marker with depth check disabled rendering is performed in a single pass with back-face culling disabled. Sets a flag indicating whether to render internal geometry of a 3D marker occluded by its front facing polygons.

</div>

## Implementation

``` dart
set isRenderInternalsEnabled(bool value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
