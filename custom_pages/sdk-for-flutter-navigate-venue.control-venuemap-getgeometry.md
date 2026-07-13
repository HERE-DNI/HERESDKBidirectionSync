---
title: "getGeometry method - VenueMap class - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue.control-venuemap-getgeometry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getGeometry.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/VenueMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getGeometry</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a>?</span> <span class="name">getGeometry</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getGeometry-param-position" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">position</span></span>

)

</div>

<div class="section desc markdown">

Tries to find a <a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a> at the specified geographic coordinates in the selected <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> in the currently selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>.

- `position` Geographic coordinates where the geometry is located.

Returns <a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry?</a>. Geometry or `null` if there is no geometry at the specified geographic coordinates.

</div>

## Implementation

``` dart
VenueGeometry? getGeometry(GeoCoordinates position);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
