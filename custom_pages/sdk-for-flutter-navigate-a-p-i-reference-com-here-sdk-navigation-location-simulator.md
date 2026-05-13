---
title: "LocationSimulator"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-navigation-location-simulator"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>LocationSimulator</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.navigation/LocationSimulator///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.navigation</a><span class="delimiter">/</span><span class="current">LocationSimulator</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Location</span><wbr></wbr><span><span>Simulator</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">LocationSimulator</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">Use the <code class="lang-kotlin">LocationSimulator</code> to generate locations along a route or a GPX document. It notifies the registered object about the current location at a fixed interval. In order to customize the interval, see <a href="../-location-simulator-options/index.html">com.here.sdk.navigation.LocationSimulatorOptions</a>. The locations are closely matched to the shape and proceeded from the start to the destination as found in the provided route or the GPX document. When providing a route, the <code class="lang-kotlin">LocationSimulator</code> uses a base speed taken from each span found in the provided route object. This base speed can be multiplied upfront with a custom <code class="lang-kotlin">speedFactor</code> for simulation purposes. Effectively, this means that traffic-related information is not considered to adjust the speed of the simulation. For the <code class="lang-kotlin">GPXTrack</code>, a speed is either based on timestamps in the original file or provided by the user. The following data is read from a <code class="lang-kotlin">GPXTrack</code> and inserted into the provided <code class="lang-kotlin">Location</code> object: <code class="lang-kotlin">latitude</code>, <code class="lang-kotlin">longitude</code>, <code class="lang-kotlin">altitude</code>, <code class="lang-kotlin">time</code>, <code class="lang-kotlin">bearingInDegrees</code>, <code class="lang-kotlin">speedInMetersPerSecond</code>, <code class="lang-kotlin">horizontalAccuracyInMeters</code>, <code class="lang-kotlin">verticalAccuracyInMeters</code> and <code class="lang-kotlin">locationTechnology</code>.</p><p class="paragraph">Note that simulation works offline and independent from any map data</p><ul><li><p class="paragraph">only the information found in the provided route or GPX document is considered.</p></li><li><p class="paragraph">When initializing the <code class="lang-kotlin">LocationSimulator</code> with a route, then interpolations take place between the vertices of the route's polyline. The distance between interpolated locations is a function of the current span's speed and the set notification interval.</p></li><li><p class="paragraph">When initializing the <code class="lang-kotlin">LocationSimulator</code> with a GPX file, the <code class="lang-kotlin">LocationSimulator</code> does not apply any interpolation on the provided location data as this would shadow the recorded GPX data.</p></li></ul><p class="paragraph">Notifications will stop after the entire route has been traveled.</p><p class="paragraph"><strong>Note:</strong> Map-matched locations are only accessible from <a href="../-route-progress/index.html">com.here.sdk.navigation.RouteProgress</a>.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-776341897%2FConstructors%2F1617540583" anchor-label="LocationSimulator" id="-776341897%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-location-simulator.html"><span>Location</span><wbr></wbr><span><span>Simulator</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-776341897%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">route<span class="token operator">: </span><a href="../../com.here.sdk.routing/-route/index.html">Route</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-location-simulator-options/index.html">LocationSimulatorOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">gpxTrack<span class="token operator">: </span><a href="../-g-p-x-track/index.html">GPXTrack</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-location-simulator-options/index.html">LocationSimulatorOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Create a location simulator</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-1289020006%2FClasslikes%2F1617540583" anchor-label="Companion" id="-1289020006%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1289020006%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="1972682291%2FProperties%2F1617540583" anchor-label="listener" id="1972682291%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="listener.html"><span><span>listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1972682291%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="listener.html">listener</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-location-listener/index.html">LocationListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The object that notifies on location updates.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1697160675%2FFunctions%2F1617540583" anchor-label="pause" id="-1697160675%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="pause.html"><span><span>pause</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1697160675%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="pause.html"><span class="token function">pause</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Pauses sending notifications to the subscribers. Calling this function has no effect when location provider is not started.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1986230438%2FFunctions%2F1617540583" anchor-label="resume" id="-1986230438%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="resume.html"><span><span>resume</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1986230438%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="resume.html"><span class="token function">resume</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Resumes sending notifications to the subscribers. Calling this function has no effect when location provider is not started.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1075735247%2FFunctions%2F1617540583" anchor-label="start" id="-1075735247%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="start.html"><span><span>start</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1075735247%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="start.html"><span class="token function">start</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Starts the location provider to send notifications to the subscribers. Calling this method will always start the location simulator from the route's first <a href="../../com.here.sdk.routing/-waypoint/index.html">com.here.sdk.routing.Waypoint</a>, even if a simulation has already been started or stopped.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1537807269%2FFunctions%2F1617540583" anchor-label="stop" id="1537807269%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="stop.html"><span><span>stop</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1537807269%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="stop.html"><span class="token function">stop</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Stops the location provider from sending notifications to the subscribers.</p></div></div></div>
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
