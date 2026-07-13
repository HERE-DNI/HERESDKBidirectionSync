---
title: "VenueLifecycleListener constructor - VenueLifecycleListener - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue.control-venuelifecyclelistener-venuelifecyclelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueLifecycleListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/VenueLifecycleListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">VenueLifecycleListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">VenueLifecycleListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onVenueAddedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onVenueAddedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a></span></span>

    ), </span>
2.  <span id="sdk-for-flutter-navigate-param-onVenueRemovedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onVenueRemovedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span></span>

    )</span>

)

</div>

<div class="section desc markdown">

The abstract class for for the <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> lifecycle events.

Use the <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a> to add and remove the <a href="sdk-for-flutter-navigate-venue-control-venuelifecyclelistener-class">VenueLifecycleListener</a>.

</div>

## Implementation

``` dart
factory VenueLifecycleListener(
  void Function(Venue) onVenueAddedLambda,
  void Function(int) onVenueRemovedLambda,

) => VenueLifecycleListener$Lambdas(
  onVenueAddedLambda,
  onVenueRemovedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
