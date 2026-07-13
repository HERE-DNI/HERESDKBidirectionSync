---
title: "lastKnownLocation property - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-lastknownlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lastKnownLocation.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">lastKnownLocation</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-location-class">Location</a>?</span> <span class="name">lastKnownLocation</span>

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

The last known location obtained by the engine. <a href="sdk-for-flutter-navigate-core-location-class">Location</a> is returned synchronously. <a href="sdk-for-flutter-navigate-core-location-class">Location</a> object has a timestamp attribute, which reflects when data was obtained. If location was never obtained - null is returned.

</div>

## Implementation

``` dart
Location? get lastKnownLocation => _location.lastKnownLocation;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
