---
title: "MapCamera (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapcamera"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapCamera.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapCamera</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapCamera</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents the camera looking onto the map view.
 Each map instance has exactly one camera that is used to manipulate
 the way the map is displayed.
 Any updates to the state of the camera will be applied while drawing the next map view frame
 and the current state of the camera reflects what is currently drawn inside the map view.
 Note: The camera can be configured and positioned even before a map scene is loaded for the first time.
 This allows for pre-setting the desired camera position, orientation, and zoom level, which will be
 applied once the map scene becomes available.
 <b>Camera Model</b>
<i>Camera Concepts and Units</i>
By default, HERE SDK uses an idealized Earth globe with a 3D-capable camera model. Being a 3D camera model means that the
 world position can be freely specified in geodetic 3D space (i.e. Earth centric) and the orientation can be freely changed around
 two axes - bearing (also known as head) and tilt (also known as pitch).
 The camera supports the look-at target with orientation on the ground way of setting up the camera in space. The camera is placed
 so that it looks at a specific geo-coordinates (placed at the <code>principal point</code>) from a given orientation and distance.
 <ul>
<li>the look-at target in geo-coordinates (latitude, longitude) in degrees and an <code>altitude</code> in meters above MSL (mean sea level) at the <code>principal point</code></li>
<li>the <code>orientation</code> at the look-at target</li>
<li>the distance of the camera from the look-at target, given as <code>distance</code> in meters or as <code>zoom-level</code></li>
</ul>
<i>Getting the current camera state</i>
The current camera state can be obtained by the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera#getState()"><code>getState()</code></a> call. It contains information about the camera look-at target (geo-coordinates and orientation) in geodetic space.
 The values are returned for the current <code>principal point</code>. This can lead to surprising or unexpected values in cases where the camera position/orientation was specified for another screen point,
 e.g. when using <a href="sdk-for-android-navigate-mapcameraupdatefactory#lookAt(com.here.sdk.core.GeoBox)"><code>MapCameraUpdateFactory.lookAt(GeoBox)</code></a> with a view rectangle, whose center does not coincide with the <code>principal point</code>.  In this case, the geo-coordinates of the
 look-at target will differ from the center of the geo-box used in the <code>lookAt</code> call.
 <i>Geo coordinates</i>
Geo-coordinates are given in degrees and follow the common nomenclature of positive northern latitudes and positive eastern longitudes.
 <i>Altitude</i>
When <code>altitude</code> is specified, it is always in meters above mean sea level (MSL).
 If this value is invalid (not-a-number) or not specified, then the terrain height at the given geo-coordinates will be looked up from the map.
 This is especially interesting in cases where terrain elevation is used within the map display.
 <i>Distance vs zoom-level vs scale</i>
Map camera <code>distance</code>, <code>zoom-level</code> and <code>scale</code> determine how much of the world is visible on the HERE map. <code>Distance</code>, <code>zoom-level</code> and <code>scale</code> are
 directly connected and changing one will automatically change the others as well (except for <code>distance</code>/<code>scale</code> changes that map to <code>zoom-level</code> values &lt; 0 or &gt; 23).
 <ul>
<li><code>distance</code>: the distance from the camera to the look-at target on the surface of the Earth, in meters</li>
<li><code>zoom-level</code>: the map zoom level, in the range [0, 3]. The relation between the width of the equator in logical pixels <code>w</code> and the zoom level <code>z</code> is: <code>w = 256 * 2^(z)</code></li>
<li><code>scale</code>: the scale of the map at the look-at target in meters on screen per meters on Earth. So a scale of 0.001 shows 10 meters on Earth within 1 cm on screen.</li>
</ul>
The following mapping represents the <code>zoom-level</code> values:
 <table>
<thead>
<tr><th>zoom-level</th><th align="center">~ scale on screen (130dpi)</th><th align="center">width of the equator in logical pixels</th><th align="center">what can be seen</th></tr>
</thead>
<tbody>
<tr><td>0</td><td align="center">1:800 million</td><td align="center">256</td><td align="center">Earth</td></tr>
<tr><td>1</td><td align="center">1:400 million</td><td align="center">512</td><td align="center"> </td></tr>
<tr><td>2</td><td align="center">1:200 million</td><td align="center">1024</td><td align="center"> </td></tr>
<tr><td>3</td><td align="center">1:100 million</td><td align="center">2048</td><td align="center"> </td></tr>
<tr><td>4</td><td align="center">1:50 million</td><td align="center">4096</td><td align="center">A continent</td></tr>
<tr><td>5</td><td align="center">1:25 million</td><td align="center">8192</td><td align="center">Large roads</td></tr>
<tr><td>6</td><td align="center">1:12 million</td><td align="center">16384</td><td align="center">Large rivers</td></tr>
<tr><td>7</td><td align="center">1:6 million</td><td align="center">32768</td><td align="center">A country</td></tr>
<tr><td>8</td><td align="center">1:3 million</td><td align="center">65536</td><td align="center"> </td></tr>
<tr><td>9</td><td align="center">1:1 million</td><td align="center">131072</td><td align="center"> </td></tr>
<tr><td>10</td><td align="center">1:780 thousand</td><td align="center">262144</td><td align="center"> </td></tr>
<tr><td>11</td><td align="center">1:390 thousand</td><td align="center">524288</td><td align="center"> </td></tr>
<tr><td>12</td><td align="center">1:195 thousand</td><td align="center">1048576</td><td align="center"> </td></tr>
<tr><td>13</td><td align="center">1:100 thousand</td><td align="center">2097152</td><td align="center"> </td></tr>
<tr><td>14</td><td align="center">1:50 thousand</td><td align="center">4194304</td><td align="center">A city</td></tr>
<tr><td>15</td><td align="center">1:25 thousand</td><td align="center">8388608</td><td align="center"> </td></tr>
<tr><td>16</td><td align="center">1:12 thousand</td><td align="center">16777216</td><td align="center">Buildings</td></tr>
<tr><td>17</td><td align="center">1:6 thousand</td><td align="center">33554432</td><td align="center">Landmarks</td></tr>
<tr><td>18</td><td align="center">1:3 thousand</td><td align="center">67108864</td><td align="center"> </td></tr>
<tr><td>19</td><td align="center">1:1 thousand</td><td align="center">134217728</td><td align="center"> </td></tr>
<tr><td>20</td><td align="center">1:7 hundred</td><td align="center">268435456</td><td align="center">Streets</td></tr>
<tr><td>21</td><td align="center">1:3 hundred</td><td align="center">536870912</td><td align="center"> </td></tr>
<tr><td>22</td><td align="center">1:1 hundred</td><td align="center">1073741824</td><td align="center"> </td></tr>
<tr><td>23</td><td align="center">1:95</td><td align="center">2147483648</td><td align="center"> </td></tr>
</tbody>
</table>
<i>Orientation</i>
The camera <code>orientation</code> is composed of two parts:
 <ul>
<li><code>bearing</code>: also known as azimuth, the view direction in clockwise degrees; 0° = north, 90° = east, 180° = south, 270° = west</li>
<li><code>tilt</code>: the angle in degrees from the vertical that the camera is looking down at the Earth; 0° = straight down.</li>
</ul>
<i>Changing the Camera</i>
All changes to the camera are encapsulated in camera updates that are created using the methods in the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdatefactory" title="class in com.here.sdk.mapview"><code>MapCameraUpdateFactory</code></a> class.
 These updates can then be applied to the <a href="sdk-for-android-navigate-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview"><code>HereMap</code></a> using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera#applyUpdate(com.here.sdk.mapview.MapCameraUpdate)"><code>applyUpdate(com.here.sdk.mapview.MapCameraUpdate)</code></a>.
 Camera updates are queued and executed when the next frame is rendered. They are executed in the order in which they were applied.
 <i>Animating the Camera</i>
Camera updates can be animated by first creating a camera animation using the methods in the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimationfactory" title="class in com.here.sdk.mapview"><code>MapCameraAnimationFactory</code></a> class and then applying this
 animation to the <a href="sdk-for-android-navigate-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview"><code>HereMap</code></a> using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera#startAnimation(com.here.sdk.mapview.MapCameraAnimation,com.here.sdk.animation.AnimationListener)"><code>startAnimation(MapCameraAnimation, AnimationListener)</code></a>.
 Only one camera animation for one camera component at a time is supported. Applying a new animation will cancel the active animation before the new one is started.
 The start position in this case is where ever the active animation happened to be at the time. Different components are camera state (<code>target pose</code> and <code>distance/zoom level/scale</code>)
 and camera projection (<code>field of view</code>, <code>focal length</code> and <code>principal point</code>).
 The running animations can also be canceled using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera#cancelAnimations()"><code>cancelAnimations()</code></a> or individual ones using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera#cancelAnimation(com.here.sdk.mapview.MapCameraAnimation)"><code>cancelAnimation(com.here.sdk.mapview.MapCameraAnimation)</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static interface </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera-drycameraupdatecallback" title="interface in com.here.sdk.mapview">MapCamera.DryCameraUpdateCallback</a></code></div>
<div className="col-last even-row-color">
<div className="block">Used to report back results of dry update application to camera.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera-farplaneconfiguration" title="class in com.here.sdk.mapview">MapCamera.FarPlaneConfiguration</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Far plane distance configuration for a zoom level.</div>
</div>
<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera-state" title="class in com.here.sdk.mapview">MapCamera.State</a></code></div>
<div className="col-last even-row-color">
<div className="block">Encapsulates state of the camera.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="setFarPlaneConfiguration(java.util.Map)">
<h3>setFarPlaneConfiguration</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setFarPlaneConfiguration</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera-farplaneconfiguration" title="class in com.here.sdk.mapview">MapCamera.FarPlaneConfiguration</a>&gt; configs)</span></div>
<div className="block"><p>Sets far plane distance configs per zoom level.
 Values are linearly interpolated between provided zoom levels.
 For z between z0 and z1:
 t = (z - z0) / (z1 - z0)
 distanceFactor(z) = lerp(distanceFactor0, distanceFactor1, t)
 minDistance(z) = lerp(minDistance0, minDistance1, t)
 Effective far plane for the current frame is:
 farPlaneInMeters = max(
 minDistance(z),
 distanceToTargetInMeters * distanceFactor(z)
 )
 Sample Configuration (balanced quality/performance, tune per zoom level):
 14.4  -&gt; FarPlaneConfiguration(1.3)
 18.34 -&gt; FarPlaneConfiguration(2.0)
 19.60 -&gt; FarPlaneConfiguration(1.3)
 minDistanceInMeters remains default in this case.
 Passing an empty map clears the per-zoom override and restores the default behavior.
 Non-finite zoom levels or values are ignored. Distance factors are clamped to 0.1 to 10.0.
 The minimum distance is clamped to a range of [100, 3000] meters.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>configs</code> - <p>Per-zoom override mapping from zoom level to distance configuration.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addListener(com.here.sdk.mapview.MapCameraListener)">
<h3>addListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralistener" title="interface in com.here.sdk.mapview">MapCameraListener</a> listener)</span></div>
<div className="block"><p>Adds a listener to this camera that will be notified on the main thread
 every time the map is redrawn with new camera parameters.
 Adding the same listener multiple times has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>The listener to add.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeListener(com.here.sdk.mapview.MapCameraListener)">
<h3>removeListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralistener" title="interface in com.here.sdk.mapview">MapCameraListener</a> observer)</span></div>
<div className="block"><p>Removes the listener from the camera.
 Trying to remove a listener that is not
 currently registered has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>observer</code> - <p>Listener to be removed from receiving state notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeListeners()">
<h3>removeListeners</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeListeners</span>()</div>
<div className="block"><p>Removes all registered listeners.</p></div>
</section>
</li>
<li>
<section className="detail" id="applyUpdate(com.here.sdk.mapview.MapCameraUpdate)">
<h3>applyUpdate</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">applyUpdate</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a> cameraUpdate)</span></div>
<div className="block"><p>Applies camera update to the map camera.
 Any ongoing camera animations will be cancelled and the corresponding camera animation listener will be notified.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>cameraUpdate</code> - <p>The update that gets applied to camera.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="dryApplyUpdate(com.here.sdk.mapview.MapCameraUpdate,com.here.sdk.mapview.MapCamera.DryCameraUpdateCallback)">
<h3>dryApplyUpdate</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">dryApplyUpdate</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a> cameraUpdate,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera-drycameraupdatecallback" title="interface in com.here.sdk.mapview">MapCamera.DryCameraUpdateCallback</a> callback)</span></div>
<div className="block"><p>Computes result of applying camera update without changing state of the map camera.
 Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>cameraUpdate</code> - <p>The update that gets dryly applied to camera.</p></dd>
<dd><code>callback</code> - <p>Called upon completion with computed map state.
     callback is called on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="startAnimation(com.here.sdk.mapview.MapCameraAnimation)">
<h3>startAnimation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">startAnimation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a> cameraAnimation)</span></div>
<div className="block"><p>Starts a given camera animation.
 Starting an animation can cause the cancelling of an ongoing animation when they both affect the same category of camera properties,
 like for example any of the look-at properties (target, orientation, map measure) or any of the projection properties (field of view, principal point, focal length).
 The corresponding listener of an ongoing animation will be notified about the cancellation in these cases.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>cameraAnimation</code> - <p>The animation to be started.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="startAnimation(com.here.sdk.mapview.MapCameraAnimation,com.here.sdk.animation.AnimationListener)">
<h3>startAnimation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">startAnimation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a> cameraAnimation,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-animationlistener" title="interface in com.here.sdk.animation">AnimationListener</a> animationListener)</span></div>
<div className="block"><p>Starts a given camera animation. The state of the animation can be tracked with the provided listener.
 Starting an animation can cause the cancelling of an ongoing animation when they both affect the same category of camera properties,
 like for example any of the look-at properties (target, orientation, map measure) or any of the projection properties (field of view, principal point, focal length).
 The corresponding listener of an ongoing animation will be notified about the cancellation in these cases.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>cameraAnimation</code> - <p>The animation to be started.</p></dd>
<dd><code>animationListener</code> - <p>Animation listener. A strong reference is kept internally up until the animation gets cancelled or completed.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="cancelAnimation(com.here.sdk.mapview.MapCameraAnimation)">
<h3>cancelAnimation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">cancelAnimation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraanimation" title="class in com.here.sdk.mapview">MapCameraAnimation</a> cameraAnimation)</span></div>
<div className="block"><p>Cancels an ongoing camera animation.
 Upon cancellation, the corresponding listener will be notified.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>cameraAnimation</code> - <p>The animation to be cancelled.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="cancelAnimations()">
<h3>cancelAnimations</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">cancelAnimations</span>()</div>
<div className="block"><p>Cancels any ongoing camera animation.
 Upon cancellation, the corresponding listener of any cancelled animation will be notified.</p></div>
</section>
</li>
<li>
<section className="detail" id="orbitBy(com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Point2D)">
<h3>orbitBy</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">orbitBy</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> delta,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> origin)</span></div>
<div className="block"><p>Orbits the camera around a specified view point by increasing tilt and bearing by specified
 delta values.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>delta</code> - <p>Camera orientation change, containing tilt and bearing angle deltas.</p></dd>
<dd><code>origin</code> - <p>Pixel point in view coordinates around which orbiting occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="zoomBy(double,com.here.sdk.core.Point2D)">
<h3>zoomBy</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">zoomBy</span><wbr/><span className="parameters">(double factor,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> origin)</span></div>
<div className="block"><p>Zooms in or out by a specified factor.
 This effectively changes the distance from the camera to the <a href="sdk-for-android-navigate-mapcamera-state#targetCoordinates"><code>MapCamera.State.targetCoordinates</code></a>
 by the specified factor, which changes <a href="sdk-for-android-navigate-mapcamera-state#zoomLevel"><code>MapCamera.State.zoomLevel</code></a> as well.
 Values above 1.0 will zoom in and values below will zoom out.
 The relation with <a href="sdk-for-android-navigate-mapcamera-state#distanceToTargetInMeters"><code>MapCamera.State.distanceToTargetInMeters</code></a> is inversely linear,
 meaning that zooming by 4 will decrease distance to target by 4 while zooming by 0.5
 will increase distance to target by 2.
 The relation with zoom level is logarithmic. Meaning that zooming by a factor of 4 will
 increase zoom level by 2 (because log2(4) == 2). So to zoom in by X zoom levels, the zoom
 factor needs to be 2^X. To zoom out by X zoom levels, zoom factor needs to be 1/(2^X).
 The zooming occurs around the specified origin inside the view.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>factor</code> - <p>The zoom factor. Values above 1.0 will zoom in and values below will zoom out.</p></dd>
<dd><code>origin</code> - <p>Pixel point in view coordinates around which zooming occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="zoomTo(double)">
<h3>zoomTo</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">zoomTo</span><wbr/><span className="parameters">(double zoomLevel)</span></div>
<div className="block"><p>Zooms to the specified zoom level. The supplied value will be clamped to the range
 of [0, 22], where 0 is a view of whole globe and 22 is street level.
 This effectively changes the distance from the camera to the target.
 The zooming occurs around the current target point.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>zoomLevel</code> - <p>The zoom level to set, clamped to the range of [0, 22].</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAt(com.here.sdk.core.GeoCoordinates)">
<h3>lookAt</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> target)</span></div>
<div className="block"><p>Makes the camera look at a new geodetic target, while
 preserving the current orientation and distance to the target.
 The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>Geodetic coordinates at which the camera will point.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAt(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMeasure)">
<h3>lookAt</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom)</span></div>
<div className="block"><p>Makes the camera look at the geodetic target with the given zoom.
 The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>Geodetic coordinates at which the camera will point.</p></dd>
<dd><code>zoom</code> - <p>The zoom level which can be provided as distance to the target point, scale or
     zoom level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAt(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure)">
<h3>lookAt</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom)</span></div>
<div className="block"><p>Makes the camera look at the geodetic target with the given zoom and orientation.
 The supplied orientation is the orientation of the camera looking
 at the target, so the resulting camera state will have the
 same orientation as the one supplied to this method.
 The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>Geodetic coordinates at which the camera will point.</p></dd>
<dd><code>orientation</code> - <p>Desired orientation of the camera.</p></dd>
<dd><code>zoom</code> - <p>The zoom level which can be provided as distance to the target point, scale or
     zoom level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.GeoOrientationUpdate)">
<h3>lookAt</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation)</span></div>
<div className="block"><p>Makes the camera look at the specified geodetic area.
 The supplied orientation is the orientation of the camera looking
 at the target, so the resulting camera state will have the
 same orientation as the one supplied to this method.
 The altitude of the target points is ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>Geodetic area at which the camera will point</p></dd>
<dd><code>orientation</code> - <p>Desired orientation of the camera</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Rectangle2D)">
<h3>lookAt</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewRectangle)</span></div>
<div className="block"><p>Makes the camera look at the specified geodetic area and pass a rectangle which specifies
 where the area should appear inside of the map view.
 The supplied orientation is the orientation of the camera looking
 at the target, so the resulting camera state will have the
 same orientation as the one supplied to this method. Please note that
 the resulting orientation might deviate from the provided orientation.
 This is particularly the case if a large geobox on world level and a
 view rectangle which is relatively small was passed to the method.
 The altitude of the target points is ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>Geodetic area which will be shown in the viewRectangle.</p></dd>
<dd><code>orientation</code> - <p>Desired orientation of the camera.</p></dd>
<dd><code>viewRectangle</code> - <p>The view rectangle in viewport pixel coordinates inside which the geographical target
     area is displayed.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDistanceToTarget(double)">
<h3>setDistanceToTarget</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDistanceToTarget</span><wbr/><span className="parameters">(double distanceInMeters)</span></div>
<div className="block"><p>Makes the camera look at current target from certain distance
 This function neither modifies target coordinates nor target orientation.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>distanceInMeters</code> - <p>Distance in meters to the target point.
     Minimal distance value is clamped to 100 meters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setOrientationAtTarget(com.here.sdk.core.GeoOrientationUpdate)">
<h3>setOrientationAtTarget</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setOrientationAtTarget</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation)</span></div>
<div className="block"><p>Changes camera orientation in relation to target location.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>orientation</code> - <p>Desired orientation of the camera.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getState()">
<h3>getState</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera-state" title="class in com.here.sdk.mapview">MapCamera.State</a></span> <span className="element-name">getState</span>()</div>
<div className="block"><p>Gets state of the camera that reflects what is currently drawn inside the map view.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Current state of the camera that reflects what is currently drawn by the map view.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPrincipalPoint()">
<h3>getPrincipalPoint</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a></span> <span className="element-name">getPrincipalPoint</span>()</div>
<div className="block"><p>Gets the pixel point that determines where the target is placed within the map view.
 By default, the principal point is located at the center of the map view.
 The value of the principal point is adjusted when the dimensions of the
 map view change, so that it stays in the same point relative to width
 and height. Meaning that when a principal point it set to bottom
 middle of the map view, it will stay in the bottom middle regardless
 of the changes to dimensions and orientation of the view.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Determines the pixel point where the target is placed within the map view. Setting a new
     principal point instantly moves the map to render the current target coordinates
     at the new principal point.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setPrincipalPoint(com.here.sdk.core.Point2D)">
<h3>setPrincipalPoint</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setPrincipalPoint</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> value)</span></div>
<div className="block"><p>Sets the pixel point that determines where the target appears within the map view.
 This instantly moves the map to render the current target coordinates
 at the new principal point.
 By default, the principal point is located at the center of the map view.
 It is set in pixels relative to the map view's origin top-left (0, 0).
 Values outside the map view's dimensions (x &lt; 0 || x &gt; width, y &lt; 0 || y &gt; height)
 will be rejected silently and the current principal point is kept.
 The value of the principal point is adjusted when the dimensions of the
 map view change, so that it stays in the same point relative to width
 and height. Meaning that when a principal point it set to bottom
 middle of the map view, it will stay in the bottom middle regardless
 of the changes to dimensions and orientation of the view.
 Note: The principal point affects all programmatical map transformations (rotate, orbit, tilt and zoom)
 and the two-finger-pan gesture to tilt the map. Other gestures, like pinch-rotate,
 are not affected.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Determines the pixel point where the target is placed within the map view. Setting a new
     principal point instantly moves the map to render the current target coordinates
     at the new principal point.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">getBoundingBox</span>()</div>
<div className="block"><p>Gets the current visible map area encompassed in a GeoBox.
 Note that this bounding box is always rectangular, and its sides are always
 parallel to the latitude and longitude. If the camera is rotated, the returned
 bounding box will be a circumscribed rectangle that is larger than the
 visible map area. Similarly, when the map is tilted (for example, if
 the map is tilted by 45 degrees), the visible map area represents
 a trapezoidal area in the world. Resulting value will then be a larger
 circumscribed rectangle that contains this trapezoid area.
 Because on this, corners of the resulting bounding box may be located
 outside of the currently visible area.
 When the map area does not fully fill the viewport, <code>null</code> is returned.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Currently visible map area encompassed in a GeoBox.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLimits()">
<h3>getLimits</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits" title="class in com.here.sdk.mapview">MapCameraLimits</a></span> <span className="element-name">getLimits</span>()</div>
<div className="block"><p>Gets a MapCameraLimits instance that controls limits for the camera settings.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Controls limits for the camera settings.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
