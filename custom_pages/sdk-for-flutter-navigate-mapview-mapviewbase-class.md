---
title: "MapViewBase class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapviewbase-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapViewBase-class-sidebar.html">

<div>

# <span class="kind-class">MapViewBase</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents the available public API from `MapView`.

</div>

<div class="section">

Implementers  
- <a href="sdk-for-flutter-navigate-mapview-heremapcontroller-class">HereMapController</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-mapviewbase">MapViewBase</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-viewToGeoCoordinatesLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span> <span class="parameter-name">viewToGeoCoordinatesLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-geoToViewCoordinatesLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a>?</span> <span class="parameter-name">geoToViewCoordinatesLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-setWatermarkLocationLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">setWatermarkLocationLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-addLifecycleListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">addLifecycleListenerLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-removeLifecycleListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">removeLifecycleListenerLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-pickLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">pickLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenemappickfilter-class">MapSceneMapPickFilter</a>?</span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a></span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbasemappickcallback">MapViewBaseMapPickCallback</a></span> <span class="parameter-name"></span></span>), </span><span id="sdk-for-flutter-navigate-param-isValidGetLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isValidGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-cameraGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcamera-class">MapCamera</a></span> <span class="parameter-name">cameraGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-gesturesGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-gestures-gestures-class">Gestures</a></span> <span class="parameter-name">gesturesGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-mapSceneGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscene-class">MapScene</a></span> <span class="parameter-name">mapSceneGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-mapContextGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a></span> <span class="parameter-name">mapContextGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-hereMapControllerCoreGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-heremapcontrollercore-class">HereMapControllerCore</a></span> <span class="parameter-name">hereMapControllerCoreGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-viewportSizeGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-size2d-class">Size2D</a></span> <span class="parameter-name">viewportSizeGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-frameRateGetLambda" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">frameRateGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-frameRateSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">frameRateSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span></span>), </span><span id="sdk-for-flutter-navigate-param-pixelScaleGetLambda" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">pixelScaleGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-watermarkSizeGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-size2d-class">Size2D</a></span> <span class="parameter-name">watermarkSizeGetLambda</span>()</span>)</span>  
Represents the available public API from `MapView`.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-camera">camera</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapcamera-class">MapCamera</a></span>  
The camera to control the view for the map. Gets the camera to control the view for the map.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-framerate">frameRate</a></span> <span class="signature">↔ int</span>  
Maximum render frame rate in frames per second. Gets maximum render frame rate in frames per second.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-gestures">gestures</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-gestures-gestures-class">Gestures</a></span>  
The gestures control object for setting up the capture of gestures. Gets the gestures control object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-heremapcontrollercore">hereMapControllerCore</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-heremapcontrollercore-class">HereMapControllerCore</a></span>  
Here Map associated with this map view. Gets the <a href="sdk-for-flutter-navigate-mapview-heremapcontrollercore-class">HereMapControllerCore</a> associated with this map view.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-isvalid">isValid</a></span> <span class="signature">→ bool</span>  
Indicates whether this instance is valid. It will be made invalid when the corresponding `SDKNativeEngine` is destroyed. Returns `true` if this instance is valid, `false` otherwise. It will be made

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-mapcontext">mapContext</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a></span>  
Map context associated with this map view. Gets the map context associated with this map view.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-mapscene">mapScene</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapscene-class">MapScene</a></span>  
Map scene associated with this map view. Gets the map scene associated with this map view.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-pixelscale">pixelScale</a></span> <span class="signature">→ double</span>  
The pixel scale factor used by this `MapView`.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-viewportsize">viewportSize</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-size2d-class">Size2D</a></span>  
The size of this map view in physical pixels. If internally the map view's render surface is not attached yet (see: <a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a>), or after the map view has been destroyed then a `Size2D` with zero width and height is returned. Gets the size of this map view in physical pixels.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-watermarksize">watermarkSize</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-size2d-class">Size2D</a></span>  
Provides the size of the watermark in physical pixels. Returns the watermark size in physical pixels.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-addlifecyclelistener">addLifecycleListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addLifecycleListener-param-lifecycleListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a></span> <span class="parameter-name">lifecycleListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a <a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a> to this map view.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-geotoviewcoordinates">geoToViewCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-geoToViewCoordinates-param-geoCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">geoCoordinates</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a>?</span> </span>  
Converts geographical coordinates to view coordinates (in pixels).

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-pick">pick</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-pick-param-filter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenemappickfilter-class">MapSceneMapPickFilter</a>?</span> <span class="parameter-name">filter</span>, </span><span id="sdk-for-flutter-navigate-pick-param-viewArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a></span> <span class="parameter-name">viewArea</span>, </span><span id="sdk-for-flutter-navigate-pick-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbasemappickcallback">MapViewBaseMapPickCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Returns all map content located inside the specified pick area.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-removelifecyclelistener">removeLifecycleListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeLifecycleListener-param-lifecycleListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a></span> <span class="parameter-name">lifecycleListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a <a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a> from this map view.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-setwatermarklocation">setWatermarkLocation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setWatermarkLocation-param-anchor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">anchor</span>, </span><span id="sdk-for-flutter-navigate-setWatermarkLocation-param-offset" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">offset</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the position of the HERE logo watermark within the map view.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-viewtogeocoordinates">viewToGeoCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-viewToGeoCoordinates-param-viewCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">viewCoordinates</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span> </span>  
Converts view coordinates (in pixels) to geographical coordinates.

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

