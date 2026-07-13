---
title: "setNormalizedPrincipalPoint method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-setnormalizedprincipalpoint"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setNormalizedPrincipalPoint</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">setNormalizedPrincipalPoint</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-setNormalizedPrincipalPoint-param-principalPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">principalPoint</span></span>

)

</div>

<div class="section desc markdown">

Creates an update to change the map camera's principal point (where the view vector intersects the image plane - default is (0.5, 0.5)).

Point values are in normalized screen coordinates.

If the principalPoint is outside \[0,1\] interval, it is clamped. (0,0) is top left of the viewport, (1,1) is bottom right.

- `principalPoint` Principal point in normalized screen coordinates.

Returns <a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate setNormalizedPrincipalPoint(Anchor2D principalPoint) => $prototype.setNormalizedPrincipalPoint(principalPoint);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

