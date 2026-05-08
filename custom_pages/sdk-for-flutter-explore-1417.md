---
title: "RouteOptions"
slug: "sdk-for-flutter-explore"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>RouteOptions</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.routing/RouteOptions///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.routing</a><span class="delimiter">/</span><span class="current">RouteOptions</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Route</span><wbr></wbr><span><span>Options</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RouteOptions</a></div><p class="paragraph">The options to specify how the route will be calculated.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-778389469%2FConstructors%2F1617540583" anchor-label="RouteOptions" id="-778389469%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-route-options"><span>Route</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-778389469%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html"><span class="token annotation builtin">JvmOverloads</span></a></div></div><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">optimizationMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">OptimizationMode</a><span class="token operator"> = </span>OptimizationMode.FASTEST<span class="token punctuation">, </span></span><span class="parameter ">alternatives<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator"> = </span><span class="token constant">0</span><span class="token punctuation">, </span></span><span class="parameter ">departureTime<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a><span class="token operator">?</span><span class="token operator"> = </span>null<span class="token punctuation">, </span></span><span class="parameter ">arrivalTime<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a><span class="token operator">?</span><span class="token operator"> = </span>null<span class="token punctuation">, </span></span><span class="parameter ">speedCapInMetersPerSecond<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span><span class="token operator"> = </span>null<span class="token punctuation">, </span></span><span class="parameter ">enableRouteHandle<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token operator"> = </span><span class="token boolean">false</span><span class="token punctuation">, </span></span><span class="parameter ">trafficOptimizationMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficOptimizationMode</a><span class="token operator"> = </span>TrafficOptimizationMode.TIME_DEPENDENT<span class="token punctuation">, </span></span><span class="parameter ">enableTolls<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token operator"> = </span><span class="token boolean">false</span><span class="token punctuation">, </span></span><span class="parameter ">optimizeWaypointsOrder<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token operator"> = </span><span class="token boolean">false</span><span class="token punctuation">, </span></span><span class="parameter ">enableRouteLabels<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token operator"> = </span><span class="token boolean">false</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-1834258517%2FProperties%2F1617540583" anchor-label="alternatives" id="-1834258517%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-alternatives"><span><span>alternatives</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1834258517%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-alternatives">alternatives</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="898170371%2FProperties%2F1617540583" anchor-label="arrivalTime" id="898170371%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-arrival-time"><span>arrival</span><wbr></wbr><span><span>Time</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="898170371%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-arrival-time">arrivalTime</a><span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-flutter-explore-traffic-optimization-mode">com.here.sdk.routing.RouteOptions.trafficOptimizationMode</a>. By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1924344856%2FProperties%2F1617540583" anchor-label="departureTime" id="-1924344856%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-departure-time"><span>departure</span><wbr></wbr><span><span>Time</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1924344856%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-departure-time">departureTime</a><span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-flutter-explore-traffic-optimization-mode">com.here.sdk.routing.RouteOptions.trafficOptimizationMode</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1347656677%2FProperties%2F1617540583" anchor-label="enableRouteHandle" id="-1347656677%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-enable-route-handle"><span>enable</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Handle</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1347656677%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-enable-route-handle">enableRouteHandle</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">A flag that indicates whether the resulting route should contain a <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteHandle</a>. Defaults to <code class="lang-kotlin">false</code>. Note that a <code class="lang-kotlin">RouteHandle</code> generated by the online <code class="lang-kotlin">RoutingEngine</code> is not compatible with the <code class="lang-kotlin">OfflineRoutingEngine</code> and vice versa.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="507798052%2FProperties%2F1617540583" anchor-label="enableRouteLabels" id="507798052%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-enable-route-labels"><span>enable</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Labels</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="507798052%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-enable-route-labels">enableRouteLabels</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Specifies whether route labels should be included in the route response. Route labels identify major highways or road names along the route. By default, this is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-350032780%2FProperties%2F1617540583" anchor-label="enableTolls" id="-350032780%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-enable-tolls"><span>enable</span><wbr></wbr><span><span>Tolls</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-350032780%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-enable-tolls">enableTolls</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">A flag that indicates whether the resulting route <a href="sdk-for-flutter-explore-tolls">com.here.sdk.routing.Section.tolls</a> properties should contain tolls data. Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-648750431%2FProperties%2F1617540583" anchor-label="optimizationMode" id="-648750431%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-optimization-mode"><span>optimization</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-648750431%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-optimization-mode">optimizationMode</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">OptimizationMode</a></div><div class="brief "><p class="paragraph">The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.OptimizationMode.FASTEST</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="253284952%2FProperties%2F1617540583" anchor-label="optimizeWaypointsOrder" id="253284952%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-optimize-waypoints-order"><span>optimize</span><wbr></wbr><span>Waypoints</span><wbr></wbr><span><span>Order</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="253284952%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-optimize-waypoints-order">optimizeWaypointsOrder</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">A flag that indicates whether the order of waypoints that is passed to <code class="lang-kotlin">calculateRoute()</code> should be optimized in the best order. The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.OptimizationMode</a>. The starting and destination <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.Waypoint</a> are not reordered. If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize). The resulting order of waypoints can be identified by their waypoint indices in the route sections (see <a href="sdk-for-flutter-explore-sections">com.here.sdk.routing.Route.sections</a>, <a href="sdk-for-flutter-explore-departure-place">com.here.sdk.routing.Section.departurePlace</a>, <a href="sdk-for-flutter-explore-arrival-place">com.here.sdk.routing.Section.arrivalPlace</a>, <a href="sdk-for-flutter-explore-waypoint-index">com.here.sdk.routing.RoutePlace.waypointIndex</a>). Currently, the waypoints order optimization is available only when using the <code class="lang-kotlin">OfflineRoutingEngine</code> (only available for the Navigate license). Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1465715150%2FProperties%2F1617540583" anchor-label="speedCapInMetersPerSecond" id="-1465715150%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-speed-cap-in-meters-per-second"><span>speed</span><wbr></wbr><span>Cap</span><wbr></wbr><span>In</span><wbr></wbr><span>Meters</span><wbr></wbr><span>Per</span><wbr></wbr><span><span>Second</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1465715150%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-speed-cap-in-meters-per-second">speedCapInMetersPerSecond</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportMode.CAR</a>, <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportMode.TRUCK</a> and <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportMode.SCOOTER</a> transport modes. For car, truck and scooter transport modes, it will affect <a href="sdk-for-flutter-explore-duration">com.here.sdk.routing.Route.duration</a> of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code class="lang-kotlin">null</code>, which means that no speed cap is set.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1888167804%2FProperties%2F1617540583" anchor-label="trafficOptimizationMode" id="1888167804%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-traffic-optimization-mode"><span>traffic</span><wbr></wbr><span>Optimization</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1888167804%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-traffic-optimization-mode">trafficOptimizationMode</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficOptimizationMode</a></div><div class="brief "><p class="paragraph">The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.TrafficOptimizationMode.TIME_DEPENDENT</a>, which enables traffic-aware routing.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-2086400688%2FFunctions%2F1617540583" anchor-label="equals" id="-2086400688%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-equals"><span><span>equals</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2086400688%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">operator override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-equals"><span class="token function">equals</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">other<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1619205738%2FFunctions%2F1617540583" anchor-label="hashCode" id="-1619205738%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-hash-code"><span>hash</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1619205738%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-hash-code"><span class="token function">hashCode</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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
