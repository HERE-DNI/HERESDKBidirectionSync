---
title: "MapView"
slug: "sdk-for-flutter-explore"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapView</title>
    <link href="../../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../../";</script>
    <script>document.documentElement.classList.replace("no-js","js");</script>
    <script>const storage = localStorage.getItem("dokka-dark-mode")
    if (storage == null) {
        const osDarkSchemePreferred = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
        if (osDarkSchemePreferred === true) {
            document.getElementsByTagName("html")[0].classList.add("theme-dark")
        }
    } else {
        const savedDarkMode = JSON.parse(storage)
        if(savedDarkMode === true) {
            document.getElementsByTagName("html")[0].classList.add("theme-dark")
        }
    }
    </script>
<script type="text/javascript" src="https://unpkg.com/kotlin-playground@1/dist/playground.min.js" async="async"></script>
<script type="text/javascript" src="../../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../../styles/style.css" rel="Stylesheet">
<link href="../../../styles/main.css" rel="Stylesheet">
<link href="../../../styles/prism.css" rel="Stylesheet">
<link href="../../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
</head>
<body>
    <div class="root">
    <nav class="navigation theme-dark" id="navigation-wrapper">
            <a class="library-name--link" href="sdk-for-flutter-explore-index">
                    API Reference
            </a>
        <button class="navigation-controls--btn navigation-controls--btn_toc ui-kit_mobile-only" id="toc-toggle"
                type="button">Toggle table of contents
        </button>
        <div class="navigation-controls--break ui-kit_mobile-only"></div>
        <div class="library-version" id="library-version">
        </div>
        <div class="navigation-controls">
        <div class="filter-section filter-section_loading" id="filter-section">
                <button class="platform-tag platform-selector jvm-like" data-active=""
                        data-filter=":modules:dokkaHtml/release">androidJvm</button>
            <div class="dropdown filter-section--dropdown" data-role="dropdown" id="filter-section-dropdown">
                <button class="button button_dropdown filter-section--dropdown-toggle" role="combobox"
                        data-role="dropdown-toggle"
                        aria-controls="platform-tags-listbox"
                        aria-haspopup="listbox"
                        aria-expanded="false"
                        aria-label="Toggle source sets"
                ></button>
                <ul role="listbox" id="platform-tags-listbox" class="dropdown--list" data-role="dropdown-listbox">
                    <div class="dropdown--header"><span>Platform filter</span>
                        <button class="button" data-role="dropdown-toggle" aria-label="Close platform filter">
                            <i class="ui-kit-icon ui-kit-icon_cross"></i>
                        </button>
                    </div>
                        <li role="option" class="dropdown--option platform-selector-option jvm-like" tabindex="0">
                            <label class="checkbox">
                                <input type="checkbox" class="checkbox--input" id=":modules:dokkaHtml/release"
                                       data-filter=":modules:dokkaHtml/release"/>
                                <span class="checkbox--icon"></span>
                                androidJvm
                            </label>
                        </li>
                </ul>
                <div class="dropdown--overlay"></div>
            </div>
        </div>
            <button class="navigation-controls--btn navigation-controls--btn_theme" id="theme-toggle-button"
                    type="button">Switch theme
            </button>
            <div class="navigation-controls--btn navigation-controls--btn_search" id="searchBar" role="button">Search in
                API
            </div>
        </div>
    </nav>
        <div id="container">
            <div class="sidebar" id="leftColumn">
                <div class="dropdown theme-dark_mobile" data-role="dropdown" id="toc-dropdown">
                    <ul role="listbox" id="toc-listbox" class="dropdown--list dropdown--list_toc-list"
                        data-role="dropdown-listbox">
                        <div class="dropdown--header">
                            <span>
                                    API Reference
                            </span>
                            <button class="button" data-role="dropdown-toggle" aria-label="Close table of contents">
                                <i class="ui-kit-icon ui-kit-icon_cross"></i>
                            </button>
                        </div>
                        <div class="sidebar--inner" id="sideMenu"></div>
                    </ul>
                    <div class="dropdown--overlay"></div>
                </div>
            </div>
            <div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapView///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MapView</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span><span>View</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">MapView</a> : <a href="https://developer.android.com/reference/kotlin/android/widget/FrameLayout.html">FrameLayout</a>, <a href="sdk-for-flutter-explore-index">MapViewBase</a></div><p class="paragraph">A view that can display a map. </p><p class="paragraph">The content of the map is controlled by <a href="sdk-for-flutter-explore-index">MapScene</a>, which is accessible by calling <a href="sdk-for-flutter-explore-get-map-scene">getMapScene</a>. To display a map, map scene needs to be loaded with <span data-unresolved-link="com.here.sdk.mapview/MapScene/loadScene/#com.here.sdk.mapview.MapScheme#com.here.sdk.mapview.MapScene.LoadSceneCallback/PointingToDeclaration/">loadScene</span>. </p><p class="paragraph">Manipulating the way the map is displayed is possible using <a href="sdk-for-flutter-explore-index">MapCamera</a>, which is accessible by calling <a href="sdk-for-flutter-explore-get-camera">getCamera</a>. </p><p class="paragraph">Gesture handling can be modified through the <a href="sdk-for-flutter-explore-index">Gestures</a> object, which is accessible by calling <a href="sdk-for-flutter-explore-get-gestures">getGestures</a>. </p><h2 class="">Permissions</h2> To use the MapView the following application permissions need to be present: android.permission.INTERNET and android.permission.ACCESS_NETWORK_STATE <h2 class="">Rendering mode</h2><code class="lang-kotlin">MapView</code> can draw the map using either <code class="lang-kotlin">SurfaceView</code> or <code class="lang-kotlin">TextureView</code>. <p class="paragraph"><code class="lang-kotlin">SurfaceView</code> is the default method, offers best performance and works best for single screen applications where there's a single <code class="lang-kotlin">MapView</code> which is not part of a complex view hierarchy and takes no part in any UI animations. This method is known to cause graphical glitches in some scenarios (like embedding multiple <code class="lang-kotlin">MapView</code>s inside a view pager), especially on Android 12 and newer. </p><p class="paragraph"><code class="lang-kotlin">TextureView</code> is less performant, but behaves like any other view and can be easily transformed and animated, making it a better fit for applications with complex UI and/or multiple <code class="lang-kotlin">MapView</code>s as part of a complex view hierarchy. </p><p class="paragraph">Rendering mode can only be set when creating a <code class="lang-kotlin">MapView</code>, by setting <a href="sdk-for-flutter-explore-render-mode">renderMode</a> and passing the options to the constructor. </p><h2 class="">Coordinate systems</h2> When dealing with view coordinates, physical pixels are used. MapView provides ways to translate between view and geographic coordinates using <a href="sdk-for-flutter-explore-view-to-geo-coordinates">viewToGeoCoordinates</a> and <a href="sdk-for-flutter-explore-geo-to-view-coordinates">geoToViewCoordinates</a> methods. Note that those two methods only work when the MapView is fully ready, so if there is a need to call them during lifecycle changes, they should be called from within <a href="sdk-for-flutter-explore-on-map-view-ready">onMapViewReady</a>. See Lifecycle section below for more details. <h2 class="">Map caching</h2><p class="paragraph">Two caching mechanisms are supported. First is in-memory cache, which keeps some number of map tiles around in memory to avoid repeated network requests or storage reads. The second mechanism is persistent cache that stores downloaded map data on the device. Persistent cache requires storage permission to be granted. </p><h2 class="">Lifecycle</h2><p class="paragraph">For <code class="lang-kotlin">MapView</code> to work correctly, it is required to call its lifecycle methods from the owner Activity: <a href="sdk-for-flutter-explore-on-create">onCreate</a>, <a href="sdk-for-flutter-explore-on-resume">onResume</a>, <a href="sdk-for-flutter-explore-on-pause">onPause</a>, <a href="sdk-for-flutter-explore-on-destroy">onDestroy</a> and <a href="sdk-for-flutter-explore-on-save-instance-state">onSaveInstanceState</a>. </p><p class="paragraph">When dealing with multiple <code class="lang-kotlin">MapView</code>s in a single Activity, an extra identifier needs to be passed to <a href="sdk-for-flutter-explore-on-create">onCreate</a> and <a href="sdk-for-flutter-explore-on-save-instance-state">onSaveInstanceState</a>. This identifier needs to be unique to all the <code class="lang-kotlin">MapView</code>s owned by the <code class="lang-kotlin">Activity</code> and needs to be the same when recreating the <code class="lang-kotlin">Activity</code>. </p><p class="paragraph">A <code class="lang-kotlin">MapView</code> is considered valid only after <a href="sdk-for-flutter-explore-on-create">onCreate</a> or <a href="sdk-for-flutter-explore-on-create">onCreate</a> and before <a href="sdk-for-flutter-explore-on-destroy">onDestroy</a> is called. <code class="lang-kotlin">MapView</code> is also invalidated when the <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.SDKNativeEngine</a> it is using is destroyed. <a href="sdk-for-flutter-explore-is-valid">isValid</a> can be used to check the state of <code class="lang-kotlin">MapView</code>. </p><p class="paragraph"><code class="lang-kotlin">MapView</code> offers additional lifecycle event exposed through <a href="sdk-for-flutter-explore-index">OnReadyListener</a>. This can be used to determine when <code class="lang-kotlin">MapView</code> is fully ready for action, which means that map scene is loaded and drawing surface is ready to render a map. This is important for coordinate conversion methods and <a href="sdk-for-flutter-explore-get-viewport-size">getViewportSize</a>, which work only when those conditions are met. When <code class="lang-kotlin">OnReadyListener</code> is set in <code class="lang-kotlin">Activity</code>'s <code class="lang-kotlin">onCreate()</code> before any other operation is performed on the <code class="lang-kotlin">MapView</code>, then <a href="sdk-for-flutter-explore-on-map-view-ready">onMapViewReady</a> is called: </p><ul><li>after map scene is successfully loaded for the first time</li><li>some time after <code class="lang-kotlin">Activity</code>'s <code class="lang-kotlin">onResume()</code>, assuming map scene had been loaded before</li></ul><p class="paragraph">Note: Before using any API in this class, <code class="lang-kotlin">SDKNativeEngine</code> must be already initialized.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="1211561056%2FConstructors%2F1617540583" anchor-label="MapView" id="1211561056%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-map-view"><span>Map</span><wbr></wbr><span><span>View</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1211561056%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">context<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapViewOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Simple constructor to use when creating a map view from code.</div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">context<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Simple constructor to use when creating a map view from code.</div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">context<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a><span class="token punctuation">, </span></span><span class="parameter ">attrs<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/util/AttributeSet.html">AttributeSet</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Creates a new instance.</div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">context<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a><span class="token punctuation">, </span></span><span class="parameter ">attrs<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/util/AttributeSet.html">AttributeSet</a><span class="token punctuation">, </span></span><span class="parameter ">defStyleAttr<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Creates a new instance.</div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">engine<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SDKNativeEngine</a><span class="token punctuation">, </span></span><span class="parameter ">context<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a><span class="token punctuation">, </span></span><span class="parameter ">attrs<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/util/AttributeSet.html">AttributeSet</a><span class="token punctuation">, </span></span><span class="parameter ">defStyleAttr<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Creates a new instance.</div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">engine<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SDKNativeEngine</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapViewOptions</a><span class="token punctuation">, </span></span><span class="parameter ">context<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a><span class="token punctuation">, </span></span><span class="parameter ">attrs<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/util/AttributeSet.html">AttributeSet</a><span class="token punctuation">, </span></span><span class="parameter ">defStyleAttr<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Creates a new instance.</div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-1374088103%2FClasslikes%2F1617540583" anchor-label="OnReadyListener" id="-1374088103%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>On</span><wbr></wbr><span>Ready</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1374088103%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/java/lang/FunctionalInterface.html"><span class="token annotation builtin">FunctionalInterface</span></a></div></div><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">OnReadyListener</a></div><div class="brief ">Listener that gets notified when MapView is fully initialized and ready to handle all operations, which means that map scene is loaded and drawing surface is ready to render a map.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2014661953%2FClasslikes%2F1617540583" anchor-label="TakeScreenshotCallback" id="-2014661953%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Take</span><wbr></wbr><span>Screenshot</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2014661953%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/java/lang/FunctionalInterface.html"><span class="token annotation builtin">FunctionalInterface</span></a></div></div><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">TakeScreenshotCallback</a></div><div class="brief ">Callback to be called on retrieval of screenshot.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1926400641%2FClasslikes%2F1617540583" anchor-label="ViewPin" id="1926400641%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>View</span><wbr></wbr><span><span>Pin</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1926400641%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">ViewPin</a></div><div class="brief ">A ViewPin is used to display Android views at a fixed location on the map.</div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="1555040436%2FFunctions%2F1617540583" anchor-label="addLifecycleListener" id="1555040436%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-lifecycle-listener"><span>add</span><wbr></wbr><span>Lifecycle</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1555040436%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-lifecycle-listener"><span class="token function">addLifecycleListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>lifecycleListener<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapViewLifecycleListener</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Adds a <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapViewLifecycleListener</a> to this map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1231283554%2FFunctions%2F1617540583" anchor-label="geoToViewCoordinates" id="-1231283554%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-geo-to-view-coordinates"><span>geo</span><wbr></wbr><span>To</span><wbr></wbr><span>View</span><wbr></wbr><span><span>Coordinates</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1231283554%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html"><span class="token annotation builtin">Nullable</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-geo-to-view-coordinates"><span class="token function">geoToViewCoordinates</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>geoCoordinates<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a></div><div class="brief ">Converts geographical coordinates to view coordinates (in pixels).</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1233873757%2FFunctions%2F1617540583" anchor-label="getCamera" id="-1233873757%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-camera"><span>get</span><wbr></wbr><span><span>Camera</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1233873757%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-camera"><span class="token function">getCamera</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCamera</a></div><div class="brief ">Gets the camera control object for the map.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1154654171%2FFunctions%2F1617540583" anchor-label="getFrameRate" id="-1154654171%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-frame-rate"><span>get</span><wbr></wbr><span>Frame</span><wbr></wbr><span><span>Rate</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1154654171%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-frame-rate"><span class="token function">getFrameRate</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief ">Gets maximum render frame rate in frames per second.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1910783906%2FFunctions%2F1617540583" anchor-label="getGestures" id="-1910783906%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-gestures"><span>get</span><wbr></wbr><span><span>Gestures</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1910783906%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-gestures"><span class="token function">getGestures</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Gestures</a></div><div class="brief ">Returns the gestures control object</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1582639386%2FFunctions%2F1617540583" anchor-label="getHereMap" id="-1582639386%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-here-map"><span>get</span><wbr></wbr><span>Here</span><wbr></wbr><span><span>Map</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1582639386%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-here-map"><span class="token function">getHereMap</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">HereMap</a></div><div class="brief ">Gets the HereMap associated with this map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-336904875%2FFunctions%2F1617540583" anchor-label="getMapContext" id="-336904875%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-map-context"><span>get</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Context</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-336904875%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-map-context"><span class="token function">getMapContext</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapContext</a></div><div class="brief ">Gets the map context associated with this map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-752334120%2FFunctions%2F1617540583" anchor-label="getMapScene" id="-752334120%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-map-scene"><span>get</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Scene</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-752334120%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-map-scene"><span class="token function">getMapScene</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScene</a></div><div class="brief ">Gets the map scene associated with this map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1888392388%2FFunctions%2F1617540583" anchor-label="getPixelScale" id="1888392388%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-pixel-scale"><span>get</span><wbr></wbr><span>Pixel</span><wbr></wbr><span><span>Scale</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1888392388%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-pixel-scale"><span class="token function">getPixelScale</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief ">Gets the pixel scale factor used by this MapView.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-781601416%2FFunctions%2F1617540583" anchor-label="getPrimaryLanguage" id="-781601416%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-primary-language"><span>get</span><wbr></wbr><span>Primary</span><wbr></wbr><span><span>Language</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-781601416%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html"><span class="token annotation builtin">Nullable</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-primary-language"><span class="token function">getPrimaryLanguage</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LanguageCode</a></div><div class="brief ">Gets code of currently set primary map display language.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2032262918%2FFunctions%2F1617540583" anchor-label="getSecondaryLanguage" id="2032262918%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-secondary-language"><span>get</span><wbr></wbr><span>Secondary</span><wbr></wbr><span><span>Language</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2032262918%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html"><span class="token annotation builtin">Nullable</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-secondary-language"><span class="token function">getSecondaryLanguage</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LanguageCode</a></div><div class="brief ">Gets code of currently set secondary map display language.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="623910419%2FFunctions%2F1617540583" anchor-label="getShadowQuality" id="623910419%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-shadow-quality"><span>get</span><wbr></wbr><span>Shadow</span><wbr></wbr><span><span>Quality</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="623910419%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-shadow-quality"><span class="token function">getShadowQuality</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">ShadowQuality</a></div><div class="brief ">Gets the currently set shadow quality.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2143297797%2FFunctions%2F1617540583" anchor-label="getViewPins" id="2143297797%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-view-pins"><span>get</span><wbr></wbr><span>View</span><wbr></wbr><span><span>Pins</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2143297797%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-view-pins"><span class="token function">getViewPins</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/util/List.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MapView.ViewPin</a><span class="token operator">&gt;</span></div><div class="brief ">Returns a copy of the list of views currently pinned to the map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1482953727%2FFunctions%2F1617540583" anchor-label="getViewportSize" id="-1482953727%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-viewport-size"><span>get</span><wbr></wbr><span>Viewport</span><wbr></wbr><span><span>Size</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1482953727%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-viewport-size"><span class="token function">getViewportSize</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Size2D</a></div><div class="brief ">Gets the size of this map view in physical pixels.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1787206157%2FFunctions%2F1617540583" anchor-label="getWatermarkSize" id="1787206157%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-watermark-size"><span>get</span><wbr></wbr><span>Watermark</span><wbr></wbr><span><span>Size</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1787206157%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-watermark-size"><span class="token function">getWatermarkSize</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Size2D</a></div><div class="brief ">Returns the watermark size in physical pixels.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1163394580%2FFunctions%2F1617540583" anchor-label="isValid" id="-1163394580%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-valid"><span>is</span><wbr></wbr><span><span>Valid</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1163394580%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-is-valid"><span class="token function">isValid</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief ">Returns whether this <code class="lang-kotlin">MapView</code> is valid.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1665374918%2FFunctions%2F1617540583" anchor-label="onCreate" id="-1665374918%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-on-create"><span>on</span><wbr></wbr><span><span>Create</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1665374918%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-on-create"><span class="token function">onCreate</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">bundle<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/os/Bundle.html">Bundle</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Call this method in the onCreate() method of the lifecycle owner before calling any other MapView methods.</div><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-on-create"><span class="token function">onCreate</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">bundle<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/os/Bundle.html">Bundle</a><span class="token punctuation">, </span></span><span class="parameter ">identifier<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/lang/String.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Call this method in the onCreate() method of the lifecycle owner before calling any other MapView methods if there are multiple MapViews instances to (re)create.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="843332003%2FFunctions%2F1617540583" anchor-label="onDestroy" id="843332003%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-on-destroy"><span>on</span><wbr></wbr><span><span>Destroy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="843332003%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-on-destroy"><span class="token function">onDestroy</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief ">Call this method in the onDestroy() method of the lifecycle owner</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="898551591%2FFunctions%2F1617540583" anchor-label="onPause" id="898551591%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-on-pause"><span>on</span><wbr></wbr><span><span>Pause</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="898551591%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-on-pause"><span class="token function">onPause</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief ">Call this method in the onPause() method of the lifecycle owner.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1171438480%2FFunctions%2F1617540583" anchor-label="onResume" id="1171438480%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-on-resume"><span>on</span><wbr></wbr><span><span>Resume</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1171438480%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-on-resume"><span class="token function">onResume</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief ">Call this method in the onResume() method of the lifecycle owner.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1207199410%2FFunctions%2F1617540583" anchor-label="onSaveInstanceState" id="-1207199410%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-on-save-instance-state"><span>on</span><wbr></wbr><span>Save</span><wbr></wbr><span>Instance</span><wbr></wbr><span><span>State</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1207199410%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-on-save-instance-state"><span class="token function">onSaveInstanceState</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">bundle<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/os/Bundle.html">Bundle</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Call this method in the onSaveInstance() method of the lifecycle owner.</div><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-on-save-instance-state"><span class="token function">onSaveInstanceState</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">bundle<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/os/Bundle.html">Bundle</a><span class="token punctuation">, </span></span><span class="parameter ">identifier<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/lang/String.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Call this method in the onSaveInstance() method of the lifecycle owner if multiple MapView instances are present.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="22876001%2FFunctions%2F1617540583" anchor-label="pick" id="22876001%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-pick"><span><span>pick</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="22876001%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-pick"><span class="token function">pick</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html"><span class="token annotation builtin">Nullable</span></a> </span>filter<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScene.MapPickFilter</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>viewArea<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Rectangle2D</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapViewBase.MapPickCallback</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Returns all map content located inside the specified pick area.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1022143004%2FFunctions%2F1617540583" anchor-label="pinView" id="1022143004%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-pin-view"><span>pin</span><wbr></wbr><span><span>View</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1022143004%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html"><span class="token annotation builtin">Nullable</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-pin-view"><span class="token function">pinView</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>view<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/view/View.html">View</a><span class="token punctuation">, </span></span><span class="parameter ">coordinates<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapView.ViewPin</a></div><div class="brief ">Pins a <a href="https://developer.android.com/reference/kotlin/android/view/View.html">View</a> to the <code class="lang-kotlin">MapView</code> and returns a proxy object that can be used to control the pinning.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1981134193%2FFunctions%2F1617540583" anchor-label="removeLifecycleListener" id="-1981134193%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-lifecycle-listener"><span>remove</span><wbr></wbr><span>Lifecycle</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1981134193%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-lifecycle-listener"><span class="token function">removeLifecycleListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>lifecycleListener<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapViewLifecycleListener</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Removes a <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapViewLifecycleListener</a> from this map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="991774576%2FFunctions%2F1617540583" anchor-label="setFixedSize" id="991774576%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-fixed-size"><span>set</span><wbr></wbr><span>Fixed</span><wbr></wbr><span><span>Size</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="991774576%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-fixed-size"><span class="token function">setFixedSize</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">width<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">height<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">factor<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Requests a fixed size to be used for rendering this MapView.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1972839134%2FFunctions%2F1617540583" anchor-label="setFrameRate" id="-1972839134%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-frame-rate"><span>set</span><wbr></wbr><span>Frame</span><wbr></wbr><span><span>Rate</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1972839134%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-frame-rate"><span class="token function">setFrameRate</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Sets maximum render frame rate in frames per second.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1177817677%2FFunctions%2F1617540583" anchor-label="setOnReadyListener" id="1177817677%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-on-ready-listener"><span>set</span><wbr></wbr><span>On</span><wbr></wbr><span>Ready</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1177817677%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-on-ready-listener"><span class="token function">setOnReadyListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">readyListener<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapView.OnReadyListener</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Sets the OnReadyListener, which will be notified once MapView initialization has been finished.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-5902699%2FFunctions%2F1617540583" anchor-label="setPrimaryLanguage" id="-5902699%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-primary-language"><span>set</span><wbr></wbr><span>Primary</span><wbr></wbr><span><span>Language</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-5902699%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-primary-language"><span class="token function">setPrimaryLanguage</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html"><span class="token annotation builtin">Nullable</span></a> </span>languageCode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LanguageCode</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Set desired primary map display language for all instances of MapView.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1311414435%2FFunctions%2F1617540583" anchor-label="setSecondaryLanguage" id="1311414435%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-secondary-language"><span>set</span><wbr></wbr><span>Secondary</span><wbr></wbr><span><span>Language</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1311414435%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-secondary-language"><span class="token function">setSecondaryLanguage</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html"><span class="token annotation builtin">Nullable</span></a> </span>languageCode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LanguageCode</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Set desired secondary map display language for all instances of MapView.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="259832498%2FFunctions%2F1617540583" anchor-label="setShadowQuality" id="259832498%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-shadow-quality"><span>set</span><wbr></wbr><span>Shadow</span><wbr></wbr><span><span>Quality</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="259832498%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-shadow-quality"><span class="token function">setShadowQuality</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">shadowQuality<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">ShadowQuality</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Set desired shadow quality for all instances of MapView/MapSurface.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="594342249%2FFunctions%2F1617540583" anchor-label="setVisibility" id="594342249%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-visibility"><span>set</span><wbr></wbr><span><span>Visibility</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="594342249%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-visibility"><span class="token function">setVisibility</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">visibility<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Sets the visibility of MapView.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="880578879%2FFunctions%2F1617540583" anchor-label="setWatermarkLocation" id="880578879%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-watermark-location"><span>set</span><wbr></wbr><span>Watermark</span><wbr></wbr><span><span>Location</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="880578879%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-watermark-location"><span class="token function">setWatermarkLocation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>anchor<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Anchor2D</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>offset<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Sets the position of the HERE logo watermark within the map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1529294786%2FFunctions%2F1617540583" anchor-label="takeScreenshot" id="1529294786%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-take-screenshot"><span>take</span><wbr></wbr><span><span>Screenshot</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1529294786%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-take-screenshot"><span class="token function">takeScreenshot</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapView.TakeScreenshotCallback</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Asynchronously retrieves a screenshot of current map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2143811402%2FFunctions%2F1617540583" anchor-label="unpinView" id="-2143811402%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-unpin-view"><span>unpin</span><wbr></wbr><span><span>View</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2143811402%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-unpin-view"><span class="token function">unpinView</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>view<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/view/View.html">View</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Removes a <a href="sdk-for-flutter-explore-index">ViewPin</a> from the <code class="lang-kotlin">MapView</code> by specifying the corresponding view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-25160360%2FFunctions%2F1617540583" anchor-label="viewToGeoCoordinates" id="-25160360%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-view-to-geo-coordinates"><span>view</span><wbr></wbr><span>To</span><wbr></wbr><span>Geo</span><wbr></wbr><span><span>Coordinates</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-25160360%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html"><span class="token annotation builtin">Nullable</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-view-to-geo-coordinates"><span class="token function">viewToGeoCoordinates</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>viewCoordinates<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a></div><div class="brief ">Converts view coordinates to geographical coordinates.</div></div></div>
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
        <a href="#content" id="go-to-top-link" class="footer--button footer--button_go-to-top"></a>
        <span>© 2026 Copyright</span>
        <span class="pull-right">
            <span>Generated by </span>
            <a class="footer--link footer--link_external" href="https://github.com/Kotlin/dokka">
                <span>dokka</span>
            </a>
        </span>
    </div>
            </div>
        </div>
    </div>
</body>
</html>
</div>
`}</HTMLBlock>
