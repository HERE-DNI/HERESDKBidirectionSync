---
title: "setVerticalFieldOfView method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-setverticalfieldofview"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setVerticalFieldOfView.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setVerticalFieldOfView</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">setVerticalFieldOfView</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-setVerticalFieldOfView-param-verticalFieldOfView" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">verticalFieldOfView</span></span>

)

</div>

<div class="section desc markdown">

Creates an update to change the vertical field of view of the map camera.

If verticalFieldOfView is not finite, no update will be applied to the map camera.

If the verticalFieldOfView is outside \[1, 150\] interval, it is clamped.

- `verticalFieldOfView` Vertical field of view in degrees.

Returns <a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate setVerticalFieldOfView(double verticalFieldOfView) => $prototype.setVerticalFieldOfView(verticalFieldOfView);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
