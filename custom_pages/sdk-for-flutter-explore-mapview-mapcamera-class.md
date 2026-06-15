---
title: "MapCamera class abstract"
slug: "sdk-for-flutter-explore-mapview-mapcamera-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCamera-class.html -->


<div>
<h1>MapCamera class abstract</h1></div>

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
<p>The current camera state can be obtained by the <a href="sdk-for-flutter-explore-mapview-mapcamera-state">MapCamera.state</a> call. It contains information about the camera look-at target (geo-coordinates and orientation) in geodetic space.
The values are returned for the current <code>principal point</code>. This can lead to surprising or unexpected values in cases where the camera position/orientation was specified for another screen point,
e.g. when using <a href="sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatarea">MapCameraUpdateFactory.lookAtArea</a> with a view rectangle, whose center does not coincide with the <code>principal point</code>.  In this case, the geo-coordinates of the
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

</tr>
<tr>
<td>2</td>
<td align="center">1:200 million</td>
<td align="center">1024</td>

</tr>
<tr>
<td>3</td>
<td align="center">1:100 million</td>
<td align="center">2048</td>

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

</tr>
<tr>
<td>9</td>
<td align="center">1:1 million</td>
<td align="center">131072</td>

</tr>
<tr>
<td>10</td>
<td align="center">1:780 thousand</td>
<td align="center">262144</td>

</tr>
<tr>
<td>11</td>
<td align="center">1:390 thousand</td>
<td align="center">524288</td>

</tr>
<tr>
<td>12</td>
<td align="center">1:195 thousand</td>
<td align="center">1048576</td>

</tr>
<tr>
<td>13</td>
<td align="center">1:100 thousand</td>
<td align="center">2097152</td>

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

</tr>
<tr>
<td>19</td>
<td align="center">1:1 thousand</td>
<td align="center">134217728</td>

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

</tr>
<tr>
<td>22</td>
<td align="center">1:1 hundred</td>
<td align="center">1073741824</td>

</tr>
<tr>
<td>23</td>
<td align="center">1:95</td>
<td align="center">2147483648</td>

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
<p>All changes to the camera are encapsulated in camera updates that are created using the methods in the <a href="sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class">MapCameraUpdateFactory</a> class.</p>
<p>These updates can then be applied to the <a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-class">HereMapControllerCore</a> using <a href="sdk-for-flutter-explore-mapview-mapcamera-applyupdate">MapCamera.applyUpdate</a>.</p>
<p>Camera updates are queued and executed when the next frame is rendered. They are executed in the order in which they were applied.</p>
<p><i>Animating the Camera</i></p>
<p>Camera updates can be animated by first creating a camera animation using the methods in the <a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-class">MapCameraAnimationFactory</a> class and then applying this
animation to the <a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-class">HereMapControllerCore</a> using <a href="sdk-for-flutter-explore-mapview-mapcamera-startanimationwithlistener">MapCamera.startAnimationWithListener</a>.</p>
<p>Only one camera animation for one camera component at a time is supported. Applying a new animation will cancel the active animation before the new one is started.
The start position in this case is where ever the active animation happened to be at the time. Different components are camera state (<code>target pose</code> and <code>distance/zoom level/scale</code>)
and camera projection (<code>field of view</code>, <code>focal length</code> and <code>principal point</code>).</p>
<p>The running animations can also be canceled using <a href="sdk-for-flutter-explore-mapview-mapcamera-cancelanimations">MapCamera.cancelAnimations</a> or individual ones using <a href="sdk-for-flutter-explore-mapview-mapcamera-cancelanimation">MapCamera.cancelAnimation</a>.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-explore-mapview-mapcamera-mapcamera">MapCamera</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-explore-mapview-mapcamera-boundingbox">boundingBox</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-limits">limits</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-principalpoint">principalPoint</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-runtimetype">runtimeType</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-state">state</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-explore-mapview-mapcamera-addlistener">addListener</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-applyupdate">applyUpdate</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-cancelanimation">cancelAnimation</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-cancelanimations">cancelAnimations</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-dryapplyupdate">dryApplyUpdate</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-lookatareawithgeoorientation">lookAtAreaWithGeoOrientation</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-lookatareawithgeoorientationandviewrectangle">lookAtAreaWithGeoOrientationAndViewRectangle</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-lookatpoint">lookAtPoint</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-lookatpointwithgeoorientationandmeasure">lookAtPointWithGeoOrientationAndMeasure</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-lookatpointwithmeasure">lookAtPointWithMeasure</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-orbitbywithgeoorientation">orbitByWithGeoOrientation</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-removelistener">removeListener</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-removelisteners">removeListeners</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-setdistancetotarget">setDistanceToTarget</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-setfarplaneconfiguration">setFarPlaneConfiguration</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-setorientationattarget">setOrientationAtTarget</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-startanimation">startAnimation</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-startanimationwithlistener">startAnimationWithListener</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-tostring">toString</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-zoomby">zoomBy</a></li><li><a href="sdk-for-flutter-explore-mapview-mapcamera-zoomto">zoomTo</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-explore-mapview-mapcamera-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
