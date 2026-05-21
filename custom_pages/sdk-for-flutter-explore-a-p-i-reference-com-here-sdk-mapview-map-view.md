---
title: "Map View"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapView///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/MapView</div>
<div class="cover">
<h1 class="cover">Map<wbr/>View</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view : <a href="https://developer.android.com/reference/kotlin/android/widget/FrameLayout.html">FrameLayout</a>, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-base</div><p class="paragraph">A view that can display a map. </p><p class="paragraph">The content of the map is controlled by /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene, which is accessible by calling /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-map-scene. To display a map, map scene needs to be loaded with loadScene. </p><p class="paragraph">Manipulating the way the map is displayed is possible using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera, which is accessible by calling /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-camera. </p><p class="paragraph">Gesture handling can be modified through the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-gestures-gestures object, which is accessible by calling /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-gestures. </p><h2 class="">Permissions</h2> To use the MapView the following application permissions need to be present: android.permission.INTERNET and android.permission.ACCESS_NETWORK_STATE <h2 class="">Rendering mode</h2><code class="lang-kotlin">MapView</code> can draw the map using either <code class="lang-kotlin">SurfaceView</code> or <code class="lang-kotlin">TextureView</code>. <p class="paragraph"><code class="lang-kotlin">SurfaceView</code> is the default method, offers best performance and works best for single screen applications where there's a single <code class="lang-kotlin">MapView</code> which is not part of a complex view hierarchy and takes no part in any UI animations. This method is known to cause graphical glitches in some scenarios (like embedding multiple <code class="lang-kotlin">MapView</code>s inside a view pager), especially on Android 12 and newer. </p><p class="paragraph"><code class="lang-kotlin">TextureView</code> is less performant, but behaves like any other view and can be easily transformed and animated, making it a better fit for applications with complex UI and/or multiple <code class="lang-kotlin">MapView</code>s as part of a complex view hierarchy. </p><p class="paragraph">Rendering mode can only be set when creating a <code class="lang-kotlin">MapView</code>, by setting /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-options-render-mode and passing the options to the constructor. </p><h2 class="">Coordinate systems</h2> When dealing with view coordinates, physical pixels are used. MapView provides ways to translate between view and geographic coordinates using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-view-to-geo-coordinates and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-geo-to-view-coordinates methods. Note that those two methods only work when the MapView is fully ready, so if there is a need to call them during lifecycle changes, they should be called from within /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-ready-listener-on-map-view-ready. See Lifecycle section below for more details. <h2 class="">Map caching</h2><p class="paragraph">Two caching mechanisms are supported. First is in-memory cache, which keeps some number of map tiles around in memory to avoid repeated network requests or storage reads. The second mechanism is persistent cache that stores downloaded map data on the device. Persistent cache requires storage permission to be granted. </p><h2 class="">Lifecycle</h2><p class="paragraph">For <code class="lang-kotlin">MapView</code> to work correctly, it is required to call its lifecycle methods from the owner Activity: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-create, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-resume, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-pause, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-destroy and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-save-instance-state. </p><p class="paragraph">When dealing with multiple <code class="lang-kotlin">MapView</code>s in a single Activity, an extra identifier needs to be passed to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-create and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-save-instance-state. This identifier needs to be unique to all the <code class="lang-kotlin">MapView</code>s owned by the <code class="lang-kotlin">Activity</code> and needs to be the same when recreating the <code class="lang-kotlin">Activity</code>. </p><p class="paragraph">A <code class="lang-kotlin">MapView</code> is considered valid only after /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-create or /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-create and before /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-destroy is called. <code class="lang-kotlin">MapView</code> is also invalidated when the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-native-engine it is using is destroyed. /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-is-valid can be used to check the state of <code class="lang-kotlin">MapView</code>. </p><p class="paragraph"><code class="lang-kotlin">MapView</code> offers additional lifecycle event exposed through /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-ready-listener. This can be used to determine when <code class="lang-kotlin">MapView</code> is fully ready for action, which means that map scene is loaded and drawing surface is ready to render a map. This is important for coordinate conversion methods and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-viewport-size, which work only when those conditions are met. When <code class="lang-kotlin">OnReadyListener</code> is set in <code class="lang-kotlin">Activity</code>'s <code class="lang-kotlin">onCreate()</code> before any other operation is performed on the <code class="lang-kotlin">MapView</code>, then /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-ready-listener-on-map-view-ready is called: </p><ul><li>after map scene is successfully loaded for the first time</li><li>some time after <code class="lang-kotlin">Activity</code>'s <code class="lang-kotlin">onResume()</code>, assuming map scene had been loaded before</li></ul><p class="paragraph">Note: Before using any API in this class, <code class="lang-kotlin">SDKNativeEngine</code> must be already initialized.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="MapView" data-filterable-set=":modules:dokkaHtml/release" data-name="1211561056%2FConstructors%2F1617540583" id="1211561056%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-map-view</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(context: <a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a>, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-options)</div><div class="brief">Simple constructor to use when creating a map view from code.</div><div class="symbol monospace">constructor(context: <a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a>)</div><div class="brief">Simple constructor to use when creating a map view from code.</div><div class="symbol monospace">constructor(context: <a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a>, attrs: <a href="https://developer.android.com/reference/kotlin/android/util/AttributeSet.html">AttributeSet</a>)</div><div class="brief">Creates a new instance.</div><div class="symbol monospace">constructor(context: <a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a>, attrs: <a href="https://developer.android.com/reference/kotlin/android/util/AttributeSet.html">AttributeSet</a>, defStyleAttr: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>)</div><div class="brief">Creates a new instance.</div><div class="symbol monospace">constructor(engine: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-native-engine, context: <a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a>, attrs: <a href="https://developer.android.com/reference/kotlin/android/util/AttributeSet.html">AttributeSet</a>, defStyleAttr: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>)</div><div class="brief">Creates a new instance.</div><div class="symbol monospace">constructor(engine: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-native-engine, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-options, context: <a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a>, attrs: <a href="https://developer.android.com/reference/kotlin/android/util/AttributeSet.html">AttributeSet</a>, defStyleAttr: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>)</div><div class="brief">Creates a new instance.</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="OnReadyListener" data-filterable-set=":modules:dokkaHtml/release" data-name="-1374088103%2FClasslikes%2F1617540583" id="-1374088103%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-ready-listener</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/java/lang/FunctionalInterface.html">FunctionalInterface</a></div></div>interface /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-ready-listener</div><div class="brief">Listener that gets notified when MapView is fully initialized and ready to handle all operations, which means that map scene is loaded and drawing surface is ready to render a map.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="TakeScreenshotCallback" data-filterable-set=":modules:dokkaHtml/release" data-name="-2014661953%2FClasslikes%2F1617540583" id="-2014661953%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-take-screenshot-callback</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/java/lang/FunctionalInterface.html">FunctionalInterface</a></div></div>interface /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-take-screenshot-callback</div><div class="brief">Callback to be called on retrieval of screenshot.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="ViewPin" data-filterable-set=":modules:dokkaHtml/release" data-name="1926400641%2FClasslikes%2F1617540583" id="1926400641%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-view-pin</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">interface /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-view-pin</div><div class="brief">A ViewPin is used to display Android views at a fixed location on the map.</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="addLifecycleListener" data-filterable-set=":modules:dokkaHtml/release" data-name="1555040436%2FFunctions%2F1617540583" id="1555040436%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-add-lifecycle-listener</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-add-lifecycle-listener(@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a> lifecycleListener: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener)</div><div class="brief">Adds a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener to this map view.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="geoToViewCoordinates" data-filterable-set=":modules:dokkaHtml/release" data-name="-1231283554%2FFunctions%2F1617540583" id="-1231283554%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-geo-to-view-coordinates</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html">Nullable</a></div></div>open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-geo-to-view-coordinates(@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a> geoCoordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point2-d</div><div class="brief">Converts geographical coordinates to view coordinates (in pixels).</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getCamera" data-filterable-set=":modules:dokkaHtml/release" data-name="-1233873757%2FFunctions%2F1617540583" id="-1233873757%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-camera</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a></div></div>open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-camera(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera</div><div class="brief">Gets the camera control object for the map.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getFrameRate" data-filterable-set=":modules:dokkaHtml/release" data-name="-1154654171%2FFunctions%2F1617540583" id="-1154654171%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-frame-rate</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-frame-rate(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief">Gets maximum render frame rate in frames per second.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getGestures" data-filterable-set=":modules:dokkaHtml/release" data-name="-1910783906%2FFunctions%2F1617540583" id="-1910783906%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-gestures</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a></div></div>open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-gestures(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-gestures-gestures</div><div class="brief">Returns the gestures control object</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getHereMap" data-filterable-set=":modules:dokkaHtml/release" data-name="-1582639386%2FFunctions%2F1617540583" id="-1582639386%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-here-map</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a></div></div>open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-here-map(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-here-map</div><div class="brief">Gets the HereMap associated with this map view.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getMapContext" data-filterable-set=":modules:dokkaHtml/release" data-name="-336904875%2FFunctions%2F1617540583" id="-336904875%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-map-context</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a></div></div>open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-map-context(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context</div><div class="brief">Gets the map context associated with this map view.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getMapScene" data-filterable-set=":modules:dokkaHtml/release" data-name="-752334120%2FFunctions%2F1617540583" id="-752334120%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-map-scene</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a></div></div>open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-map-scene(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene</div><div class="brief">Gets the map scene associated with this map view.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getPixelScale" data-filterable-set=":modules:dokkaHtml/release" data-name="1888392388%2FFunctions%2F1617540583" id="1888392388%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-pixel-scale</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-pixel-scale(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief">Gets the pixel scale factor used by this MapView.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getPrimaryLanguage" data-filterable-set=":modules:dokkaHtml/release" data-name="-781601416%2FFunctions%2F1617540583" id="-781601416%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-primary-language</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html">Nullable</a></div></div>open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-primary-language(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-language-code</div><div class="brief">Gets code of currently set primary map display language.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getSecondaryLanguage" data-filterable-set=":modules:dokkaHtml/release" data-name="2032262918%2FFunctions%2F1617540583" id="2032262918%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-secondary-language</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html">Nullable</a></div></div>open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-secondary-language(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-language-code</div><div class="brief">Gets code of currently set secondary map display language.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getShadowQuality" data-filterable-set=":modules:dokkaHtml/release" data-name="623910419%2FFunctions%2F1617540583" id="623910419%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-shadow-quality</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-shadow-quality(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-shadow-quality</div><div class="brief">Gets the currently set shadow quality.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getViewPins" data-filterable-set=":modules:dokkaHtml/release" data-name="2143297797%2FFunctions%2F1617540583" id="2143297797%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-view-pins</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-view-pins(): <a href="https://developer.android.com/reference/kotlin/java/util/List.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-view-pin&gt;</div><div class="brief">Returns a copy of the list of views currently pinned to the map view.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getViewportSize" data-filterable-set=":modules:dokkaHtml/release" data-name="-1482953727%2FFunctions%2F1617540583" id="-1482953727%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-viewport-size</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-viewport-size(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-size2-d</div><div class="brief">Gets the size of this map view in physical pixels.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getWatermarkSize" data-filterable-set=":modules:dokkaHtml/release" data-name="1787206157%2FFunctions%2F1617540583" id="1787206157%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-watermark-size</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a></div></div>open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-get-watermark-size(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-size2-d</div><div class="brief">Returns the watermark size in physical pixels.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="isValid" data-filterable-set=":modules:dokkaHtml/release" data-name="-1163394580%2FFunctions%2F1617540583" id="-1163394580%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-is-valid</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-is-valid(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief">Returns whether this <code class="lang-kotlin">MapView</code> is valid.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="onCreate" data-filterable-set=":modules:dokkaHtml/release" data-name="-1665374918%2FFunctions%2F1617540583" id="-1665374918%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-create</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-create(bundle: <a href="https://developer.android.com/reference/kotlin/android/os/Bundle.html">Bundle</a>)</div><div class="brief">Call this method in the onCreate() method of the lifecycle owner before calling any other MapView methods.</div><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-create(bundle: <a href="https://developer.android.com/reference/kotlin/android/os/Bundle.html">Bundle</a>, identifier: <a href="https://developer.android.com/reference/kotlin/java/lang/String.html">String</a>)</div><div class="brief">Call this method in the onCreate() method of the lifecycle owner before calling any other MapView methods if there are multiple MapViews instances to (re)create.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="onDestroy" data-filterable-set=":modules:dokkaHtml/release" data-name="843332003%2FFunctions%2F1617540583" id="843332003%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-destroy</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-destroy()</div><div class="brief">Call this method in the onDestroy() method of the lifecycle owner</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="onPause" data-filterable-set=":modules:dokkaHtml/release" data-name="898551591%2FFunctions%2F1617540583" id="898551591%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-pause</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-pause()</div><div class="brief">Call this method in the onPause() method of the lifecycle owner.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="onResume" data-filterable-set=":modules:dokkaHtml/release" data-name="1171438480%2FFunctions%2F1617540583" id="1171438480%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-resume</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-resume()</div><div class="brief">Call this method in the onResume() method of the lifecycle owner.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="onSaveInstanceState" data-filterable-set=":modules:dokkaHtml/release" data-name="-1207199410%2FFunctions%2F1617540583" id="-1207199410%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-save-instance-state</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-save-instance-state(bundle: <a href="https://developer.android.com/reference/kotlin/android/os/Bundle.html">Bundle</a>)</div><div class="brief">Call this method in the onSaveInstance() method of the lifecycle owner.</div><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-save-instance-state(bundle: <a href="https://developer.android.com/reference/kotlin/android/os/Bundle.html">Bundle</a>, identifier: <a href="https://developer.android.com/reference/kotlin/java/lang/String.html">String</a>)</div><div class="brief">Call this method in the onSaveInstance() method of the lifecycle owner if multiple MapView instances are present.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="pick" data-filterable-set=":modules:dokkaHtml/release" data-name="22876001%2FFunctions%2F1617540583" id="22876001%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-pick</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-pick(@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html">Nullable</a> filter: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-map-pick-filter, @<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a> viewArea: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-rectangle2-d, @<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a> callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-base-map-pick-callback)</div><div class="brief">Returns all map content located inside the specified pick area.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="pinView" data-filterable-set=":modules:dokkaHtml/release" data-name="1022143004%2FFunctions%2F1617540583" id="1022143004%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-pin-view</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html">Nullable</a></div></div>open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-pin-view(@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a> view: <a href="https://developer.android.com/reference/kotlin/android/view/View.html">View</a>, coordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-view-pin</div><div class="brief">Pins a <a href="https://developer.android.com/reference/kotlin/android/view/View.html">View</a> to the <code class="lang-kotlin">MapView</code> and returns a proxy object that can be used to control the pinning.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeLifecycleListener" data-filterable-set=":modules:dokkaHtml/release" data-name="-1981134193%2FFunctions%2F1617540583" id="-1981134193%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-remove-lifecycle-listener</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-remove-lifecycle-listener(@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a> lifecycleListener: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener)</div><div class="brief">Removes a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener from this map view.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setFixedSize" data-filterable-set=":modules:dokkaHtml/release" data-name="991774576%2FFunctions%2F1617540583" id="991774576%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-fixed-size</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-fixed-size(width: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>, height: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>, factor: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>)</div><div class="brief">Requests a fixed size to be used for rendering this MapView.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setFrameRate" data-filterable-set=":modules:dokkaHtml/release" data-name="-1972839134%2FFunctions%2F1617540583" id="-1972839134%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-frame-rate</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-frame-rate(value: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>)</div><div class="brief">Sets maximum render frame rate in frames per second.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setOnReadyListener" data-filterable-set=":modules:dokkaHtml/release" data-name="1177817677%2FFunctions%2F1617540583" id="1177817677%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-on-ready-listener</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-on-ready-listener(readyListener: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-on-ready-listener)</div><div class="brief">Sets the OnReadyListener, which will be notified once MapView initialization has been finished.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setPrimaryLanguage" data-filterable-set=":modules:dokkaHtml/release" data-name="-5902699%2FFunctions%2F1617540583" id="-5902699%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-primary-language</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-primary-language(@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html">Nullable</a> languageCode: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-language-code)</div><div class="brief">Set desired primary map display language for all instances of MapView.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setSecondaryLanguage" data-filterable-set=":modules:dokkaHtml/release" data-name="1311414435%2FFunctions%2F1617540583" id="1311414435%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-secondary-language</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-secondary-language(@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html">Nullable</a> languageCode: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-language-code)</div><div class="brief">Set desired secondary map display language for all instances of MapView.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setShadowQuality" data-filterable-set=":modules:dokkaHtml/release" data-name="259832498%2FFunctions%2F1617540583" id="259832498%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-shadow-quality</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-shadow-quality(shadowQuality: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-shadow-quality)</div><div class="brief">Set desired shadow quality for all instances of MapView/MapSurface.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setVisibility" data-filterable-set=":modules:dokkaHtml/release" data-name="594342249%2FFunctions%2F1617540583" id="594342249%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-visibility</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-visibility(visibility: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>)</div><div class="brief">Sets the visibility of MapView.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setWatermarkLocation" data-filterable-set=":modules:dokkaHtml/release" data-name="880578879%2FFunctions%2F1617540583" id="880578879%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-watermark-location</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-set-watermark-location(@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a> anchor: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-anchor2-d, @<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a> offset: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point2-d)</div><div class="brief">Sets the position of the HERE logo watermark within the map view.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="takeScreenshot" data-filterable-set=":modules:dokkaHtml/release" data-name="1529294786%2FFunctions%2F1617540583" id="1529294786%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-take-screenshot</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-take-screenshot(callback: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-take-screenshot-callback)</div><div class="brief">Asynchronously retrieves a screenshot of current map view.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="unpinView" data-filterable-set=":modules:dokkaHtml/release" data-name="-2143811402%2FFunctions%2F1617540583" id="-2143811402%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-unpin-view</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-unpin-view(@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a> view: <a href="https://developer.android.com/reference/kotlin/android/view/View.html">View</a>)</div><div class="brief">Removes a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-view-pin from the <code class="lang-kotlin">MapView</code> by specifying the corresponding view.</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="viewToGeoCoordinates" data-filterable-set=":modules:dokkaHtml/release" data-name="-25160360%2FFunctions%2F1617540583" id="-25160360%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-view-to-geo-coordinates</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html">Nullable</a></div></div>open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-view-to-geo-coordinates(@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a> viewCoordinates: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point2-d): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates</div><div class="brief">Converts view coordinates to geographical coordinates.</div></div></div>
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
