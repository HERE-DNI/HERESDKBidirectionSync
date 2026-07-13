---
title: "removeLocationListener method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-removelocationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- removeLocationListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">removeLocationListener</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">removeLocationListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-removeLocationListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a></span> <span class="parameter-name">listener</span></span>

)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

Removes a <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a> from the engine.

</div>

## Implementation

``` dart
void removeLocationListener(LocationListener listener) {
  LocationUpdateListenerBridge? bridge = _locationUpdateListeners.remove(listener);
  if (bridge == null) {
    return;
  }
  _location.removeLocationListener(bridge);
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
