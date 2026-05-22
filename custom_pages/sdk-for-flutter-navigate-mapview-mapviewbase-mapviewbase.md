---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapviewbase-mapviewbase"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapViewBase.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapviewbase-class</li>
<li class="self-crumb">MapViewBase factory constructor</li>
</ol>
<div class="self-name">MapViewBase</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapview/MapViewBase-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapViewBase constructor</h1></div>
<section class="multi-line-signature">
MapViewBase(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-core-geocoordinates-class? viewToGeoCoordinatesLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-point2d-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-core-point2d-class? geoToViewCoordinatesLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geocoordinates-class</li>
</ol>), </li>
<li>void setWatermarkLocationLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-anchor2d-class, </li>
<li>/sdk-for-flutter-navigate-core-point2d-class</li>
</ol>), </li>
<li>void addLifecycleListenerLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class</li>
</ol>), </li>
<li>void removeLifecycleListenerLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class</li>
</ol>), </li>
<li>void pickLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-mapscenemappickfilter-class?, </li>
<li>/sdk-for-flutter-navigate-core-rectangle2d-class, </li>
<li>/sdk-for-flutter-navigate-mapview-mapviewbasemappickcallback </li>
</ol>), </li>
<li>bool isValidGetLambda(), </li>
<li>/sdk-for-flutter-navigate-mapview-mapcamera-class cameraGetLambda(), </li>
<li>/sdk-for-flutter-navigate-gestures-gestures-class gesturesGetLambda(), </li>
<li>/sdk-for-flutter-navigate-mapview-mapscene-class mapSceneGetLambda(), </li>
<li>/sdk-for-flutter-navigate-mapview-mapcontext-class mapContextGetLambda(), </li>
<li>/sdk-for-flutter-navigate-mapview-heremapcontrollercore-class hereMapControllerCoreGetLambda(), </li>
<li>/sdk-for-flutter-navigate-core-size2d-class viewportSizeGetLambda(), </li>
<li>int frameRateGetLambda(), </li>
<li>void frameRateSetLambda(<ol class="parameter-list single-line"> <li>int</li>
</ol>), </li>
<li>double pixelScaleGetLambda(), </li>
<li>/sdk-for-flutter-navigate-core-size2d-class watermarkSizeGetLambda(), </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Represents the available public API from  <code>MapView</code>.</p>
</section>
<section class="summary source-code" id="source">
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
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapviewbase-class</li>
<li class="self-crumb">MapViewBase factory constructor</li>
</ol>
<h5>MapViewBase class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
