---
title: "VenueLevelSelectionListener constructor - VenueLevelSelectionListener - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue-control-venuelevelselectionlistener-venuelevelselectionlistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/VenueLevelSelectionListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">VenueLevelSelectionListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">VenueLevelSelectionListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onLevelSelectedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onLevelSelectedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>?</span>, </span>
    4.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a></span>, </span>

    )</span>

)

</div>

<div class="section desc markdown">

The abstract class for for the <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> selection event.

Use the <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a> to add and remove the <a href="sdk-for-flutter-navigate-venue-control-venuelevelselectionlistener-class">VenueLevelSelectionListener</a>.

</div>

## Implementation

``` dart
factory VenueLevelSelectionListener(
  void Function(Venue, VenueDrawing, VenueLevel?, VenueLevel) onLevelSelectedLambda,

) => VenueLevelSelectionListener$Lambdas(
  onLevelSelectedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

