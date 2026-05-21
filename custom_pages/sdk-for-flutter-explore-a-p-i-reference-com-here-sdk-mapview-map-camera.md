---
title: "Map Camera"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapCamera///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/MapCamera</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Camera</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">Represents the camera looking onto the map view.</p><p class="paragraph">Each map instance has exactly one camera that is used to manipulate the way the map is displayed.</p><p class="paragraph">Any updates to the state of the camera will be applied while drawing the next map view frame and the current state of the camera reflects what is currently drawn inside the map view.</p><p class="paragraph">Note: The camera can be configured and positioned even before a map scene is loaded for the first time. This allows for pre-setting the desired camera position, orientation, and zoom level, which will be applied once the map scene becomes available.</p><p class="paragraph"><b>Camera Model</b></p><p class="paragraph"><i>Camera Concepts and Units</i></p><p class="paragraph">By default, HERE SDK uses an idealized Earth globe with a 3D-capable camera model. Being a 3D camera model means that the world position can be freely specified in geodetic 3D space (i.e. Earth centric) and the orientation can be freely changed around two axes - bearing (also known as head) and tilt (also known as pitch).</p><p class="paragraph">The camera supports the look-at target with orientation on the ground way of setting up the camera in space. The camera is placed so that it looks at a specific geo-coordinates (placed at the <code class="lang-kotlin">principal point</code>) from a given orientation and distance.</p><ul><li><p class="paragraph">the look-at target in geo-coordinates (latitude, longitude) in degrees and an <code class="lang-kotlin">altitude</code> in meters above MSL (mean sea level) at the <code class="lang-kotlin">principal point</code></p></li><li><p class="paragraph">the <code class="lang-kotlin">orientation</code> at the look-at target</p></li><li><p class="paragraph">the distance of the camera from the look-at target, given as <code class="lang-kotlin">distance</code> in meters or as <code class="lang-kotlin">zoom-level</code></p></li></ul><p class="paragraph"><i>Getting the current camera state</i></p><p class="paragraph">The current camera state can be obtained by the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-state call. It contains information about the camera look-at target (geo-coordinates and orientation) in geodetic space. The values are returned for the current <code class="lang-kotlin">principal point</code>. This can lead to surprising or unexpected values in cases where the camera position/orientation was specified for another screen point, e.g. when using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update-factory-companion-look-at with a view rectangle, whose center does not coincide with the <code class="lang-kotlin">principal point</code>.  In this case, the geo-coordinates of the look-at target will differ from the center of the geo-box used in the <code class="lang-kotlin">lookAt</code> call.</p><p class="paragraph"><i>Geo coordinates</i></p><p class="paragraph">Geo-coordinates are given in degrees and follow the common nomenclature of positive northern latitudes and positive eastern longitudes.</p><p class="paragraph"><i>Altitude</i></p><p class="paragraph">When <code class="lang-kotlin">altitude</code> is specified, it is always in meters above mean sea level (MSL). If this value is invalid (not-a-number) or not specified, then the terrain height at the given geo-coordinates will be looked up from the map. This is especially interesting in cases where terrain elevation is used within the map display.</p><p class="paragraph"><i>Distance vs zoom-level vs scale</i></p><p class="paragraph">Map camera <code class="lang-kotlin">distance</code>, <code class="lang-kotlin">zoom-level</code> and <code class="lang-kotlin">scale</code> determine how much of the world is visible on the HERE map. <code class="lang-kotlin">Distance</code>, <code class="lang-kotlin">zoom-level</code> and <code class="lang-kotlin">scale</code> are directly connected and changing one will automatically change the others as well (except for <code class="lang-kotlin">distance</code>/<code class="lang-kotlin">scale</code> changes that map to <code class="lang-kotlin">zoom-level</code> values &lt; 0 or 23).</p><ul><li><p class="paragraph"><code class="lang-kotlin">distance</code>: the distance from the camera to the look-at target on the surface of the Earth, in meters</p></li><li><p class="paragraph"><code class="lang-kotlin">zoom-level</code>: the map zoom level, in the range \[0, 3]. The relation between the width of the equator in logical pixels <code class="lang-kotlin">w</code> and the zoom level <code class="lang-kotlin">z</code> is: <code class="lang-kotlin">w = 256 * 2^(z)</code></p></li><li><p class="paragraph"><code class="lang-kotlin">scale</code>: the scale of the map at the look-at target in meters on screen per meters on Earth. So a scale of 0.001 shows 10 meters on Earth within 1 cm on screen.</p></li></ul><p class="paragraph">The following mapping represents the <code class="lang-kotlin">zoom-level</code> values:</p><table><thead><tr><th>zoom-level</th><th>~ scale on screen (130dpi)</th><th>width of the equator in logical pixels</th><th>what can be seen</th></tr></thead><tbody><tr><td>0</td><td>1:800 million</td><td>256</td><td>Earth</td></tr><tr><td>1</td><td>1:400 million</td><td>512</td><td></td></tr><tr><td>2</td><td>1:200 million</td><td>1024</td><td></td></tr><tr><td>3</td><td>1:100 million</td><td>2048</td><td></td></tr><tr><td>4</td><td>1:50 million</td><td>4096</td><td>A continent</td></tr><tr><td>5</td><td>1:25 million</td><td>8192</td><td>Large roads</td></tr><tr><td>6</td><td>1:12 million</td><td>16384</td><td>Large rivers</td></tr><tr><td>7</td><td>1:6 million</td><td>32768</td><td>A country</td></tr><tr><td>8</td><td>1:3 million</td><td>65536</td><td></td></tr><tr><td>9</td><td>1:1 million</td><td>131072</td><td></td></tr><tr><td>10</td><td>1:780 thousand</td><td>262144</td><td></td></tr><tr><td>11</td><td>1:390 thousand</td><td>524288</td><td></td></tr><tr><td>12</td><td>1:195 thousand</td><td>1048576</td><td></td></tr><tr><td>13</td><td>1:100 thousand</td><td>2097152</td><td></td></tr><tr><td>14</td><td>1:50 thousand</td><td>4194304</td><td>A city</td></tr><tr><td>15</td><td>1:25 thousand</td><td>8388608</td><td></td></tr><tr><td>16</td><td>1:12 thousand</td><td>16777216</td><td>Buildings</td></tr><tr><td>17</td><td>1:6 thousand</td><td>33554432</td><td>Landmarks</td></tr><tr><td>18</td><td>1:3 thousand</td><td>67108864</td><td></td></tr><tr><td>19</td><td>1:1 thousand</td><td>134217728</td><td></td></tr><tr><td>20</td><td>1:7 hundred</td><td>268435456</td><td>Streets</td></tr><tr><td>21</td><td>1:3 hundred</td><td>536870912</td><td></td></tr><tr><td>22</td><td>1:1 hundred</td><td>1073741824</td><td></td></tr><tr><td>23</td><td>1:95</td><td>2147483648</td><td></td></tr></tbody></table><p class="paragraph"><i>Orientation</i></p><p class="paragraph">The camera <code class="lang-kotlin">orientation</code> is composed of two parts:</p><ul><li><p class="paragraph"><code class="lang-kotlin">bearing</code>: also known as azimuth, the view direction in clockwise degrees; 0° = north, 90° = east, 180° = south, 270° = west</p></li><li><p class="paragraph"><code class="lang-kotlin">tilt</code>: the angle in degrees from the vertical that the camera is looking down at the Earth; 0° = straight down.</p></li></ul><p class="paragraph"><i>Changing the Camera</i></p><p class="paragraph">All changes to the camera are encapsulated in camera updates that are created using the methods in the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update-factory class.</p><p class="paragraph">These updates can then be applied to the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-here-map using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-apply-update.</p><p class="paragraph">Camera updates are queued and executed when the next frame is rendered. They are executed in the order in which they were applied.</p><p class="paragraph"><i>Animating the Camera</i></p><p class="paragraph">Camera updates can be animated by first creating a camera animation using the methods in the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory class and then applying this animation to the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-here-map using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-start-animation.</p><p class="paragraph">Only one camera animation for one camera component at a time is supported. Applying a new animation will cancel the active animation before the new one is started. The start position in this case is where ever the active animation happened to be at the time. Different components are camera state (<code class="lang-kotlin">target pose</code> and <code class="lang-kotlin">distance/zoom level/scale</code>) and camera projection (<code class="lang-kotlin">field of view</code>, <code class="lang-kotlin">focal length</code> and <code class="lang-kotlin">principal point</code>).</p><p class="paragraph">The running animations can also be canceled using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-cancel-animations or individual ones using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-cancel-animation.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-2140172955%2FClasslikes%2F1617540583" id="-2140172955%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-companion</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="DryCameraUpdateCallback" data-filterable-set=":modules:dokkaHtml/release" data-name="1403522995%2FClasslikes%2F1617540583" id="1403522995%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-dry-camera-update-callback</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun interface /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-dry-camera-update-callback</div><div class="brief"><p class="paragraph">Used to report back results of dry update application to camera.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="FarPlaneConfiguration" data-filterable-set=":modules:dokkaHtml/release" data-name="530304160%2FClasslikes%2F1617540583" id="530304160%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-far-plane-configuration</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-far-plane-configuration</div><div class="brief"><p class="paragraph">Far plane distance configuration for a zoom level.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="State" data-filterable-set=":modules:dokkaHtml/release" data-name="-1756472448%2FClasslikes%2F1617540583" id="-1756472448%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-state</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-state</div><div class="brief"><p class="paragraph">Encapsulates state of the camera.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="boundingBox" data-filterable-set=":modules:dokkaHtml/release" data-name="1971793975%2FProperties%2F1617540583" id="1971793975%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-bounding-box</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-bounding-box: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box?</div><div class="brief"><p class="paragraph">Currently visible map area encompassed in a GeoBox. Note that this bounding box is always rectangular, and its sides are always parallel to the latitude and longitude. If the camera is rotated, the returned bounding box will be a circumscribed rectangle that is larger than the visible map area. Similarly, when the map is tilted (for example, if the map is tilted by 45 degrees), the visible map area represents a trapezoidal area in the world. Resulting value will then be a larger circumscribed rectangle that contains this trapezoid area. Because on this, corners of the resulting bounding box may be located outside of the currently visible area.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="limits" data-filterable-set=":modules:dokkaHtml/release" data-name="-73896476%2FProperties%2F1617540583" id="-73896476%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-limits</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-limits: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-limits</div><div class="brief"><p class="paragraph">Controls limits for the camera settings.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="principalPoint" data-filterable-set=":modules:dokkaHtml/release" data-name="-133913542%2FProperties%2F1617540583" id="-133913542%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-principal-point</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-principal-point: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point2-d</div><div class="brief"><p class="paragraph">Determines the pixel point where the target is placed within the map view. Setting a new principal point instantly moves the map to render the current target coordinates at the new principal point.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="state" data-filterable-set=":modules:dokkaHtml/release" data-name="-239475411%2FProperties%2F1617540583" id="-239475411%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-state</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-state: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-state</div><div class="brief"><p class="paragraph">Current state of the camera that reflects what is currently drawn by the map view.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="addListener" data-filterable-set=":modules:dokkaHtml/release" data-name="919659942%2FFunctions%2F1617540583" id="919659942%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-add-listener</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-add-listener(listener: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-listener)</div><div class="brief"><p class="paragraph">Adds a listener to this camera that will be notified on the main thread every time the map is redrawn with new camera parameters.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="applyUpdate" data-filterable-set=":modules:dokkaHtml/release" data-name="1430173199%2FFunctions%2F1617540583" id="1430173199%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-apply-update</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-apply-update(cameraUpdate: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update)</div><div class="brief"><p class="paragraph">Applies camera update to the map camera.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="cancelAnimation" data-filterable-set=":modules:dokkaHtml/release" data-name="-1851544935%2FFunctions%2F1617540583" id="-1851544935%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-cancel-animation</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-cancel-animation(cameraAnimation: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation)</div><div class="brief"><p class="paragraph">Cancels an ongoing camera animation.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="cancelAnimations" data-filterable-set=":modules:dokkaHtml/release" data-name="2020595923%2FFunctions%2F1617540583" id="2020595923%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-cancel-animations</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-cancel-animations()</div><div class="brief"><p class="paragraph">Cancels any ongoing camera animation.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="dryApplyUpdate" data-filterable-set=":modules:dokkaHtml/release" data-name="-2278392%2FFunctions%2F1617540583" id="-2278392%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-dry-apply-update</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-dry-apply-update(cameraUpdate: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-dry-camera-update-callback)</div><div class="brief"><p class="paragraph">Computes result of applying camera update without changing state of the map camera.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="lookAt" data-filterable-set=":modules:dokkaHtml/release" data-name="1228059061%2FFunctions%2F1617540583" id="1228059061%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-look-at</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-look-at(target: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates)</div><div class="brief"><p class="paragraph">Makes the camera look at a new geodetic target, while preserving the current orientation and distance to the target.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-look-at(target: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box, orientation: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-orientation-update)</div><div class="brief"><p class="paragraph">Makes the camera look at the specified geodetic area.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-look-at(target: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, zoom: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure)</div><div class="brief"><p class="paragraph">Makes the camera look at the geodetic target with the given zoom.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-look-at(target: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box, orientation: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-orientation-update, viewRectangle: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-rectangle2-d)</div><div class="brief"><p class="paragraph">Makes the camera look at the specified geodetic area and pass a rectangle which specifies where the area should appear inside of the map view.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-look-at(target: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, orientation: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-orientation-update, zoom: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure)</div><div class="brief"><p class="paragraph">Makes the camera look at the geodetic target with the given zoom and orientation.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="orbitBy" data-filterable-set=":modules:dokkaHtml/release" data-name="200172438%2FFunctions%2F1617540583" id="200172438%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-orbit-by</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-orbit-by(delta: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-orientation-update, origin: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point2-d)</div><div class="brief"><p class="paragraph">Orbits the camera around a specified view point by increasing tilt and bearing by specified delta values.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeListener" data-filterable-set=":modules:dokkaHtml/release" data-name="-83404287%2FFunctions%2F1617540583" id="-83404287%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-remove-listener</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-remove-listener(observer: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-listener)</div><div class="brief"><p class="paragraph">Removes the listener from the camera.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeListeners" data-filterable-set=":modules:dokkaHtml/release" data-name="1535403427%2FFunctions%2F1617540583" id="1535403427%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-remove-listeners</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-remove-listeners()</div><div class="brief"><p class="paragraph">Removes all registered listeners.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setDistanceToTarget" data-filterable-set=":modules:dokkaHtml/release" data-name="1124118633%2FFunctions%2F1617540583" id="1124118633%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-set-distance-to-target</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-set-distance-to-target(distanceInMeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>)</div><div class="brief"><p class="paragraph">Makes the camera look at current target from certain distance</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setFarPlaneConfiguration" data-filterable-set=":modules:dokkaHtml/release" data-name="-849468779%2FFunctions%2F1617540583" id="-849468779%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-set-far-plane-configuration</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-set-far-plane-configuration(configs: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-far-plane-configuration&gt;)</div><div class="brief"><p class="paragraph">Sets far plane distance configs per zoom level.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setOrientationAtTarget" data-filterable-set=":modules:dokkaHtml/release" data-name="1354436760%2FFunctions%2F1617540583" id="1354436760%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-set-orientation-at-target</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-set-orientation-at-target(orientation: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-orientation-update)</div><div class="brief"><p class="paragraph">Changes camera orientation in relation to target location.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="startAnimation" data-filterable-set=":modules:dokkaHtml/release" data-name="-1824565636%2FFunctions%2F1617540583" id="-1824565636%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-start-animation</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-start-animation(cameraAnimation: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation)</div><div class="brief"><p class="paragraph">Starts a given camera animation.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-start-animation(cameraAnimation: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation, animationListener: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-animation-animation-listener)</div><div class="brief"><p class="paragraph">Starts a given camera animation. The state of the animation can be tracked with the provided listener.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="zoomBy" data-filterable-set=":modules:dokkaHtml/release" data-name="-624004995%2FFunctions%2F1617540583" id="-624004995%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-zoom-by</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-zoom-by(factor: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, origin: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point2-d)</div><div class="brief"><p class="paragraph">Zooms in or out by a specified factor.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="zoomTo" data-filterable-set=":modules:dokkaHtml/release" data-name="-1950450954%2FFunctions%2F1617540583" id="-1950450954%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-zoom-to</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-zoom-to(zoomLevel: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>)</div><div class="brief"><p class="paragraph">Zooms to the specified zoom level. The supplied value will be clamped to the range of \[0, 22\], where 0 is a view of whole globe and 22 is street level.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="footer">
<a class="footer--button footer--button_go-to-top" href="#content" id="go-to-top-link"></a>
© 2026 Copyright

Generated by 
<a class="footer--link footer--link_external" href="https://github.com/Kotlin/dokka">
dokka
</a>

</div>
</div>

</div>

</div>
`
}</HTMLBlock>
