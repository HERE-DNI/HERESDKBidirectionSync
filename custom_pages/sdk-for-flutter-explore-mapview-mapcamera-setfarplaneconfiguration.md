---
title: "setFarPlaneConfiguration method - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcamera-setfarplaneconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setFarPlaneConfiguration.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setFarPlaneConfiguration</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setFarPlaneConfiguration</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-setFarPlaneConfiguration-param-configs" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>, <span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-class">MapCameraFarPlaneConfiguration</a></span>\></span></span> <span class="parameter-name">configs</span></span>

)

</div>

<div class="section desc markdown">

Sets far plane distance configs per zoom level.

Values are linearly interpolated between provided zoom levels. For z between z0 and z1: t = (z - z0) / (z1 - z0) distanceFactor(z) = lerp(distanceFactor0, distanceFactor1, t) minDistance(z) = lerp(minDistance0, minDistance1, t)

Effective far plane for the current frame is: farPlaneInMeters = max( minDistance(z), distanceToTargetInMeters \* distanceFactor(z) )

Sample Configuration (balanced quality/performance, tune per zoom level): 14.4 -\> FarPlaneConfiguration(1.3) 18.34 -\> FarPlaneConfiguration(2.0) 19.60 -\> FarPlaneConfiguration(1.3) minDistanceInMeters remains default in this case. Passing an empty map clears the per-zoom override and restores the default behavior. Non-finite zoom levels or values are ignored. Distance factors are clamped to 0.1 to 10.0. The minimum distance is clamped to a range of \[100, 3000\] meters.

- `configs` Per-zoom override mapping from zoom level to distance configuration.

</div>

## Implementation

``` dart
void setFarPlaneConfiguration(Map<double, MapCameraFarPlaneConfiguration> configs);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
