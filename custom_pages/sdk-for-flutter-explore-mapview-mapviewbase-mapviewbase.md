---
title: "MapViewBase constructor - MapViewBase - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapviewbase-mapviewbase"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapViewBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapViewBase</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapViewBase</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-viewToGeoCoordinatesLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>?</span> <span class="parameter-name">viewToGeoCoordinatesLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span></span>

    ), </span>
2.  <span id="sdk-for-flutter-explore-param-geoToViewCoordinatesLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a>?</span> <span class="parameter-name">geoToViewCoordinatesLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span></span>

    ), </span>
3.  <span id="sdk-for-flutter-explore-param-setWatermarkLocationLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">setWatermarkLocationLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a></span>, </span>
    2.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span></span>

    ), </span>
4.  <span id="sdk-for-flutter-explore-param-addLifecycleListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">addLifecycleListenerLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a></span></span>

    ), </span>
5.  <span id="sdk-for-flutter-explore-param-removeLifecycleListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">removeLifecycleListenerLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a></span></span>

    ), </span>
6.  <span id="sdk-for-flutter-explore-param-pickLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">pickLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapscenemappickfilter-class">MapSceneMapPickFilter</a>?</span>, </span>
    2.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-rectangle2d-class">Rectangle2D</a></span>, </span>
    3.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapviewbasemappickcallback">MapViewBaseMapPickCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
7.  <span id="sdk-for-flutter-explore-param-isValidGetLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isValidGetLambda</span>(), </span>
8.  <span id="sdk-for-flutter-explore-param-cameraGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcamera-class">MapCamera</a></span> <span class="parameter-name">cameraGetLambda</span>(), </span>
9.  <span id="sdk-for-flutter-explore-param-gesturesGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-gestures-gestures-class">Gestures</a></span> <span class="parameter-name">gesturesGetLambda</span>(), </span>
10. <span id="sdk-for-flutter-explore-param-mapSceneGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapscene-class">MapScene</a></span> <span class="parameter-name">mapSceneGetLambda</span>(), </span>
11. <span id="sdk-for-flutter-explore-param-mapContextGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcontext-class">MapContext</a></span> <span class="parameter-name">mapContextGetLambda</span>(), </span>
12. <span id="sdk-for-flutter-explore-param-hereMapControllerCoreGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-class">HereMapControllerCore</a></span> <span class="parameter-name">hereMapControllerCoreGetLambda</span>(), </span>
13. <span id="sdk-for-flutter-explore-param-viewportSizeGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-size2d-class">Size2D</a></span> <span class="parameter-name">viewportSizeGetLambda</span>(), </span>
14. <span id="sdk-for-flutter-explore-param-frameRateGetLambda" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">frameRateGetLambda</span>(), </span>
15. <span id="sdk-for-flutter-explore-param-frameRateSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">frameRateSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation">int</span></span>

    ), </span>
16. <span id="sdk-for-flutter-explore-param-pixelScaleGetLambda" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">pixelScaleGetLambda</span>(), </span>
17. <span id="sdk-for-flutter-explore-param-watermarkSizeGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-size2d-class">Size2D</a></span> <span class="parameter-name">watermarkSizeGetLambda</span>(), </span>

)

</div>

<div class="section desc markdown">

Represents the available public API from `MapView`.

</div>

## Implementation

``` dart
factory MapViewBase(
  GeoCoordinates? Function(Point2D) viewToGeoCoordinatesLambda,
  Point2D? Function(GeoCoordinates) geoToViewCoordinatesLambda,
  void Function(Anchor2D, Point2D) setWatermarkLocationLambda,
  void Function(MapViewLifecycleListener) addLifecycleListenerLambda,
  void Function(MapViewLifecycleListener) removeLifecycleListenerLambda,
  void Function(MapSceneMapPickFilter?, Rectangle2D, MapViewBaseMapPickCallback) pickLambda,
  bool Function() isValidGetLambda,
  MapCamera Function() cameraGetLambda,
  Gestures Function() gesturesGetLambda,
  MapScene Function() mapSceneGetLambda,
  MapContext Function() mapContextGetLambda,
  HereMapControllerCore Function() hereMapControllerCoreGetLambda,
  Size2D Function() viewportSizeGetLambda,
  int Function() frameRateGetLambda,
  void Function(int) frameRateSetLambda,
  double Function() pixelScaleGetLambda,
  Size2D Function() watermarkSizeGetLambda
) => MapViewBase$Lambdas(
  viewToGeoCoordinatesLambda,
  geoToViewCoordinatesLambda,
  setWatermarkLocationLambda,
  addLifecycleListenerLambda,
  removeLifecycleListenerLambda,
  pickLambda,
  isValidGetLambda,
  cameraGetLambda,
  gesturesGetLambda,
  mapSceneGetLambda,
  mapContextGetLambda,
  hereMapControllerCoreGetLambda,
  viewportSizeGetLambda,
  frameRateGetLambda,
  frameRateSetLambda,
  pixelScaleGetLambda,
  watermarkSizeGetLambda
);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

