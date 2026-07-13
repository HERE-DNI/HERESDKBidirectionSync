---
title: "startAnimation method - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-startanimation"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">startAnimation</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">startAnimation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-startAnimation-param-cameraAnimation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> <span class="parameter-name">cameraAnimation</span></span>

)

</div>

<div class="section desc markdown">

Starts a given camera animation.

Starting an animation can cause the cancelling of an ongoing animation when they both affect the same category of camera properties, like for example any of the look-at properties (target, orientation, map measure) or any of the projection properties (field of view, principal point, focal length). The corresponding listener of an ongoing animation will be notified about the cancellation in these cases.

- `cameraAnimation` The animation to be started.

</div>

## Implementation

``` dart
void startAnimation(MapCameraAnimation cameraAnimation);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

