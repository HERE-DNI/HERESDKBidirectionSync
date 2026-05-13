---
title: "AreaCameraBehavior"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-navigation-area-camera-behavior"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>AreaCameraBehavior</title>
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
            <a class="library-name--link" href="../../../index.html">
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.navigation/AreaCameraBehavior///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.navigation</a><span class="delimiter">/</span><span class="current">AreaCameraBehavior</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Area</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Behavior</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">AreaCameraBehavior</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a>, <a href="../-camera-behavior/index.html">CameraBehavior</a></div><p class="paragraph">Use this class to show an overview of geo points. By default, the orientation of the camera will be perpendicular to the Earth's surface (ie. looking towards the center of the Earth), while bearing will be towards north.</p><p class="paragraph">Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are subject to change without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="339703140%2FConstructors%2F1617540583" anchor-label="AreaCameraBehavior" id="339703140%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-area-camera-behavior.html"><span>Area</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Behavior</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="339703140%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-397549351%2FClasslikes%2F1617540583" anchor-label="Companion" id="-397549351%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-397549351%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="1109122463%2FProperties%2F1617540583" anchor-label="cameraAnimationDuration" id="1109122463%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="camera-animation-duration.html"><span>camera</span><wbr></wbr><span>Animation</span><wbr></wbr><span><span>Duration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1109122463%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="camera-animation-duration.html">cameraAnimationDuration</a><span class="token operator">: </span><a href="../../com.here.time/-duration/index.html">Duration</a></div><div class="brief "><p class="paragraph">The duration of camera animation in milliseconds. If there is an animation, it will last for specified period of time. Defaults to 500 milliseconds, or half a second.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="688728239%2FProperties%2F1617540583" anchor-label="cameraBearingInDegrees" id="688728239%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="camera-bearing-in-degrees.html"><span>camera</span><wbr></wbr><span>Bearing</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Degrees</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="688728239%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="camera-bearing-in-degrees.html">cameraBearingInDegrees</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">Camera bearing in degrees. The direction in which the camera will point in degrees clockwise, relative to true North. The input should range between \[0, 360]\. Defaults to true North (0 degrees).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-81694606%2FProperties%2F1617540583" anchor-label="cameraTiltInDegrees" id="-81694606%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="camera-tilt-in-degrees.html"><span>camera</span><wbr></wbr><span>Tilt</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Degrees</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-81694606%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="camera-tilt-in-degrees.html">cameraTiltInDegrees</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">Camera tilt in degrees. The tilt of the camera relative to the axis perpendicular to the ground. Defaults to 0 degrees, meaning that it will look straight down into the ground.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-899501058%2FProperties%2F1617540583" anchor-label="isCurrentPositionIncluded" id="-899501058%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-current-position-included.html"><span>is</span><wbr></wbr><span>Current</span><wbr></wbr><span>Position</span><wbr></wbr><span><span>Included</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-899501058%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="is-current-position-included.html">isCurrentPositionIncluded</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Include current position in camera view. Decides if the current position should be added to the set of visible points. Note that if the current position is in the vicinity of any of the visible points, setting this to <code class="lang-kotlin">false</code> will not explicitly exclude the current position from the camera view. However if displaying an area potentially away from the current position, this does need to be explicitly set to <code class="lang-kotlin">false</code> or it will try to include the current position. Defaults to false.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1551190693%2FProperties%2F1617540583" anchor-label="maxZoom" id="-1551190693%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="max-zoom.html"><span>max</span><wbr></wbr><span><span>Zoom</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1551190693%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="max-zoom.html">maxZoom</a><span class="token operator">: </span><a href="../../com.here.sdk.mapview/-map-measure/index.html">MapMeasure</a></div><div class="brief "><p class="paragraph">Maximal allowed zoom. Defines maximal zoom level to be applied to enclose geodetic bounding box. Defaults to a <a href="../../com.here.sdk.mapview/-map-measure/index.html">com.here.sdk.mapview.MapMeasure</a> with kind <a href="../../com.here.sdk.mapview/-map-measure/-kind/-z-o-o-m_-l-e-v-e-l/index.html">com.here.sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL</a> and value 20.0. Note: <a href="../../com.here.sdk.mapview/-map-measure/-kind/-s-c-a-l-e/index.html">com.here.sdk.mapview.MapMeasure.Kind.SCALE</a> is not supported.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="439366799%2FProperties%2F1617540583" anchor-label="normalizedPrincipalPoint" id="439366799%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="normalized-principal-point.html"><span>normalized</span><wbr></wbr><span>Principal</span><wbr></wbr><span><span>Point</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="439366799%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="normalized-principal-point.html">normalizedPrincipalPoint</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-anchor2-d/index.html">Anchor2D</a></div><div class="brief "><p class="paragraph">The normalized principal point. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1461007164%2FProperties%2F1617540583" anchor-label="principalPointAnimationDuration" id="1461007164%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="principal-point-animation-duration.html"><span>principal</span><wbr></wbr><span>Point</span><wbr></wbr><span>Animation</span><wbr></wbr><span><span>Duration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1461007164%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="principal-point-animation-duration.html">principalPointAnimationDuration</a><span class="token operator">: </span><a href="../../com.here.time/-duration/index.html">Duration</a></div><div class="brief "><p class="paragraph">The duration of principal point animation in milliseconds. If the principal point is changed, the change will be animated over this duration. Defaults to 500 milliseconds, or half a second.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1873995784%2FProperties%2F1617540583" anchor-label="viewRectangle" id="1873995784%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="view-rectangle.html"><span>view</span><wbr></wbr><span><span>Rectangle</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1873995784%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="view-rectangle.html">viewRectangle</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-rectangle2-d/index.html">Rectangle2D</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The view rectangle for camera updates. Defines a sub-space of the screen that the behavior should consider for camera updates. Defaults to <code class="lang-kotlin">null</code>. If not set, it uses the viewport bounds of the underlying map view.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="1798523625%2FFunctions%2F1617540583" anchor-label="getVisiblePoints" id="1798523625%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-visible-points.html"><span>get</span><wbr></wbr><span>Visible</span><wbr></wbr><span><span>Points</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1798523625%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-visible-points.html"><span class="token function">getVisiblePoints</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../../com.here.sdk.core/-geo-coordinates/index.html">GeoCoordinates</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Gets configured visible geo points.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2066165659%2FFunctions%2F1617540583" anchor-label="setVisiblePoints" id="2066165659%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-visible-points.html"><span>set</span><wbr></wbr><span>Visible</span><wbr></wbr><span><span>Points</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2066165659%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-visible-points.html"><span class="token function">setVisiblePoints</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">visiblePoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../../com.here.sdk.core/-geo-coordinates/index.html">GeoCoordinates</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets the list of geo points to show in the camera view.</p></div></div></div>
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
`
}</HTMLBlock>
