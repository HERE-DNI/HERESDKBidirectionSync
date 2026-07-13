---
title: "lookAtPoint method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtPoint.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookAtPoint</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">lookAtPoint</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-lookAtPoint-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a></span> <span class="parameter-name">target</span></span>

)

</div>

<div class="section desc markdown">

Creates an update to position the map camera to look at the given target, preserving the current orientation at look-at target and map measure.

Any target sub-element value that is not finite will be excluded from the update.

The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

- `target` The look-at target position in geodetic coordinates, altitude is ignored, the target is considered to be located on the ground.

Returns <a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate lookAtPoint(GeoCoordinatesUpdate target) => $prototype.lookAtPoint(target);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
