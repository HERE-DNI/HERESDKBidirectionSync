---
title: "selectVenueAsyncWithErrors method - VenueMap class - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasyncwitherrors"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/VenueMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">selectVenueAsyncWithErrors</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">selectVenueAsyncWithErrors</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-selectVenueAsyncWithErrors-param-venueId" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">venueId</span>, </span>
2.  <span id="sdk-for-flutter-navigate-selectVenueAsyncWithErrors-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueloaderrorcallback">VenueLoadErrorCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Downloads a <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> if needed and selects a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>.

- `venueId` The ID of the venue to download and select.

- `callback` Callback to receives the error while venue load on the main thread.

</div>

## Implementation

``` dart
void selectVenueAsyncWithErrors(int venueId, VenueLoadErrorCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

