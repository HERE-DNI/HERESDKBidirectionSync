---
title: "VenueMapListener constructor - VenueMapListener - venue.service library - Dart API"
slug: "sdk-for-flutter-navigate-venue-service-venuemaplistener-venuemaplistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.service/VenueMapListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">VenueMapListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">VenueMapListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onGetVenueCompletedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onGetVenueCompletedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a>?</span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">bool</span>, </span>
    4.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-style-venuestyle-class">VenueStyle</a>?</span>, </span>

    )</span>

)

</div>

<div class="section desc markdown">

The abstract class for listeners for venue loading events in <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a>.

</div>

## Implementation

``` dart
factory VenueMapListener(
  void Function(String, VenueModel?, bool, VenueStyle?) onGetVenueCompletedLambda,

) => VenueMapListener$Lambdas(
  onGetVenueCompletedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

