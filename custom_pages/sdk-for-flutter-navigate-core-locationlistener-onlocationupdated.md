---
title: "onLocationUpdated method - LocationListener class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-locationlistener-onlocationupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onLocationUpdated.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/LocationListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onLocationUpdated</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onLocationUpdated</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onLocationUpdated-param-location" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">location</span></span>

)

</div>

<div class="section desc markdown">

Called each time a new location is available.

In a navigation context while using the `Navigator` or `VisualNavigator`, it's required to set the `Location.time` parameter for each `Location` object so that the HERE SDK can map-match the locations properly. If the `Location.time` parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the `bearing` and `speed` parameters for each `Location` object. Invoked on the main thread.

- `location` Current location.

</div>

## Implementation

``` dart
void onLocationUpdated(Location location);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
