---
title: "updateLocationAccuracy method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-updatelocationaccuracy"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">updateLocationAccuracy</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="name">updateLocationAccuracy</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-updateLocationAccuracy-param-locationAccuracy" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span> <span class="parameter-name">locationAccuracy</span></span>

)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

Reconfigures the location engine with desired LocationAccuracy.

This method is a faster way to change location accuracy for already started location engine, than calling <a href="sdk-for-flutter-navigate-location-locationenginebase-stop">LocationEngineBase.stop</a> and <a href="sdk-for-flutter-navigate-location-locationenginebase-startwithlocationoptions">LocationEngineBase.startWithLocationOptions</a> in sequence. Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notReady</a>, if called for unstarted location engine.

`locationAccuracy` Desired location accuracy. Requested accuracy is not guaranteed.

Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. Engine status. Valid values are defined in <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>

</div>

## Implementation

``` dart
LocationEngineStatus updateLocationAccuracy(LocationAccuracy locationAccuracy) =>
    _location.updateLocationAccuracy(locationAccuracy);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

