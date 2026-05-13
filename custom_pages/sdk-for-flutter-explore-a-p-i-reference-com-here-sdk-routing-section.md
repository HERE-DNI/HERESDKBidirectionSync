---
title: "Section"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-section"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>Section</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.routing/Section///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.routing</a><span class="delimiter">/</span><span class="current">Section</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Section</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">Section</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">A section is a part of the route between two stopovers. A stopover is a location on the route where a stop is made.</p><p class="paragraph"><strong>Note:</strong> A section contains a list of <a href="../-section-notice/index.html">com.here.sdk.routing.SectionNotice</a> objects that describe <i>potential issues</i> after the route was calculated. If the list is non-empty, it is recommended to evaluate possible violations against the requested route options and reject the route if deemed necessary.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="359432316%2FClasslikes%2F1617540583" anchor-label="Companion" id="359432316%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="359432316%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="1481220826%2FProperties%2F1617540583" anchor-label="arrivalLocationTime" id="1481220826%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="arrival-location-time.html"><span>arrival</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Time</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1481220826%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="arrival-location-time.html">arrivalLocationTime</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-location-time/index.html">LocationTime</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The arrival location time of this section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1876703113%2FProperties%2F1617540583" anchor-label="arrivalPlace" id="-1876703113%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="arrival-place.html"><span>arrival</span><wbr></wbr><span><span>Place</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1876703113%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="arrival-place.html">arrivalPlace</a><span class="token operator">: </span><a href="../-route-place/index.html">RoutePlace</a></div><div class="brief "><p class="paragraph">The arrival place. Describes the arrival place.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1089226354%2FProperties%2F1617540583" anchor-label="boundingBox" id="-1089226354%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="bounding-box.html"><span>bounding</span><wbr></wbr><span><span>Box</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1089226354%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="bounding-box.html">boundingBox</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-box/index.html">GeoBox</a></div><div class="brief "><p class="paragraph">The closest rectangular area where this section fits in.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1628113377%2FProperties%2F1617540583" anchor-label="consumptionInKilowattHours" id="1628113377%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="consumption-in-kilowatt-hours.html"><span>consumption</span><wbr></wbr><span>In</span><wbr></wbr><span>Kilowatt</span><wbr></wbr><span><span>Hours</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1628113377%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="consumption-in-kilowatt-hours.html">consumptionInKilowattHours</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1280184511%2FProperties%2F1617540583" anchor-label="departureLocationTime" id="1280184511%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="departure-location-time.html"><span>departure</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Time</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1280184511%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="departure-location-time.html">departureLocationTime</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-location-time/index.html">LocationTime</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The departure location time of this section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="922288690%2FProperties%2F1617540583" anchor-label="departurePlace" id="922288690%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="departure-place.html"><span>departure</span><wbr></wbr><span><span>Place</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="922288690%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="departure-place.html">departurePlace</a><span class="token operator">: </span><a href="../-route-place/index.html">RoutePlace</a></div><div class="brief "><p class="paragraph">Describes the departure place.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-516642255%2FProperties%2F1617540583" anchor-label="duration" id="-516642255%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="duration.html"><span><span>duration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-516642255%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="duration.html">duration</a><span class="token operator">: </span><a href="../../com.here.time/-duration/index.html">Duration</a></div><div class="brief "><p class="paragraph">The estimated time in seconds needed to travel along this section, including real-time traffic delays if available.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1319912723%2FProperties%2F1617540583" anchor-label="geometry" id="1319912723%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="geometry.html"><span><span>geometry</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1319912723%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="geometry.html">geometry</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-polyline/index.html">GeoPolyline</a></div><div class="brief "><p class="paragraph">The <a href="../../com.here.sdk.core/-geo-polyline/index.html">com.here.sdk.core.GeoPolyline</a> object representing the polyline of this section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1905458571%2FProperties%2F1617540583" anchor-label="indoorSectionDetails" id="-1905458571%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="indoor-section-details.html"><span>indoor</span><wbr></wbr><span>Section</span><wbr></wbr><span><span>Details</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1905458571%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="indoor-section-details.html">indoorSectionDetails</a><span class="token operator">: </span><a href="../-indoor-section-details/index.html">IndoorSectionDetails</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Indoor routing section information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-616006576%2FProperties%2F1617540583" anchor-label="lengthInMeters" id="-616006576%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="length-in-meters.html"><span>length</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-616006576%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="length-in-meters.html">lengthInMeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The length of this section in meters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1112123205%2FProperties%2F1617540583" anchor-label="maneuvers" id="-1112123205%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="maneuvers.html"><span><span>maneuvers</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1112123205%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="maneuvers.html">maneuvers</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-maneuver/index.html">Maneuver</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The maneuvers for this section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1787490422%2FProperties%2F1617540583" anchor-label="noThroughRestrictions" id="-1787490422%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="no-through-restrictions.html"><span>no</span><wbr></wbr><span>Through</span><wbr></wbr><span><span>Restrictions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1787490422%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="no-through-restrictions.html">noThroughRestrictions</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-violated-restriction/index.html">ViolatedRestriction</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of no through restriction The no through restriction area is part of the road network that do not allow through traffic. For example the <code class="lang-kotlin">Resident only</code> sign indicates that vehicles are only allowed to enter this area if they are making a stop. This area will be set only if <code class="lang-kotlin">origin</code>, <code class="lang-kotlin">destination</code> or <code class="lang-kotlin">via</code> waypoint will be requested within the area.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1106025049%2FProperties%2F1617540583" anchor-label="passthroughWaypoints" id="-1106025049%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="passthrough-waypoints.html"><span>passthrough</span><wbr></wbr><span><span>Waypoints</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1106025049%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="passthrough-waypoints.html">passthroughWaypoints</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-pass-through-waypoint/index.html">PassThroughWaypoint</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of passthrough waypoints in this section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-534467688%2FProperties%2F1617540583" anchor-label="postActions" id="-534467688%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="post-actions.html"><span>post</span><wbr></wbr><span><span>Actions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-534467688%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="post-actions.html">postActions</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-post-action/index.html">PostAction</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The post actions that must be done after the arrival at the end of the section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1094143915%2FProperties%2F1617540583" anchor-label="preActions" id="1094143915%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="pre-actions.html"><span>pre</span><wbr></wbr><span><span>Actions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1094143915%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="pre-actions.html">preActions</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-pre-action/index.html">PreAction</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The preceding actions that must be done prior to departure at the beginning of the section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="333267471%2FProperties%2F1617540583" anchor-label="sectionNotices" id="333267471%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="section-notices.html"><span>section</span><wbr></wbr><span><span>Notices</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="333267471%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="section-notices.html">sectionNotices</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-section-notice/index.html">SectionNotice</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The notices which explain the issues encountered during processing of this section. For example, while the scooter transport mode is selected, if no reasonable alternative route is possible except violating controlled-access to highway rule for the section, one notice is generated for the violation. The user must judge all the notices carefully before proceeding.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1482227102%2FProperties%2F1617540583" anchor-label="sectionTransportMode" id="1482227102%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="section-transport-mode.html"><span>section</span><wbr></wbr><span>Transport</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1482227102%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="section-transport-mode.html">sectionTransportMode</a><span class="token operator">: </span><a href="../-section-transport-mode/index.html">SectionTransportMode</a></div><div class="brief "><p class="paragraph">The transport mode of this section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-115437332%2FProperties%2F1617540583" anchor-label="spans" id="-115437332%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="spans.html"><span><span>spans</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-115437332%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="spans.html">spans</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-span/index.html">Span</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The <a href="../-span/index.html">com.here.sdk.routing.Span</a>'s that constitute this section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1227585635%2FProperties%2F1617540583" anchor-label="tolls" id="-1227585635%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="tolls.html"><span><span>tolls</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1227585635%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="tolls.html">tolls</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-toll/index.html">Toll</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">All the tolls for this section. Note that tolls are found depending on the transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor route sections have no tolls, too. <strong>Note</strong>: If you're using the <code class="lang-kotlin">OfflineRoutingEngine</code>, be aware that this feature is currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors. Additionally, this feature and related APIs may be updated in future releases without going through the deprecation process. Note that the <code class="lang-kotlin">OfflineRoutingEngine</code> is only available with the Navigate license. If you're using the <code class="lang-kotlin">RoutingEngine</code>, this feature is considered to be stable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="62392959%2FProperties%2F1617540583" anchor-label="trafficDelay" id="62392959%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="traffic-delay.html"><span>traffic</span><wbr></wbr><span><span>Delay</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="62392959%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="traffic-delay.html">trafficDelay</a><span class="token operator">: </span><a href="../../com.here.time/-duration/index.html">Duration</a></div><div class="brief "><p class="paragraph">The estimated extra time in seconds spent due to traffic delays along this section. Negative values indicate that the route can be traversed faster than usual.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1122797215%2FProperties%2F1617540583" anchor-label="trafficIncidents" id="-1122797215%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="traffic-incidents.html"><span>traffic</span><wbr></wbr><span><span>Incidents</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1122797215%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="traffic-incidents.html">trafficIncidents</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-traffic-incident-on-route/index.html">TrafficIncidentOnRoute</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of traffic incidents that are found on the section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1051766070%2FProperties%2F1617540583" anchor-label="transitDetails" id="1051766070%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="transit-details.html"><span>transit</span><wbr></wbr><span><span>Details</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1051766070%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="transit-details.html">transitDetails</a><span class="token operator">: </span><a href="../-transit-section-details/index.html">TransitSectionDetails</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The transit details which are avilable for transit sections of a route.</p></div></div></div>
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
