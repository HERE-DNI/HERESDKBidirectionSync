---
title: "applyUpdate method - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcamera-applyupdate"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">applyUpdate</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">applyUpdate</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-applyUpdate-param-cameraUpdate" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="parameter-name">cameraUpdate</span></span>

)

</div>

<div class="section desc markdown">

Applies camera update to the map camera.

Any ongoing camera animations will be cancelled and the corresponding camera animation listener will be notified.

- `cameraUpdate` The update that gets applied to camera.

</div>

## Implementation

``` dart
void applyUpdate(MapCameraUpdate cameraUpdate);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

