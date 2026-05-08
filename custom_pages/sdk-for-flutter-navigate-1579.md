---
title: "AutomotiveCameraBehavior"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>AutomotiveCameraBehavior</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.navigation/AutomotiveCameraBehavior///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.navigation</a><span class="delimiter">/</span><span class="current">AutomotiveCameraBehavior</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Automotive</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Behavior</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">AutomotiveCameraBehavior</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a>, <a href="sdk-for-flutter-explore-index">CameraBehavior</a></div><p class="paragraph">Provides a high-level camera controller for automotive navigation that manages both tracking and area camera behaviors. This class acts as a facade, delegating camera operations to either a <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TrackingCameraBehavior</a> for following the vehicle during navigation or an <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.AreaCameraBehavior</a> for showing overview areas such as points of interest or route previews.</p><p class="paragraph">The controller supports three states: tracking mode (following the vehicle), area mode (showing geographic regions), or inactive (no automatic camera control). The inactive state allows external control of the camera, such as when responding to user touch events or when UI logic temporarily disables automatic camera behavior.</p><p class="paragraph">Camera configuration, including animation durations, zoom policies, and maneuver handling settings, can be provided through a JSON configuration string or file. The configuration is validated and parsed during construction.</p><p class="paragraph">Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-734509880%2FConstructors%2F1617540583" anchor-label="AutomotiveCameraBehavior" id="-734509880%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-automotive-camera-behavior"><span>Automotive</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Behavior</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-734509880%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class with default camera behaviors and configuration. This constructor automatically creates and configures the underlying <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TrackingCameraBehavior</a> and <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.AreaCameraBehavior</a> instances with default settings.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">configJson<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class configured from a JSON string. The JSON configuration is validated during construction and applied to the underlying <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TrackingCameraBehavior</a> and <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.AreaCameraBehavior</a> instances.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-374119072%2FClasslikes%2F1617540583" anchor-label="ActiveCameraType" id="-374119072%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Active</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-374119072%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">ActiveCameraType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">AutomotiveCameraBehavior.ActiveCameraType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Defines the type of camera currently handling camera updates.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1147725839%2FClasslikes%2F1617540583" anchor-label="Companion" id="-1147725839%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1147725839%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1583551414%2FClasslikes%2F1617540583" anchor-label="OrientationMode" id="-1583551414%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Orientation</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1583551414%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">OrientationMode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">AutomotiveCameraBehavior.OrientationMode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Defines the visual presentation modes for the camera orientation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-1257551829%2FProperties%2F1617540583" anchor-label="activeCameraType" id="-1257551829%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-active-camera-type"><span>active</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1257551829%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-active-camera-type">activeCameraType</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">AutomotiveCameraBehavior.ActiveCameraType</a></div><div class="brief "><p class="paragraph">The active camera type. Defines which camera behavior is currently active: <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.AutomotiveCameraBehavior.ActiveCameraType.NONE</a> (free navigation), <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.AutomotiveCameraBehavior.ActiveCameraType.TRACKING</a>, or <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.AutomotiveCameraBehavior.ActiveCameraType.AREA</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="617496337%2FProperties%2F1617540583" anchor-label="isManeuverDetectionEnabled" id="617496337%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-maneuver-detection-enabled"><span>is</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span>Detection</span><wbr></wbr><span><span>Enabled</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="617496337%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-maneuver-detection-enabled">isManeuverDetectionEnabled</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Enables or disables automatic camera adjustments during upcoming maneuvers. When enabled, the tracking camera automatically adjusts zoom and framing to provide better visibility of upcoming turns and maneuvers during navigation. The specific adjustments and their timing are defined in the camera configuration.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1474368905%2FProperties%2F1617540583" anchor-label="normalizedPrincipalPoint" id="-1474368905%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-normalized-principal-point"><span>normalized</span><wbr></wbr><span>Principal</span><wbr></wbr><span><span>Point</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1474368905%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-normalized-principal-point">normalizedPrincipalPoint</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Anchor2D</a></div><div class="brief "><p class="paragraph">The normalized principal point. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1105756343%2FProperties%2F1617540583" anchor-label="orientationMode" id="1105756343%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-orientation-mode"><span>orientation</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1105756343%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-orientation-mode">orientationMode</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">AutomotiveCameraBehavior.OrientationMode</a></div><div class="brief "><p class="paragraph">The current orientation mode of the camera. Defines the camera's viewing angle and orientation for tracking mode. In <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.AutomotiveCameraBehavior.OrientationMode.MODE_2D</a>, the camera looks straight down and rotates with the vehicle heading. In <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.AutomotiveCameraBehavior.OrientationMode.MODE_3D</a>, the camera is tilted for a perspective view. In <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.AutomotiveCameraBehavior.OrientationMode.MODE_NORTH_UP</a>, the camera maintains north-up orientation regardless of vehicle heading.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2128270112%2FProperties%2F1617540583" anchor-label="viewRectangle" id="2128270112%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-view-rectangle"><span>view</span><wbr></wbr><span><span>Rectangle</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2128270112%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-view-rectangle">viewRectangle</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Rectangle2D</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The view rectangle for camera updates. Defines a sub-space of the screen that the behavior should consider for camera updates. This property is forwarded to both the tracking and area cameras, ensuring consistent viewport constraints across all camera modes. If not set, it uses the viewport bounds of the underlying map view.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-9425850%2FFunctions%2F1617540583" anchor-label="setAreaCameraBehaviorGeobox" id="-9425850%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-area-camera-behavior-geobox"><span>set</span><wbr></wbr><span>Area</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Behavior</span><wbr></wbr><span><span>Geobox</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-9425850%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-area-camera-behavior-geobox"><span class="token function">setAreaCameraBehaviorGeobox</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">geobox<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoBox</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Configures the Area camera to frame the specified geographic bounding box. The camera automatically calculates the appropriate zoom level and center position to ensure the entire area is visible within the viewport.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-761993003%2FFunctions%2F1617540583" anchor-label="setAreaCameraBehaviorVisiblePoints" id="-761993003%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-area-camera-behavior-visible-points"><span>set</span><wbr></wbr><span>Area</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Behavior</span><wbr></wbr><span>Visible</span><wbr></wbr><span><span>Points</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-761993003%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-area-camera-behavior-visible-points"><span class="token function">setAreaCameraBehaviorVisiblePoints</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">points<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">includeCurrentPosition<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Configures the Area camera to frame the specified points. The camera calculates the optimal zoom level and center position to display all provided coordinates within the viewport. Use this for showing a single point of interest or multiple points such as safety cameras.</p></div></div></div>
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
