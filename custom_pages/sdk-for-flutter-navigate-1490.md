---
title: "MapScene"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapScene</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapScene///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MapScene</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span><span>Scene</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">MapScene</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><p class="paragraph">Represents a map scene and exposes the functionality to manipulate its content.</p><h2> Map schemes</h2><p class="paragraph">The content of the displayed map and how it looks is specified by a <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapScheme</a> which is set when loading a scene with <a href="sdk-for-flutter-explore-load-scene">com.here.sdk.mapview.MapScene.loadScene</a>. It is also possible to load your own custom map scheme from a file bundled with your application. Supported file formats are:</p><ul><li><p class="paragraph">JSON (file extension '.json'; e.g. 'my_custom_style.json')</p></li><li><p class="paragraph">ZIP archive (file extension '.zip'; e.g. 'my_custom_style.zip'), with the following archive structure:</p></li></ul><ul><li><p class="paragraph">root folder: any, not empty (e.g. 'my_custom_style')</p></li><li><p class="paragraph">JSON configuration: '<root folder>/style.json'</p></li><li><p class="paragraph">custom assets folder: '<root folder>/assets'</p></li></ul><h2> Map features</h2><p class="paragraph">Different map schemes offer different sets of features, for example showing traffic or 3D buildings. Some features have multiple modes of operation, but most have only one. <a href="sdk-for-flutter-explore-get-supported-features">com.here.sdk.mapview.MapScene.getSupportedFeatures</a> can be used to check what features and modes are supported for the current scene. Features can be enabled using <a href="sdk-for-flutter-explore-enable-features">com.here.sdk.mapview.MapScene.enableFeatures</a> and disabled with <a href="sdk-for-flutter-explore-disable-features">com.here.sdk.mapview.MapScene.disableFeatures</a>. Checking which features are currently enabled can be done using <a href="sdk-for-flutter-explore-get-active-features">com.here.sdk.mapview.MapScene.getActiveFeatures</a>. For convenience, <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapFeatures</a> and <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapFeatureModes</a> hold constants for feature and mode names.</p><p class="paragraph">Since version 4.15.0, map features cannot be controlled using <a href="sdk-for-flutter-explore-set-layer-visibility">com.here.sdk.mapview.MapScene.setLayerVisibility</a>, since <a href="sdk-for-flutter-explore-set-layer-visibility">com.here.sdk.mapview.MapScene.setLayerVisibility</a> controls only visibility of the layers which are corresponding to the features enabled either by <a href="sdk-for-flutter-explore-enable-features">com.here.sdk.mapview.MapScene.enableFeatures</a> or enabled by default for the scene.</p><h2> Map layers</h2><p class="paragraph">A map scheme is organized in layers, which can be controlled using <a href="sdk-for-flutter-explore-set-layer-visibility">com.here.sdk.mapview.MapScene.setLayerVisibility</a>. It's possible to change the visibility state of any map layer as long as the name is known.</p><p class="paragraph">Layer visibility settings persist between scene reloading.</p><h2> User content</h2><p class="paragraph">User generated content can be visualised on the map using <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapPolyline</a>, <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapPolygon</a>, <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMarker</a>, <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMarkerCluster</a>, <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapArrow</a>, <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMarker3D</a> and <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapImageOverlay</a> (collectively referred to as &quot;map items&quot;). Those can be added to and removed from the scene by respective add and remove methods. The render order of the map items is according to the list above. The order of objects within the same type can be controlled using the <code class="lang-kotlin">drawOrder</code> property of each object.</p><p class="paragraph">Be careful when adding a very large number of map items as this can have a negative impact on the performance of the app. To work around this limitation the following approach can be used: Register to map camera updates using <a href="sdk-for-flutter-explore-add-listener">com.here.sdk.mapview.MapCamera.addListener</a>. Query the bounding box of the camera viewport using <a href="sdk-for-flutter-explore-bounding-box">com.here.sdk.mapview.MapCamera.boundingBox</a> (it may be extended) and then use the method <a href="sdk-for-flutter-explore-contains">com.here.sdk.core.GeoBox.contains</a> in combination with <a href="sdk-for-flutter-explore-distance-to-target-in-meters">com.here.sdk.mapview.MapCamera.State.distanceToTargetInMeters</a> to determine which map items are actually visible to the user in the current camera viewport and thus need to be added to the map.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-2079948464%2FClasslikes%2F1617540583" anchor-label="Companion" id="-2079948464%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2079948464%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-131692399%2FClasslikes%2F1617540583" anchor-label="LoadSceneCallback" id="-131692399%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Load</span><wbr></wbr><span>Scene</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-131692399%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">LoadSceneCallback</a></div><div class="brief "><p class="paragraph">Called on the main thread after <code class="lang-kotlin">loadScene()</code> method finishes loading the scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-503278201%2FClasslikes%2F1617540583" anchor-label="MapPickFilter" id="-503278201%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Map</span><wbr></wbr><span>Pick</span><wbr></wbr><span><span>Filter</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-503278201%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">MapPickFilter</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Filter for the map content to be picked.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-1846503564%2FProperties%2F1617540583" anchor-label="lights" id="-1846503564%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-lights"><span><span>lights</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1846503564%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-lights">lights</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapSceneLights</a></div><div class="brief "><p class="paragraph">Controls lights present in the scene. Provides access to a MapSceneLights instance that controls the lights in the scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-2101049656%2FFunctions%2F1617540583" anchor-label="addMapArrow" id="-2101049656%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-map-arrow"><span>add</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Arrow</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2101049656%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-map-arrow"><span class="token function">addMapArrow</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapArrow<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapArrow</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a map arrow to this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1929028350%2FFunctions%2F1617540583" anchor-label="addMapImageOverlay" id="-1929028350%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-map-image-overlay"><span>add</span><wbr></wbr><span>Map</span><wbr></wbr><span>Image</span><wbr></wbr><span><span>Overlay</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1929028350%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-map-image-overlay"><span class="token function">addMapImageOverlay</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">overlay<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapImageOverlay</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a map image overlay to this map scene. Adding the same overlay instance multiple times has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1819153784%2FFunctions%2F1617540583" anchor-label="addMapMarker" id="1819153784%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-map-marker"><span>add</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Marker</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1819153784%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-map-marker"><span class="token function">addMapMarker</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">marker<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMarker</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a map marker to this map scene. Adding the same marker instance multiple times has no effect. Adding a marker that is already part of a map marker cluster has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-221298442%2FFunctions%2F1617540583" anchor-label="addMapMarker3d" id="-221298442%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-map-marker3d"><span>add</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Marker3d</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-221298442%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-map-marker3d"><span class="token function">addMapMarker3d</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">marker<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMarker3D</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a 3D map marker to this map scene. Does nothing if the marker instance was already added to the scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1508269480%2FFunctions%2F1617540583" anchor-label="addMapMarkerCluster" id="1508269480%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-map-marker-cluster"><span>add</span><wbr></wbr><span>Map</span><wbr></wbr><span>Marker</span><wbr></wbr><span><span>Cluster</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1508269480%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-map-marker-cluster"><span class="token function">addMapMarkerCluster</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">cluster<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMarkerCluster</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a map marker cluster to the map. Either the contained individual map markers or the cluster markers will be displayed. Adding the same map marker cluster instance multiple times has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-123825099%2FFunctions%2F1617540583" anchor-label="addMapMarkers" id="-123825099%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-map-markers"><span>add</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Markers</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-123825099%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-map-markers"><span class="token function">addMapMarkers</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">markers<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MapMarker</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds multiple map markers to this map scene. Adding the same marker instances multiple times has no effect. Adding markers that are already part of a map marker cluster has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1658123465%2FFunctions%2F1617540583" anchor-label="addMapMarkers3d" id="-1658123465%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-map-markers3d"><span>add</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Markers3d</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1658123465%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-map-markers3d"><span class="token function">addMapMarkers3d</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">markers<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MapMarker3D</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds multiple 3D map markers to this map scene. Adding the same 3D marker instances multiple times has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="961816168%2FFunctions%2F1617540583" anchor-label="addMapPolygon" id="961816168%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-map-polygon"><span>add</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Polygon</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="961816168%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-map-polygon"><span class="token function">addMapPolygon</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapPolygon<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapPolygon</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a map polygon to this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="61332825%2FFunctions%2F1617540583" anchor-label="addMapPolygons" id="61332825%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-map-polygons"><span>add</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Polygons</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="61332825%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-map-polygons"><span class="token function">addMapPolygons</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapPolygons<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MapPolygon</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds multiple map polygons to this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1693769708%2FFunctions%2F1617540583" anchor-label="addMapPolyline" id="1693769708%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-map-polyline"><span>add</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Polyline</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1693769708%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-map-polyline"><span class="token function">addMapPolyline</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapPolyline<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapPolyline</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a map polyline to this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-906407819%2FFunctions%2F1617540583" anchor-label="addMapPolylines" id="-906407819%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-map-polylines"><span>add</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Polylines</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-906407819%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-map-polylines"><span class="token function">addMapPolylines</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapPolylines<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MapPolyline</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds map polylines to this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1628937262%2FFunctions%2F1617540583" anchor-label="disableFeatures" id="1628937262%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-disable-features"><span>disable</span><wbr></wbr><span><span>Features</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1628937262%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-disable-features"><span class="token function">disableFeatures</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">features<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Disables specified map features. Those will become inactive after next map redraw, meaning that <a href="sdk-for-flutter-explore-get-active-features">com.here.sdk.mapview.MapScene.getActiveFeatures</a> will return updated list of active features only after the redraw happens.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-912245601%2FFunctions%2F1617540583" anchor-label="enableFeatures" id="-912245601%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-enable-features"><span>enable</span><wbr></wbr><span><span>Features</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-912245601%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-enable-features"><span class="token function">enableFeatures</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">features<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Enables specified map features. Those will become active after next map redraw, meaning that <a href="sdk-for-flutter-explore-get-active-features">com.here.sdk.mapview.MapScene.getActiveFeatures</a> will return updated list of active features only after the redraw happens.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="131210192%2FFunctions%2F1617540583" anchor-label="getActiveFeatures" id="131210192%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-active-features"><span>get</span><wbr></wbr><span>Active</span><wbr></wbr><span><span>Features</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="131210192%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-active-features"><span class="token function">getActiveFeatures</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Gets map features that are currently active. Active features are features that are either enabled via a call to <a href="sdk-for-flutter-explore-enable-features">com.here.sdk.mapview.MapScene.enableFeatures</a> or that are enabled by default in the scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2085843772%2FFunctions%2F1617540583" anchor-label="getSupportedFeatures" id="2085843772%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-supported-features"><span>get</span><wbr></wbr><span>Supported</span><wbr></wbr><span><span>Features</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2085843772%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-supported-features"><span class="token function">getSupportedFeatures</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">&gt;</span><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Gets features and all of their modes supported by the currently loaded scene configuration.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1993428859%2FFunctions%2F1617540583" anchor-label="loadScene" id="-1993428859%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-load-scene"><span>load</span><wbr></wbr><span><span>Scene</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1993428859%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-load-scene"><span class="token function">loadScene</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">options<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapSceneLoadOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScene.LoadSceneCallback</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Asynchronously loads a map scene using MapSceneLoadOptions.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-load-scene"><span class="token function">loadScene</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapScheme<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScheme</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScene.LoadSceneCallback</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Asynchronously loads a map scene described by a specified map scheme. Any previous map scene config will be replaced. The loaded scene is cached and so any changes made to the scene files on disk might not get reflected on a successive call to this function. Instead the reloadScene API can handle such use-cases to force-update the scene.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-load-scene"><span class="token function">loadScene</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">configurationFile<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScene.LoadSceneCallback</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Asynchronously loads a map scene described by a specified file in one of the supported formats. Any previous map scene config will be replaced.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-load-scene"><span class="token function">loadScene</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">configurationFile<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">watermarkStyle<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WatermarkStyle</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScene.LoadSceneCallback</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Asynchronously loads a map scene described by a specified file in one of the supported formats. The style of the HERE watermark matching the map scheme is specified. Any previous map scene config will be replaced.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1576412662%2FFunctions%2F1617540583" anchor-label="reloadScene" id="1576412662%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-reload-scene"><span>reload</span><wbr></wbr><span><span>Scene</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1576412662%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-reload-scene"><span class="token function">reloadScene</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Asynchronously reloads the current map scene from file. This skips any cached data used internally and reloads the scene including any changes made to the (custom) map styles in JSON.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2025575880%2FFunctions%2F1617540583" anchor-label="removeAllMapItems" id="2025575880%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-all-map-items"><span>remove</span><wbr></wbr><span>All</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Items</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2025575880%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-all-map-items"><span class="token function">removeAllMapItems</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes all map objects from this map scene. This includes polylines, polygons, markers and clusters, arrows, image overlays. It is much faster than removing the objects one by one.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-916327057%2FFunctions%2F1617540583" anchor-label="removeAllMapMarkers" id="-916327057%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-all-map-markers"><span>remove</span><wbr></wbr><span>All</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Markers</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-916327057%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-all-map-markers"><span class="token function">removeAllMapMarkers</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes all map markers from this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="874454910%2FFunctions%2F1617540583" anchor-label="removeAllMapMarkers3d" id="874454910%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-all-map-markers3d"><span>remove</span><wbr></wbr><span>All</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Markers3d</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="874454910%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-all-map-markers3d"><span class="token function">removeAllMapMarkers3d</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes all 3D map markers from this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1711889991%2FFunctions%2F1617540583" anchor-label="removeAllMapPolygons" id="-1711889991%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-all-map-polygons"><span>remove</span><wbr></wbr><span>All</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Polygons</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1711889991%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-all-map-polygons"><span class="token function">removeAllMapPolygons</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes all map polygons from this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-347483979%2FFunctions%2F1617540583" anchor-label="removeAllMapPolylines" id="-347483979%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-all-map-polylines"><span>remove</span><wbr></wbr><span>All</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Polylines</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-347483979%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-all-map-polylines"><span class="token function">removeAllMapPolylines</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes all map polylines from this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="693410435%2FFunctions%2F1617540583" anchor-label="removeMapArrow" id="693410435%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-map-arrow"><span>remove</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Arrow</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="693410435%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-map-arrow"><span class="token function">removeMapArrow</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapArrow<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapArrow</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a map arrow from this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1673448829%2FFunctions%2F1617540583" anchor-label="removeMapImageOverlay" id="1673448829%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-map-image-overlay"><span>remove</span><wbr></wbr><span>Map</span><wbr></wbr><span>Image</span><wbr></wbr><span><span>Overlay</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1673448829%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-map-image-overlay"><span class="token function">removeMapImageOverlay</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">overlay<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapImageOverlay</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a map image overlay from this map scene. Removing an overlay instance that is not part of this scene has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1354226061%2FFunctions%2F1617540583" anchor-label="removeMapMarker" id="-1354226061%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-map-marker"><span>remove</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Marker</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1354226061%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-map-marker"><span class="token function">removeMapMarker</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">marker<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMarker</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a map marker from this map scene. Removing a marker instance that is not a part of this scene or belongs to a marker cluster has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="670194801%2FFunctions%2F1617540583" anchor-label="removeMapMarker3d" id="670194801%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-map-marker3d"><span>remove</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Marker3d</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="670194801%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-map-marker3d"><span class="token function">removeMapMarker3d</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">marker<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMarker3D</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a 3D map marker from this map scene. Removing a marker instance that is not on this scene has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1745197923%2FFunctions%2F1617540583" anchor-label="removeMapMarkerCluster" id="1745197923%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-map-marker-cluster"><span>remove</span><wbr></wbr><span>Map</span><wbr></wbr><span>Marker</span><wbr></wbr><span><span>Cluster</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1745197923%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-map-marker-cluster"><span class="token function">removeMapMarkerCluster</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">cluster<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMarkerCluster</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a map marker cluster from the map. Removing a map marker cluster that is not on this scene has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1115689328%2FFunctions%2F1617540583" anchor-label="removeMapMarkers" id="1115689328%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-map-markers"><span>remove</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Markers</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1115689328%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-map-markers"><span class="token function">removeMapMarkers</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">markers<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MapMarker</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes multiple map markers from this map scene. Removing marker instances that are not a part of this scene or belong to a marker cluster has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-213552398%2FFunctions%2F1617540583" anchor-label="removeMapMarkers3d" id="-213552398%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-map-markers3d"><span>remove</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Markers3d</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-213552398%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-map-markers3d"><span class="token function">removeMapMarkers3d</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">markers<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MapMarker3D</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes multiple 3D map markers from this map scene. Removing marker instances that are not a part of this scene has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="770565283%2FFunctions%2F1617540583" anchor-label="removeMapPolygon" id="770565283%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-map-polygon"><span>remove</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Polygon</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="770565283%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-map-polygon"><span class="token function">removeMapPolygon</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapPolygon<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapPolygon</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a map polygon from this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1528756180%2FFunctions%2F1617540583" anchor-label="removeMapPolygons" id="1528756180%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-map-polygons"><span>remove</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Polygons</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1528756180%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-map-polygons"><span class="token function">removeMapPolygons</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapPolygons<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MapPolygon</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes multiple map polygon from this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1709704345%2FFunctions%2F1617540583" anchor-label="removeMapPolyline" id="-1709704345%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-map-polyline"><span>remove</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Polyline</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1709704345%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-map-polyline"><span class="token function">removeMapPolyline</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapPolyline<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapPolyline</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a map polyline from this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="538163248%2FFunctions%2F1617540583" anchor-label="removeMapPolylines" id="538163248%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-map-polylines"><span>remove</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Polylines</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="538163248%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-map-polylines"><span class="token function">removeMapPolylines</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapPolylines<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MapPolyline</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes map polylines from this map scene.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="662036798%2FFunctions%2F1617540583" anchor-label="setLayerVisibility" id="662036798%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-layer-visibility"><span>set</span><wbr></wbr><span>Layer</span><wbr></wbr><span><span>Visibility</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="662036798%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-layer-visibility"><span class="token function">setLayerVisibility</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">layerName<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">visibility<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VisibilityState</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Immediately changes the visibility of a specified map layer.</p></div></div></div>
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
