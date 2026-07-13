---
title: "principalPoint property - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcamera-principalpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- principalPoint.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">principalPoint</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span> <span class="name">principalPoint</span>

</div>

<div class="section desc markdown">

Determines the pixel point where the target is placed within the map view. Setting a new principal point instantly moves the map to render the current target coordinates at the new principal point. Gets the pixel point that determines where the target is placed within the map view. By default, the principal point is located at the center of the map view.

The value of the principal point is adjusted when the dimensions of the map view change, so that it stays in the same point relative to width and height. Meaning that when a principal point it set to bottom middle of the map view, it will stay in the bottom middle regardless of the changes to dimensions and orientation of the view.

</div>

## Implementation

``` dart
Point2D get principalPoint;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">principalPoint=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-principalPoint-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Determines the pixel point where the target is placed within the map view. Setting a new principal point instantly moves the map to render the current target coordinates at the new principal point. Sets the pixel point that determines where the target appears within the map view. This instantly moves the map to render the current target coordinates at the new principal point.

By default, the principal point is located at the center of the map view. It is set in pixels relative to the map view's origin top-left (0, 0). Values outside the map view's dimensions (x \< 0 \|\| x \> width, y \< 0 \|\| y \> height) will be rejected silently and the current principal point is kept.

The value of the principal point is adjusted when the dimensions of the map view change, so that it stays in the same point relative to width and height. Meaning that when a principal point it set to bottom middle of the map view, it will stay in the bottom middle regardless of the changes to dimensions and orientation of the view.

Note: The principal point affects all programmatical map transformations (rotate, orbit, tilt and zoom) and the two-finger-pan gesture to tilt the map. Other gestures, like pinch-rotate, are not affected.

</div>

## Implementation

``` dart
set principalPoint(Point2D value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
