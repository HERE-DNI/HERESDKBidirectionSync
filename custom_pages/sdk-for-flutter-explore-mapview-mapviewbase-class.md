---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mapviewbase-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapViewBase-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapViewBase-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapViewBase/MapViewBase.html">MapViewBase</a></li>
<li class="section-title">
<a href="mapview/MapViewBase-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapViewBase/camera.html">camera</a></li>
<li><a href="mapview/MapViewBase/frameRate.html">frameRate</a></li>
<li><a href="mapview/MapViewBase/gestures.html">gestures</a></li>
<li class="inherited"><a href="mapview/MapViewBase/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapViewBase/hereMapControllerCore.html">hereMapControllerCore</a></li>
<li><a href="mapview/MapViewBase/isValid.html">isValid</a></li>
<li><a href="mapview/MapViewBase/mapContext.html">mapContext</a></li>
<li><a href="mapview/MapViewBase/mapScene.html">mapScene</a></li>
<li><a href="mapview/MapViewBase/pixelScale.html">pixelScale</a></li>
<li class="inherited"><a href="mapview/MapViewBase/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/MapViewBase/viewportSize.html">viewportSize</a></li>
<li><a href="mapview/MapViewBase/watermarkSize.html">watermarkSize</a></li>
<li class="section-title"><a href="mapview/MapViewBase-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MapViewBase/addLifecycleListener.html">addLifecycleListener</a></li>
<li><a href="mapview/MapViewBase/geoToViewCoordinates.html">geoToViewCoordinates</a></li>
<li class="inherited"><a href="mapview/MapViewBase/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MapViewBase/pick.html">pick</a></li>
<li><a href="mapview/MapViewBase/removeLifecycleListener.html">removeLifecycleListener</a></li>
<li><a href="mapview/MapViewBase/setWatermarkLocation.html">setWatermarkLocation</a></li>
<li class="inherited"><a href="mapview/MapViewBase/toString.html">toString</a></li>
<li><a href="mapview/MapViewBase/viewToGeoCoordinates.html">viewToGeoCoordinates</a></li>
<li class="section-title inherited"><a href="mapview/MapViewBase-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapViewBase/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapViewBase class</li>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapViewBase-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapViewBase class abstract</h1></div>
<section class="desc markdown">
<p>Represents the available public API from  <code>MapView</code>.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implementers</dt>
<dd><ul class="comma-separated clazz-relationships">
<li><a href="../mapview/HereMapController-class.html">/sdk-for-flutter-explore-mapview-heremapcontroller-class</a></li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapViewBase">
<a href="../mapview/MapViewBase/MapViewBase.html">/sdk-for-flutter-explore-mapview-mapviewbase-mapviewbase</a>(<a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>? viewToGeoCoordinatesLambda(<a href="../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a>), <a href="../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a>? geoToViewCoordinatesLambda(<a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>), void setWatermarkLocationLambda(<a href="../core/Anchor2D-class.html">/sdk-for-flutter-explore-core-anchor2d-class</a>, <a href="../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a>), void addLifecycleListenerLambda(<a href="../mapview/MapViewLifecycleListener-class.html">/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class</a>), void removeLifecycleListenerLambda(<a href="../mapview/MapViewLifecycleListener-class.html">/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class</a>), void pickLambda(<a href="../mapview/MapSceneMapPickFilter-class.html">/sdk-for-flutter-explore-mapview-mapscenemappickfilter-class</a>?, <a href="../core/Rectangle2D-class.html">/sdk-for-flutter-explore-core-rectangle2d-class</a>, <a href="../mapview/MapViewBaseMapPickCallback.html">/sdk-for-flutter-explore-mapview-mapviewbasemappickcallback</a> ), bool isValidGetLambda(), <a href="../mapview/MapCamera-class.html">/sdk-for-flutter-explore-mapview-mapcamera-class</a> cameraGetLambda(), <a href="../gestures/Gestures-class.html">/sdk-for-flutter-explore-gestures-gestures-class</a> gesturesGetLambda(), <a href="../mapview/MapScene-class.html">/sdk-for-flutter-explore-mapview-mapscene-class</a> mapSceneGetLambda(), <a href="../mapview/MapContext-class.html">/sdk-for-flutter-explore-mapview-mapcontext-class</a> mapContextGetLambda(), <a href="../mapview/HereMapControllerCore-class.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-class</a> hereMapControllerCoreGetLambda(), <a href="../core/Size2D-class.html">/sdk-for-flutter-explore-core-size2d-class</a> viewportSizeGetLambda(), int frameRateGetLambda(), void frameRateSetLambda(int), double pixelScaleGetLambda(), <a href="../core/Size2D-class.html">/sdk-for-flutter-explore-core-size2d-class</a> watermarkSizeGetLambda())
</dt>
<dd>
          Represents the available public API from  <code>MapView</code>.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="camera">
<a href="../mapview/MapViewBase/camera.html">/sdk-for-flutter-explore-mapview-mapviewbase-camera</a>
→ <a href="../mapview/MapCamera-class.html">/sdk-for-flutter-explore-mapview-mapcamera-class</a>
</dt>
<dd>
  The camera to control the view for the map.
Gets the camera to control the view for the map.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="frameRate">
<a href="../mapview/MapViewBase/frameRate.html">/sdk-for-flutter-explore-mapview-mapviewbase-framerate</a>
↔ int
</dt>
<dd>
  Maximum render frame rate in frames per second.
Gets maximum render frame rate in frames per second.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="gestures">
<a href="../mapview/MapViewBase/gestures.html">/sdk-for-flutter-explore-mapview-mapviewbase-gestures</a>
→ <a href="../gestures/Gestures-class.html">/sdk-for-flutter-explore-gestures-gestures-class</a>
</dt>
<dd>
  The gestures control object for setting up the capture of gestures.
Gets the gestures control object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapViewBase/hashCode.html">/sdk-for-flutter-explore-mapview-mapviewbase-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="hereMapControllerCore">
<a href="../mapview/MapViewBase/hereMapControllerCore.html">/sdk-for-flutter-explore-mapview-mapviewbase-heremapcontrollercore</a>
→ <a href="../mapview/HereMapControllerCore-class.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-class</a>
</dt>
<dd>
  Here Map associated with this map view.
Gets the <a href="../mapview/HereMapControllerCore-class.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-class</a> associated with this map view.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isValid">
<a href="../mapview/MapViewBase/isValid.html">/sdk-for-flutter-explore-mapview-mapviewbase-isvalid</a>
→ bool
</dt>
<dd>
  Indicates whether this instance is valid.
It will be made invalid when the corresponding <code>SDKNativeEngine</code> is destroyed.
Returns <code>true</code> if this instance is valid, <code>false</code> otherwise. It will be made
  <div class="features">no setter</div>
</dd>
<dt class="property" id="mapContext">
<a href="../mapview/MapViewBase/mapContext.html">/sdk-for-flutter-explore-mapview-mapviewbase-mapcontext</a>
→ <a href="../mapview/MapContext-class.html">/sdk-for-flutter-explore-mapview-mapcontext-class</a>
</dt>
<dd>
  Map context associated with this map view.
Gets the map context associated with this map view.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="mapScene">
<a href="../mapview/MapViewBase/mapScene.html">/sdk-for-flutter-explore-mapview-mapviewbase-mapscene</a>
→ <a href="../mapview/MapScene-class.html">/sdk-for-flutter-explore-mapview-mapscene-class</a>
</dt>
<dd>
  Map scene associated with this map view.
Gets the map scene associated with this map view.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="pixelScale">
<a href="../mapview/MapViewBase/pixelScale.html">/sdk-for-flutter-explore-mapview-mapviewbase-pixelscale</a>
→ double
</dt>
<dd>
  The pixel scale factor used by this <code>MapView</code>.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapViewBase/runtimeType.html">/sdk-for-flutter-explore-mapview-mapviewbase-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="viewportSize">
<a href="../mapview/MapViewBase/viewportSize.html">/sdk-for-flutter-explore-mapview-mapviewbase-viewportsize</a>
→ <a href="../core/Size2D-class.html">/sdk-for-flutter-explore-core-size2d-class</a>
</dt>
<dd>
  The size of this map view in physical pixels.
If internally the map view's render surface is not attached yet
(see: <a href="../mapview/MapViewLifecycleListener-class.html">/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class</a>), or after the map view has been destroyed
then a <code>Size2D</code> with zero width and height is returned.
Gets the size of this map view in physical pixels.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="watermarkSize">
<a href="../mapview/MapViewBase/watermarkSize.html">/sdk-for-flutter-explore-mapview-mapviewbase-watermarksize</a>
→ <a href="../core/Size2D-class.html">/sdk-for-flutter-explore-core-size2d-class</a>
</dt>
<dd>
  Provides the size of the watermark in physical pixels.
Returns the watermark size in physical pixels.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="addLifecycleListener">
<a href="../mapview/MapViewBase/addLifecycleListener.html">/sdk-for-flutter-explore-mapview-mapviewbase-addlifecyclelistener</a>(<wbr/><a href="../mapview/MapViewLifecycleListener-class.html">/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class</a> lifecycleListener)
    → void

</dt>
<dd>
  Adds a <a href="../mapview/MapViewLifecycleListener-class.html">/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class</a> to this map view.
  

</dd>
<dt class="callable" id="geoToViewCoordinates">
<a href="../mapview/MapViewBase/geoToViewCoordinates.html">/sdk-for-flutter-explore-mapview-mapviewbase-geotoviewcoordinates</a>(<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> geoCoordinates)
    → <a href="../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a>?

</dt>
<dd>
  Converts geographical coordinates to view coordinates (in pixels).
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapViewBase/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mapviewbase-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="pick">
<a href="../mapview/MapViewBase/pick.html">/sdk-for-flutter-explore-mapview-mapviewbase-pick</a>(<wbr/><a href="../mapview/MapSceneMapPickFilter-class.html">/sdk-for-flutter-explore-mapview-mapscenemappickfilter-class</a>? filter, <a href="../core/Rectangle2D-class.html">/sdk-for-flutter-explore-core-rectangle2d-class</a> viewArea, <a href="../mapview/MapViewBaseMapPickCallback.html">/sdk-for-flutter-explore-mapview-mapviewbasemappickcallback</a> callback)
    → void

</dt>
<dd>
  Returns all map content located inside the specified pick area.
  

</dd>
<dt class="callable" id="removeLifecycleListener">
<a href="../mapview/MapViewBase/removeLifecycleListener.html">/sdk-for-flutter-explore-mapview-mapviewbase-removelifecyclelistener</a>(<wbr/><a href="../mapview/MapViewLifecycleListener-class.html">/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class</a> lifecycleListener)
    → void

</dt>
<dd>
  Removes a <a href="../mapview/MapViewLifecycleListener-class.html">/sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class</a> from this map view.
  

</dd>
<dt class="callable" id="setWatermarkLocation">
<a href="../mapview/MapViewBase/setWatermarkLocation.html">/sdk-for-flutter-explore-mapview-mapviewbase-setwatermarklocation</a>(<wbr/><a href="../core/Anchor2D-class.html">/sdk-for-flutter-explore-core-anchor2d-class</a> anchor, <a href="../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a> offset)
    → void

</dt>
<dd>
  Sets the position of the HERE logo watermark within the map view.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapViewBase/toString.html">/sdk-for-flutter-explore-mapview-mapviewbase-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="viewToGeoCoordinates">
<a href="../mapview/MapViewBase/viewToGeoCoordinates.html">/sdk-for-flutter-explore-mapview-mapviewbase-viewtogeocoordinates</a>(<wbr/><a href="../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a> viewCoordinates)
    → <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>?

</dt>
<dd>
  Converts view coordinates (in pixels) to geographical coordinates.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../mapview/MapViewBase/operator_equals.html">/sdk-for-flutter-explore-mapview-mapviewbase-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapViewBase class</li>
</ol>
<h5>mapview library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>
