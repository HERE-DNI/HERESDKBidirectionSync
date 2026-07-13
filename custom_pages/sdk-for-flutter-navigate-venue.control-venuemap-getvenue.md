---
title: "getVenue method - VenueMap class - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue.control-venuemap-getvenue"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/VenueMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getVenue</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>?</span> <span class="name">getVenue</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getVenue-param-position" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">position</span></span>

)

</div>

<div class="section desc markdown">

Tries to find a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> at the specified geographic coordinates.

- `position` Geographic coordinates where a venue is located.

Returns <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue?</a>. Venue or `null` if there is no venue at the specified geographic coordinates.

</div>

## Implementation

``` dart
Venue? getVenue(GeoCoordinates position);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

