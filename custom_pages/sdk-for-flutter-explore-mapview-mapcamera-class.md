---
title: "MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcamera-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCamera-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCamera-class-sidebar.html">

<div>

# <span class="kind-class">MapCamera</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents the camera looking onto the map view.

Each map instance has exactly one camera that is used to manipulate the way the map is displayed.

Any updates to the state of the camera will be applied while drawing the next map view frame and the current state of the camera reflects what is currently drawn inside the map view.

Note: The camera can be configured and positioned even before a map scene is loaded for the first time. This allows for pre-setting the desired camera position, orientation, and zoom level, which will be applied once the map scene becomes available.

**Camera Model**

*Camera Concepts and Units*

By default, HERE SDK uses an idealized Earth globe with a 3D-capable camera model. Being a 3D camera model means that the world position can be freely specified in geodetic 3D space (i.e. Earth centric) and the orientation can be freely changed around two axes - bearing (also known as head) and tilt (also known as pitch).

The camera supports the look-at target with orientation on the ground way of setting up the camera in space. The camera is placed so that it looks at a specific geo-coordinates (placed at the `principal point`) from a given orientation and distance.

- the look-at target in geo-coordinates (latitude, longitude) in degrees and an `altitude` in meters above MSL (mean sea level) at the `principal point`
- the `orientation` at the look-at target
- the distance of the camera from the look-at target, given as `distance` in meters or as `zoom-level`

*Getting the current camera state*

The current camera state can be obtained by the <a href="sdk-for-flutter-explore-mapview-mapcamera-state">MapCamera.state</a> call. It contains information about the camera look-at target (geo-coordinates and orientation) in geodetic space. The values are returned for the current `principal point`. This can lead to surprising or unexpected values in cases where the camera position/orientation was specified for another screen point, e.g. when using <a href="sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatarea">MapCameraUpdateFactory.lookAtArea</a> with a view rectangle, whose center does not coincide with the `principal point`. In this case, the geo-coordinates of the look-at target will differ from the center of the geo-box used in the `lookAt` call.

*Geo coordinates*

Geo-coordinates are given in degrees and follow the common nomenclature of positive northern latitudes and positive eastern longitudes.

*Altitude*

When `altitude` is specified, it is always in meters above mean sea level (MSL). If this value is invalid (not-a-number) or not specified, then the terrain height at the given geo-coordinates will be looked up from the map. This is especially interesting in cases where terrain elevation is used within the map display.

*Distance vs zoom-level vs scale*

Map camera `distance`, `zoom-level` and `scale` determine how much of the world is visible on the HERE map. `Distance`, `zoom-level` and `scale` are directly connected and changing one will automatically change the others as well (except for `distance`/`scale` changes that map to `zoom-level` values \< 0 or \> 23).

- `distance`: the distance from the camera to the look-at target on the surface of the Earth, in meters

- `zoom-level`: the map zoom level, in the range \[0, 3\]. The relation between the width of the equator in logical pixels `w` and the zoom level `z` is:

      w = 256 * 2^(z)

- `scale`: the scale of the map at the look-at target in meters on screen per meters on Earth. So a scale of 0.001 shows 10 meters on Earth within 1 cm on screen.

The following mapping represents the `zoom-level` values:

| zoom-level | ~ scale on screen (130dpi) | width of the equator in logical pixels | what can be seen |
|----|:--:|:--:|:--:|
| 0 | 1:800 million | 256 | Earth |
| 1 | 1:400 million | 512 |  |
| 2 | 1:200 million | 1024 |  |
| 3 | 1:100 million | 2048 |  |
| 4 | 1:50 million | 4096 | A continent |
| 5 | 1:25 million | 8192 | Large roads |
| 6 | 1:12 million | 16384 | Large rivers |
| 7 | 1:6 million | 32768 | A country |
| 8 | 1:3 million | 65536 |  |
| 9 | 1:1 million | 131072 |  |
| 10 | 1:780 thousand | 262144 |  |
| 11 | 1:390 thousand | 524288 |  |
| 12 | 1:195 thousand | 1048576 |  |
| 13 | 1:100 thousand | 2097152 |  |
| 14 | 1:50 thousand | 4194304 | A city |
| 15 | 1:25 thousand | 8388608 |  |
| 16 | 1:12 thousand | 16777216 | Buildings |
| 17 | 1:6 thousand | 33554432 | Landmarks |
| 18 | 1:3 thousand | 67108864 |  |
| 19 | 1:1 thousand | 134217728 |  |
| 20 | 1:7 hundred | 268435456 | Streets |
| 21 | 1:3 hundred | 536870912 |  |
| 22 | 1:1 hundred | 1073741824 |  |
| 23 | 1:95 | 2147483648 |  |

*Orientation*

The camera `orientation` is composed of two parts:

- `bearing`: also known as azimuth, the view direction in clockwise degrees; 0° = north, 90° = east, 180° = south, 270° = west
- `tilt`: the angle in degrees from the vertical that the camera is looking down at the Earth; 0° = straight down.

*Changing the Camera*

All changes to the camera are encapsulated in camera updates that are created using the methods in the <a href="sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class">MapCameraUpdateFactory</a> class.

These updates can then be applied to the <a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-class">HereMapControllerCore</a> using <a href="sdk-for-flutter-explore-mapview-mapcamera-applyupdate">MapCamera.applyUpdate</a>.

Camera updates are queued and executed when the next frame is rendered. They are executed in the order in which they were applied.

*Animating the Camera*

Camera updates can be animated by first creating a camera animation using the methods in the <a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-class">MapCameraAnimationFactory</a> class and then applying this animation to the <a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-class">HereMapControllerCore</a> using <a href="sdk-for-flutter-explore-mapview-mapcamera-startanimationwithlistener">MapCamera.startAnimationWithListener</a>.

Only one camera animation for one camera component at a time is supported. Applying a new animation will cancel the active animation before the new one is started. The start position in this case is where ever the active animation happened to be at the time. Different components are camera state (`target pose` and `distance/zoom level/scale`) and camera projection (`field of view`, `focal length` and `principal point`).

The running animations can also be canceled using <a href="sdk-for-flutter-explore-mapview-mapcamera-cancelanimations">MapCamera.cancelAnimations</a> or individual ones using <a href="sdk-for-flutter-explore-mapview-mapcamera-cancelanimation">MapCamera.cancelAnimation</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-mapcamera">MapCamera</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-boundingbox">boundingBox</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>?</span>  
Currently visible map area encompassed in a GeoBox. Note that this bounding box is always rectangular, and its sides are always parallel to the latitude and longitude. If the camera is rotated, the returned bounding box will be a circumscribed rectangle that is larger than the visible map area. Similarly, when the map is tilted (for example, if the map is tilted by 45 degrees), the visible map area represents a trapezoidal area in the world. Resulting value will then be a larger circumscribed rectangle that contains this trapezoid area. Because on this, corners of the resulting bounding box may be located outside of the currently visible area.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-limits">limits</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-mapview-mapcameralimits-class">MapCameraLimits</a></span>  
Controls limits for the camera settings. Gets a MapCameraLimits instance that controls limits for the camera settings.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-principalpoint">principalPoint</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span>  
Determines the pixel point where the target is placed within the map view. Setting a new principal point instantly moves the map to render the current target coordinates at the new principal point. Gets the pixel point that determines where the target is placed within the map view. By default, the principal point is located at the center of the map view.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-state">state</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-mapview-mapcamerastate-class">MapCameraState</a></span>  
Current state of the camera that reflects what is currently drawn by the map view. Gets state of the camera that reflects what is currently drawn inside the map view.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-addlistener">addListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcameralistener-class">MapCameraListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a listener to this camera that will be notified every time the map is redrawn with new camera parameters.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-applyupdate">applyUpdate</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-applyUpdate-param-cameraUpdate" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="parameter-name">cameraUpdate</span></span>) <span class="returntype parameter">→ void</span> </span>  
Applies camera update to the map camera.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-cancelanimation">cancelAnimation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-cancelAnimation-param-cameraAnimation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> <span class="parameter-name">cameraAnimation</span></span>) <span class="returntype parameter">→ void</span> </span>  
Cancels an ongoing camera animation.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-cancelanimations">cancelAnimations</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Cancels any ongoing camera animation.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-dryapplyupdate">dryApplyUpdate</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-dryApplyUpdate-param-cameraUpdate" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="parameter-name">cameraUpdate</span>, </span><span id="sdk-for-flutter-explore-dryApplyUpdate-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcameradrycameraupdatecallback">MapCameraDryCameraUpdateCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Computes result of applying camera update without changing state of the map camera.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-lookatareawithgeoorientation">lookAtAreaWithGeoOrientation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-lookAtAreaWithGeoOrientation-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-explore-lookAtAreaWithGeoOrientation-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span></span>) <span class="returntype parameter">→ void</span> </span>  
Makes the camera look at the specified geodetic area.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-lookatareawithgeoorientationandviewrectangle">lookAtAreaWithGeoOrientationAndViewRectangle</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-lookAtAreaWithGeoOrientationAndViewRectangle-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-explore-lookAtAreaWithGeoOrientationAndViewRectangle-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span><span id="sdk-for-flutter-explore-lookAtAreaWithGeoOrientationAndViewRectangle-param-viewRectangle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-rectangle2d-class">Rectangle2D</a></span> <span class="parameter-name">viewRectangle</span></span>) <span class="returntype parameter">→ void</span> </span>  
Makes the camera look at the specified geodetic area and pass a rectangle which specifies where the area should appear inside of the map view.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-lookatpoint">lookAtPoint</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-lookAtPoint-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">target</span></span>) <span class="returntype parameter">→ void</span> </span>  
Makes the camera look at a new geodetic target, while preserving the current orientation and distance to the target.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-lookatpointwithgeoorientationandmeasure">lookAtPointWithGeoOrientationAndMeasure</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-lookAtPointWithGeoOrientationAndMeasure-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-explore-lookAtPointWithGeoOrientationAndMeasure-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span><span id="sdk-for-flutter-explore-lookAtPointWithGeoOrientationAndMeasure-param-zoom" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">zoom</span></span>) <span class="returntype parameter">→ void</span> </span>  
Makes the camera look at the geodetic target with the given zoom and orientation.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-lookatpointwithmeasure">lookAtPointWithMeasure</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-lookAtPointWithMeasure-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-explore-lookAtPointWithMeasure-param-zoom" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">zoom</span></span>) <span class="returntype parameter">→ void</span> </span>  
Makes the camera look at the geodetic target with the given zoom.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-orbitbywithgeoorientation">orbitByWithGeoOrientation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-orbitByWithGeoOrientation-param-delta" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">delta</span>, </span><span id="sdk-for-flutter-explore-orbitByWithGeoOrientation-param-origin" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span> <span class="parameter-name">origin</span></span>) <span class="returntype parameter">→ void</span> </span>  
Orbits the camera around a specified view point by increasing tilt and bearing by specified delta values.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-removelistener">removeListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeListener-param-observer" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcameralistener-class">MapCameraListener</a></span> <span class="parameter-name">observer</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes the listener from the camera.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-removelisteners">removeListeners</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Removes all registered listeners.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-setdistancetotarget">setDistanceToTarget</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setDistanceToTarget-param-distanceInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceInMeters</span></span>) <span class="returntype parameter">→ void</span> </span>  
Makes the camera look at current target from certain distance

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-setfarplaneconfiguration">setFarPlaneConfiguration</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setFarPlaneConfiguration-param-configs" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>, <span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-class">MapCameraFarPlaneConfiguration</a></span>\></span></span> <span class="parameter-name">configs</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets far plane distance configs per zoom level.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-setorientationattarget">setOrientationAtTarget</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setOrientationAtTarget-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span></span>) <span class="returntype parameter">→ void</span> </span>  
Changes camera orientation in relation to target location.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-startanimation">startAnimation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-startAnimation-param-cameraAnimation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> <span class="parameter-name">cameraAnimation</span></span>) <span class="returntype parameter">→ void</span> </span>  
Starts a given camera animation.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-startanimationwithlistener">startAnimationWithListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-startAnimationWithListener-param-cameraAnimation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> <span class="parameter-name">cameraAnimation</span>, </span><span id="sdk-for-flutter-explore-startAnimationWithListener-param-animationListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-animationlistener-class">AnimationListener</a></span> <span class="parameter-name">animationListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Starts a given camera animation.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-zoomby">zoomBy</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-zoomBy-param-factor" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">factor</span>, </span><span id="sdk-for-flutter-explore-zoomBy-param-origin" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span> <span class="parameter-name">origin</span></span>) <span class="returntype parameter">→ void</span> </span>  
Zooms in or out by a specified factor.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-zoomto">zoomTo</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-zoomTo-param-zoomLevel" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">zoomLevel</span></span>) <span class="returntype parameter">→ void</span> </span>  
Zooms to the specified zoom level.

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamera-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
