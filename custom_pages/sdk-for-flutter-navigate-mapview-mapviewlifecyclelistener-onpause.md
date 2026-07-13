---
title: "onPause method - MapViewLifecycleListener class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-onpause"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapViewLifecycleListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onPause</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onPause</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Called when the map view to which this <a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a> is attached to gets paused (usually when the app goes into background).

This should be used by components that perform continuous updates to pause those updates until <a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-onresume">MapViewLifecycleListener.onResume</a> is called.

</div>

## Implementation

``` dart
void onPause();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

