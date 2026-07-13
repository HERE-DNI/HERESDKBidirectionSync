---
title: "isAccuracyVisualized property - LocationIndicator class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-locationindicator-isaccuracyvisualized"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isAccuracyVisualized.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/LocationIndicator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">isAccuracyVisualized</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">isAccuracyVisualized</span>

</div>

<div class="section desc markdown">

Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo. Returns whether <a href="sdk-for-flutter-navigate-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a> is used to scale the accuracy indicator halo. Default is `false`, in which case the halo has a fixed and zoom level independent size.

</div>

## Implementation

``` dart
bool get isAccuracyVisualized;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">isAccuracyVisualized=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-isAccuracyVisualized-param-value" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo. Sets whether <a href="sdk-for-flutter-navigate-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a> is used to scale the accuracy indicator halo. Default is `false`, in which case the halo has a fixed and zoom level independent size.

When set to `true`, the radius of the halo corresponds to the value of <a href="sdk-for-flutter-navigate-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a> passed to <a href="sdk-for-flutter-navigate-mapview-locationindicator-updatelocation">LocationIndicator.updateLocation</a> and scales in world coordinates.

For values smaller than 20 meters the halo is hidden. The radius of the halo is limited to 500 meters and values higher than that or `null` will keep the halo at that size.

If the location indicator is set to inactive (which can be checked via <a href="sdk-for-flutter-navigate-mapview-locationindicator-isactive">LocationIndicator.isActive</a> flag), then the halo is always hidden. The value of this property remains unchanged regardless of the flag's value. If the location indicator is set to active:

- Built-in location indicators:
  - The halo is always shown.
  - If the accuracy visualization is set to `true`, the size of the halo scales with <a href="sdk-for-flutter-navigate-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a> in world coordinates.
  - If the accuracy visualization is set to `false`, halo displays at a default size.
- Custom location indicator:
  - If the accuracy visualization is set to `true`, halo is shown and the size of the halo scales with <a href="sdk-for-flutter-navigate-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a> in world coordinates.
  - If the accuracy visualization is set to `false`, no halo is shown since it might not fit together with the custom 3d model.

</div>

## Implementation

``` dart
set isAccuracyVisualized(bool value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
