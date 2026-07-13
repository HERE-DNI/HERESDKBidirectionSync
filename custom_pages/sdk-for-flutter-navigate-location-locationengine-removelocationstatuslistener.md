---
title: "removeLocationStatusListener method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-removelocationstatuslistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">removeLocationStatusListener</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">removeLocationStatusListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-removeLocationStatusListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a></span> <span class="parameter-name">listener</span></span>

)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

Removes a <a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a> from the engine.

</div>

## Implementation

``` dart
void removeLocationStatusListener(LocationStatusListener listener) {
  LocationStatusListenerBridge? bridge = _locationStatusListeners.remove(listener);
  if (bridge == null) {
    return;
  }
  _location.removeLocationStatusListener(bridge);
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

