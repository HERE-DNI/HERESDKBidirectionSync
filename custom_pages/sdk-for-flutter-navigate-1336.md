---
title: "Companion"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>Companion</title>
    <link href="../../../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../../../";</script>
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
<script type="text/javascript" src="../../../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../../../styles/style.css" rel="Stylesheet">
<link href="../../../../styles/main.css" rel="Stylesheet">
<link href="../../../../styles/prism.css" rel="Stylesheet">
<link href="../../../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapContentSettings.Companion///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapContentSettings</a><span class="delimiter">/</span><span class="current">Companion</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Companion</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1078767124%2FFunctions%2F1617540583" anchor-label="configureVehicleRestrictionFilter" id="-1078767124%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-configure-vehicle-restriction-filter"><span>configure</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span>Restriction</span><wbr></wbr><span><span>Filter</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1078767124%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-configure-vehicle-restriction-filter"><span class="token function">configureVehicleRestrictionFilter</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportSpecs<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TransportSpecification</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Configures a filter for <a href="sdk-for-flutter-explore-v-e-h-i-c-l-e-r-e-s-t-r-i-c-t-i-o-n-s">com.here.sdk.mapview.MapFeatures.VEHICLE_RESTRICTIONS</a> to show only the restrictions matching the transport specifications when the feature is enabled.</p></div><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-configure-vehicle-restriction-filter"><span class="token function"><strike>configureVehicleRestrictionFilter</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TransportMode</a><span class="token punctuation">, </span></span><span class="parameter ">truckSpecifications<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TruckSpecifications</a><span class="token punctuation">, </span></span><span class="parameter ">hazardousMaterials<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="sdk-for-flutter-explore-index">HazardousMaterial</a><span class="token operator">&gt;</span><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">tunnelCategory<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TunnelCategory</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Configure a filter for <a href="sdk-for-flutter-explore-v-e-h-i-c-l-e-r-e-s-t-r-i-c-t-i-o-n-s">com.here.sdk.mapview.MapFeatures.VEHICLE_RESTRICTIONS</a> to show only the restrictions matching the specified criteria when the feature is enabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-196697684%2FFunctions%2F1617540583" anchor-label="filterTrafficIncidents" id="-196697684%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-filter-traffic-incidents"><span>filter</span><wbr></wbr><span>Traffic</span><wbr></wbr><span><span>Incidents</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-196697684%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-filter-traffic-incidents"><span class="token function">filterTrafficIncidents</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">trafficIncidents<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="sdk-for-flutter-explore-index">TrafficIncidentType</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Filters the displayed traffic incidents so that only the ones applicable to the specified criteria are shown when general display of traffic incidents is enabled. The display of traffic incidents can be enabled using <a href="sdk-for-flutter-explore-enable-features">com.here.sdk.mapview.MapScene.enableFeatures</a> with <a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-i-n-c-i-d-e-n-t-s">com.here.sdk.mapview.MapFeatures.TRAFFIC_INCIDENTS</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2133659306%2FFunctions%2F1617540583" anchor-label="resetPoiCategoriesVisibility" id="-2133659306%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-reset-poi-categories-visibility"><span>reset</span><wbr></wbr><span>Poi</span><wbr></wbr><span>Categories</span><wbr></wbr><span><span>Visibility</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2133659306%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-reset-poi-categories-visibility"><span class="token function">resetPoiCategoriesVisibility</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Resets POI categories visibility to their default state.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-941282841%2FFunctions%2F1617540583" anchor-label="resetTrafficIncidentFilter" id="-941282841%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-reset-traffic-incident-filter"><span>reset</span><wbr></wbr><span>Traffic</span><wbr></wbr><span>Incident</span><wbr></wbr><span><span>Filter</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-941282841%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-reset-traffic-incident-filter"><span class="token function">resetTrafficIncidentFilter</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes all filters regarding Traffic Incidents so that all incidents will be displayed, when the display of Traffic Incidents is enabled using <a href="sdk-for-flutter-explore-enable-features">com.here.sdk.mapview.MapScene.enableFeatures</a> with <a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-i-n-c-i-d-e-n-t-s">com.here.sdk.mapview.MapFeatures.TRAFFIC_INCIDENTS</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1963677293%2FFunctions%2F1617540583" anchor-label="resetTrafficRefreshPeriod" id="1963677293%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-reset-traffic-refresh-period"><span>reset</span><wbr></wbr><span>Traffic</span><wbr></wbr><span>Refresh</span><wbr></wbr><span><span>Period</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1963677293%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-reset-traffic-refresh-period"><span class="token function">resetTrafficRefreshPeriod</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Resets the traffic data (both flow and incidents) refresh period so the default traffic information validity time and the refresh period derived from the refresh period of the traffic server is used.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1444379124%2FFunctions%2F1617540583" anchor-label="resetVehicleRestrictionFilter" id="1444379124%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-reset-vehicle-restriction-filter"><span>reset</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span>Restriction</span><wbr></wbr><span><span>Filter</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1444379124%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-reset-vehicle-restriction-filter"><span class="token function">resetVehicleRestrictionFilter</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes all filters regarding vehicle restrictions so that all restrictions will be displayed, when the display of vehicle restrictions is enabled by enabling feature using <a href="sdk-for-flutter-explore-enable-features">com.here.sdk.mapview.MapScene.enableFeatures</a> with <a href="sdk-for-flutter-explore-v-e-h-i-c-l-e-r-e-s-t-r-i-c-t-i-o-n-s">com.here.sdk.mapview.MapFeatures.VEHICLE_RESTRICTIONS</a> and setting layer visibility using <a href="sdk-for-flutter-explore-set-layer-visibility">com.here.sdk.mapview.MapScene.setLayerVisibility</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1608623585%2FFunctions%2F1617540583" anchor-label="setPoiCategoriesVisibility" id="-1608623585%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-poi-categories-visibility"><span>set</span><wbr></wbr><span>Poi</span><wbr></wbr><span>Categories</span><wbr></wbr><span><span>Visibility</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1608623585%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-poi-categories-visibility"><span class="token function">setPoiCategoriesVisibility</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">categoryIds<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">visibility<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VisibilityState</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets visibility for embedded carto POI categories (points of interest that are visible on the map, by default). For HERE standard map schemes all available POI categories are visible by default for each selected map scheme. Note that not all POI categories are available for all map schemes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="957121718%2FFunctions%2F1617540583" anchor-label="setTrafficRefreshPeriod" id="957121718%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-traffic-refresh-period"><span>set</span><wbr></wbr><span>Traffic</span><wbr></wbr><span>Refresh</span><wbr></wbr><span><span>Period</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="957121718%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-traffic-refresh-period"><span class="token function">setTrafficRefreshPeriod</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Duration</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets the traffic data refresh period for both <a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-f-l-o-w">com.here.sdk.mapview.MapFeatures.TRAFFIC_FLOW</a> and <a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-i-n-c-i-d-e-n-t-s">com.here.sdk.mapview.MapFeatures.TRAFFIC_INCIDENTS</a>. By default, the traffic information validity time and the refresh period is derived from the refresh period of HERE's traffic server. The period set by this function will override the server's default setting for upcoming traffic data requests. Defaults to 60 seconds.</p></div></div></div>
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
