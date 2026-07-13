---
title: "MapCameraDryCameraUpdateCallback typedef - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameradrycameraupdatecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraDryCameraUpdateCallback.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">MapCameraDryCameraUpdateCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">MapCameraDryCameraUpdateCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-cameraState" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcamerastate-class">MapCameraState</a>?</span> <span class="parameter-name">cameraState</span></span>)</span></span>

</div>

<div class="section desc markdown">

Used to report back results of dry update application to camera.

Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `cameraState` Map camera state after dry application of update

</div>

## Implementation

``` dart
typedef MapCameraDryCameraUpdateCallback = void Function(MapCameraState? cameraState);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
