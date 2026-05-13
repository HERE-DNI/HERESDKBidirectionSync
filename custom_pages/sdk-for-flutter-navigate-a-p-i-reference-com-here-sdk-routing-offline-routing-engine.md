---
title: "OfflineRoutingEngine"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-routing-offline-routing-engine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>OfflineRoutingEngine</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.routing/OfflineRoutingEngine///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.routing</a><span class="delimiter">/</span><span class="current">OfflineRoutingEngine</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Offline</span><wbr></wbr><span>Routing</span><wbr></wbr><span><span>Engine</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">OfflineRoutingEngine</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a>, <a href="../-routing-interface/index.html">RoutingInterface</a></div><p class="paragraph">Use this class to calculate a route offline from A to B with a number of waypoints in between.</p><p class="paragraph">Route calculation is done asynchronously, and requires map data that is available offline. This can be temporarily cached map data or downloaded offline map data stored in the persisted storage via <code class="lang-kotlin">MapDownloader</code>. Note that when using the cache there is a risk of missing data and this may reduce the overall quality of the route or can result in a <a href="../-routing-error/-n-o_-r-o-u-t-e_-f-o-u-n-d/index.html">com.here.sdk.routing.RoutingError.NO_ROUTE_FOUND</a> error.</p><p class="paragraph">The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data, but it does not contain traffic information.</p><p class="paragraph">Unlike the <code class="lang-kotlin">RoutingEngine</code> (which requires an online connection), this engine allows to use an unlimited number of waypoints.</p><p class="paragraph">As an alternative to this engine, consider to use the <code class="lang-kotlin">RoutingEngine</code> for online route calculations to get fresher traffic, maneuver, route handles and street information, and to use a more elaborate algorithms to calculate the fastest route.</p><p class="paragraph">For offline bus routing, enable &quot;OFFLINE_BUS_ROUTING&quot; as feature configuration. For more details, please look at <a href="../../com.here.sdk.core.engine/-s-d-k-options/index.html">com.here.sdk.core.engine.SDKOptions</a>. If this feature is not enabled, the engine may not be able to find bus routes.</p><p class="paragraph"><strong>Note:</strong> EV routing is available when calculating a route using the <a href="../-routing-options/index.html">com.here.sdk.routing.RoutingOptions</a>, by setting the <a href="../-routing-options/ev-options.html">com.here.sdk.routing.RoutingOptions.evOptions</a>.</p><p class="paragraph"><strong>Note:</strong> Traffic related information is completely excluded. No historic traffic patterns are taking into consideration for the ETA. Currently blocked or closed roads or roads with traffic incident are not considered offline, i.e. the road may pass through such road. Only seasonal road closures are considered based on the departure time, if given. Traffic information is only considered for online route calculation with the <code class="lang-kotlin">RoutingEngine</code>.</p><p class="paragraph"><strong>Note:</strong> Route handles produced by this engine are not compatible with those created by the <code class="lang-kotlin">RoutingEngine</code>. Importing, refreshing, or returning to a route via a route handle is supported only when the route was calculated with the same engine. However, this engine supports returning to a route calculated with the <code class="lang-kotlin">RoutingEngine</code> when the route object is provided.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-2114666689%2FConstructors%2F1617540583" anchor-label="OfflineRoutingEngine" id="-2114666689%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-offline-routing-engine.html"><span>Offline</span><wbr></wbr><span>Routing</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2114666689%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">sdkEngine<span class="token operator">: </span><a href="../../com.here.sdk.core.engine/-s-d-k-native-engine/index.html">SDKNativeEngine</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of OfflineRoutingEngine.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">sdkEngine<span class="token operator">: </span><a href="../../com.here.sdk.core.engine/-s-d-k-native-engine/index.html">SDKNativeEngine</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-offline-routing-engine-options/index.html">OfflineRoutingEngineOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of OfflineRoutingEngine.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="422448256%2FClasslikes%2F1617540583" anchor-label="Companion" id="422448256%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="422448256%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="2008969441%2FProperties%2F1617540583" anchor-label="trafficDataProvider" id="2008969441%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="traffic-data-provider.html"><span>traffic</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Provider</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2008969441%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="traffic-data-provider.html">trafficDataProvider</a><span class="token operator">: </span><a href="../../com.here.sdk.traffic/-traffic-data-provider/index.html">TrafficDataProvider</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The traffic data provider that gets internal traffic information considering in routing. If the traffic data provider is <code class="lang-kotlin">null</code>, traffic is not considered in routing.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="283443652%2FFunctions%2F1617540583" anchor-label="calculateRoute" id="283443652%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="calculate-route.html"><span>calculate</span><wbr></wbr><span><span>Route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="283443652%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">bicycleOptions<span class="token operator">: </span><a href="../-bicycle-options/index.html">BicycleOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a bicycle route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">busOptions<span class="token operator">: </span><a href="../-bus-options/index.html">BusOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a bus route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">carOptions<span class="token operator">: </span><a href="../-car-options/index.html">CarOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a car route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">evCarOptions<span class="token operator">: </span><a href="../-e-v-car-options/index.html">EVCarOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates an electric car route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">evTruckOptions<span class="token operator">: </span><a href="../-e-v-truck-options/index.html">EVTruckOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates an electic truck route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">pedestrianOptions<span class="token operator">: </span><a href="../-pedestrian-options/index.html">PedestrianOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a pedestrian route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">privateBusOptions<span class="token operator">: </span><a href="../-private-bus-options/index.html">PrivateBusOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a private bus route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function">calculateRoute</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-routing-options/index.html">RoutingOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">scooterOptions<span class="token operator">: </span><a href="../-scooter-options/index.html">ScooterOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a scooter route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">taxiOptions<span class="token operator">: </span><a href="../-taxi-options/index.html">TaxiOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a taxi route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">truckOptions<span class="token operator">: </span><a href="../-truck-options/index.html">TruckOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a truck route from one point to another, passing through the given waypoints in the given order.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-611609350%2FFunctions%2F1617540583" anchor-label="dispose" id="-611609350%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="dispose.html"><span><span>dispose</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-611609350%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="dispose.html"><span class="token function">dispose</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Cancels pending requests and closes the background worker thread. <strong>Note:</strong> This method should be called from main thread.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2048474602%2FFunctions%2F1617540583" anchor-label="importRoute" id="2048474602%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="import-route.html"><span>import</span><wbr></wbr><span><span>Route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2048474602%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="import-route.html"><span class="token function"><strike>importRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">routeHandle<span class="token operator">: </span><a href="../-route-handle/index.html">RouteHandle</a><span class="token punctuation">, </span></span><span class="parameter ">refreshRouteOptions<span class="token operator">: </span><a href="../-refresh-route-options/index.html">RefreshRouteOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="import-route.html"><span class="token function">importRoute</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">routeHandle<span class="token operator">: </span><a href="../-route-handle/index.html">RouteHandle</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-routing-options/index.html">RoutingOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously recreates a route from the <a href="../-route-handle/index.html">com.here.sdk.routing.RouteHandle</a> provided, i.e. refreshes a previously calculated route, with the specified <a href="../-refresh-route-options/index.html">com.here.sdk.routing.RefreshRouteOptions</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1764747894%2FFunctions%2F1617540583" anchor-label="refreshRoute" id="1764747894%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="refresh-route.html"><span>refresh</span><wbr></wbr><span><span>Route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1764747894%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="refresh-route.html"><span class="token function">refreshRoute</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">refreshRouteParameters<span class="token operator">: </span><a href="../-refresh-route-parameters/index.html">RefreshRouteParameters</a><span class="token punctuation">, </span></span><span class="parameter ">routingOptions<span class="token operator">: </span><a href="../-routing-options/index.html">RoutingOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously refreshes a previously calculated route from the provided <a href="../-route-handle/index.html">com.here.sdk.routing.RouteHandle</a>, updating the starting point and route metadata based on <a href="../-routing-options/index.html">com.here.sdk.routing.RoutingOptions</a>. The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1038065886%2FFunctions%2F1617540583" anchor-label="returnToRoute" id="-1038065886%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="return-to-route.html"><span>return</span><wbr></wbr><span>To</span><wbr></wbr><span><span>Route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1038065886%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="return-to-route.html"><span class="token function">returnToRoute</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">route<span class="token operator">: </span><a href="../-route/index.html">Route</a><span class="token punctuation">, </span></span><span class="parameter ">startingPoint<span class="token operator">: </span><a href="../-waypoint/index.html">Waypoint</a><span class="token punctuation">, </span></span><span class="parameter ">lastTraveledSectionIndex<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">traveledDistanceOnLastSectionInMeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a new route that leads back to the original route. The part of the original route which was already traveled by the user is ignored.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1451299676%2FFunctions%2F1617540583" anchor-label="setInternalOption" id="-1451299676%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-internal-option.html"><span>set</span><wbr></wbr><span>Internal</span><wbr></wbr><span><span>Option</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1451299676%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-internal-option.html"><span class="token function">setInternalOption</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">key<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">This method sets internal options that controls offline route calculation behavior. Unsupported options will be logged as warnings. Undocumented options can change their meaning without going through deprecation process.</p></div></div></div>
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
