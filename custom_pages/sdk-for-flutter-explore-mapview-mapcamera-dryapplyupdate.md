---
title: "dryApplyUpdate method - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcamera-dryapplyupdate"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">dryApplyUpdate</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">dryApplyUpdate</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-dryApplyUpdate-param-cameraUpdate" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="parameter-name">cameraUpdate</span>, </span>
2.  <span id="sdk-for-flutter-explore-dryApplyUpdate-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcameradrycameraupdatecallback">MapCameraDryCameraUpdateCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Computes result of applying camera update without changing state of the map camera.

Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `cameraUpdate` The update that gets dryly applied to camera.

- `callback` Called upon completion with computed map state. The callback is called from an arbitrary thread.

</div>

## Implementation

``` dart
void dryApplyUpdate(MapCameraUpdate cameraUpdate, MapCameraDryCameraUpdateCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

