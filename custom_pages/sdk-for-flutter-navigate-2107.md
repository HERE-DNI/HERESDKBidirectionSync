---
title: "Maneuver"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>Maneuver</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.routing/Maneuver///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.routing</a><span class="delimiter">/</span><span class="current">Maneuver</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Maneuver</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Maneuver</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><p class="paragraph">This class provides all the information for a maneuver. The directional information (e.g. road names, road numbers and signpost direction) is stored in <a href="sdk-for-flutter-explore-road-texts">com.here.sdk.routing.Maneuver.roadTexts</a> and <a href="sdk-for-flutter-explore-next-road-texts">com.here.sdk.routing.Maneuver.nextRoadTexts</a> attributes. As for the motorway exit information, it can be obtained from <a href="sdk-for-flutter-explore-exit-sign-texts">com.here.sdk.routing.Maneuver.exitSignTexts</a> attribute.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1207930028%2FClasslikes%2F1617540583" anchor-label="Companion" id="1207930028%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1207930028%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-126503009%2FProperties%2F1617540583" anchor-label="action" id="-126503009%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-action"><span><span>action</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-126503009%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-action">action</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">ManeuverAction</a></div><div class="brief "><p class="paragraph">Indicates the maneuver action.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1618925514%2FProperties%2F1617540583" anchor-label="coordinates" id="1618925514%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-coordinates"><span><span>coordinates</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1618925514%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-coordinates">coordinates</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a></div><div class="brief "><p class="paragraph">Geographic coordinates where the maneuver is located.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1071079458%2FProperties%2F1617540583" anchor-label="countryCode" id="1071079458%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-country-code"><span>country</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1071079458%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-country-code">countryCode</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The country code of the maneuver position. The value is <code class="lang-kotlin">null</code> when no data is available.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1727485953%2FProperties%2F1617540583" anchor-label="duration" id="1727485953%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-duration"><span><span>duration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1727485953%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-duration">duration</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Duration</a></div><div class="brief "><p class="paragraph">The estimated time in seconds needed to perform the maneuver.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1903959014%2FProperties%2F1617540583" anchor-label="exitSignTexts" id="-1903959014%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-exit-sign-texts"><span>exit</span><wbr></wbr><span>Sign</span><wbr></wbr><span><span>Texts</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1903959014%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-exit-sign-texts">exitSignTexts</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LocalizedTexts</a></div><div class="brief "><p class="paragraph">The textual attributes of the exit sign. These might contain exit number(s) and/or name(s). These attributes are only available for the Navigate license. Otherwise, the attributes are always empty.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1863426554%2FProperties%2F1617540583" anchor-label="intersectionNames" id="-1863426554%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-intersection-names"><span>intersection</span><wbr></wbr><span><span>Names</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1863426554%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-intersection-names">intersectionNames</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LocalizedTexts</a></div><div class="brief "><p class="paragraph">The textual attributes of the intersection. These attributes are only available for the Navigate license. Otherwise, the attributes are always empty. <strong>Note:</strong> Routes calculated with OfflineRoutingEngine are not supported.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="413503008%2FProperties%2F1617540583" anchor-label="lengthInMeters" id="413503008%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-length-in-meters"><span>length</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="413503008%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-length-in-meters">lengthInMeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The length of the maneuver in meters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="140530386%2FProperties%2F1617540583" anchor-label="nextRoadTexts" id="140530386%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-next-road-texts"><span>next</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Texts</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="140530386%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-next-road-texts">nextRoadTexts</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RoadTexts</a></div><div class="brief "><p class="paragraph">The textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point. These attributes are only available for the Navigate license. Otherwise, the attributes are always empty.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="317703138%2FProperties%2F1617540583" anchor-label="offset" id="317703138%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-offset"><span><span>offset</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="317703138%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-offset">offset</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">Index over <a href="sdk-for-flutter-explore-geometry">com.here.sdk.routing.Section.geometry</a> where the maneuver is located.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2115117953%2FProperties%2F1617540583" anchor-label="roadTexts" id="-2115117953%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-road-texts"><span>road</span><wbr></wbr><span><span>Texts</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2115117953%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-road-texts">roadTexts</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RoadTexts</a></div><div class="brief "><p class="paragraph">The textual attributes of the current road containing road names, road numbers and signpost direction (towards) information. <strong>Note:</strong> These attributes are only available for the Navigate license. Otherwise, the attributes are always empty.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1591441287%2FProperties%2F1617540583" anchor-label="roundaboutAngleInDegrees" id="1591441287%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-roundabout-angle-in-degrees"><span>roundabout</span><wbr></wbr><span>Angle</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Degrees</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1591441287%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-roundabout-angle-in-degrees">roundaboutAngleInDegrees</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout. This is done to provide a better orientation for drivers. For better results, the incoming and outcoming route parts can be around 50 meters in length. In addition, these parts lie usually around 30 meters away from the actual roundabout. Therefore, the resulting arc does not necessarily represent the exact curved path a vehicle has to follow within a roundabout from the point of entry to the point of exit. Instead, it reflects the route path before and after the roundabout to highlight the directional change along the route. The angle can have a value from -360.0 to 360.0, and it is positive in right-hand side driving country, and negative in left-hand side countries. Note that the value is available for both the enter roundabout actions and the exit roundabout actions. Both maneuvers have the same value. When the incoming or outgoing route parts are curvy or when the roundabout itself is not representing a perfect circle, then the accuracy of the angle may be compromised. <strong>Note:</strong> These attributes are only available for the Navigate license.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-115720504%2FProperties%2F1617540583" anchor-label="sectionIndex" id="-115720504%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-section-index"><span>section</span><wbr></wbr><span><span>Index</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-115720504%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-section-index">sectionIndex</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">Index over <a href="sdk-for-flutter-explore-sections">com.here.sdk.routing.Route.sections</a> indicating the section to which the maneuver belongs to.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1998539224%2FProperties%2F1617540583" anchor-label="signpost" id="1998539224%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-signpost"><span><span>signpost</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1998539224%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-signpost">signpost</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Signpost</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Gets the <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.Signpost</a> object.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1468721341%2FProperties%2F1617540583" anchor-label="spanIndex" id="1468721341%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-span-index"><span>span</span><wbr></wbr><span><span>Index</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1468721341%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-span-index">spanIndex</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">Index over <a href="sdk-for-flutter-explore-spans">com.here.sdk.routing.Section.spans</a> indicating the first span after the maneuver point. <strong>Note:</strong> The span index for the last maneuvers (those maneuvers with maneuver action set to <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.ManeuverAction.ARRIVE</a>) cannot be used, since these maneuvers are placed after the last span of the route and the span index for them would be greater than the span list size.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-774153592%2FProperties%2F1617540583" anchor-label="text" id="-774153592%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-text"><span><span>text</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-774153592%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-text">text</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">The maneuver instruction. The text is formatted and localized as specified via <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteTextOptions</a>. <strong>Note for users of the Navigate license:</strong> This text is meant to be displayed in a preview context, whereas real-time <code class="lang-kotlin">EventTextListener</code> texts are meant to be used for spoken voice announcements during a trip.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-587286007%2FProperties%2F1617540583" anchor-label="turnAngleInDegrees" id="-587286007%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-turn-angle-in-degrees"><span>turn</span><wbr></wbr><span>Angle</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Degrees</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-587286007%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-turn-angle-in-degrees">turnAngleInDegrees</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The angle of the turn component of the maneuver. The angle increases clockwise and small values are used for going straight, i.e. a positive number means there is a right turn and a negative number is a left turn. Some maneuvers like Depart, Arrive and Roundabout pass doesn't have a well defined angle, so the value is omitted. <strong>Note:</strong> These attributes are only available for the Navigate license.</p></div></div></div>
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
