---
title: "VenueInfoListListener constructor - VenueInfoListListener - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue-control-venueinfolistlistener-venueinfolistlistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/VenueInfoListListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">VenueInfoListListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">VenueInfoListListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onVenueInfoListLoadLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onVenueInfoListLoadLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueinfodatalist">VenueInfoDataList</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

The abstract class for for the list of <a href="sdk-for-flutter-navigate-venue-data-venueinfo-class">VenueInfo</a> load event.

Use <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a> to add and remove the <a href="sdk-for-flutter-navigate-venue-control-venueinfolistlistener-class">VenueInfoListListener</a>.

</div>

## Implementation

``` dart
factory VenueInfoListListener(
  void Function(VenueInfoDataList) onVenueInfoListLoadLambda,

) => VenueInfoListListener$Lambdas(
  onVenueInfoListLoadLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

