---
title: "setPauseLocationUpdatesAutomatically method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-setpauselocationupdatesautomatically"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setPauseLocationUpdatesAutomatically</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="name">setPauseLocationUpdatesAutomatically</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setPauseLocationUpdatesAutomatically-param-allowed" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">allowed</span></span>

)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

On iOS devices this controls automatic pausing of location updates e.g. for improving device's battery life at times when location data is unlikely to change. By default automatic pausing of location updates is allowed. Set `allowed` to true to allow automatic pausing of location updates, or false to disable them. When calling this method then <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> is returned.

On Android devices this is not supported and <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> is returned.

</div>

## Implementation

``` dart
LocationEngineStatus setPauseLocationUpdatesAutomatically(bool allowed) {
  if (Platform.isIOS) {
    return _location.setPauseLocationUpdatesAutomatically(allowed);
  }
  return LocationEngineStatus.notSupported;
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

