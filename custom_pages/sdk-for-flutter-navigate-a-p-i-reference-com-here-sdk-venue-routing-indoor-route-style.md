---
title: "IndoorRouteStyle"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-venue-routing-indoor-route-style"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>IndoorRouteStyle</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.venue.routing/IndoorRouteStyle///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.venue.routing</a><span class="delimiter">/</span><span class="current">IndoorRouteStyle</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Indoor</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Style</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">IndoorRouteStyle</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">Represents a style of the indoor route. Contains information about route colors and widths. Optionally, this style allows to set <a href="../../com.here.sdk.mapview/-map-marker/index.html">com.here.sdk.mapview.MapMarker</a> instances that can be used for specific route elements.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-1908098277%2FConstructors%2F1617540583" anchor-label="IndoorRouteStyle" id="-1908098277%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-indoor-route-style.html"><span>Indoor</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Style</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1908098277%2FConstructors%2F1617540583"></span>
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
        <div class="table"><a data-name="-458491797%2FClasslikes%2F1617540583" anchor-label="Companion" id="-458491797%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-458491797%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="-1983954116%2FProperties%2F1617540583" anchor-label="destinationMarker" id="-1983954116%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="destination-marker.html"><span>destination</span><wbr></wbr><span><span>Marker</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1983954116%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="destination-marker.html">destinationMarker</a><span class="token operator">: </span><a href="../../com.here.sdk.mapview/-map-marker/index.html">MapMarker</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">A <a href="../../com.here.sdk.mapview/-map-marker/index.html">com.here.sdk.mapview.MapMarker</a> instance representing the destination of the route. By default, no map marker is provided The destination map marker of the resulting route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="809129856%2FProperties%2F1617540583" anchor-label="driveMarker" id="809129856%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="drive-marker.html"><span>drive</span><wbr></wbr><span><span>Marker</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="809129856%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="drive-marker.html">driveMarker</a><span class="token operator">: </span><a href="../../com.here.sdk.mapview/-map-marker/index.html">MapMarker</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">A <a href="../../com.here.sdk.mapview/-map-marker/index.html">com.here.sdk.mapview.MapMarker</a> instance representing the drive point of the route. By default, no map marker is provided. The drive map marker of the resulting route. It signals that a user should take a transport vehicle.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1132450420%2FProperties%2F1617540583" anchor-label="indoorPolylineColor" id="1132450420%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="indoor-polyline-color.html"><span>indoor</span><wbr></wbr><span>Polyline</span><wbr></wbr><span><span>Color</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1132450420%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="indoor-polyline-color.html">indoorPolylineColor</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-color/index.html">Color</a></div><div class="brief "><p class="paragraph">The color value. The default color is #48DAD0. The color of polylines for indoor route sections.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-559040143%2FProperties%2F1617540583" anchor-label="indoorPolylineWidth" id="-559040143%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="indoor-polyline-width.html"><span>indoor</span><wbr></wbr><span>Polyline</span><wbr></wbr><span><span>Width</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-559040143%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="indoor-polyline-width.html">indoorPolylineWidth</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">The width in pixels. Default value is 15 pixels The width in pixels of polylines for indoor route sections.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-401157720%2FProperties%2F1617540583" anchor-label="startMarker" id="-401157720%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="start-marker.html"><span>start</span><wbr></wbr><span><span>Marker</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-401157720%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="start-marker.html">startMarker</a><span class="token operator">: </span><a href="../../com.here.sdk.mapview/-map-marker/index.html">MapMarker</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">A <a href="../../com.here.sdk.mapview/-map-marker/index.html">com.here.sdk.mapview.MapMarker</a> instance representing the start of the route. By default, no map marker is provided. The start map marker of the resulting route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1248937165%2FProperties%2F1617540583" anchor-label="walkMarker" id="-1248937165%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="walk-marker.html"><span>walk</span><wbr></wbr><span><span>Marker</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1248937165%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="walk-marker.html">walkMarker</a><span class="token operator">: </span><a href="../../com.here.sdk.mapview/-map-marker/index.html">MapMarker</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">A <a href="../../com.here.sdk.mapview/-map-marker/index.html">com.here.sdk.mapview.MapMarker</a> instance representing the walk point of the route. By default, no map marker is provided. The walk map marker of the resulting route. It signals that a user should leave their transport vehicle and continue on foot.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="41736126%2FFunctions%2F1617540583" anchor-label="getIndoorMarkerFor" id="41736126%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-indoor-marker-for.html"><span>get</span><wbr></wbr><span>Indoor</span><wbr></wbr><span>Marker</span><wbr></wbr><span><span>For</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="41736126%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-indoor-marker-for.html"><span class="token function">getIndoorMarkerFor</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">feature<span class="token operator">: </span><a href="../../com.here.sdk.routing/-indoor-level-change-features/index.html">IndoorLevelChangeFeatures</a><span class="token punctuation">, </span></span><span class="parameter ">deltaZ<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.mapview/-map-marker/index.html">MapMarker</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns a <a href="../../com.here.sdk.mapview/-map-marker/index.html">com.here.sdk.mapview.MapMarker</a> for a given indoor feature and the number of levels to change. By default, no map markers are provided.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-448240570%2FFunctions%2F1617540583" anchor-label="setIndoorMarkersFor" id="-448240570%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-indoor-markers-for.html"><span>set</span><wbr></wbr><span>Indoor</span><wbr></wbr><span>Markers</span><wbr></wbr><span><span>For</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-448240570%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-indoor-markers-for.html"><span class="token function">setIndoorMarkersFor</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">feature<span class="token operator">: </span><a href="../../com.here.sdk.routing/-indoor-level-change-features/index.html">IndoorLevelChangeFeatures</a><span class="token punctuation">, </span></span><span class="parameter ">upMarker<span class="token operator">: </span><a href="../../com.here.sdk.mapview/-map-marker/index.html">MapMarker</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">downMarker<span class="token operator">: </span><a href="../../com.here.sdk.mapview/-map-marker/index.html">MapMarker</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">exitMarker<span class="token operator">: </span><a href="../../com.here.sdk.mapview/-map-marker/index.html">MapMarker</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets map markers for the given indoor feature.</p></div></div></div>
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
