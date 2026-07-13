---
title: "GeoOrientationUpdate constructor - GeoOrientationUpdate - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-geoorientationupdate-geoorientationupdate"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoOrientationUpdate-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">GeoOrientationUpdate</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">GeoOrientationUpdate</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-bearing" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">bearing</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-tilt" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">tilt</span></span>

)

</div>

<div class="section desc markdown">

- `bearing` Bearing in degrees. When the passed value is `null` bearing is not updated and the current value is kept. NaN value is converted to `null`.

- `tilt` Tilt in degrees. When the passed value is `null` tilt is not updated and the current value is kept. NaN value is converted to `null`.

</div>

## Implementation

``` dart
factory GeoOrientationUpdate(double? bearing, double? tilt) => $prototype.$init(bearing, tilt);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

