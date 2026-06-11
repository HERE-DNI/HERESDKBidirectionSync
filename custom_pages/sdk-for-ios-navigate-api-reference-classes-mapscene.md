---
title: "sdk-for-ios-navigate-api-reference-classes-mapscene"
slug: "sdk-for-ios-navigate-api-reference-classes-mapscene"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapScene"></a>
<a title="MapScene Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>
<img alt="" id="carat" src="/carat.png"/>
        MapScene Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapScene</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapScene</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapScene</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapScene</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a map scene and exposes the functionality to manipulate its content.</p>
<h2 class="heading" id="map-schemes">Map schemes</h2>
<p>The content of the displayed map and how it looks is specified by a
<code><a href="sdk-for-ios-navigate-api-reference-enums-mapscheme">MapScheme</a></code> which is set when loading a scene with <code>MapScene.loadScene(MapScheme, MapScene.LoadSceneCompletionHandler?)</code>.
It is also possible to load your own custom map scheme from a file bundled
with your application. Supported file formats are:</p>
<ul>
<li>JSON (file extension ‘.json’; e.g. ‘my_custom_style.json’)</li>
<li>ZIP archive (file extension ‘.zip’; e.g. ‘my_custom_style.zip’), with the following archive structure:

<ul>
<li>root folder: any, not empty (e.g. ‘my_custom_style’)</li>
<li>JSON configuration: ‘<root folder="">/style.json’</root></li>
<li>custom assets folder: ‘<root folder="">/assets’</root></li>
</ul></li>
</ul>
<h2 class="heading" id="map-features">Map features</h2>
<p>Different map schemes offer different sets of features, for example showing traffic or 3D buildings.
Some features have multiple modes of operation, but most have only one.
<code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC20getSupportedFeaturesSDySSSaySSGGyF">MapScene.getSupportedFeatures(...)</a></code> can be used to check what features and modes are supported
for the current scene. Features can be enabled using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code> and disabled
with <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC15disableFeaturesyySaySSGF">MapScene.disableFeatures(...)</a></code>. Checking which features are currently enabled can be done using
<code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF">MapScene.getActiveFeatures(...)</a></code>. For convenience, <code><a href="sdk-for-ios-navigate-api-reference-structs-mapfeatures">MapFeatures</a></code> and <code><a href="sdk-for-ios-navigate-api-reference-structs-mapfeaturemodes">MapFeatureModes</a></code> hold
constants for feature and mode names.</p>
<p>Since version 4.15.0, map features cannot be controlled using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF">MapScene.setLayerVisibility(...)</a></code>, since <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF">MapScene.setLayerVisibility(...)</a></code> controls
only visibility of the layers which are corresponding to the features enabled either by <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code>
or enabled by default for the scene.</p>
<h2 class="heading" id="map-layers">Map layers</h2>
<p>A map scheme is organized in layers, which can be controlled using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF">MapScene.setLayerVisibility(...)</a></code>.
It’s possible to change the visibility state of any map layer as long as the name is known.</p>
<p>Layer visibility settings persist between scene reloading.</p>
<h2 class="heading" id="user-content">User content</h2>
<p>User generated content can be visualised on the map using <code><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline">MapPolyline</a></code>, <code><a href="sdk-for-ios-navigate-api-reference-classes-mappolygon">MapPolygon</a></code>, <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></code>,
<code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarkercluster">MapMarkerCluster</a></code>, <code><a href="sdk-for-ios-navigate-api-reference-classes-maparrow">MapArrow</a></code>, <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3d">MapMarker3D</a></code> and <code><a href="sdk-for-ios-navigate-api-reference-classes-mapimageoverlay">MapImageOverlay</a></code>
(collectively referred to as “map items”). Those can be added to and removed
from the scene by respective add and remove methods. The render order of the map items
is according to the list above. The order of objects within the same type can be controlled using
the <code>drawOrder</code> property of each object.</p>
<p>Be careful when adding a very large number of map items as this can have a negative impact on
the performance of the app.
To work around this limitation the following approach can be used:
Register to map camera updates using <code><a href="../Classes/MapCamera.html#/s:7heresdk9MapCameraC11addDelegateyyAA0bcE0_pF">MapCamera.addDelegate(...)</a></code>. Query the bounding box of the
camera viewport using <code><a href="../Classes/MapCamera.html#/s:7heresdk9MapCameraC11boundingBoxAA03GeoE0VSgvp">MapCamera.boundingBox</a></code> (it may be extended) and then use the method
<code>GeoBox.contains(GeoCoordinates)</code> in combination with <code><a href="../Classes/MapCamera/State.html#/s:7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp">MapCamera.State.distanceToTargetInMeters</a></code> to
determine which map items are actually visible to the user in the current camera viewport and
thus need to be added to the map.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC04LoadC17CompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/LoadSceneCompletionHandler"></a>
<a class="token" href="#/s:7heresdk8MapSceneC04LoadC17CompletionHandlera">LoadSceneCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called on the main thread after <code>loadScene()</code> method finishes loading
the scene.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">LoadSceneCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">loadSceneError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maperror">MapError</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>loadSceneError</em>
</code>
</td>
<td>
<div>
<p>The load scene error</p>
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
<a name="/s:7heresdk8MapSceneC6lightsAA0bC6LightsCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lights"></a>
<a class="token" href="#/s:7heresdk8MapSceneC6lightsAA0bC6LightsCvp">lights</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Controls lights present in the scene.
Provides access to a MapSceneLights instance that controls the lights in the scene.</p>
<p>The behavior of the returned MapSceneLights instance depends on the state of the scene:</p>
<ul>
<li>If the scene is not loaded, the returned MapSceneLights instance will not contain any light settings, as lights are not loaded without a scene.</li>
<li>If the scene is loaded, the returned MapSceneLights instance reflects the current light settings of the loaded scene.</li>
</ul>
<p>Scene Change Behavior:</p>
<ul>
<li>If the scene changes, the MapSceneLights instance will be updated to reflect the light settings of the new scene.</li>
<li>Any user-defined settings to MapSceneLights will be overridden by the new scene’s light settings when the scene changes.</li>
</ul>
<p>Error Handling:</p>
<ul>
<li>If the scene is loaded and the loaded scene does not utilize or specify light settings:

<ul>
<li>If the lights are not present, the error callback may return a NO_LIGHTS state.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lights</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapscenelights">MapSceneLights</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC0B10PickFilterC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapPickFilter"></a>
<a class="token" href="#/s:7heresdk8MapSceneC0B10PickFilterC">MapPickFilter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Filter for the map content to be picked.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapscene-mappickfilter">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapPickFilter</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapscene">MapScene</a></span><span class="o">.</span><span class="kt">MapPickFilter</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapscene">MapScene</a></span><span class="o">.</span><span class="kt">MapPickFilter</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC04loadC09mapScheme10completionyAA0bF0O_yAA0B5ErrorOSgcSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/loadScene(mapScheme:completion:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC04loadC09mapScheme10completionyAA0bF0O_yAA0B5ErrorOSgcSgtF">loadScene(mapScheme:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously loads a map scene described by a specified map scheme.
Any previous map scene config will be replaced. The loaded scene is cached and so any changes
made to the scene files on disk might not get reflected on a successive call to this function.
Instead the reloadScene API can handle such use-cases to force-update the scene.</p>
<p>Map features enabled or disabled using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code>
and <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC15disableFeaturesyySaySSGF">MapScene.disableFeatures(...)</a></code> will be reset to defaults for the new
scene configuration.</p>
<p>The callback is called on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">loadScene</span><span class="p">(</span><span class="nv">mapScheme</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-mapscheme">MapScheme</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kt">MapScene</span><span class="o">.</span><span class="kt"><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC04LoadC17CompletionHandlera">LoadSceneCompletionHandler</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapScheme</em>
</code>
</td>
<td>
<div>
<p>Map scheme.</p>
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
<p>Optional callback that will receive the result of this operation.</p>
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
<a name="/s:7heresdk8MapSceneC04loadC08fromFile10completionySS_yAA0B5ErrorOSgcSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/loadScene(fromFile:completion:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC04loadC08fromFile10completionySS_yAA0B5ErrorOSgcSgtF">loadScene(fromFile:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously loads a map scene described by a specified file in one of the supported formats.
Any previous map scene config will be replaced.</p>
<p>When loading the same file again, consider to call <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC06reloadC0yyF">reloadScene()</a></code> instead.</p>
<p>Map features enabled or disabled using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code>
and <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC15disableFeaturesyySaySSGF">MapScene.disableFeatures(...)</a></code> will be reset to defaults for the new
scene configuration.</p>
<p>The callback is called on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">loadScene</span><span class="p">(</span><span class="n">fromFile</span> <span class="nv">configurationFile</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kt">MapScene</span><span class="o">.</span><span class="kt"><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC04LoadC17CompletionHandlera">LoadSceneCompletionHandler</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>configurationFile</em>
</code>
</td>
<td>
<div>
<p>Map scheme configuration file. It must contain the whole scene configuration.
In case it contains references to other files, they have to be reachable under
the paths specified in the main configuration file.</p>
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
<p>Optional callback that will receive the result of this operation.</p>
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
<a name="/s:7heresdk8MapSceneC04loadC08fromFile14watermarkStyle10completionySS_AA09WatermarkH0OyAA0B5ErrorOSgcSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/loadScene(fromFile:watermarkStyle:completion:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC04loadC08fromFile14watermarkStyle10completionySS_AA09WatermarkH0OyAA0B5ErrorOSgcSgtF">loadScene(fromFile:<wbr/>watermarkStyle:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously loads a map scene described by a specified file in one of the supported formats.
The style of the HERE watermark matching the map scheme is specified. Any previous map scene
config will be replaced.</p>
<p>When loading the same file again, consider to call <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC06reloadC0yyF">reloadScene()</a></code> instead.</p>
<p>Map features enabled or disabled using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code>
and <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC15disableFeaturesyySaySSGF">MapScene.disableFeatures(...)</a></code> will be reset to defaults for the new
scene configuration.</p>
<p>The callback is called on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">loadScene</span><span class="p">(</span><span class="n">fromFile</span> <span class="nv">configurationFile</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">watermarkStyle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-watermarkstyle">WatermarkStyle</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kt">MapScene</span><span class="o">.</span><span class="kt"><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC04LoadC17CompletionHandlera">LoadSceneCompletionHandler</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>configurationFile</em>
</code>
</td>
<td>
<div>
<p>Map scheme configuration file. It must contain the whole scene configuration.
In case it contains references to other files, they have to be reachable under
the paths specified in the main configuration file.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>watermarkStyle</em>
</code>
</td>
<td>
<div>
<p>The style for the HERE watermark, see <code><a href="sdk-for-ios-navigate-api-reference-enums-watermarkstyle">WatermarkStyle</a></code>.</p>
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
<p>Optional callback that will receive the result of this operation.</p>
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
<a name="/s:7heresdk8MapSceneC04loadC07options10completionyAA0bC11LoadOptionsC_yAA0B5ErrorOSgcSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/loadScene(options:completion:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC04loadC07options10completionyAA0bC11LoadOptionsC_yAA0B5ErrorOSgcSgtF">loadScene(options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously loads a map scene using MapSceneLoadOptions.</p>
<p>This is an unified API that supports loading from either a map scheme or configuration file,
with optional feature and watermark configuration. It’s more efficient to load the scene with
this function by specifying the list of enabled features and disabled features, compared to
loading the scene first and enabling or disabling map features in the scene loading callback
function.</p>
<p>Configuration defaults are used for features that are not part of the enabled features or
disabled features parameters. When a feature is in both the enabled and disabled lists,
the feature is considered as requested to be enabled. If the same feature is present multiple
times in the enabled list with different modes, then the feature is considered as requested
to be enabled, but with an unspecified mode (any of the many specified in the enabled list).</p>
<p>Any previous map scene config will be replaced. The callback is called on the main thread.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">loadScene</span><span class="p">(</span><span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="../Maps.html#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kt">MapScene</span><span class="o">.</span><span class="kt"><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC04LoadC17CompletionHandlera">LoadSceneCompletionHandler</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>Scene configuration options created using MapSceneLoadOptionsBuilder.</p>
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
<p>Optional callback that will receive the result of this operation.</p>
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
<a name="/s:7heresdk8MapSceneC03addB8PolylineyyAA0bE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapPolyline(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC03addB8PolylineyyAA0bE0CF">addMapPolyline(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a map polyline to this map scene.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapPolyline</span><span class="p">(</span><span class="n">_</span> <span class="nv">mapPolyline</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline">MapPolyline</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapPolyline</em>
</code>
</td>
<td>
<div>
<p>The map polyline to be added to this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC03addB9PolylinesyySayAA0B8PolylineCGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapPolylines(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC03addB9PolylinesyySayAA0B8PolylineCGF">addMapPolylines(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds map polylines to this map scene.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapPolyline API to add a very large number of
polylines (especially 1000+ also depending on their complexity) is not recommended.
Adding this many polylines has a negative impact on the performance leading to
stuttering of the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <code>MapScene</code> class doc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapPolylines</span><span class="p">(</span><span class="n">_</span> <span class="nv">mapPolylines</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline">MapPolyline</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapPolylines</em>
</code>
</td>
<td>
<div>
<p>The map polylines to be added to this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC06removeB8PolylineyyAA0bE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapPolyline(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC06removeB8PolylineyyAA0bE0CF">removeMapPolyline(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a map polyline from this map scene.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapPolyline</span><span class="p">(</span><span class="n">_</span> <span class="nv">mapPolyline</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline">MapPolyline</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapPolyline</em>
</code>
</td>
<td>
<div>
<p>The map polyline to be removed from this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC06removeB9PolylinesyySayAA0B8PolylineCGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapPolylines(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC06removeB9PolylinesyySayAA0B8PolylineCGF">removeMapPolylines(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes map polylines from this map scene.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapPolylines</span><span class="p">(</span><span class="n">_</span> <span class="nv">mapPolylines</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline">MapPolyline</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapPolylines</em>
</code>
</td>
<td>
<div>
<p>The map polylines to be removed from this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC09removeAllB9PolylinesyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeAllMapPolylines()"></a>
<a class="token" href="#/s:7heresdk8MapSceneC09removeAllB9PolylinesyyF">removeAllMapPolylines()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all map polylines from this map scene.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeAllMapPolylines</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC03addB5ArrowyyAA0bE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapArrow(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC03addB5ArrowyyAA0bE0CF">addMapArrow(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a map arrow to this map scene.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapArrow API to add a very large number of arrows
(especially 1000+ also depending on their complexity) is not recommended.
Adding this many arrows has a negative impact on the performance leading to stuttering of the
app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <code>MapScene</code> class doc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapArrow</span><span class="p">(</span><span class="n">_</span> <span class="nv">mapArrow</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-maparrow">MapArrow</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapArrow</em>
</code>
</td>
<td>
<div>
<p>The map arrow to be added to this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC06removeB5ArrowyyAA0bE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapArrow(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC06removeB5ArrowyyAA0bE0CF">removeMapArrow(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a map arrow from this map scene.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapArrow</span><span class="p">(</span><span class="n">_</span> <span class="nv">mapArrow</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-maparrow">MapArrow</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapArrow</em>
</code>
</td>
<td>
<div>
<p>The map arrow to be removed from this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC03addB6MarkeryyAA0bE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapMarker(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC03addB6MarkeryyAA0bE0CF">addMapMarker(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a map marker to this map scene. Adding the same marker instance multiple times
has no effect. Adding a marker that is already part of a map marker cluster has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapMarker</span><span class="p">(</span><span class="n">_</span> <span class="nv">marker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>marker</em>
</code>
</td>
<td>
<div>
<p>The marker to be added to this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC03addB7MarkersyySayAA0B6MarkerCGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapMarkers(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC03addB7MarkersyySayAA0B6MarkerCGF">addMapMarkers(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds multiple map markers to this map scene. Adding the same marker instances multiple times
has no effect. Adding markers that are already part of a map marker cluster has no effect.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapMarkers API to add a very large number of markers
(several thousands, especially 10000+) is not recommended. Adding this many markers will have
a negative impact on the performance leading to stuttering of the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <code>MapScene</code> class doc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapMarkers</span><span class="p">(</span><span class="n">_</span> <span class="nv">markers</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>markers</em>
</code>
</td>
<td>
<div>
<p>The list of markers to be added to this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC06removeB6MarkeryyAA0bE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapMarker(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC06removeB6MarkeryyAA0bE0CF">removeMapMarker(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a map marker from this map scene. Removing a marker instance that is not
a part of this scene or belongs to a marker cluster has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapMarker</span><span class="p">(</span><span class="n">_</span> <span class="nv">marker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>marker</em>
</code>
</td>
<td>
<div>
<p>The marker to be removed from this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC06removeB7MarkersyySayAA0B6MarkerCGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapMarkers(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC06removeB7MarkersyySayAA0B6MarkerCGF">removeMapMarkers(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes multiple map markers from this map scene. Removing marker instances that are not
a part of this scene or belong to a marker cluster has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapMarkers</span><span class="p">(</span><span class="n">_</span> <span class="nv">markers</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>markers</em>
</code>
</td>
<td>
<div>
<p>The list of markers to be removed from this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC09removeAllB7MarkersyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeAllMapMarkers()"></a>
<a class="token" href="#/s:7heresdk8MapSceneC09removeAllB7MarkersyyF">removeAllMapMarkers()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all map markers from this map scene.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeAllMapMarkers</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC03addB13MarkerClusteryyAA0beF0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapMarkerCluster(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC03addB13MarkerClusteryyAA0beF0CF">addMapMarkerCluster(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a map marker cluster to the map. Either the contained individual map markers or the
cluster markers will be displayed. Adding the same map marker cluster instance multiple times
has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapMarkerCluster</span><span class="p">(</span><span class="n">_</span> <span class="nv">cluster</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarkercluster">MapMarkerCluster</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>cluster</em>
</code>
</td>
<td>
<div>
<p>The marker cluster to be added to this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC06removeB13MarkerClusteryyAA0beF0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapMarkerCluster(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC06removeB13MarkerClusteryyAA0beF0CF">removeMapMarkerCluster(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a map marker cluster from the map. Removing a map marker cluster that is not on this
scene has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapMarkerCluster</span><span class="p">(</span><span class="n">_</span> <span class="nv">cluster</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarkercluster">MapMarkerCluster</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>cluster</em>
</code>
</td>
<td>
<div>
<p>The marker cluster to be removed from this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC03addB8Marker3dyyAA0B8Marker3DCF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapMarker3d(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC03addB8Marker3dyyAA0B8Marker3DCF">addMapMarker3d(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a 3D map marker to this map scene.
Does nothing if the marker instance was already added to the scene.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapMarker3D API to add a very large number of 3D
markers (especially 500+ also depending on the complexity of the 3D object) is not
recommended. Adding this many 3D markers has a negative impact on the performance leading to
stuttering of the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <code>MapScene</code> class doc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapMarker3d</span><span class="p">(</span><span class="n">_</span> <span class="nv">marker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3d">MapMarker3D</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>marker</em>
</code>
</td>
<td>
<div>
<p>The marker to be added to this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC03addB9Markers3dyySayAA0B8Marker3DCGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapMarkers3d(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC03addB9Markers3dyySayAA0B8Marker3DCGF">addMapMarkers3d(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds multiple 3D map markers to this map scene. Adding the same 3D marker instances multiple
times has no effect.</p>
<p><strong>Note:</strong>
Due to technical limitations, using the MapMarkers3D API to add a very large number of 3D
markers (especially 500+) is not recommended. Adding this many markers will have a
negative impact on the performance leading to stuttering of the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <code>MapScene</code> class doc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapMarkers3d</span><span class="p">(</span><span class="n">_</span> <span class="nv">markers</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3d">MapMarker3D</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>markers</em>
</code>
</td>
<td>
<div>
<p>The list of 3D markers to be added to this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC06removeB8Marker3dyyAA0B8Marker3DCF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapMarker3d(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC06removeB8Marker3dyyAA0B8Marker3DCF">removeMapMarker3d(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a 3D map marker from this map scene. Removing a marker instance that is not on this
scene has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapMarker3d</span><span class="p">(</span><span class="n">_</span> <span class="nv">marker</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3d">MapMarker3D</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>marker</em>
</code>
</td>
<td>
<div>
<p>The marker to be removed from this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC06removeB9Markers3dyySayAA0B8Marker3DCGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapMarkers3d(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC06removeB9Markers3dyySayAA0B8Marker3DCGF">removeMapMarkers3d(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes multiple 3D map markers from this map scene. Removing marker instances that are not
a part of this scene has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapMarkers3d</span><span class="p">(</span><span class="n">_</span> <span class="nv">markers</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3d">MapMarker3D</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>markers</em>
</code>
</td>
<td>
<div>
<p>The list of 3D markers to be removed from this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC09removeAllB9Markers3dyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeAllMapMarkers3d()"></a>
<a class="token" href="#/s:7heresdk8MapSceneC09removeAllB9Markers3dyyF">removeAllMapMarkers3d()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all 3D map markers from this map scene.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeAllMapMarkers3d</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC03addB7PolygonyyAA0bE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapPolygon(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC03addB7PolygonyyAA0bE0CF">addMapPolygon(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a map polygon to this map scene.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapPolygon API to add a very large number of polygons
(especially 1000+ also depending on their complexity) is not recommended.
Adding this many polygons has a negative impact on the performance leading to stuttering of
the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <code>MapScene</code> class doc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapPolygon</span><span class="p">(</span><span class="n">_</span> <span class="nv">mapPolygon</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolygon">MapPolygon</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapPolygon</em>
</code>
</td>
<td>
<div>
<p>The map polygon to be added to this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC03addB8PolygonsyySayAA0B7PolygonCGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapPolygons(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC03addB8PolygonsyySayAA0B7PolygonCGF">addMapPolygons(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds multiple map polygons to this map scene.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapPolygon API to add a very large number of polygons
(especially 1000+ also depending on their complexity) is not recommended.
Adding this many polygons has a negative impact on the performance leading to stuttering of
the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <code>MapScene</code> class doc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapPolygons</span><span class="p">(</span><span class="n">_</span> <span class="nv">mapPolygons</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolygon">MapPolygon</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapPolygons</em>
</code>
</td>
<td>
<div>
<p>The map polygons to be added to this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC06removeB7PolygonyyAA0bE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapPolygon(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC06removeB7PolygonyyAA0bE0CF">removeMapPolygon(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a map polygon from this map scene.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapPolygon</span><span class="p">(</span><span class="n">_</span> <span class="nv">mapPolygon</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolygon">MapPolygon</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapPolygon</em>
</code>
</td>
<td>
<div>
<p>The map polygon to be removed from this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC06removeB8PolygonsyySayAA0B7PolygonCGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapPolygons(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC06removeB8PolygonsyySayAA0B7PolygonCGF">removeMapPolygons(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes multiple map polygon from this map scene.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapPolygons</span><span class="p">(</span><span class="n">_</span> <span class="nv">mapPolygons</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolygon">MapPolygon</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapPolygons</em>
</code>
</td>
<td>
<div>
<p>The map polygons to be removed from this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC09removeAllB8PolygonsyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeAllMapPolygons()"></a>
<a class="token" href="#/s:7heresdk8MapSceneC09removeAllB8PolygonsyyF">removeAllMapPolygons()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all map polygons from this map scene.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeAllMapPolygons</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC03addB12ImageOverlayyyAA0beF0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapImageOverlay(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC03addB12ImageOverlayyyAA0beF0CF">addMapImageOverlay(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a map image overlay to this map scene.
Adding the same overlay instance multiple times has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapImageOverlay</span><span class="p">(</span><span class="n">_</span> <span class="nv">overlay</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapimageoverlay">MapImageOverlay</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>overlay</em>
</code>
</td>
<td>
<div>
<p>The overlay to be added to this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC06removeB12ImageOverlayyyAA0beF0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapImageOverlay(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC06removeB12ImageOverlayyyAA0beF0CF">removeMapImageOverlay(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a map image overlay from this map scene.
Removing an overlay instance that is not part of this scene has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapImageOverlay</span><span class="p">(</span><span class="n">_</span> <span class="nv">overlay</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapimageoverlay">MapImageOverlay</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>overlay</em>
</code>
</td>
<td>
<div>
<p>The overlay to be removed from this map scene.</p>
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
<a name="/s:7heresdk8MapSceneC09removeAllB5ItemsyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeAllMapItems()"></a>
<a class="token" href="#/s:7heresdk8MapSceneC09removeAllB5ItemsyyF">removeAllMapItems()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all map objects from this map scene.
This includes polylines, polygons, markers and clusters, arrows, image overlays.
It is much faster than removing the objects one by one.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeAllMapItems</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setLayerVisibility(layerName:visibility:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF">setLayerVisibility(layerName:<wbr/>visibility:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Immediately changes the visibility of a specified map layer.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setLayerVisibility</span><span class="p">(</span><span class="nv">layerName</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">visibility</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-visibilitystate">VisibilityState</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>layerName</em>
</code>
</td>
<td>
<div>
<p>The name of the map layer to be changed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>visibility</em>
</code>
</td>
<td>
<div>
<p>The new visibility state of the layer.</p>
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
<a name="/s:7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getActiveFeatures()"></a>
<a class="token" href="#/s:7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF">getActiveFeatures()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets map features that are currently active. Active features are features that are either
enabled via a call to <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code> or that are enabled by default in the scene.</p>
<p>The key to the resulting map is the name of the feature
and the value is the active mode.</p>
<p>Result is empty if scene has not been loaded.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getActiveFeatures</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt">String</span> <span class="p">:</span> <span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The map of active features.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC20getSupportedFeaturesSDySSSaySSGGyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getSupportedFeatures()"></a>
<a class="token" href="#/s:7heresdk8MapSceneC20getSupportedFeaturesSDySSSaySSGGyF">getSupportedFeatures()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets features and all of their modes supported by the currently
loaded scene configuration.</p>
<p>The key to the resulting map is the name of the feature
and the value is a list of modes for that feature.</p>
<p>Result is empty if scene has not been loaded.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getSupportedFeatures</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt">String</span> <span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]]</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The map of supported features and all their modes.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/enableFeatures(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">enableFeatures(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables specified map features. Those will become active
after next map redraw, meaning that <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF">MapScene.getActiveFeatures(...)</a></code> will
return updated list of active features only after the redraw happens.</p>
<p>Does not affect features that were not specified.
Unsupported features are ignored.</p>
<p>May cause the current map configuration to be reloaded.</p>
<p>See <code><a href="sdk-for-ios-navigate-api-reference-structs-mapfeatures">MapFeatures</a></code> for feature names and <code><a href="sdk-for-ios-navigate-api-reference-structs-mapfeaturemodes">MapFeatureModes</a></code> for
feature mode names.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">enableFeatures</span><span class="p">(</span><span class="n">_</span> <span class="nv">features</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span> <span class="p">:</span> <span class="kt">String</span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>features</em>
</code>
</td>
<td>
<div>
<p>The list of features to enable, key is the name of the feature
(see <code><a href="sdk-for-ios-navigate-api-reference-structs-mapfeatures">MapFeatures</a></code>), value specifies its mode (see <code><a href="sdk-for-ios-navigate-api-reference-structs-mapfeaturemodes">MapFeatureModes</a></code>).</p>
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
<a name="/s:7heresdk8MapSceneC15disableFeaturesyySaySSGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/disableFeatures(_:)"></a>
<a class="token" href="#/s:7heresdk8MapSceneC15disableFeaturesyySaySSGF">disableFeatures(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Disables specified map features. Those will become inactive
after next map redraw, meaning that <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF">MapScene.getActiveFeatures(...)</a></code> will
return updated list of active features only after the redraw happens.</p>
<p>Does not affect features that were not specified.
Unsupported features are ignored.</p>
<p>May cause the current map configuration to be reloaded.</p>
<p>See <code><a href="sdk-for-ios-navigate-api-reference-structs-mapfeatures">MapFeatures</a></code> for feature names.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">disableFeatures</span><span class="p">(</span><span class="n">_</span> <span class="nv">features</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>features</em>
</code>
</td>
<td>
<div>
<p>The names of features to disable (see <code><a href="sdk-for-ios-navigate-api-reference-structs-mapfeatures">MapFeatures</a></code>).</p>
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
<a name="/s:7heresdk8MapSceneC06reloadC0yyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/reloadScene()"></a>
<a class="token" href="#/s:7heresdk8MapSceneC06reloadC0yyF">reloadScene()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously reloads the current map scene from file. This skips any cached data used internally and reloads the
scene including any changes made to the (custom) map styles in JSON.</p>
<p><code>MapFeature</code> settings will be preserved.</p>
<p>Internal optimization checks will be skipped to ensure all custom style changes are loaded. Therefore,
calling this method may take slightly longer than calling one of the <code>loadScene(..)</code> overloads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">reloadScene</span><span class="p">()</span></code></pre>
</div>
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

`
}</HTMLBlock>
