---
title: "getPauseLocationUpdatesAutomatically method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-getpauselocationupdatesautomatically"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getPauseLocationUpdatesAutomatically</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">getPauseLocationUpdatesAutomatically</span>(<wbr></wbr>)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

On iOS devices this checks if automatic pausing of location updates is enabled. Returns true if automatic pausing of location updates is enabled, false otherwise.

On Android devices this is not supported and false is returned.

</div>

## Implementation

``` dart
bool getPauseLocationUpdatesAutomatically() {
  if (Platform.isIOS) {
    return _location.getPauseLocationUpdatesAutomatically();
  }
  return false;
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

