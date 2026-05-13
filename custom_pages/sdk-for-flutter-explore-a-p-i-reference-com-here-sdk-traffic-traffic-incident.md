---
title: "TrafficIncident"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-traffic-traffic-incident"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>TrafficIncident</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.traffic/TrafficIncident///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.traffic</a><span class="delimiter">/</span><span class="current">TrafficIncident</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Traffic</span><wbr></wbr><span><span>Incident</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">TrafficIncident</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a>, <a href="../-traffic-incident-base/index.html">TrafficIncidentBase</a></div><p class="paragraph">TrafficIncident provides details about a traffic incident.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-1290391397%2FClasslikes%2F1617540583" anchor-label="Companion" id="-1290391397%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1290391397%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1603265896%2FClasslikes%2F1617540583" anchor-label="RestrictedVehicleCategory" id="-1603265896%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-restricted-vehicle-category/index.html"><span>Restricted</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1603265896%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-restricted-vehicle-category/index.html">RestrictedVehicleCategory</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-restricted-vehicle-category/index.html">TrafficIncident.RestrictedVehicleCategory</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">The vehicle categories that can be restricted. Note, a vehicle can belong to several categories (e.g. a passenger motor car belongs to <a href="-restricted-vehicle-category/-c-a-r/index.html">com.here.sdk.traffic.TrafficIncident.RestrictedVehicleCategory.CAR</a>, <a href="-restricted-vehicle-category/-m-o-t-o-r_-v-e-h-i-c-l-e/index.html">com.here.sdk.traffic.TrafficIncident.RestrictedVehicleCategory.MOTOR_VEHICLE</a>, and <a href="-restricted-vehicle-category/-a-l-l/index.html">com.here.sdk.traffic.TrafficIncident.RestrictedVehicleCategory.ALL</a>). A vehicle is restricted if it belongs to the category presented in the map <a href="vehicle-restrictions.html">com.here.sdk.traffic.TrafficIncident.vehicleRestrictions</a> and at least one of the vehicle properties is under the matching <a href="-vehicle-restriction/index.html">com.here.sdk.traffic.TrafficIncident.VehicleRestriction</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-318678533%2FClasslikes%2F1617540583" anchor-label="VehicleRestriction" id="-318678533%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-vehicle-restriction/index.html"><span>Vehicle</span><wbr></wbr><span><span>Restriction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-318678533%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-vehicle-restriction/index.html">VehicleRestriction</a></div><div class="brief "><p class="paragraph">The vehicle restriction representing a vehicle category and relevant restriction rules.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="1051330926%2FProperties%2F1617540583" anchor-label="codes" id="1051330926%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="codes.html"><span><span>codes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1051330926%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="codes.html">codes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category. Codes are given in order of importance, so the first item in the list is considered the primary cause of the incident.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-990214888%2FProperties%2F1617540583" anchor-label="description" id="-990214888%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="description.html"><span><span>description</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-990214888%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">val </span><a href="description.html">description</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-localized-text/index.html">LocalizedText</a></div><div class="brief "><p class="paragraph">The human readable description of the incident, possibly with location information. The description is currently not present in our map data. Therefore, when accessing the data from a picked carto POI via <code class="lang-kotlin">TrafficIncidentResult</code>, then always an empty string is returned. This does not apply when using the <code class="lang-kotlin">TrafficEngine</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1256755148%2FProperties%2F1617540583" anchor-label="endTime" id="1256755148%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="end-time.html"><span>end</span><wbr></wbr><span><span>Time</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1256755148%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">val </span><a href="end-time.html">endTime</a><span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The time until which the incident is valid, after this time the incident should not be considered. The value is <code class="lang-kotlin">null</code> if it hasn't been provided by the traffic incidents supplier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="674017749%2FProperties%2F1617540583" anchor-label="entryTime" id="674017749%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="entry-time.html"><span>entry</span><wbr></wbr><span><span>Time</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="674017749%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="entry-time.html">entryTime</a><span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The time the incident was entered into the system. The value is <code class="lang-kotlin">null</code> if it hasn't been provided by the traffic incidents supplier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2147355467%2FProperties%2F1617540583" anchor-label="id" id="2147355467%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="id.html"><span><span>id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2147355467%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="id.html">id</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">The unique current identifier for a traffic incident.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="156271872%2FProperties%2F1617540583" anchor-label="impact" id="156271872%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="impact.html"><span><span>impact</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="156271872%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">val </span><a href="impact.html">impact</a><span class="token operator">: </span><a href="../-traffic-incident-impact/index.html">TrafficIncidentImpact</a></div><div class="brief "><p class="paragraph">The impact of the incident. The value is <a href="../-traffic-incident-impact/-u-n-k-n-o-w-n/index.html">com.here.sdk.traffic.TrafficIncidentImpact.UNKNOWN</a> if it hasn't been provided by the traffic incidents supplier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1978838032%2FProperties%2F1617540583" anchor-label="isRoadClosed" id="1978838032%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-road-closed.html"><span>is</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Closed</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1978838032%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="is-road-closed.html">isRoadClosed</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">The flag indicates whether road is closed or not.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1539850718%2FProperties%2F1617540583" anchor-label="junctionsTraversability" id="1539850718%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="junctions-traversability.html"><span>junctions</span><wbr></wbr><span><span>Traversability</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1539850718%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="junctions-traversability.html">junctionsTraversability</a><span class="token operator">: </span><a href="../-junctions-traversability/index.html">JunctionsTraversability</a></div><div class="brief "><p class="paragraph">The traversability of junctions along the affected road.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1819435215%2FProperties%2F1617540583" anchor-label="location" id="-1819435215%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="location.html"><span><span>location</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1819435215%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="location.html">location</a><span class="token operator">: </span><a href="../-traffic-location/index.html">TrafficLocation</a></div><div class="brief "><p class="paragraph">The location of the incident.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="410416570%2FProperties%2F1617540583" anchor-label="originalId" id="410416570%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="original-id.html"><span>original</span><wbr></wbr><span><span>Id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="410416570%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="original-id.html">originalId</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">The unique identifier of the first traffic incident. The original id remains the same whenever the traffic incident is updated and <a href="id.html">com.here.sdk.traffic.TrafficIncident.id</a> is changed. Once an incident chain has been created, this value will never change. The traffic incident an be looked up by original id using <a href="../-traffic-engine/lookup-incident.html">com.here.sdk.traffic.TrafficEngine.lookupIncident</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="557168001%2FProperties%2F1617540583" anchor-label="parentId" id="557168001%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="parent-id.html"><span>parent</span><wbr></wbr><span><span>Id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="557168001%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="parent-id.html">parentId</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The identifier of another incident to which this incident is linked. The value is <code class="lang-kotlin">null</code> if the incident doesn't have a parent.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1409530853%2FProperties%2F1617540583" anchor-label="startTime" id="1409530853%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="start-time.html"><span>start</span><wbr></wbr><span><span>Time</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1409530853%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">val </span><a href="start-time.html">startTime</a><span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The time from which the incident is valid, before this time the incident should not be considered. The value is <code class="lang-kotlin">null</code> if it hasn't been provided by the traffic incidents supplier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="466647086%2FProperties%2F1617540583" anchor-label="summary" id="466647086%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="summary.html"><span><span>summary</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="466647086%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="summary.html">summary</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-localized-text/index.html">LocalizedText</a></div><div class="brief "><p class="paragraph">The human readable summary of the incident. The summary field provides a short version of the description containing no location information. The expected summary language can be managed via <a href="../-traffic-incidents-query-options/language-code.html">com.here.sdk.traffic.TrafficIncidentsQueryOptions.languageCode</a> and <a href="../-traffic-incident-lookup-options/language-code.html">com.here.sdk.traffic.TrafficIncidentLookupOptions.languageCode</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-439620660%2FProperties%2F1617540583" anchor-label="type" id="-439620660%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="type.html"><span><span>type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-439620660%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">val </span><a href="type.html">type</a><span class="token operator">: </span><a href="../-traffic-incident-type/index.html">TrafficIncidentType</a></div><div class="brief "><p class="paragraph">The category of the incident. The value is <a href="../-traffic-incident-type/-u-n-k-n-o-w-n/index.html">com.here.sdk.traffic.TrafficIncidentType.UNKNOWN</a> if it hasn't been provided by the traffic incidents supplier.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-697344383%2FProperties%2F1617540583" anchor-label="vehicleRestrictions" id="-697344383%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="vehicle-restrictions.html"><span>vehicle</span><wbr></wbr><span><span>Restrictions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-697344383%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="vehicle-restrictions.html">vehicleRestrictions</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="-restricted-vehicle-category/index.html">TrafficIncident.RestrictedVehicleCategory</a><span class="token punctuation">, </span><a href="-vehicle-restriction/index.html">TrafficIncident.VehicleRestriction</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The map of restricted vehicle categories to restrictions. A vehicle is restricted if at least one restriction field is applicable for it. If the map is empty, there're no restricted vehicles for the incident.</p></div></div></div>
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
