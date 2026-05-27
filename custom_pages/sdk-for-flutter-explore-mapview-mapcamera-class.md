---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mapcamera-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapCamera-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapCamera-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapCamera/MapCamera.html">MapCamera</a></li>
<li class="section-title">
<a href="mapview/MapCamera-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapCamera/boundingBox.html">boundingBox</a></li>
<li class="inherited"><a href="mapview/MapCamera/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapCamera/limits.html">limits</a></li>
<li><a href="mapview/MapCamera/principalPoint.html">principalPoint</a></li>
<li class="inherited"><a href="mapview/MapCamera/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/MapCamera/state.html">state</a></li>
<li class="section-title"><a href="mapview/MapCamera-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MapCamera/addListener.html">addListener</a></li>
<li><a href="mapview/MapCamera/applyUpdate.html">applyUpdate</a></li>
<li><a href="mapview/MapCamera/cancelAnimation.html">cancelAnimation</a></li>
<li><a href="mapview/MapCamera/cancelAnimations.html">cancelAnimations</a></li>
<li><a href="mapview/MapCamera/dryApplyUpdate.html">dryApplyUpdate</a></li>
<li><a href="mapview/MapCamera/lookAtAreaWithGeoOrientation.html">lookAtAreaWithGeoOrientation</a></li>
<li><a href="mapview/MapCamera/lookAtAreaWithGeoOrientationAndViewRectangle.html">lookAtAreaWithGeoOrientationAndViewRectangle</a></li>
<li><a href="mapview/MapCamera/lookAtPoint.html">lookAtPoint</a></li>
<li><a href="mapview/MapCamera/lookAtPointWithGeoOrientationAndMeasure.html">lookAtPointWithGeoOrientationAndMeasure</a></li>
<li><a href="mapview/MapCamera/lookAtPointWithMeasure.html">lookAtPointWithMeasure</a></li>
<li class="inherited"><a href="mapview/MapCamera/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MapCamera/orbitByWithGeoOrientation.html">orbitByWithGeoOrientation</a></li>
<li><a href="mapview/MapCamera/removeListener.html">removeListener</a></li>
<li><a href="mapview/MapCamera/removeListeners.html">removeListeners</a></li>
<li><a href="mapview/MapCamera/setDistanceToTarget.html">setDistanceToTarget</a></li>
<li><a href="mapview/MapCamera/setFarPlaneConfiguration.html">setFarPlaneConfiguration</a></li>
<li><a href="mapview/MapCamera/setOrientationAtTarget.html">setOrientationAtTarget</a></li>
<li><a href="mapview/MapCamera/startAnimation.html">startAnimation</a></li>
<li><a href="mapview/MapCamera/startAnimationWithListener.html">startAnimationWithListener</a></li>
<li class="inherited"><a href="mapview/MapCamera/toString.html">toString</a></li>
<li><a href="mapview/MapCamera/zoomBy.html">zoomBy</a></li>
<li><a href="mapview/MapCamera/zoomTo.html">zoomTo</a></li>
<li class="section-title inherited"><a href="mapview/MapCamera-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapCamera/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapCamera class</li>
</ol>
<div class="self-name">MapCamera</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCamera-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapCamera class abstract</h1></div>
<section class="desc markdown">
<p>Represents the camera looking onto the map view.</p>
<p>Each map instance has exactly one camera that is used to manipulate
the way the map is displayed.</p>
<p>Any updates to the state of the camera will be applied while drawing the next map view frame
and the current state of the camera reflects what is currently drawn inside the map view.</p>
<p>Note: The camera can be configured and positioned even before a map scene is loaded for the first time.
This allows for pre-setting the desired camera position, orientation, and zoom level, which will be
applied once the map scene becomes available.</p>
<p><b>Camera Model</b></p>
<p><i>Camera Concepts and Units</i></p>
<p>By default, HERE SDK uses an idealized Earth globe with a 3D-capable camera model. Being a 3D camera model means that the
world position can be freely specified in geodetic 3D space (i.e. Earth centric) and the orientation can be freely changed around
two axes - bearing (also known as head) and tilt (also known as pitch).</p>
<p>The camera supports the look-at target with orientation on the ground way of setting up the camera in space. The camera is placed
so that it looks at a specific geo-coordinates (placed at the <code>principal point</code>) from a given orientation and distance.</p>
<ul>
<li>the look-at target in geo-coordinates (latitude, longitude) in degrees and an <code>altitude</code> in meters above MSL (mean sea level) at the <code>principal point</code></li>
<li>the <code>orientation</code> at the look-at target</li>
<li>the distance of the camera from the look-at target, given as <code>distance</code> in meters or as <code>zoom-level</code></li>
</ul>
<p><i>Getting the current camera state</i></p>
<p>The current camera state can be obtained by the <a href="../mapview/MapCamera/state.html">/sdk-for-flutter-explore-mapview-mapcamera-state</a> call. It contains information about the camera look-at target (geo-coordinates and orientation) in geodetic space.
The values are returned for the current <code>principal point</code>. This can lead to surprising or unexpected values in cases where the camera position/orientation was specified for another screen point,
e.g. when using <a href="../mapview/MapCameraUpdateFactory/lookAtArea.html">/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatarea</a> with a view rectangle, whose center does not coincide with the <code>principal point</code>.  In this case, the geo-coordinates of the
look-at target will differ from the center of the geo-box used in the <code>lookAt</code> call.</p>
<p><i>Geo coordinates</i></p>
<p>Geo-coordinates are given in degrees and follow the common nomenclature of positive northern latitudes and positive eastern longitudes.</p>
<p><i>Altitude</i></p>
<p>When <code>altitude</code> is specified, it is always in meters above mean sea level (MSL).
If this value is invalid (not-a-number) or not specified, then the terrain height at the given geo-coordinates will be looked up from the map.
This is especially interesting in cases where terrain elevation is used within the map display.</p>
<p><i>Distance vs zoom-level vs scale</i></p>
<p>Map camera <code>distance</code>, <code>zoom-level</code> and <code>scale</code> determine how much of the world is visible on the HERE map. <code>Distance</code>, <code>zoom-level</code> and <code>scale</code> are
directly connected and changing one will automatically change the others as well (except for <code>distance</code>/<code>scale</code> changes that map to <code>zoom-level</code> values &lt; 0 or &gt; 23).</p>
<ul>
<li><code>distance</code>: the distance from the camera to the look-at target on the surface of the Earth, in meters</li>
<li><code>zoom-level</code>: the map zoom level, in the range [0, 3]. The relation between the width of the equator in logical pixels <code>w</code> and the zoom level <code>z</code> is: <code>w = 256 * 2^(z)</code></li>
<li><code>scale</code>: the scale of the map at the look-at target in meters on screen per meters on Earth. So a scale of 0.001 shows 10 meters on Earth within 1 cm on screen.</li>
</ul>
<p>The following mapping represents the <code>zoom-level</code> values:</p>
<table>
<thead>
<tr>
<th>zoom-level</th>
<th align="center">~ scale on screen (130dpi)</th>
<th align="center">width of the equator in logical pixels</th>
<th align="center">what can be seen</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td align="center">1:800 million</td>
<td align="center">256</td>
<td align="center">Earth</td>
</tr>
<tr>
<td>1</td>
<td align="center">1:400 million</td>
<td align="center">512</td>
<td align="center"></td>
</tr>
<tr>
<td>2</td>
<td align="center">1:200 million</td>
<td align="center">1024</td>
<td align="center"></td>
</tr>
<tr>
<td>3</td>
<td align="center">1:100 million</td>
<td align="center">2048</td>
<td align="center"></td>
</tr>
<tr>
<td>4</td>
<td align="center">1:50 million</td>
<td align="center">4096</td>
<td align="center">A continent</td>
</tr>
<tr>
<td>5</td>
<td align="center">1:25 million</td>
<td align="center">8192</td>
<td align="center">Large roads</td>
</tr>
<tr>
<td>6</td>
<td align="center">1:12 million</td>
<td align="center">16384</td>
<td align="center">Large rivers</td>
</tr>
<tr>
<td>7</td>
<td align="center">1:6 million</td>
<td align="center">32768</td>
<td align="center">A country</td>
</tr>
<tr>
<td>8</td>
<td align="center">1:3 million</td>
<td align="center">65536</td>
<td align="center"></td>
</tr>
<tr>
<td>9</td>
<td align="center">1:1 million</td>
<td align="center">131072</td>
<td align="center"></td>
</tr>
<tr>
<td>10</td>
<td align="center">1:780 thousand</td>
<td align="center">262144</td>
<td align="center"></td>
</tr>
<tr>
<td>11</td>
<td align="center">1:390 thousand</td>
<td align="center">524288</td>
<td align="center"></td>
</tr>
<tr>
<td>12</td>
<td align="center">1:195 thousand</td>
<td align="center">1048576</td>
<td align="center"></td>
</tr>
<tr>
<td>13</td>
<td align="center">1:100 thousand</td>
<td align="center">2097152</td>
<td align="center"></td>
</tr>
<tr>
<td>14</td>
<td align="center">1:50 thousand</td>
<td align="center">4194304</td>
<td align="center">A city</td>
</tr>
<tr>
<td>15</td>
<td align="center">1:25 thousand</td>
<td align="center">8388608</td>
<td align="center"></td>
</tr>
<tr>
<td>16</td>
<td align="center">1:12 thousand</td>
<td align="center">16777216</td>
<td align="center">Buildings</td>
</tr>
<tr>
<td>17</td>
<td align="center">1:6 thousand</td>
<td align="center">33554432</td>
<td align="center">Landmarks</td>
</tr>
<tr>
<td>18</td>
<td align="center">1:3 thousand</td>
<td align="center">67108864</td>
<td align="center"></td>
</tr>
<tr>
<td>19</td>
<td align="center">1:1 thousand</td>
<td align="center">134217728</td>
<td align="center"></td>
</tr>
<tr>
<td>20</td>
<td align="center">1:7 hundred</td>
<td align="center">268435456</td>
<td align="center">Streets</td>
</tr>
<tr>
<td>21</td>
<td align="center">1:3 hundred</td>
<td align="center">536870912</td>
<td align="center"></td>
</tr>
<tr>
<td>22</td>
<td align="center">1:1 hundred</td>
<td align="center">1073741824</td>
<td align="center"></td>
</tr>
<tr>
<td>23</td>
<td align="center">1:95</td>
<td align="center">2147483648</td>
<td align="center"></td>
</tr>
</tbody>
</table>
<p><i>Orientation</i></p>
<p>The camera <code>orientation</code> is composed of two parts:</p>
<ul>
<li><code>bearing</code>: also known as azimuth, the view direction in clockwise degrees; 0° = north, 90° = east, 180° = south, 270° = west</li>
<li><code>tilt</code>: the angle in degrees from the vertical that the camera is looking down at the Earth; 0° = straight down.</li>
</ul>
<p><i>Changing the Camera</i></p>
<p>All changes to the camera are encapsulated in camera updates that are created using the methods in the <a href="../mapview/MapCameraUpdateFactory-class.html">/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class</a> class.</p>
<p>These updates can then be applied to the <a href="../mapview/HereMapControllerCore-class.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-class</a> using <a href="../mapview/MapCamera/applyUpdate.html">/sdk-for-flutter-explore-mapview-mapcamera-applyupdate</a>.</p>
<p>Camera updates are queued and executed when the next frame is rendered. They are executed in the order in which they were applied.</p>
<p><i>Animating the Camera</i></p>
<p>Camera updates can be animated by first creating a camera animation using the methods in the <a href="../mapview/MapCameraAnimationFactory-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-class</a> class and then applying this
animation to the <a href="../mapview/HereMapControllerCore-class.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-class</a> using <a href="../mapview/MapCamera/startAnimationWithListener.html">/sdk-for-flutter-explore-mapview-mapcamera-startanimationwithlistener</a>.</p>
<p>Only one camera animation for one camera component at a time is supported. Applying a new animation will cancel the active animation before the new one is started.
The start position in this case is where ever the active animation happened to be at the time. Different components are camera state (<code>target pose</code> and <code>distance/zoom level/scale</code>)
and camera projection (<code>field of view</code>, <code>focal length</code> and <code>principal point</code>).</p>
<p>The running animations can also be canceled using <a href="../mapview/MapCamera/cancelAnimations.html">/sdk-for-flutter-explore-mapview-mapcamera-cancelanimations</a> or individual ones using <a href="../mapview/MapCamera/cancelAnimation.html">/sdk-for-flutter-explore-mapview-mapcamera-cancelanimation</a>.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapCamera">
<a href="../mapview/MapCamera/MapCamera.html">/sdk-for-flutter-explore-mapview-mapcamera-mapcamera</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="boundingBox">
<a href="../mapview/MapCamera/boundingBox.html">/sdk-for-flutter-explore-mapview-mapcamera-boundingbox</a>
→ <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>?
</dt>
<dd>
  Currently visible map area encompassed in a GeoBox.
Note that this bounding box is always rectangular, and its sides are always
parallel to the latitude and longitude. If the camera is rotated, the returned
bounding box will be a circumscribed rectangle that is larger than the
visible map area. Similarly, when the map is tilted (for example, if
the map is tilted by 45 degrees), the visible map area represents
a trapezoidal area in the world. Resulting value will then be a larger
circumscribed rectangle that contains this trapezoid area.
Because on this, corners of the resulting bounding box may be located
outside of the currently visible area.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapCamera/hashCode.html">/sdk-for-flutter-explore-mapview-mapcamera-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="limits">
<a href="../mapview/MapCamera/limits.html">/sdk-for-flutter-explore-mapview-mapcamera-limits</a>
→ <a href="../mapview/MapCameraLimits-class.html">/sdk-for-flutter-explore-mapview-mapcameralimits-class</a>
</dt>
<dd>
  Controls limits for the camera settings.
Gets a MapCameraLimits instance that controls limits for the camera settings.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="principalPoint">
<a href="../mapview/MapCamera/principalPoint.html">/sdk-for-flutter-explore-mapview-mapcamera-principalpoint</a>
↔ <a href="../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a>
</dt>
<dd>
  Determines the pixel point where the target is placed within the map view. Setting a new
principal point instantly moves the map to render the current target coordinates
at the new principal point.
Gets the pixel point that determines where the target is placed within the map view.
By default, the principal point is located at the center of the map view.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapCamera/runtimeType.html">/sdk-for-flutter-explore-mapview-mapcamera-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="state">
<a href="../mapview/MapCamera/state.html">/sdk-for-flutter-explore-mapview-mapcamera-state</a>
→ <a href="../mapview/MapCameraState-class.html">/sdk-for-flutter-explore-mapview-mapcamerastate-class</a>
</dt>
<dd>
  Current state of the camera that reflects what is currently drawn by the map view.
Gets state of the camera that reflects what is currently drawn inside the map view.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="addListener">
<a href="../mapview/MapCamera/addListener.html">/sdk-for-flutter-explore-mapview-mapcamera-addlistener</a>(<wbr/><a href="../mapview/MapCameraListener-class.html">/sdk-for-flutter-explore-mapview-mapcameralistener-class</a> listener)
    → void

</dt>
<dd>
  Adds a listener to this camera that will be notified
every time the map is redrawn with new camera parameters.
  

</dd>
<dt class="callable" id="applyUpdate">
<a href="../mapview/MapCamera/applyUpdate.html">/sdk-for-flutter-explore-mapview-mapcamera-applyupdate</a>(<wbr/><a href="../mapview/MapCameraUpdate-class.html">/sdk-for-flutter-explore-mapview-mapcameraupdate-class</a> cameraUpdate)
    → void

</dt>
<dd>
  Applies camera update to the map camera.
  

</dd>
<dt class="callable" id="cancelAnimation">
<a href="../mapview/MapCamera/cancelAnimation.html">/sdk-for-flutter-explore-mapview-mapcamera-cancelanimation</a>(<wbr/><a href="../mapview/MapCameraAnimation-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimation-class</a> cameraAnimation)
    → void

</dt>
<dd>
  Cancels an ongoing camera animation.
  

</dd>
<dt class="callable" id="cancelAnimations">
<a href="../mapview/MapCamera/cancelAnimations.html">/sdk-for-flutter-explore-mapview-mapcamera-cancelanimations</a>(<wbr/>)
    → void

</dt>
<dd>
  Cancels any ongoing camera animation.
  

</dd>
<dt class="callable" id="dryApplyUpdate">
<a href="../mapview/MapCamera/dryApplyUpdate.html">/sdk-for-flutter-explore-mapview-mapcamera-dryapplyupdate</a>(<wbr/><a href="../mapview/MapCameraUpdate-class.html">/sdk-for-flutter-explore-mapview-mapcameraupdate-class</a> cameraUpdate, <a href="../mapview/MapCameraDryCameraUpdateCallback.html">/sdk-for-flutter-explore-mapview-mapcameradrycameraupdatecallback</a> callback)
    → void

</dt>
<dd>
  Computes result of applying camera update without changing state of the map camera.
  

</dd>
<dt class="callable" id="lookAtAreaWithGeoOrientation">
<a href="../mapview/MapCamera/lookAtAreaWithGeoOrientation.html">/sdk-for-flutter-explore-mapview-mapcamera-lookatareawithgeoorientation</a>(<wbr/><a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> target, <a href="../core/GeoOrientationUpdate-class.html">/sdk-for-flutter-explore-core-geoorientationupdate-class</a> orientation)
    → void

</dt>
<dd>
  Makes the camera look at the specified geodetic area.
  

</dd>
<dt class="callable" id="lookAtAreaWithGeoOrientationAndViewRectangle">
<a href="../mapview/MapCamera/lookAtAreaWithGeoOrientationAndViewRectangle.html">/sdk-for-flutter-explore-mapview-mapcamera-lookatareawithgeoorientationandviewrectangle</a>(<wbr/><a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> target, <a href="../core/GeoOrientationUpdate-class.html">/sdk-for-flutter-explore-core-geoorientationupdate-class</a> orientation, <a href="../core/Rectangle2D-class.html">/sdk-for-flutter-explore-core-rectangle2d-class</a> viewRectangle)
    → void

</dt>
<dd>
  Makes the camera look at the specified geodetic area and pass a rectangle which specifies
where the area should appear inside of the map view.
  

</dd>
<dt class="callable" id="lookAtPoint">
<a href="../mapview/MapCamera/lookAtPoint.html">/sdk-for-flutter-explore-mapview-mapcamera-lookatpoint</a>(<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> target)
    → void

</dt>
<dd>
  Makes the camera look at a new geodetic target, while
preserving the current orientation and distance to the target.
  

</dd>
<dt class="callable" id="lookAtPointWithGeoOrientationAndMeasure">
<a href="../mapview/MapCamera/lookAtPointWithGeoOrientationAndMeasure.html">/sdk-for-flutter-explore-mapview-mapcamera-lookatpointwithgeoorientationandmeasure</a>(<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> target, <a href="../core/GeoOrientationUpdate-class.html">/sdk-for-flutter-explore-core-geoorientationupdate-class</a> orientation, <a href="../mapview/MapMeasure-class.html">/sdk-for-flutter-explore-mapview-mapmeasure-class</a> zoom)
    → void

</dt>
<dd>
  Makes the camera look at the geodetic target with the given zoom and orientation.
  

</dd>
<dt class="callable" id="lookAtPointWithMeasure">
<a href="../mapview/MapCamera/lookAtPointWithMeasure.html">/sdk-for-flutter-explore-mapview-mapcamera-lookatpointwithmeasure</a>(<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> target, <a href="../mapview/MapMeasure-class.html">/sdk-for-flutter-explore-mapview-mapmeasure-class</a> zoom)
    → void

</dt>
<dd>
  Makes the camera look at the geodetic target with the given zoom.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapCamera/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mapcamera-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="orbitByWithGeoOrientation">
<a href="../mapview/MapCamera/orbitByWithGeoOrientation.html">/sdk-for-flutter-explore-mapview-mapcamera-orbitbywithgeoorientation</a>(<wbr/><a href="../core/GeoOrientationUpdate-class.html">/sdk-for-flutter-explore-core-geoorientationupdate-class</a> delta, <a href="../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a> origin)
    → void

</dt>
<dd>
  Orbits the camera around a specified view point by increasing tilt and bearing by specified
delta values.
  

</dd>
<dt class="callable" id="removeListener">
<a href="../mapview/MapCamera/removeListener.html">/sdk-for-flutter-explore-mapview-mapcamera-removelistener</a>(<wbr/><a href="../mapview/MapCameraListener-class.html">/sdk-for-flutter-explore-mapview-mapcameralistener-class</a> observer)
    → void

</dt>
<dd>
  Removes the listener from the camera.
  

</dd>
<dt class="callable" id="removeListeners">
<a href="../mapview/MapCamera/removeListeners.html">/sdk-for-flutter-explore-mapview-mapcamera-removelisteners</a>(<wbr/>)
    → void

</dt>
<dd>
  Removes all registered listeners.
  

</dd>
<dt class="callable" id="setDistanceToTarget">
<a href="../mapview/MapCamera/setDistanceToTarget.html">/sdk-for-flutter-explore-mapview-mapcamera-setdistancetotarget</a>(<wbr/>double distanceInMeters)
    → void

</dt>
<dd>
  Makes the camera look at current target from certain distance
  

</dd>
<dt class="callable" id="setFarPlaneConfiguration">
<a href="../mapview/MapCamera/setFarPlaneConfiguration.html">/sdk-for-flutter-explore-mapview-mapcamera-setfarplaneconfiguration</a>(<wbr/>Map&lt;<wbr/>double, <a href="../mapview/MapCameraFarPlaneConfiguration-class.html">/sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-class</a>&gt; configs)
    → void

</dt>
<dd>
  Sets far plane distance configs per zoom level.
  

</dd>
<dt class="callable" id="setOrientationAtTarget">
<a href="../mapview/MapCamera/setOrientationAtTarget.html">/sdk-for-flutter-explore-mapview-mapcamera-setorientationattarget</a>(<wbr/><a href="../core/GeoOrientationUpdate-class.html">/sdk-for-flutter-explore-core-geoorientationupdate-class</a> orientation)
    → void

</dt>
<dd>
  Changes camera orientation in relation to target location.
  

</dd>
<dt class="callable" id="startAnimation">
<a href="../mapview/MapCamera/startAnimation.html">/sdk-for-flutter-explore-mapview-mapcamera-startanimation</a>(<wbr/><a href="../mapview/MapCameraAnimation-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimation-class</a> cameraAnimation)
    → void

</dt>
<dd>
  Starts a given camera animation.
  

</dd>
<dt class="callable" id="startAnimationWithListener">
<a href="../mapview/MapCamera/startAnimationWithListener.html">/sdk-for-flutter-explore-mapview-mapcamera-startanimationwithlistener</a>(<wbr/><a href="../mapview/MapCameraAnimation-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimation-class</a> cameraAnimation, <a href="../animation/AnimationListener-class.html">/sdk-for-flutter-explore-animation-animationlistener-class</a> animationListener)
    → void

</dt>
<dd>
  Starts a given camera animation.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapCamera/toString.html">/sdk-for-flutter-explore-mapview-mapcamera-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="zoomBy">
<a href="../mapview/MapCamera/zoomBy.html">/sdk-for-flutter-explore-mapview-mapcamera-zoomby</a>(<wbr/>double factor, <a href="../core/Point2D-class.html">/sdk-for-flutter-explore-core-point2d-class</a> origin)
    → void

</dt>
<dd>
  Zooms in or out by a specified factor.
  

</dd>
<dt class="callable" id="zoomTo">
<a href="../mapview/MapCamera/zoomTo.html">/sdk-for-flutter-explore-mapview-mapcamera-zoomto</a>(<wbr/>double zoomLevel)
    → void

</dt>
<dd>
  Zooms to the specified zoom level.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../mapview/MapCamera/operator_equals.html">/sdk-for-flutter-explore-mapview-mapcamera-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">MapCamera class</li>
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
