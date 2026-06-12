---
title: "MapViewBase constructor"
slug: "sdk-for-flutter-navigate-mapview-mapviewbase-mapviewbase"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapViewBase.html -->


<div>
<h1>MapViewBase constructor</h1></div>

MapViewBase(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>? viewToGeoCoordinatesLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-point2d-class">Point2D</a></li>
</ol>), </li>
<li><a href="/sdk-for-flutter-navigate-core-point2d-class">Point2D</a>? geoToViewCoordinatesLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></li>
</ol>), </li>
<li>void setWatermarkLocationLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a>, </li>
<li><a href="/sdk-for-flutter-navigate-core-point2d-class">Point2D</a></li>
</ol>), </li>
<li>void addLifecycleListenerLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a></li>
</ol>), </li>
<li>void removeLifecycleListenerLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a></li>
</ol>), </li>
<li>void pickLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-mapscenemappickfilter-class">MapSceneMapPickFilter</a>?, </li>
<li><a href="/sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a>, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mapviewbasemappickcallback">MapViewBaseMapPickCallback</a> </li>
</ol>), </li>
<li>bool isValidGetLambda(), </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mapcamera-class">MapCamera</a> cameraGetLambda(), </li>
<li><a href="/sdk-for-flutter-navigate-gestures-gestures-class">Gestures</a> gesturesGetLambda(), </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mapscene-class">MapScene</a> mapSceneGetLambda(), </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a> mapContextGetLambda(), </li>
<li><a href="/sdk-for-flutter-navigate-mapview-heremapcontrollercore-class">HereMapControllerCore</a> hereMapControllerCoreGetLambda(), </li>
<li><a href="/sdk-for-flutter-navigate-core-size2d-class">Size2D</a> viewportSizeGetLambda(), </li>
<li>int frameRateGetLambda(), </li>
<li>void frameRateSetLambda(<ol class="parameter-list single-line"> <li>int</li>
</ol>), </li>
<li>double pixelScaleGetLambda(), </li>
<li><a href="/sdk-for-flutter-navigate-core-size2d-class">Size2D</a> watermarkSizeGetLambda(), </li>
</ol>)
    

<p>Represents the available public API from  <code>MapView</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapViewBase(
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
) =&gt; MapViewBase$Lambdas(
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
);</code></pre>

 



</div>
`
}</HTMLBlock>
