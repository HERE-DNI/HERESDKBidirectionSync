---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-classes-mapcamera"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapCamera.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapCamera"></a>
<a title="MapCamera Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapCamera Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapCamera</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapCamera</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCamera</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCamera</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
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
<p>The current camera state can be obtained by the <code><a href="../Classes/MapCamera.html#/s:7heresdk9MapCameraC5stateAC5StateVvp">MapCamera.state</a></code> call. It contains information about the camera look-at target (geo-coordinates and orientation) in geodetic space.
The values are returned for the current <code>principal point</code>. This can lead to surprising or unexpected values in cases where the camera position/orientation was specified for another screen point,
e.g. when using <code>MapCameraUpdateFactory.lookAt(GeoBox)</code> with a view rectangle, whose center does not coincide with the <code>principal point</code>.  In this case, the geo-coordinates of the
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
<table><thead>
<tr>
<th>zoom-level</th>
<th style="text-align: center">~ scale on screen (130dpi)</th>
<th style="text-align: center">width of the equator in logical pixels</th>
<th style="text-align: center">what can be seen</th>
</tr>
</thead><tbody>
<tr>
<td>0</td>
<td style="text-align: center">1:800 million</td>
<td style="text-align: center">256</td>
<td style="text-align: center">Earth</td>
</tr>
<tr>
<td>1</td>
<td style="text-align: center">1:400 million</td>
<td style="text-align: center">512</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>2</td>
<td style="text-align: center">1:200 million</td>
<td style="text-align: center">1024</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>3</td>
<td style="text-align: center">1:100 million</td>
<td style="text-align: center">2048</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>4</td>
<td style="text-align: center">1:50 million</td>
<td style="text-align: center">4096</td>
<td style="text-align: center">A continent</td>
</tr>
<tr>
<td>5</td>
<td style="text-align: center">1:25 million</td>
<td style="text-align: center">8192</td>
<td style="text-align: center">Large roads</td>
</tr>
<tr>
<td>6</td>
<td style="text-align: center">1:12 million</td>
<td style="text-align: center">16384</td>
<td style="text-align: center">Large rivers</td>
</tr>
<tr>
<td>7</td>
<td style="text-align: center">1:6 million</td>
<td style="text-align: center">32768</td>
<td style="text-align: center">A country</td>
</tr>
<tr>
<td>8</td>
<td style="text-align: center">1:3 million</td>
<td style="text-align: center">65536</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>9</td>
<td style="text-align: center">1:1 million</td>
<td style="text-align: center">131072</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>10</td>
<td style="text-align: center">1:780 thousand</td>
<td style="text-align: center">262144</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>11</td>
<td style="text-align: center">1:390 thousand</td>
<td style="text-align: center">524288</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>12</td>
<td style="text-align: center">1:195 thousand</td>
<td style="text-align: center">1048576</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>13</td>
<td style="text-align: center">1:100 thousand</td>
<td style="text-align: center">2097152</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>14</td>
<td style="text-align: center">1:50 thousand</td>
<td style="text-align: center">4194304</td>
<td style="text-align: center">A city</td>
</tr>
<tr>
<td>15</td>
<td style="text-align: center">1:25 thousand</td>
<td style="text-align: center">8388608</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>16</td>
<td style="text-align: center">1:12 thousand</td>
<td style="text-align: center">16777216</td>
<td style="text-align: center">Buildings</td>
</tr>
<tr>
<td>17</td>
<td style="text-align: center">1:6 thousand</td>
<td style="text-align: center">33554432</td>
<td style="text-align: center">Landmarks</td>
</tr>
<tr>
<td>18</td>
<td style="text-align: center">1:3 thousand</td>
<td style="text-align: center">67108864</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>19</td>
<td style="text-align: center">1:1 thousand</td>
<td style="text-align: center">134217728</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>20</td>
<td style="text-align: center">1:7 hundred</td>
<td style="text-align: center">268435456</td>
<td style="text-align: center">Streets</td>
</tr>
<tr>
<td>21</td>
<td style="text-align: center">1:3 hundred</td>
<td style="text-align: center">536870912</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>22</td>
<td style="text-align: center">1:1 hundred</td>
<td style="text-align: center">1073741824</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>23</td>
<td style="text-align: center">1:95</td>
<td style="text-align: center">2147483648</td>
<td style="text-align: center"></td>
</tr>
</tbody></table>
<p><i>Orientation</i></p>
<p>The camera <code>orientation</code> is composed of two parts:</p>
<ul>
<li><code>bearing</code>: also known as azimuth, the view direction in clockwise degrees; 0° = north, 90° = east, 180° = south, 270° = west</li>
<li><code>tilt</code>: the angle in degrees from the vertical that the camera is looking down at the Earth; 0° = straight down.</li>
</ul>
<p><i>Changing the Camera</i></p>
<p>All changes to the camera are encapsulated in camera updates that are created using the methods in the <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraupdatefactory">MapCameraUpdateFactory</a></code> class.</p>
<p>These updates can then be applied to the <code><a href="sdk-for-ios-explore-api-reference-..-classes-heremap">HereMap</a></code> using <code><a href="../Classes/MapCamera.html#/s:7heresdk9MapCameraC11applyUpdateyyAA0bcE0CF">MapCamera.applyUpdate(...)</a></code>.</p>
<p>Camera updates are queued and executed when the next frame is rendered. They are executed in the order in which they were applied.</p>
<p><i>Animating the Camera</i></p>
<p>Camera updates can be animated by first creating a camera animation using the methods in the <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraanimationfactory">MapCameraAnimationFactory</a></code> class and then applying this
animation to the <code><a href="sdk-for-ios-explore-api-reference-..-classes-heremap">HereMap</a></code> using <code>MapCamera.startAnimation(MapCameraAnimation, AnimationDelegate)</code>.</p>
<p>Only one camera animation for one camera component at a time is supported. Applying a new animation will cancel the active animation before the new one is started.
The start position in this case is where ever the active animation happened to be at the time. Different components are camera state (<code>target pose</code> and <code>distance/zoom level/scale</code>)
and camera projection (<code>field of view</code>, <code>focal length</code> and <code>principal point</code>).</p>
<p>The running animations can also be canceled using <code><a href="../Classes/MapCamera.html#/s:7heresdk9MapCameraC16cancelAnimationsyyF">MapCamera.cancelAnimations(...)</a></code> or individual ones using <code><a href="../Classes/MapCamera.html#/s:7heresdk9MapCameraC15cancelAnimationyyAA0bcE0CF">MapCamera.cancelAnimation(...)</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC03DryC13UpdateHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/DryCameraUpdateHandler"></a>
<a class="token" href="#/s:7heresdk9MapCameraC03DryC13UpdateHandlera">DryCameraUpdateHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Used to report back results of dry update application to camera.</p>
<p>Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">DryCameraUpdateHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">cameraState</span><span class="p">:</span> <span class="kt">MapCamera</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcamera-state">State</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>cameraState</em>
</code>
</td>
<td>
<div>
<p>Map camera state after dry application of update</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC5stateAC5StateVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/state"></a>
<a class="token" href="#/s:7heresdk9MapCameraC5stateAC5StateVvp">state</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Current state of the camera that reflects what is currently drawn by the map view.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">state</span><span class="p">:</span> <span class="kt">MapCamera</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcamera-state">State</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC14principalPointAA7Point2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/principalPoint"></a>
<a class="token" href="#/s:7heresdk9MapCameraC14principalPointAA7Point2DVvp">principalPoint</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Determines the pixel point where the target is placed within the map view. Setting a new
principal point instantly moves the map to render the current target coordinates
at the new principal point.
By default, the principal point is located at the center of the map view.
It is set in pixels relative to the map view’s origin top-left (0, 0).
Values outside the map view’s dimensions (x &lt; 0 || x &gt; width, y &lt; 0 || y &gt; height)
will be rejected silently and the current principal point is kept.</p>
<p>The value of the principal point is adjusted when the dimensions of the
map view change, so that it stays in the same point relative to width
and height. Meaning that when a principal point it set to bottom
middle of the map view, it will stay in the bottom middle regardless
of the changes to dimensions and orientation of the view.</p>
<p>Note: The principal point affects all programmatical map transformations (rotate, orbit, tilt and zoom)
and the two-finger-pan gesture to tilt the map. Other gestures, like pinch-rotate,
are not affected.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">principalPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-point2d">Point2D</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC11boundingBoxAA03GeoE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/boundingBox"></a>
<a class="token" href="#/s:7heresdk9MapCameraC11boundingBoxAA03GeoE0VSgvp">boundingBox</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Currently visible map area encompassed in a GeoBox.
Note that this bounding box is always rectangular, and its sides are always
parallel to the latitude and longitude. If the camera is rotated, the returned
bounding box will be a circumscribed rectangle that is larger than the
visible map area. Similarly, when the map is tilted (for example, if
the map is tilted by 45 degrees), the visible map area represents
a trapezoidal area in the world. Resulting value will then be a larger
circumscribed rectangle that contains this trapezoid area.
Because on this, corners of the resulting bounding box may be located
outside of the currently visible area.</p>
<p>When the map area does not fully fill the viewport, <code>nil</code> is returned.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">boundingBox</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geobox">GeoBox</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC6limitsAA0bC6LimitsCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/limits"></a>
<a class="token" href="#/s:7heresdk9MapCameraC6limitsAA0bC6LimitsCvp">limits</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Controls limits for the camera settings.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">limits</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameralimits">MapCameraLimits</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC5StateV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/State"></a>
<a class="token" href="#/s:7heresdk9MapCameraC5StateV">State</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Encapsulates state of the camera.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-mapcamera-state">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">State</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC21FarPlaneConfigurationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/FarPlaneConfiguration"></a>
<a class="token" href="#/s:7heresdk9MapCameraC21FarPlaneConfigurationV">FarPlaneConfiguration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Far plane distance configuration for a zoom level.</p>
<p>Effective far plane is computed from both parameters as:
farPlaneInMeters = max(
minDistanceInMeters,
distanceToTargetInMeters * distanceFactor
)</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-mapcamera-farplaneconfiguration">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">FarPlaneConfiguration</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC24setFarPlaneConfigurationyySDySdAC0efG0VGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setFarPlaneConfiguration(_:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC24setFarPlaneConfigurationyySDySdAC0efG0VGF">setFarPlaneConfiguration(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets far plane distance configs per zoom level.</p>
<p>Values are linearly interpolated between provided zoom levels.
For z between z0 and z1:
t = (z - z0) / (z1 - z0)
distanceFactor(z) = lerp(distanceFactor0, distanceFactor1, t)
minDistance(z) = lerp(minDistance0, minDistance1, t)</p>
<p>Effective far plane for the current frame is:
farPlaneInMeters = max(
minDistance(z),
distanceToTargetInMeters * distanceFactor(z)
)</p>
<p>Sample Configuration (balanced quality/performance, tune per zoom level):
14.4  -&gt; FarPlaneConfiguration(1.3)
18.34 -&gt; FarPlaneConfiguration(2.0)
19.60 -&gt; FarPlaneConfiguration(1.3)
minDistanceInMeters remains default in this case.
Passing an empty map clears the per-zoom override and restores the default behavior.
Non-finite zoom levels or values are ignored. Distance factors are clamped to 0.1 to 10.0.
The minimum distance is clamped to a range of [100, 3000] meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setFarPlaneConfiguration</span><span class="p">(</span><span class="n">_</span> <span class="nv">configs</span><span class="p">:</span> <span class="p">[</span><span class="kt">Double</span> <span class="p">:</span> <span class="kt">MapCamera</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcamera-farplaneconfiguration">FarPlaneConfiguration</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>configs</em>
</code>
</td>
<td>
<div>
<p>Per-zoom override mapping from zoom level to distance configuration.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC11addDelegateyyAA0bcE0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC11addDelegateyyAA0bcE0_pF">addDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a delegate to this camera that will be notified on the main thread
every time the map is redrawn with new camera parameters.</p>
<p>Adding the same delegate multiple times has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-mapcameradelegate">MapCameraDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The delegate to add.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC14removeDelegateyyAA0bcE0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC14removeDelegateyyAA0bcE0_pF">removeDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes the delegate from the camera.</p>
<p>Trying to remove a delegate that is not
currently registered has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-mapcameradelegate">MapCameraDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>Delegate to be removed from receiving state notifications.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC15removeDelegatesyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeDelegates()"></a>
<a class="token" href="#/s:7heresdk9MapCameraC15removeDelegatesyyF">removeDelegates()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all registered delegates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeDelegates</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC11applyUpdateyyAA0bcE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/applyUpdate(_:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC11applyUpdateyyAA0bcE0CF">applyUpdate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Applies camera update to the map camera.</p>
<p>Any ongoing camera animations will be cancelled and the corresponding camera animation delegate will be notified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">applyUpdate</span><span class="p">(</span><span class="n">_</span> <span class="nv">cameraUpdate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraupdate">MapCameraUpdate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>cameraUpdate</em>
</code>
</td>
<td>
<div>
<p>The update that gets applied to camera.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC14dryApplyUpdate_10completionyAA0bcF0C_yAC5StateVSgctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/dryApplyUpdate(_:completion:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC14dryApplyUpdate_10completionyAA0bcF0C_yAC5StateVSgctF">dryApplyUpdate(_:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Computes result of applying camera update without changing state of the map camera.</p>
<p>Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">dryApplyUpdate</span><span class="p">(</span><span class="n">_</span> <span class="nv">cameraUpdate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraupdate">MapCameraUpdate</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt">MapCamera</span><span class="o">.</span><span class="kt"><a href="../Classes/MapCamera.html#/s:7heresdk9MapCameraC03DryC13UpdateHandlera">DryCameraUpdateHandler</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>cameraUpdate</em>
</code>
</td>
<td>
<div>
<p>The update that gets dryly applied to camera.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Called upon completion with computed map state.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC14startAnimationyyAA0bcE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/startAnimation(_:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC14startAnimationyyAA0bcE0CF">startAnimation(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Starts a given camera animation.</p>
<p>Starting an animation can cause the cancelling of an ongoing animation when they both affect the same category of camera properties,
like for example any of the look-at properties (target, orientation, map measure) or any of the projection properties (field of view, principal point, focal length).
The corresponding delegate of an ongoing animation will be notified about the cancellation in these cases.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">startAnimation</span><span class="p">(</span><span class="n">_</span> <span class="nv">cameraAnimation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraanimation">MapCameraAnimation</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>cameraAnimation</em>
</code>
</td>
<td>
<div>
<p>The animation to be started.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_ptF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/startAnimation(_:animationDelegate:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_ptF">startAnimation(_:<wbr/>animationDelegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Starts a given camera animation. The state of the animation can be tracked with the provided listener.</p>
<p>Starting an animation can cause the cancelling of an ongoing animation when they both affect the same category of camera properties,
like for example any of the look-at properties (target, orientation, map measure) or any of the projection properties (field of view, principal point, focal length).
The corresponding delegate of an ongoing animation will be notified about the cancellation in these cases.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">startAnimation</span><span class="p">(</span><span class="n">_</span> <span class="nv">cameraAnimation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraanimation">MapCameraAnimation</a></span><span class="p">,</span> <span class="nv">animationDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-animationdelegate">AnimationDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>cameraAnimation</em>
</code>
</td>
<td>
<div>
<p>The animation to be started.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>animationDelegate</em>
</code>
</td>
<td>
<div>
<p>Animation delegate. A strong reference is kept internally up until the animation gets cancelled or completed.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC15cancelAnimationyyAA0bcE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/cancelAnimation(_:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC15cancelAnimationyyAA0bcE0CF">cancelAnimation(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Cancels an ongoing camera animation.</p>
<p>Upon cancellation, the corresponding delegate will be notified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">cancelAnimation</span><span class="p">(</span><span class="n">_</span> <span class="nv">cameraAnimation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraanimation">MapCameraAnimation</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>cameraAnimation</em>
</code>
</td>
<td>
<div>
<p>The animation to be cancelled.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC16cancelAnimationsyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/cancelAnimations()"></a>
<a class="token" href="#/s:7heresdk9MapCameraC16cancelAnimationsyyF">cancelAnimations()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Cancels any ongoing camera animation.</p>
<p>Upon cancellation, the corresponding delegate of any cancelled animation will be notified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">cancelAnimations</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC7orbitBy_6aroundyAA20GeoOrientationUpdateV_AA7Point2DVtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/orbitBy(_:around:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC7orbitBy_6aroundyAA20GeoOrientationUpdateV_AA7Point2DVtF">orbitBy(_:<wbr/>around:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Orbits the camera around a specified view point by increasing tilt and bearing by specified
delta values.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">orbitBy</span><span class="p">(</span><span class="n">_</span> <span class="nv">delta</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">,</span> <span class="n">around</span> <span class="nv">origin</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-point2d">Point2D</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delta</em>
</code>
</td>
<td>
<div>
<p>Camera orientation change, containing tilt and bearing angle deltas.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>origin</em>
</code>
</td>
<td>
<div>
<p>Pixel point in view coordinates around which orbiting occurs.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC6zoomBy_6aroundySd_AA7Point2DVtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/zoomBy(_:around:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC6zoomBy_6aroundySd_AA7Point2DVtF">zoomBy(_:<wbr/>around:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Zooms in or out by a specified factor.</p>
<p>This effectively changes the distance from the camera to the <code><a href="../Classes/MapCamera/State.html#/s:7heresdk9MapCameraC5StateV17targetCoordinatesAA03GeoF0Vvp">MapCamera.State.targetCoordinates</a></code>
by the specified factor, which changes <code><a href="../Classes/MapCamera/State.html#/s:7heresdk9MapCameraC5StateV9zoomLevelSdvp">MapCamera.State.zoomLevel</a></code> as well.</p>
<p>Values above 1.0 will zoom in and values below will zoom out.</p>
<p>The relation with <code><a href="../Classes/MapCamera/State.html#/s:7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp">MapCamera.State.distanceToTargetInMeters</a></code> is inversely linear,
meaning that zooming by 4 will decrease distance to target by 4 while zooming by 0.5
will increase distance to target by 2.</p>
<p>The relation with zoom level is logarithmic. Meaning that zooming by a factor of 4 will
increase zoom level by 2 (because log2(4) == 2). So to zoom in by X zoom levels, the zoom
factor needs to be 2^X. To zoom out by X zoom levels, zoom factor needs to be 1/(2^X).</p>
<p>The zooming occurs around the specified origin inside the view.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">zoomBy</span><span class="p">(</span><span class="n">_</span> <span class="nv">factor</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="n">around</span> <span class="nv">origin</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-point2d">Point2D</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>factor</em>
</code>
</td>
<td>
<div>
<p>The zoom factor. Values above 1.0 will zoom in and values below will zoom out.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>origin</em>
</code>
</td>
<td>
<div>
<p>Pixel point in view coordinates around which zooming occurs.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC6zoomTo0D5LevelySd_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/zoomTo(zoomLevel:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC6zoomTo0D5LevelySd_tF">zoomTo(zoomLevel:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Zooms to the specified zoom level. The supplied value will be clamped to the range
of [0, 22], where 0 is a view of whole globe and 22 is street level.</p>
<p>This effectively changes the distance from the camera to the target.
The zooming occurs around the current target point.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">zoomTo</span><span class="p">(</span><span class="nv">zoomLevel</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>zoomLevel</em>
</code>
</td>
<td>
<div>
<p>The zoom level to set, clamped to the range of [0, 22].</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC6lookAt5pointyAA14GeoCoordinatesV_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(point:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC6lookAt5pointyAA14GeoCoordinatesV_tF">lookAt(point:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Makes the camera look at a new geodetic target, while
preserving the current orientation and distance to the target.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">point</span> <span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>Geodetic coordinates at which the camera will point.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC6lookAt5point4zoomyAA14GeoCoordinatesV_AA0B7MeasureVtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(point:zoom:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC6lookAt5point4zoomyAA14GeoCoordinatesV_AA0B7MeasureVtF">lookAt(point:<wbr/>zoom:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Makes the camera look at the geodetic target with the given zoom.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">point</span> <span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">zoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-mapmeasure">MapMeasure</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>Geodetic coordinates at which the camera will point.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>zoom</em>
</code>
</td>
<td>
<div>
<p>The zoom level which can be provided as distance to the target point, scale or
zoom level.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC6lookAt5point11orientation4zoomyAA14GeoCoordinatesV_AA0I17OrientationUpdateVAA0B7MeasureVtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(point:orientation:zoom:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC6lookAt5point11orientation4zoomyAA14GeoCoordinatesV_AA0I17OrientationUpdateVAA0B7MeasureVtF">lookAt(point:<wbr/>orientation:<wbr/>zoom:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Makes the camera look at the geodetic target with the given zoom and orientation.</p>
<p>The supplied orientation is the orientation of the camera looking
at the target, so the resulting camera state will have the
same orientation as the one supplied to this method.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">point</span> <span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">orientation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">,</span> <span class="nv">zoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-mapmeasure">MapMeasure</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>Geodetic coordinates at which the camera will point.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>orientation</em>
</code>
</td>
<td>
<div>
<p>Desired orientation of the camera.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>zoom</em>
</code>
</td>
<td>
<div>
<p>The zoom level which can be provided as distance to the target point, scale or
zoom level.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC6lookAt4area11orientationyAA6GeoBoxV_AA0H17OrientationUpdateVtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(area:orientation:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC6lookAt4area11orientationyAA6GeoBoxV_AA0H17OrientationUpdateVtF">lookAt(area:<wbr/>orientation:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Makes the camera look at the specified geodetic area.</p>
<p>The supplied orientation is the orientation of the camera looking
at the target, so the resulting camera state will have the
same orientation as the one supplied to this method.</p>
<p>The altitude of the target points is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">area</span> <span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geobox">GeoBox</a></span><span class="p">,</span> <span class="nv">orientation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>Geodetic area at which the camera will point</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>orientation</em>
</code>
</td>
<td>
<div>
<p>Desired orientation of the camera</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC6lookAt4area11orientation13viewRectangleyAA6GeoBoxV_AA0J17OrientationUpdateVAA11Rectangle2DVtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(area:orientation:viewRectangle:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC6lookAt4area11orientation13viewRectangleyAA6GeoBoxV_AA0J17OrientationUpdateVAA11Rectangle2DVtF">lookAt(area:<wbr/>orientation:<wbr/>viewRectangle:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Makes the camera look at the specified geodetic area and pass a rectangle which specifies
where the area should appear inside of the map view.</p>
<p>The supplied orientation is the orientation of the camera looking
at the target, so the resulting camera state will have the
same orientation as the one supplied to this method. Please note that
the resulting orientation might deviate from the provided orientation.
This is particularly the case if a large geobox on world level and a
view rectangle which is relatively small was passed to the method.</p>
<p>The altitude of the target points is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">area</span> <span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geobox">GeoBox</a></span><span class="p">,</span> <span class="nv">orientation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">,</span> <span class="nv">viewRectangle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-rectangle2d">Rectangle2D</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>Geodetic area which will be shown in the viewRectangle.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>orientation</em>
</code>
</td>
<td>
<div>
<p>Desired orientation of the camera.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>viewRectangle</em>
</code>
</td>
<td>
<div>
<p>The view rectangle in viewport pixel coordinates inside which the geographical target
area is displayed.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC19setDistanceToTarget16distanceInMetersySd_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setDistanceToTarget(distanceInMeters:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC19setDistanceToTarget16distanceInMetersySd_tF">setDistanceToTarget(distanceInMeters:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Makes the camera look at current target from certain distance</p>
<p>This function neither modifies target coordinates nor target orientation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setDistanceToTarget</span><span class="p">(</span><span class="nv">distanceInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>distanceInMeters</em>
</code>
</td>
<td>
<div>
<p>Distance in meters to the target point.
Minimal distance value is clamped to 100 meters.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC22setOrientationAtTargetyyAA03GeoE6UpdateVF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setOrientationAtTarget(_:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC22setOrientationAtTargetyyAA03GeoE6UpdateVF">setOrientationAtTarget(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Changes camera orientation in relation to target location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setOrientationAtTarget</span><span class="p">(</span><span class="n">_</span> <span class="nv">orientation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>orientation</em>
</code>
</td>
<td>
<div>
<p>Desired orientation of the camera.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>
