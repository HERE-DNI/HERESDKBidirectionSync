---
title: "Map Scene"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapScene///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/MapScene</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Scene</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">Represents a map scene and exposes the functionality to manipulate its content.</p><h2> Map schemes</h2><p class="paragraph">The content of the displayed map and how it looks is specified by a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scheme which is set when loading a scene with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-scene. It is also possible to load your own custom map scheme from a file bundled with your application. Supported file formats are:</p><ul><li><p class="paragraph">JSON (file extension '.json'; e.g. 'my_custom_style.json')</p></li><li><p class="paragraph">ZIP archive (file extension '.zip'; e.g. 'my_custom_style.zip'), with the following archive structure:</p></li></ul><ul><li><p class="paragraph">root folder: any, not empty (e.g. 'my_custom_style')</p></li><li><p class="paragraph">JSON configuration: '<root folder="">/style.json'</root></p></li><li><p class="paragraph">custom assets folder: '<root folder="">/assets'</root></p></li></ul><h2> Map features</h2><p class="paragraph">Different map schemes offer different sets of features, for example showing traffic or 3D buildings. Some features have multiple modes of operation, but most have only one. /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-get-supported-features can be used to check what features and modes are supported for the current scene. Features can be enabled using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-enable-features and disabled with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-disable-features. Checking which features are currently enabled can be done using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-get-active-features. For convenience, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-features and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-feature-modes hold constants for feature and mode names.</p><p class="paragraph">Since version 4.15.0, map features cannot be controlled using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-set-layer-visibility, since /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-set-layer-visibility controls only visibility of the layers which are corresponding to the features enabled either by /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-enable-features or enabled by default for the scene.</p><h2> Map layers</h2><p class="paragraph">A map scheme is organized in layers, which can be controlled using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-set-layer-visibility. It's possible to change the visibility state of any map layer as long as the name is known.</p><p class="paragraph">Layer visibility settings persist between scene reloading.</p><h2> User content</h2><p class="paragraph">User generated content can be visualised on the map using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-arrow, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay (collectively referred to as "map items"). Those can be added to and removed from the scene by respective add and remove methods. The render order of the map items is according to the list above. The order of objects within the same type can be controlled using the <code class="lang-kotlin">drawOrder</code> property of each object.</p><p class="paragraph">Be careful when adding a very large number of map items as this can have a negative impact on the performance of the app. To work around this limitation the following approach can be used: Register to map camera updates using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-add-listener. Query the bounding box of the camera viewport using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-bounding-box (it may be extended) and then use the method /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-box-contains in combination with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-state-distance-to-target-in-meters to determine which map items are actually visible to the user in the current camera viewport and thus need to be added to the map.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-2079948464%2FClasslikes%2F1617540583" id="-2079948464%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-companion</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="LoadSceneCallback" data-filterable-set=":modules:dokkaHtml/release" data-name="-131692399%2FClasslikes%2F1617540583" id="-131692399%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-scene-callback</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun interface /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-scene-callback</div><div class="brief"><p class="paragraph">Called on the main thread after <code class="lang-kotlin">loadScene()</code> method finishes loading the scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="MapPickFilter" data-filterable-set=":modules:dokkaHtml/release" data-name="-503278201%2FClasslikes%2F1617540583" id="-503278201%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-map-pick-filter</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-map-pick-filter : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><div class="brief"><p class="paragraph">Filter for the map content to be picked.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="lights" data-filterable-set=":modules:dokkaHtml/release" data-name="-1846503564%2FProperties%2F1617540583" id="-1846503564%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-lights</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-lights: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-lights</div><div class="brief"><p class="paragraph">Controls lights present in the scene. Provides access to a MapSceneLights instance that controls the lights in the scene.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="addMapArrow" data-filterable-set=":modules:dokkaHtml/release" data-name="-2101049656%2FFunctions%2F1617540583" id="-2101049656%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-arrow</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-arrow(mapArrow: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-arrow)</div><div class="brief"><p class="paragraph">Adds a map arrow to this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="addMapImageOverlay" data-filterable-set=":modules:dokkaHtml/release" data-name="-1929028350%2FFunctions%2F1617540583" id="-1929028350%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-image-overlay</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-image-overlay(overlay: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay)</div><div class="brief"><p class="paragraph">Adds a map image overlay to this map scene. Adding the same overlay instance multiple times has no effect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="addMapMarker" data-filterable-set=":modules:dokkaHtml/release" data-name="1819153784%2FFunctions%2F1617540583" id="1819153784%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-marker</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-marker(marker: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker)</div><div class="brief"><p class="paragraph">Adds a map marker to this map scene. Adding the same marker instance multiple times has no effect. Adding a marker that is already part of a map marker cluster has no effect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="addMapMarker3d" data-filterable-set=":modules:dokkaHtml/release" data-name="-221298442%2FFunctions%2F1617540583" id="-221298442%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-marker3d</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-marker3d(marker: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d)</div><div class="brief"><p class="paragraph">Adds a 3D map marker to this map scene. Does nothing if the marker instance was already added to the scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="addMapMarkerCluster" data-filterable-set=":modules:dokkaHtml/release" data-name="1508269480%2FFunctions%2F1617540583" id="1508269480%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-marker-cluster</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-marker-cluster(cluster: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster)</div><div class="brief"><p class="paragraph">Adds a map marker cluster to the map. Either the contained individual map markers or the cluster markers will be displayed. Adding the same map marker cluster instance multiple times has no effect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="addMapMarkers" data-filterable-set=":modules:dokkaHtml/release" data-name="-123825099%2FFunctions%2F1617540583" id="-123825099%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-markers</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-markers(markers: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker&gt;)</div><div class="brief"><p class="paragraph">Adds multiple map markers to this map scene. Adding the same marker instances multiple times has no effect. Adding markers that are already part of a map marker cluster has no effect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="addMapMarkers3d" data-filterable-set=":modules:dokkaHtml/release" data-name="-1658123465%2FFunctions%2F1617540583" id="-1658123465%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-markers3d</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-markers3d(markers: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d&gt;)</div><div class="brief"><p class="paragraph">Adds multiple 3D map markers to this map scene. Adding the same 3D marker instances multiple times has no effect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="addMapPolygon" data-filterable-set=":modules:dokkaHtml/release" data-name="961816168%2FFunctions%2F1617540583" id="961816168%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-polygon</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-polygon(mapPolygon: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon)</div><div class="brief"><p class="paragraph">Adds a map polygon to this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="addMapPolygons" data-filterable-set=":modules:dokkaHtml/release" data-name="61332825%2FFunctions%2F1617540583" id="61332825%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-polygons</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-polygons(mapPolygons: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon&gt;)</div><div class="brief"><p class="paragraph">Adds multiple map polygons to this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="addMapPolyline" data-filterable-set=":modules:dokkaHtml/release" data-name="1693769708%2FFunctions%2F1617540583" id="1693769708%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-polyline</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-polyline(mapPolyline: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline)</div><div class="brief"><p class="paragraph">Adds a map polyline to this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="addMapPolylines" data-filterable-set=":modules:dokkaHtml/release" data-name="-906407819%2FFunctions%2F1617540583" id="-906407819%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-polylines</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-polylines(mapPolylines: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline&gt;)</div><div class="brief"><p class="paragraph">Adds map polylines to this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="disableFeatures" data-filterable-set=":modules:dokkaHtml/release" data-name="1628937262%2FFunctions%2F1617540583" id="1628937262%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-disable-features</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-disable-features(features: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>&gt;)</div><div class="brief"><p class="paragraph">Disables specified map features. Those will become inactive after next map redraw, meaning that /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-get-active-features will return updated list of active features only after the redraw happens.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="enableFeatures" data-filterable-set=":modules:dokkaHtml/release" data-name="-912245601%2FFunctions%2F1617540583" id="-912245601%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-enable-features</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-enable-features(features: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>&gt;)</div><div class="brief"><p class="paragraph">Enables specified map features. Those will become active after next map redraw, meaning that /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-get-active-features will return updated list of active features only after the redraw happens.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getActiveFeatures" data-filterable-set=":modules:dokkaHtml/release" data-name="131210192%2FFunctions%2F1617540583" id="131210192%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-get-active-features</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-get-active-features(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>&gt;</div><div class="brief"><p class="paragraph">Gets map features that are currently active. Active features are features that are either enabled via a call to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-enable-features or that are enabled by default in the scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getSupportedFeatures" data-filterable-set=":modules:dokkaHtml/release" data-name="2085843772%2FFunctions%2F1617540583" id="2085843772%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-get-supported-features</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-get-supported-features(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>&gt;&gt;</div><div class="brief"><p class="paragraph">Gets features and all of their modes supported by the currently loaded scene configuration.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="loadScene" data-filterable-set=":modules:dokkaHtml/release" data-name="-1993428859%2FFunctions%2F1617540583" id="-1993428859%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-scene</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-scene(options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-options, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-scene-callback?)</div><div class="brief"><p class="paragraph">Asynchronously loads a map scene using MapSceneLoadOptions.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-scene(mapScheme: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scheme, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-scene-callback?)</div><div class="brief"><p class="paragraph">Asynchronously loads a map scene described by a specified map scheme. Any previous map scene config will be replaced. The loaded scene is cached and so any changes made to the scene files on disk might not get reflected on a successive call to this function. Instead the reloadScene API can handle such use-cases to force-update the scene.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-scene(configurationFile: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-scene-callback?)</div><div class="brief"><p class="paragraph">Asynchronously loads a map scene described by a specified file in one of the supported formats. Any previous map scene config will be replaced.</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-scene(configurationFile: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, watermarkStyle: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-watermark-style, callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-scene-callback?)</div><div class="brief"><p class="paragraph">Asynchronously loads a map scene described by a specified file in one of the supported formats. The style of the HERE watermark matching the map scheme is specified. Any previous map scene config will be replaced.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="reloadScene" data-filterable-set=":modules:dokkaHtml/release" data-name="1576412662%2FFunctions%2F1617540583" id="1576412662%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-reload-scene</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-reload-scene()</div><div class="brief"><p class="paragraph">Asynchronously reloads the current map scene from file. This skips any cached data used internally and reloads the scene including any changes made to the (custom) map styles in JSON.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeAllMapItems" data-filterable-set=":modules:dokkaHtml/release" data-name="2025575880%2FFunctions%2F1617540583" id="2025575880%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-all-map-items</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-all-map-items()</div><div class="brief"><p class="paragraph">Removes all map objects from this map scene. This includes polylines, polygons, markers and clusters, arrows, image overlays. It is much faster than removing the objects one by one.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeAllMapMarkers" data-filterable-set=":modules:dokkaHtml/release" data-name="-916327057%2FFunctions%2F1617540583" id="-916327057%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-all-map-markers</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-all-map-markers()</div><div class="brief"><p class="paragraph">Removes all map markers from this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeAllMapMarkers3d" data-filterable-set=":modules:dokkaHtml/release" data-name="874454910%2FFunctions%2F1617540583" id="874454910%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-all-map-markers3d</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-all-map-markers3d()</div><div class="brief"><p class="paragraph">Removes all 3D map markers from this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeAllMapPolygons" data-filterable-set=":modules:dokkaHtml/release" data-name="-1711889991%2FFunctions%2F1617540583" id="-1711889991%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-all-map-polygons</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-all-map-polygons()</div><div class="brief"><p class="paragraph">Removes all map polygons from this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeAllMapPolylines" data-filterable-set=":modules:dokkaHtml/release" data-name="-347483979%2FFunctions%2F1617540583" id="-347483979%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-all-map-polylines</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-all-map-polylines()</div><div class="brief"><p class="paragraph">Removes all map polylines from this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeMapArrow" data-filterable-set=":modules:dokkaHtml/release" data-name="693410435%2FFunctions%2F1617540583" id="693410435%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-arrow</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-arrow(mapArrow: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-arrow)</div><div class="brief"><p class="paragraph">Removes a map arrow from this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeMapImageOverlay" data-filterable-set=":modules:dokkaHtml/release" data-name="1673448829%2FFunctions%2F1617540583" id="1673448829%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-image-overlay</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-image-overlay(overlay: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image-overlay)</div><div class="brief"><p class="paragraph">Removes a map image overlay from this map scene. Removing an overlay instance that is not part of this scene has no effect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeMapMarker" data-filterable-set=":modules:dokkaHtml/release" data-name="-1354226061%2FFunctions%2F1617540583" id="-1354226061%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-marker</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-marker(marker: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker)</div><div class="brief"><p class="paragraph">Removes a map marker from this map scene. Removing a marker instance that is not a part of this scene or belongs to a marker cluster has no effect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeMapMarker3d" data-filterable-set=":modules:dokkaHtml/release" data-name="670194801%2FFunctions%2F1617540583" id="670194801%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-marker3d</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-marker3d(marker: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d)</div><div class="brief"><p class="paragraph">Removes a 3D map marker from this map scene. Removing a marker instance that is not on this scene has no effect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeMapMarkerCluster" data-filterable-set=":modules:dokkaHtml/release" data-name="1745197923%2FFunctions%2F1617540583" id="1745197923%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-marker-cluster</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-marker-cluster(cluster: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster)</div><div class="brief"><p class="paragraph">Removes a map marker cluster from the map. Removing a map marker cluster that is not on this scene has no effect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeMapMarkers" data-filterable-set=":modules:dokkaHtml/release" data-name="1115689328%2FFunctions%2F1617540583" id="1115689328%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-markers</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-markers(markers: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker&gt;)</div><div class="brief"><p class="paragraph">Removes multiple map markers from this map scene. Removing marker instances that are not a part of this scene or belong to a marker cluster has no effect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeMapMarkers3d" data-filterable-set=":modules:dokkaHtml/release" data-name="-213552398%2FFunctions%2F1617540583" id="-213552398%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-markers3d</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-markers3d(markers: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d&gt;)</div><div class="brief"><p class="paragraph">Removes multiple 3D map markers from this map scene. Removing marker instances that are not a part of this scene has no effect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeMapPolygon" data-filterable-set=":modules:dokkaHtml/release" data-name="770565283%2FFunctions%2F1617540583" id="770565283%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-polygon</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-polygon(mapPolygon: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon)</div><div class="brief"><p class="paragraph">Removes a map polygon from this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeMapPolygons" data-filterable-set=":modules:dokkaHtml/release" data-name="1528756180%2FFunctions%2F1617540583" id="1528756180%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-polygons</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-polygons(mapPolygons: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polygon&gt;)</div><div class="brief"><p class="paragraph">Removes multiple map polygon from this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeMapPolyline" data-filterable-set=":modules:dokkaHtml/release" data-name="-1709704345%2FFunctions%2F1617540583" id="-1709704345%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-polyline</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-polyline(mapPolyline: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline)</div><div class="brief"><p class="paragraph">Removes a map polyline from this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeMapPolylines" data-filterable-set=":modules:dokkaHtml/release" data-name="538163248%2FFunctions%2F1617540583" id="538163248%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-polylines</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-remove-map-polylines(mapPolylines: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline&gt;)</div><div class="brief"><p class="paragraph">Removes map polylines from this map scene.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setLayerVisibility" data-filterable-set=":modules:dokkaHtml/release" data-name="662036798%2FFunctions%2F1617540583" id="662036798%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-set-layer-visibility</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-set-layer-visibility(layerName: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, visibility: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-visibility-state)</div><div class="brief"><p class="paragraph">Immediately changes the visibility of a specified map layer.</p></div></div></div>
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
