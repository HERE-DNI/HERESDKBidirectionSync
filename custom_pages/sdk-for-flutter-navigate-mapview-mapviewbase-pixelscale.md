---
title: "pixelScale property - MapViewBase class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapviewbase-pixelscale"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapViewBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">pixelScale</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">double</span> <span class="name">pixelScale</span>

</div>

<div class="section desc markdown">

The pixel scale factor used by this `MapView`.

Pixel scale is 0.0 if the map view is not initialized.

In cases where the `MapView` moves in between screens (e.g. from main screen to a CarPlay screen), / the most up-to-date pixel scale value can be obtained after a render target gets attached to the view. / To get notified when a render target gets attached to the `MapView`, see <a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a>. It is used to support screen resolution and size independence. This value is a derivative of the device's screen pixel density and is a direct analog of

devicePixelRatio from FlutterView, ViewConfiguration or MediaQueryData. It can be used to translate between physical pixels and

logical pixels according to the formula:

logicalPixels = pixels / pixelScale. Gets the pixel scale factor used by this `MapView`.

</div>

## Implementation

``` dart
double get pixelScale;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

