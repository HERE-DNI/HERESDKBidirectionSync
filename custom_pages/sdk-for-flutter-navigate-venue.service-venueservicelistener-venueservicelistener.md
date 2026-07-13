---
title: "VenueServiceListener constructor - VenueServiceListener - venue.service library - Dart API"
slug: "sdk-for-flutter-navigate-venue.service-venueservicelistener-venueservicelistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.service/VenueServiceListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">VenueServiceListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">VenueServiceListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onInitializationCompletedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onInitializationCompletedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-service-venueserviceinitstatus">VenueServiceInitStatus</a></span></span>

    ), </span>
2.  <span id="sdk-for-flutter-navigate-param-onVenueServiceStoppedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onVenueServiceStoppedLambda</span>()</span>

)

</div>

<div class="section desc markdown">

The abstract class for listeners for lifecycle events in <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a>.

</div>

## Implementation

``` dart
factory VenueServiceListener(
  void Function(VenueServiceInitStatus) onInitializationCompletedLambda,
  void Function() onVenueServiceStoppedLambda,

) => VenueServiceListener$Lambdas(
  onInitializationCompletedLambda,
  onVenueServiceStoppedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

