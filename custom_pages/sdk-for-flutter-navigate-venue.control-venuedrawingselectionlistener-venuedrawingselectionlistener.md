---
title: "VenueDrawingSelectionListener constructor - VenueDrawingSelectionListener - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue.control-venuedrawingselectionlistener-venuedrawingselectionlistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/VenueDrawingSelectionListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">VenueDrawingSelectionListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">VenueDrawingSelectionListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onDrawingSelectedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onDrawingSelectedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>?</span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

The abstract class for for the <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> selection event.

Use the <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a> to add and remove the <a href="sdk-for-flutter-navigate-venue-control-venuedrawingselectionlistener-class">VenueDrawingSelectionListener</a>.

</div>

## Implementation

``` dart
factory VenueDrawingSelectionListener(
  void Function(Venue, VenueDrawing?, VenueDrawing) onDrawingSelectedLambda,

) => VenueDrawingSelectionListener$Lambdas(
  onDrawingSelectedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

