---
title: "addLocationListener method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-addlocationlistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">addLocationListener</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">addLocationListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-addLocationListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a></span> <span class="parameter-name">listener</span></span>

)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

Adds a <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a> to the engine to get notified when there is a new location update available. Supports more than one listener, instance is added only once.

</div>

## Implementation

``` dart
void addLocationListener(LocationListener listener) {
  if (!_locationUpdateListeners.containsKey(listener)) {
    _locationUpdateListeners[listener] = LocationUpdateListenerBridge(listener);
  }
  _location.addLocationListener(_locationUpdateListeners[listener]!);
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

