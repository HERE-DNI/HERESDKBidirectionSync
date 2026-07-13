---
title: "update method - ElectronicHorizonEngine class - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-update"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">update</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">update</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-update-param-mapMatchedLocation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation</a></span> <span class="parameter-name">mapMatchedLocation</span></span>

)

</div>

<div class="section desc markdown">

Updates the electronic horizon paths based on the provided map-matched location.

This method returns immediately and does not block. When internal calculation is complete, callbacks are called on the main thread. When multiple updates are triggered while processing is still running, intermediate locations are skipped and only the last location is processed.

- `mapMatchedLocation` The map-matched location that defines the current vehicle position on the road network.

</div>

## Implementation

``` dart
void update(MapMatchedLocation mapMatchedLocation);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

