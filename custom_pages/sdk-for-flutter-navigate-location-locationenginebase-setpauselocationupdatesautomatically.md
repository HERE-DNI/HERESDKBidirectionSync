---
title: "setPauseLocationUpdatesAutomatically method - LocationEngineBase class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationenginebase-setpauselocationupdatesautomatically"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setPauseLocationUpdatesAutomatically</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="name">setPauseLocationUpdatesAutomatically</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setPauseLocationUpdatesAutomatically-param-allowed" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">allowed</span></span>

)

</div>

<div class="section desc markdown">

Controls automatic pausing of location updates e.g.

for improving device's battery life at times when location data is unlikely to change. By default automatic pausing of location updates is allowed.

- `allowed` Set to `true` to allow automatic pausing of location updates, or `false` to disable them.

Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> on platforms which do not support automatic pausing of location updates.

</div>

## Implementation

``` dart
LocationEngineStatus setPauseLocationUpdatesAutomatically(bool allowed);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

