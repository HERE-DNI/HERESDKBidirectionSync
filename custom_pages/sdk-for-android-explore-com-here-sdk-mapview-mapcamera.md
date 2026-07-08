---
title: "MapCamera (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcamera"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.MapCamera →
com.here.NativeBase com.here.sdk.mapview.MapCamera →
com.here.sdk.mapview.MapCamera

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapCamera</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Represents the camera looking onto the map view. Each map instance has
exactly one camera that is used to manipulate the way the map is
displayed. Any updates to the state of the camera will be applied while
drawing the next map view frame and the current state of the camera
reflects what is currently drawn inside the map view. Note: The camera
can be configured and positioned even before a map scene is loaded for
the first time. This allows for pre-setting the desired camera position,
orientation, and zoom level, which will be applied once the map scene
becomes available. Camera Model Camera Concepts and Units By default,
HERE SDK uses an idealized Earth globe with a 3D-capable camera model.
Being a 3D camera model means that the world position can be freely
specified in geodetic 3D space (i.e. Earth centric) and the orientation
can be freely changed around two axes - bearing (also known as head) and
tilt (also known as pitch). The camera supports the look-at target with
orientation on the ground way of setting up the camera in space. The
camera is placed so that it looks at a specific geo-coordinates (placed
at the principal point ) from a given orientation and distance. the
look-at target in geo-coordinates (latitude, longitude) in degrees and
an altitude in meters above MSL (mean sea level) at the principal point
the orientation at the look-at target the distance of the camera from
the look-at target, given as distance in meters or as zoom-level Getting
the current camera state The current camera state can be obtained by the
getState() call. It contains information about the camera look-at target
(geo-coordinates and orientation) in geodetic space. The values are
returned for the current principal point . This can lead to surprising
or unexpected values in cases where the camera position/orientation was
specified for another screen point, e.g. when using
MapCameraUpdateFactory.lookAt(GeoBox) with a view rectangle, whose
center does not coincide with the principal point . In this case, the
geo-coordinates of the look-at target will differ from the center of the
geo-box used in the lookAt call. Geo coordinates Geo-coordinates are
given in degrees and follow the common nomenclature of positive northern
latitudes and positive eastern longitudes. Altitude When altitude is
specified, it is always in meters above mean sea level (MSL). If this
value is invalid (not-a-number) or not specified, then the terrain
height at the given geo-coordinates will be looked up from the map. This
is especially interesting in cases where terrain elevation is used
within the map display. Distance vs zoom-level vs scale Map camera
distance , zoom-level and scale determine how much of the world is
visible on the HERE map. Distance , zoom-level and scale are directly
connected and changing one will automatically change the others as well
(except for distance / scale changes that map to zoom-level values \< 0
or \> 23). distance : the distance from the camera to the look-at target
on the surface of the Earth, in meters zoom-level : the map zoom level,
in the range \[0, 3\]. The relation between the width of the equator in
logical pixels w and the zoom level z is: w = 256 \* 2^(z) scale : the
scale of the map at the look-at target in meters on screen per meters on
Earth. So a scale of 0.001 shows 10 meters on Earth within 1 cm on
screen. The following mapping represents the zoom-level values:
zoom-level ~ scale on screen (130dpi) width of the equator in logical
pixels what can be seen 0 1:800 million 256 Earth 1 1:400 million 512 2
1:200 million 1024 3 1:100 million 2048 4 1:50 million 4096 A continent
5 1:25 million 8192 Large roads 6 1:12 million 16384 Large rivers 7 1:6
million 32768 A country 8 1:3 million 65536 9 1:1 million 131072 10
1:780 thousand 262144 11 1:390 thousand 524288 12 1:195 thousand 1048576
13 1:100 thousand 2097152 14 1:50 thousand 4194304 A city 15 1:25
thousand 8388608 16 1:12 thousand 16777216 Buildings 17 1:6 thousand
33554432 Landmarks 18 1:3 thousand 67108864 19 1:1 thousand 134217728 20
1:7 hundred 268435456 Streets 21 1:3 hundred 536870912 22 1:1 hundred
1073741824 23 1:95 2147483648 Orientation The camera orientation is
composed of two parts: bearing : also known as azimuth, the view
direction in clockwise degrees; 0° = north, 90° = east, 180° = south,
270° = west tilt : the angle in degrees from the vertical that the
camera is looking down at the Earth; 0° = straight down. Changing the
Camera All changes to the camera are encapsulated in camera updates that
are created using the methods in the MapCameraUpdateFactory class. These
updates can then be applied to the HereMap using
applyUpdate(com.here.sdk.mapview.MapCameraUpdate) . Camera updates are
queued and executed when the next frame is rendered. They are executed
in the order in which they were applied. Animating the Camera Camera
updates can be animated by first creating a camera animation using the
methods in the MapCameraAnimationFactory class and then applying this
animation to the HereMap using startAnimation(MapCameraAnimation,
AnimationListener) . Only one camera animation for one camera component
at a time is supported. Applying a new animation will cancel the active
animation before the new one is started. The start position in this case
is where ever the active animation happened to be at the time. Different
components are camera state ( target pose and distance/zoom level/scale
) and camera projection ( field of view , focal length and principal
point ). The running animations can also be canceled using
cancelAnimations() or individual ones using
cancelAnimation(com.here.sdk.mapview.MapCameraAnimation) .

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static interface `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-drycameraupdatecallback"
  class="type-name-link"
  title="interface in com.here.sdk.mapview"><code>MapCamera.DryCameraUpdateCallback</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Used to report back results of dry update application to camera.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-farplaneconfiguration"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapCamera.FarPlaneConfiguration</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Far plane distance configuration for a zoom level.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapCamera.State</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Encapsulates state of the camera.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addListener ( MapCameraListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a listener to this camera that will be notified on the main
  thread every time the map is redrawn with new camera parameters.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      applyUpdate ( MapCameraUpdate cameraUpdate)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Applies camera update to the map camera.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      cancelAnimation ( MapCameraAnimation cameraAnimation)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Cancels an ongoing camera animation.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      cancelAnimations ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Cancels any ongoing camera animation.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      dryApplyUpdate ( MapCameraUpdate cameraUpdate, MapCamera.DryCameraUpdateCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Computes result of applying camera update without changing state of
  the map camera.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getBoundingBox ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current visible map area encompassed in a GeoBox.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapCameraLimits`](sdk-for-android-explore-com-here-sdk-mapview-mapcameralimits "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLimits ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a MapCameraLimits instance that controls limits for the camera
  settings.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Point2D`](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPrincipalPoint ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the pixel point that determines where the target is placed within
  the map view.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapCamera.State`](sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getState ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets state of the camera that reflects what is currently drawn inside
  the map view.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      lookAt ( GeoBox target, GeoOrientationUpdate orientation)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Makes the camera look at the specified geodetic area.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      lookAt ( GeoBox target, GeoOrientationUpdate orientation, Rectangle2D viewRectangle)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Makes the camera look at the specified geodetic area and pass a
  rectangle which specifies where the area should appear inside of the
  map view.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      lookAt ( GeoCoordinates target)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Makes the camera look at a new geodetic target, while preserving the
  current orientation and distance to the target.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      lookAt ( GeoCoordinates target, GeoOrientationUpdate orientation, MapMeasure zoom)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Makes the camera look at the geodetic target with the given zoom and
  orientation.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      lookAt ( GeoCoordinates target, MapMeasure zoom)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Makes the camera look at the geodetic target with the given zoom.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      orbitBy ( GeoOrientationUpdate delta, Point2D origin)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Orbits the camera around a specified view point by increasing tilt and
  bearing by specified delta values.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeListener ( MapCameraListener observer)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes the listener from the camera.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeListeners ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes all registered listeners.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDistanceToTarget (double distanceInMeters)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Makes the camera look at current target from certain distance

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setFarPlaneConfiguration ( Map < Double , MapCamera.FarPlaneConfiguration > configs)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets far plane distance configs per zoom level.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setOrientationAtTarget ( GeoOrientationUpdate orientation)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Changes camera orientation in relation to target location.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setPrincipalPoint ( Point2D value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the pixel point that determines where the target appears within
  the map view.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      startAnimation ( MapCameraAnimation cameraAnimation)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Starts a given camera animation.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      startAnimation ( MapCameraAnimation cameraAnimation, AnimationListener animationListener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Starts a given camera animation.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      zoomBy (double factor, Point2D origin)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Zooms in or out by a specified factor.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      zoomTo (double zoomLevel)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Zooms to the specified zoom level.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-setFarPlaneConfiguration-java-util-Map"
    class="section detail">

    ### setFarPlaneConfiguration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFarPlaneConfiguration</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,[MapCamera.FarPlaneConfiguration](sdk-for-android-explore-com-here-sdk-mapview-mapcamera-farplaneconfiguration "class in com.here.sdk.mapview")\> configs)</span>

    </div>

    <div class="block">

    Sets far plane distance configs per zoom level. Values are linearly
    interpolated between provided zoom levels. For z between z0 and z1:
    t = (z - z0) / (z1 - z0) distanceFactor(z) = lerp(distanceFactor0,
    distanceFactor1, t) minDistance(z) = lerp(minDistance0,
    minDistance1, t) Effective far plane for the current frame is:
    farPlaneInMeters = max( minDistance(z), distanceToTargetInMeters \*
    distanceFactor(z) ) Sample Configuration (balanced
    quality/performance, tune per zoom level): 14.4 -\>
    FarPlaneConfiguration(1.3) 18.34 -\> FarPlaneConfiguration(2.0)
    19.60 -\> FarPlaneConfiguration(1.3) minDistanceInMeters remains
    default in this case. Passing an empty map clears the per-zoom
    override and restores the default behavior. Non-finite zoom levels
    or values are ignored. Distance factors are clamped to 0.1 to 10.0.
    The minimum distance is clamped to a range of \[100, 3000\] meters.

    </div>

    Parameters:  
    `configs` -

    Per-zoom override mapping from zoom level to distance configuration.

    </div>

  - <div id="sdk-for-android-explore-addListener-com-here-sdk-mapview-MapCameraListener"
    class="section detail">

    ### addListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addListener</span><span class="parameters">(@NonNull
    [MapCameraListener](sdk-for-android-explore-com-here-sdk-mapview-mapcameralistener "interface in com.here.sdk.mapview") listener)</span>

    </div>

    <div class="block">

    Adds a listener to this camera that will be notified on the main
    thread every time the map is redrawn with new camera parameters.
    Adding the same listener multiple times has no effect.

    </div>

    Parameters:  
    `listener` -

    The listener to add.

    </div>

  - <div id="sdk-for-android-explore-removeListener-com-here-sdk-mapview-MapCameraListener"
    class="section detail">

    ### removeListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeListener</span><span class="parameters">(@NonNull
    [MapCameraListener](sdk-for-android-explore-com-here-sdk-mapview-mapcameralistener "interface in com.here.sdk.mapview") observer)</span>

    </div>

    <div class="block">

    Removes the listener from the camera. Trying to remove a listener
    that is not currently registered has no effect.

    </div>

    Parameters:  
    `observer` -

    Listener to be removed from receiving state notifications.

    </div>

  - <div id="sdk-for-android-explore-removeListeners"
    class="section detail">

    ### removeListeners

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeListeners</span>()

    </div>

    <div class="block">

    Removes all registered listeners.

    </div>

    </div>

  - <div id="sdk-for-android-explore-applyUpdate-com-here-sdk-mapview-MapCameraUpdate"
    class="section detail">

    ### applyUpdate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">applyUpdate</span><span class="parameters">(@NonNull
    [MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview") cameraUpdate)</span>

    </div>

    <div class="block">

    Applies camera update to the map camera. Any ongoing camera
    animations will be cancelled and the corresponding camera animation
    listener will be notified.

    </div>

    Parameters:  
    `cameraUpdate` -

    The update that gets applied to camera.

    </div>

  - <div id="sdk-for-android-explore-dryApplyUpdate-com-here-sdk-mapview-MapCameraUpdate-com-here-sdk-mapview-MapCamera-DryCameraUpdateCallback"
    class="section detail">

    ### dryApplyUpdate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dryApplyUpdate</span><span class="parameters">(@NonNull
    [MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview") cameraUpdate,
    @NonNull
    [MapCamera.DryCameraUpdateCallback](sdk-for-android-explore-com-here-sdk-mapview-mapcamera-drycameraupdatecallback "interface in com.here.sdk.mapview") callback)</span>

    </div>

    <div class="block">

    Computes result of applying camera update without changing state of
    the map camera. Note that this is a beta release of this feature, so
    there could be a few bugs and unexpected behaviors. Related APIs may
    change for new releases without a deprecation process.

    </div>

    Parameters:  
    `cameraUpdate` -

    The update that gets dryly applied to camera.

    `callback` -

    Called upon completion with computed map state. callback is called
    on the main thread.

    </div>

  - <div id="sdk-for-android-explore-startAnimation-com-here-sdk-mapview-MapCameraAnimation"
    class="section detail">

    ### startAnimation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startAnimation</span><span class="parameters">(@NonNull
    [MapCameraAnimation](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation "class in com.here.sdk.mapview") cameraAnimation)</span>

    </div>

    <div class="block">

    Starts a given camera animation. Starting an animation can cause the
    cancelling of an ongoing animation when they both affect the same
    category of camera properties, like for example any of the look-at
    properties (target, orientation, map measure) or any of the
    projection properties (field of view, principal point, focal
    length). The corresponding listener of an ongoing animation will be
    notified about the cancellation in these cases.

    </div>

    Parameters:  
    `cameraAnimation` -

    The animation to be started.

    </div>

  - <div id="sdk-for-android-explore-startAnimation-com-here-sdk-mapview-MapCameraAnimation-com-here-sdk-animation-AnimationListener"
    class="section detail">

    ### startAnimation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startAnimation</span><span class="parameters">(@NonNull
    [MapCameraAnimation](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation "class in com.here.sdk.mapview") cameraAnimation,
    @NonNull
    [AnimationListener](sdk-for-android-explore-com-here-sdk-animation-animationlistener "interface in com.here.sdk.animation") animationListener)</span>

    </div>

    <div class="block">

    Starts a given camera animation. The state of the animation can be
    tracked with the provided listener. Starting an animation can cause
    the cancelling of an ongoing animation when they both affect the
    same category of camera properties, like for example any of the
    look-at properties (target, orientation, map measure) or any of the
    projection properties (field of view, principal point, focal
    length). The corresponding listener of an ongoing animation will be
    notified about the cancellation in these cases.

    </div>

    Parameters:  
    `cameraAnimation` -

    The animation to be started.

    `animationListener` -

    Animation listener. A strong reference is kept internally up until
    the animation gets cancelled or completed.

    </div>

  - <div id="sdk-for-android-explore-cancelAnimation-com-here-sdk-mapview-MapCameraAnimation"
    class="section detail">

    ### cancelAnimation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">cancelAnimation</span><span class="parameters">(@NonNull
    [MapCameraAnimation](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation "class in com.here.sdk.mapview") cameraAnimation)</span>

    </div>

    <div class="block">

    Cancels an ongoing camera animation. Upon cancellation, the
    corresponding listener will be notified.

    </div>

    Parameters:  
    `cameraAnimation` -

    The animation to be cancelled.

    </div>

  - <div id="sdk-for-android-explore-cancelAnimations"
    class="section detail">

    ### cancelAnimations

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">cancelAnimations</span>()

    </div>

    <div class="block">

    Cancels any ongoing camera animation. Upon cancellation, the
    corresponding listener of any cancelled animation will be notified.

    </div>

    </div>

  - <div id="sdk-for-android-explore-orbitBy-com-here-sdk-core-GeoOrientationUpdate-com-here-sdk-core-Point2D"
    class="section detail">

    ### orbitBy

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">orbitBy</span><span class="parameters">(@NonNull
    [GeoOrientationUpdate](sdk-for-android-explore-com-here-sdk-core-geoorientationupdate "class in com.here.sdk.core") delta,
    @NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") origin)</span>

    </div>

    <div class="block">

    Orbits the camera around a specified view point by increasing tilt
    and bearing by specified delta values.

    </div>

    Parameters:  
    `delta` -

    Camera orientation change, containing tilt and bearing angle deltas.

    `origin` -

    Pixel point in view coordinates around which orbiting occurs.

    </div>

  - <div id="sdk-for-android-explore-zoomBy-double-com-here-sdk-core-Point2D"
    class="section detail">

    ### zoomBy

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">zoomBy</span><span class="parameters">(double factor,
    @NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") origin)</span>

    </div>

    <div class="block">

    Zooms in or out by a specified factor. This effectively changes the
    distance from the camera to the MapCamera.State.targetCoordinates by
    the specified factor, which changes MapCamera.State.zoomLevel as
    well. Values above 1.0 will zoom in and values below will zoom out.
    The relation with MapCamera.State.distanceToTargetInMeters is
    inversely linear, meaning that zooming by 4 will decrease distance
    to target by 4 while zooming by 0.5 will increase distance to target
    by 2. The relation with zoom level is logarithmic. Meaning that
    zooming by a factor of 4 will increase zoom level by 2 (because
    log2(4) == 2). So to zoom in by X zoom levels, the zoom factor needs
    to be 2^X. To zoom out by X zoom levels, zoom factor needs to be
    1/(2^X). The zooming occurs around the specified origin inside the
    view.

    </div>

    Parameters:  
    `factor` -

    The zoom factor. Values above 1.0 will zoom in and values below will
    zoom out.

    `origin` -

    Pixel point in view coordinates around which zooming occurs.

    </div>

  - <div id="sdk-for-android-explore-zoomTo-double"
    class="section detail">

    ### zoomTo

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">zoomTo</span><span class="parameters">(double zoomLevel)</span>

    </div>

    <div class="block">

    Zooms to the specified zoom level. The supplied value will be
    clamped to the range of \[0, 22\], where 0 is a view of whole globe
    and 22 is street level. This effectively changes the distance from
    the camera to the target. The zooming occurs around the current
    target point.

    </div>

    Parameters:  
    `zoomLevel` -

    The zoom level to set, clamped to the range of \[0, 22\].

    </div>

  - <div id="sdk-for-android-explore-lookAt-com-here-sdk-core-GeoCoordinates"
    class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") target)</span>

    </div>

    <div class="block">

    Makes the camera look at a new geodetic target, while preserving the
    current orientation and distance to the target. The altitude of the
    target point is ignored. Any subsequent camera updates and
    animations will consider the target point as being located on the
    ground.

    </div>

    Parameters:  
    `target` -

    Geodetic coordinates at which the camera will point.

    </div>

  - <div id="sdk-for-android-explore-lookAt-com-here-sdk-core-GeoCoordinates-com-here-sdk-mapview-MapMeasure"
    class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") target,
    @NonNull
    [MapMeasure](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview") zoom)</span>

    </div>

    <div class="block">

    Makes the camera look at the geodetic target with the given zoom.
    The altitude of the target point is ignored. Any subsequent camera
    updates and animations will consider the target point as being
    located on the ground.

    </div>

    Parameters:  
    `target` -

    Geodetic coordinates at which the camera will point.

    `zoom` -

    The zoom level which can be provided as distance to the target
    point, scale or zoom level.

    </div>

  - <div id="sdk-for-android-explore-lookAt-com-here-sdk-core-GeoCoordinates-com-here-sdk-core-GeoOrientationUpdate-com-here-sdk-mapview-MapMeasure"
    class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") target,
    @NonNull
    [GeoOrientationUpdate](sdk-for-android-explore-com-here-sdk-core-geoorientationupdate "class in com.here.sdk.core") orientation,
    @NonNull
    [MapMeasure](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview") zoom)</span>

    </div>

    <div class="block">

    Makes the camera look at the geodetic target with the given zoom and
    orientation. The supplied orientation is the orientation of the
    camera looking at the target, so the resulting camera state will
    have the same orientation as the one supplied to this method. The
    altitude of the target point is ignored. Any subsequent camera
    updates and animations will consider the target point as being
    located on the ground.

    </div>

    Parameters:  
    `target` -

    Geodetic coordinates at which the camera will point.

    `orientation` -

    Desired orientation of the camera.

    `zoom` -

    The zoom level which can be provided as distance to the target
    point, scale or zoom level.

    </div>

  - <div id="sdk-for-android-explore-lookAt-com-here-sdk-core-GeoBox-com-here-sdk-core-GeoOrientationUpdate"
    class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") target,
    @NonNull
    [GeoOrientationUpdate](sdk-for-android-explore-com-here-sdk-core-geoorientationupdate "class in com.here.sdk.core") orientation)</span>

    </div>

    <div class="block">

    Makes the camera look at the specified geodetic area. The supplied
    orientation is the orientation of the camera looking at the target,
    so the resulting camera state will have the same orientation as the
    one supplied to this method. The altitude of the target points is
    ignored.

    </div>

    Parameters:  
    `target` -

    Geodetic area at which the camera will point

    `orientation` -

    Desired orientation of the camera

    </div>

  - <div id="sdk-for-android-explore-lookAt-com-here-sdk-core-GeoBox-com-here-sdk-core-GeoOrientationUpdate-com-here-sdk-core-Rectangle2D"
    class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") target,
    @NonNull
    [GeoOrientationUpdate](sdk-for-android-explore-com-here-sdk-core-geoorientationupdate "class in com.here.sdk.core") orientation,
    @NonNull
    [Rectangle2D](sdk-for-android-explore-com-here-sdk-core-rectangle2d "class in com.here.sdk.core") viewRectangle)</span>

    </div>

    <div class="block">

    Makes the camera look at the specified geodetic area and pass a
    rectangle which specifies where the area should appear inside of the
    map view. The supplied orientation is the orientation of the camera
    looking at the target, so the resulting camera state will have the
    same orientation as the one supplied to this method. Please note
    that the resulting orientation might deviate from the provided
    orientation. This is particularly the case if a large geobox on
    world level and a view rectangle which is relatively small was
    passed to the method. The altitude of the target points is ignored.

    </div>

    Parameters:  
    `target` -

    Geodetic area which will be shown in the viewRectangle.

    `orientation` -

    Desired orientation of the camera.

    `viewRectangle` -

    The view rectangle in viewport pixel coordinates inside which the
    geographical target area is displayed.

    </div>

  - <div id="sdk-for-android-explore-setDistanceToTarget-double"
    class="section detail">

    ### setDistanceToTarget

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDistanceToTarget</span><span class="parameters">(double distanceInMeters)</span>

    </div>

    <div class="block">

    Makes the camera look at current target from certain distance This
    function neither modifies target coordinates nor target orientation.

    </div>

    Parameters:  
    `distanceInMeters` -

    Distance in meters to the target point. Minimal distance value is
    clamped to 100 meters.

    </div>

  - <div id="sdk-for-android-explore-setOrientationAtTarget-com-here-sdk-core-GeoOrientationUpdate"
    class="section detail">

    ### setOrientationAtTarget

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOrientationAtTarget</span><span class="parameters">(@NonNull
    [GeoOrientationUpdate](sdk-for-android-explore-com-here-sdk-core-geoorientationupdate "class in com.here.sdk.core") orientation)</span>

    </div>

    <div class="block">

    Changes camera orientation in relation to target location.

    </div>

    Parameters:  
    `orientation` -

    Desired orientation of the camera.

    </div>

  - <div id="sdk-for-android-explore-getState" class="section detail">

    ### getState

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapCamera.State](sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state "class in com.here.sdk.mapview")</span> <span class="element-name">getState</span>()

    </div>

    <div class="block">

    Gets state of the camera that reflects what is currently drawn
    inside the map view.

    </div>

    Returns:  
    Current state of the camera that reflects what is currently drawn by
    the map view.

    </div>

  - <div id="sdk-for-android-explore-getPrincipalPoint"
    class="section detail">

    ### getPrincipalPoint

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core")</span> <span class="element-name">getPrincipalPoint</span>()

    </div>

    <div class="block">

    Gets the pixel point that determines where the target is placed
    within the map view. By default, the principal point is located at
    the center of the map view. The value of the principal point is
    adjusted when the dimensions of the map view change, so that it
    stays in the same point relative to width and height. Meaning that
    when a principal point it set to bottom middle of the map view, it
    will stay in the bottom middle regardless of the changes to
    dimensions and orientation of the view.

    </div>

    Returns:  
    Determines the pixel point where the target is placed within the map
    view. Setting a new principal point instantly moves the map to
    render the current target coordinates at the new principal point.

    </div>

  - <div id="sdk-for-android-explore-setPrincipalPoint-com-here-sdk-core-Point2D"
    class="section detail">

    ### setPrincipalPoint

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPrincipalPoint</span><span class="parameters">(@NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets the pixel point that determines where the target appears within
    the map view. This instantly moves the map to render the current
    target coordinates at the new principal point. By default, the
    principal point is located at the center of the map view. It is set
    in pixels relative to the map view's origin top-left (0, 0). Values
    outside the map view's dimensions (x \< 0 \|\| x \> width, y \< 0
    \|\| y \> height) will be rejected silently and the current
    principal point is kept. The value of the principal point is
    adjusted when the dimensions of the map view change, so that it
    stays in the same point relative to width and height. Meaning that
    when a principal point it set to bottom middle of the map view, it
    will stay in the bottom middle regardless of the changes to
    dimensions and orientation of the view. Note: The principal point
    affects all programmatical map transformations (rotate, orbit, tilt
    and zoom) and the two-finger-pan gesture to tilt the map. Other
    gestures, like pinch-rotate, are not affected.

    </div>

    Parameters:  
    `value` -

    Determines the pixel point where the target is placed within the map
    view. Setting a new principal point instantly moves the map to
    render the current target coordinates at the new principal point.

    </div>

  - <div id="sdk-for-android-explore-getBoundingBox"
    class="section detail">

    ### getBoundingBox

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")</span> <span class="element-name">getBoundingBox</span>()

    </div>

    <div class="block">

    Gets the current visible map area encompassed in a GeoBox. Note that
    this bounding box is always rectangular, and its sides are always
    parallel to the latitude and longitude. If the camera is rotated,
    the returned bounding box will be a circumscribed rectangle that is
    larger than the visible map area. Similarly, when the map is tilted
    (for example, if the map is tilted by 45 degrees), the visible map
    area represents a trapezoidal area in the world. Resulting value
    will then be a larger circumscribed rectangle that contains this
    trapezoid area. Because on this, corners of the resulting bounding
    box may be located outside of the currently visible area. When the
    map area does not fully fill the viewport, null is returned.

    </div>

    Returns:  
    Currently visible map area encompassed in a GeoBox.

    </div>

  - <div id="sdk-for-android-explore-getLimits" class="section detail">

    ### getLimits

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapCameraLimits](sdk-for-android-explore-com-here-sdk-mapview-mapcameralimits "class in com.here.sdk.mapview")</span> <span class="element-name">getLimits</span>()

    </div>

    <div class="block">

    Gets a MapCameraLimits instance that controls limits for the camera
    settings.

    </div>

    Returns:  
    Controls limits for the camera settings.

    </div>

  </div>

