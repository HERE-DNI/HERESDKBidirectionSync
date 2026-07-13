---
title: "viewToGeoCoordinates method - MapViewBase class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapviewbase-viewtogeocoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- viewToGeoCoordinates.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapViewBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">viewToGeoCoordinates</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>?</span> <span class="name">viewToGeoCoordinates</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-viewToGeoCoordinates-param-viewCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span> <span class="parameter-name">viewCoordinates</span></span>

)

</div>

<div class="section desc markdown">

Converts view coordinates (in pixels) to geographical coordinates.

An optional altitude component of the resulting geographical coordinate is not set.

If the view coordinates specify a point above a horizon, then the result is geographical coordinates of the point on a horizon below the specified view coordinates.

The fog effect is ignored for the calculation, meaning that for the view point within the area covered by the fog, the result is geographical coordinates that would be displayed at the specified point if the fog effect was not applied.

If the render surface is not attached, it will return `null`.

- `viewCoordinates` Point inside the view to convert.

Returns <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates?</a>. The geographical coordinates under specified view point or `null` if there is no render surface attached.

</div>

## Implementation

``` dart
GeoCoordinates? viewToGeoCoordinates(Point2D viewCoordinates);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
