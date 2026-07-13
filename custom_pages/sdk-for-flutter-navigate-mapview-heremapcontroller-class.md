---
title: "HereMapController class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-heremapcontroller-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- HereMapController-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/HereMapController-class-sidebar.html">

<div>

# <span class="kind-class">HereMapController</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Allows interacting with the map displayed by <a href="sdk-for-flutter-navigate-mapview-heremap-class">HereMap</a> widget.

</div>

<div class="section">

Inheritance  
- Object
- <a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a>
- HereMapController

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapcontroller-heremapcontroller">HereMapController</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-id" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">id</span></span>)</span>  
<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-camera">camera</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapcamera-class">MapCamera</a></span>  
The camera to control the view for the map. Gets the camera to control the view for the map.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-framerate">frameRate</a></span> <span class="signature">↔ int</span>  
Maximum render frame rate in frames per second. Gets maximum render frame rate in frames per second.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-gestures">gestures</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-gestures-gestures-class">Gestures</a></span>  
The gestures control object for setting up the capture of gestures. Gets the gestures control object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-heremapcontrollercore">hereMapControllerCore</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-heremapcontrollercore-class">HereMapControllerCore</a></span>  
Here Map associated with this map view. Gets the <a href="sdk-for-flutter-navigate-mapview-heremapcontrollercore-class">HereMapControllerCore</a> associated with this map view.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-isvalid">isValid</a></span> <span class="signature">→ bool</span>  
Indicates whether this instance is valid. It will be made invalid when the corresponding `SDKNativeEngine` is destroyed. Returns `true` if this instance is valid, `false` otherwise. It will be made

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-mapcontext">mapContext</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a></span>  
Map context associated with this map view. Gets the map context associated with this map view.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-mapscene">mapScene</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapscene-class">MapScene</a></span>  
Map scene associated with this map view. Gets the map scene associated with this map view.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-pixelscale">pixelScale</a></span> <span class="signature">→ double</span>  
The pixel scale factor used by this `MapView`.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-viewportsize">viewportSize</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-size2d-class">Size2D</a></span>  
The size of this map view in physical pixels. If internally the map view's render surface is not attached yet (see: <a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a>), or after the map view has been destroyed then a `Size2D` with zero width and height is returned. Gets the size of this map view in physical pixels.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-watermarksize">watermarkSize</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-size2d-class">Size2D</a></span>  
Provides the size of the watermark in physical pixels. Returns the watermark size in physical pixels.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapcontroller-widgetpins">widgetPins</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a></span>\></span></span>  
Gets a list of currently added widget pins.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-addlifecyclelistener">addLifecycleListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addLifecycleListener-param-lifecycleListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a></span> <span class="parameter-name">lifecycleListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a <a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a> to this map view.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-geotoviewcoordinates">geoToViewCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-geoToViewCoordinates-param-geoCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">geoCoordinates</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a>?</span> </span>  
Converts geographical coordinates to view coordinates (in pixels).

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapcontroller-pause">pause</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Pauses the map widget.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-pick">pick</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-pick-param-filter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenemappickfilter-class">MapSceneMapPickFilter</a>?</span> <span class="parameter-name">filter</span>, </span><span id="sdk-for-flutter-navigate-pick-param-viewArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a></span> <span class="parameter-name">viewArea</span>, </span><span id="sdk-for-flutter-navigate-pick-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbasemappickcallback">MapViewBaseMapPickCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Returns all map content located inside the specified pick area.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapcontroller-pinwidget">pinWidget</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-pinWidget-param-widget" class="parameter"><span class="type-annotation">Widget</span> <span class="parameter-name">widget</span>, </span><span id="sdk-for-flutter-navigate-pinWidget-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, {</span><span id="sdk-for-flutter-navigate-pinWidget-param-anchor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a>?</span> <span class="parameter-name">anchor</span></span>}) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a>?</span> </span>  
Pins a `Widget` to the MapView and returns a proxy object that can be used to control the pinning.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-removelifecyclelistener">removeLifecycleListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeLifecycleListener-param-lifecycleListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a></span> <span class="parameter-name">lifecycleListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a <a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a> from this map view.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapcontroller-resume">resume</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Resumes the map widget.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-setwatermarklocation">setWatermarkLocation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setWatermarkLocation-param-anchor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">anchor</span>, </span><span id="sdk-for-flutter-navigate-setWatermarkLocation-param-offset" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">offset</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the position of the HERE logo watermark within the map view.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapcontroller-takescreenshot">takeScreenshot</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-takeScreenshot-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-takescreenshotcallback">TakeScreenshotCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Asynchronously retrieves a screenshot of the map view.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapcontroller-unpinwidget">unpinWidget</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-unpinWidget-param-widget" class="parameter"><span class="type-annotation">Widget</span> <span class="parameter-name">widget</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a <a href="sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a> from the MapView by specifying the corresponding `Widget`. Trying to unpin a widget that was not pinned or has been unpinned before has no effect. All pinned widgets equal to `widget` will be removed.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-viewtogeocoordinates">viewToGeoCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-viewToGeoCoordinates-param-viewCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">viewCoordinates</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span> </span>  
Converts view coordinates (in pixels) to geographical coordinates.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapcontroller-primarylanguage">primaryLanguage</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>?</span>  
The code of desired primary map display language.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapcontroller-secondarylanguage">secondaryLanguage</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>?</span>  
The code of desired secondary map display language. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapcontroller-shadowquality">shadowQuality</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-shadowquality">ShadowQuality</a></span>  
The current shadow quality. Default shadow quality is <a href="sdk-for-flutter-navigate-mapview-shadowquality">ShadowQuality.medium</a>. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
