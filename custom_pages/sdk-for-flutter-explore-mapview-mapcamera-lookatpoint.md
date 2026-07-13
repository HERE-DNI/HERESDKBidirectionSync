---
title: "lookAtPoint method - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcamera-lookatpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtPoint.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookAtPoint</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">lookAtPoint</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-lookAtPoint-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">target</span></span>

)

</div>

<div class="section desc markdown">

Makes the camera look at a new geodetic target, while preserving the current orientation and distance to the target.

The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

- `target` Geodetic coordinates at which the camera will point.

</div>

## Implementation

``` dart
void lookAtPoint(GeoCoordinates target);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
