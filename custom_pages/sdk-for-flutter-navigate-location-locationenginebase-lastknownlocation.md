---
title: "lastKnownLocation property - LocationEngineBase class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationenginebase-lastknownlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lastKnownLocation.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">lastKnownLocation</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-location-class">Location</a>?</span> <span class="name">lastKnownLocation</span>

</div>

<div class="section desc markdown">

The last known location obtained by the `LocationEngine`. It is persisted throughout the app's lifecycle. This property can be obtained without starting the `LocationEngine`. However, the initial value might be `null` if no location has ever been obtained by the `LocationEngine`. The time attribute of the `Location` object indicates when the last location was obtained. Note: In order to receive continuous location updates, add a `LocationListener`. Gets the last known location obtained by the `LocationEngine`. It is persisted throughout the app's lifecycle.

</div>

## Implementation

``` dart
Location? get lastKnownLocation;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
