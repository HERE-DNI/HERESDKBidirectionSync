---
title: "addVenueAsyncWithErrorsStr method - VenueMap class - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue-control-venuemap-addvenueasyncwitherrorsstr"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/VenueMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">addVenueAsyncWithErrorsStr</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">addVenueAsyncWithErrorsStr</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-addVenueAsyncWithErrorsStr-param-venueIdentifier" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">venueIdentifier</span>, </span>
2.  <span id="sdk-for-flutter-navigate-addVenueAsyncWithErrorsStr-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueloaderrorcallback">VenueLoadErrorCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Downloads and adds a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> to the <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>.

Method will do nothing if the venue already exists on the venue map.

- `venueIdentifier` The ID of the venue to download and add.

- `callback` Callback to receives the error while venue load on the main thread.

</div>

## Implementation

``` dart
void addVenueAsyncWithErrorsStr(String venueIdentifier, VenueLoadErrorCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

