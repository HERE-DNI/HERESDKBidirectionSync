---
title: "MapCameraListener constructor - MapCameraListener - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameralistener-mapcameralistener"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapCameraListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapCameraListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-onMapCameraUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onMapCameraUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcamerastate-class">MapCameraState</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Abstract class for objects that want to get updates whenever the map is redrawn after camera parameters change.

</div>

## Implementation

``` dart
factory MapCameraListener(
  void Function(MapCameraState) onMapCameraUpdatedLambda,

) => MapCameraListener$Lambdas(
  onMapCameraUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

