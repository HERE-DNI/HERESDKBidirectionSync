---
title: "LocationListener constructor - LocationListener - core library - Dart API"
slug: "sdk-for-flutter-explore-core-locationlistener-locationlistener"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/LocationListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">LocationListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">LocationListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-onLocationUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onLocationUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-location-class">Location</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications about location updates.

</div>

## Implementation

``` dart
factory LocationListener(
  void Function(Location) onLocationUpdatedLambda,

) => LocationListener$Lambdas(
  onLocationUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

