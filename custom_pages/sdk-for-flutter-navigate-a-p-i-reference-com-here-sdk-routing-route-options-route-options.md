---
title: "RouteOptions"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-routing-route-options-route-options"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -route-options.html -->
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.routing/RouteOptions/RouteOptions/#com.here.sdk.routing.OptimizationMode#kotlin.Int#java.util.Date?#java.util.Date?#kotlin.Double?#kotlin.Boolean#com.here.sdk.routing.TrafficOptimizationMode#kotlin.Boolean#kotlin.Boolean#kotlin.Boolean/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.routing</a><span class="delimiter">/</span><a href="index.html">RouteOptions</a><span class="delimiter">/</span><span class="current">RouteOptions</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Route</span><wbr></wbr><span><span>Options</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html"><span class="token annotation builtin">JvmOverloads</span></a></div></div><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">optimizationMode<span class="token operator">: </span><a href="../-optimization-mode/index.html">OptimizationMode</a><span class="token operator"> = </span>OptimizationMode.FASTEST<span class="token punctuation">, </span></span><span class="parameter ">alternatives<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator"> = </span><span class="token constant">0</span><span class="token punctuation">, </span></span><span class="parameter ">departureTime<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a><span class="token operator">?</span><span class="token operator"> = </span>null<span class="token punctuation">, </span></span><span class="parameter ">arrivalTime<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a><span class="token operator">?</span><span class="token operator"> = </span>null<span class="token punctuation">, </span></span><span class="parameter ">speedCapInMetersPerSecond<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span><span class="token operator"> = </span>null<span class="token punctuation">, </span></span><span class="parameter ">enableRouteHandle<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token operator"> = </span><span class="token boolean">false</span><span class="token punctuation">, </span></span><span class="parameter ">trafficOptimizationMode<span class="token operator">: </span><a href="../-traffic-optimization-mode/index.html">TrafficOptimizationMode</a><span class="token operator"> = </span>TrafficOptimizationMode.TIME_DEPENDENT<span class="token punctuation">, </span></span><span class="parameter ">enableTolls<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token operator"> = </span><span class="token boolean">false</span><span class="token punctuation">, </span></span><span class="parameter ">optimizeWaypointsOrder<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token operator"> = </span><span class="token boolean">false</span><span class="token punctuation">, </span></span><span class="parameter ">enableRouteLabels<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token operator"> = </span><span class="token boolean">false</span></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a new instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>optimization</span><wbr></wbr><span><span>Mode</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The optimization mode to be used for route calculation. By default, it is <a href="../-optimization-mode/-f-a-s-t-e-s-t/index.html">com.here.sdk.routing.OptimizationMode.FASTEST</a>.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>alternatives</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>departure</span><wbr></wbr><span><span>Time</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="traffic-optimization-mode.html">com.here.sdk.routing.RouteOptions.trafficOptimizationMode</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.</p><p class="paragraph"><strong>Note</strong>:</p><ul><li><p class="paragraph">Both departure time and <a href="arrival-time.html">com.here.sdk.routing.RouteOptions.arrivalTime</a> cannot be set at the same time.</p></li><li><p class="paragraph">This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</p></li></ul></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>arrival</span><wbr></wbr><span><span>Time</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="traffic-optimization-mode.html">com.here.sdk.routing.RouteOptions.trafficOptimizationMode</a>. By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.</p><p class="paragraph"><strong>Note</strong>:</p><ul><li><p class="paragraph">Both <a href="departure-time.html">com.here.sdk.routing.RouteOptions.departureTime</a> and arrival time cannot be set at the same time.</p></li><li><p class="paragraph">This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</p></li></ul></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>speed</span><wbr></wbr><span>Cap</span><wbr></wbr><span>In</span><wbr></wbr><span>Meters</span><wbr></wbr><span>Per</span><wbr></wbr><span><span>Second</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for <a href="../../com.here.sdk.transport/-transport-mode/-c-a-r/index.html">com.here.sdk.transport.TransportMode.CAR</a>, <a href="../../com.here.sdk.transport/-transport-mode/-t-r-u-c-k/index.html">com.here.sdk.transport.TransportMode.TRUCK</a> and <a href="../../com.here.sdk.transport/-transport-mode/-s-c-o-o-t-e-r/index.html">com.here.sdk.transport.TransportMode.SCOOTER</a> transport modes. For car, truck and scooter transport modes, it will affect <a href="../-route/duration.html">com.here.sdk.routing.Route.duration</a> of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code class="lang-kotlin">null</code>, which means that no speed cap is set.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>enable</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Handle</span></span></u></div></span></div><div><div class="title"><p class="paragraph">A flag that indicates whether the resulting route should contain a <a href="../-route-handle/index.html">com.here.sdk.routing.RouteHandle</a>. Defaults to <code class="lang-kotlin">false</code>. Note that a <code class="lang-kotlin">RouteHandle</code> generated by the online <code class="lang-kotlin">RoutingEngine</code> is not compatible with the <code class="lang-kotlin">OfflineRoutingEngine</code> and vice versa.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>traffic</span><wbr></wbr><span>Optimization</span><wbr></wbr><span><span>Mode</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The traffic optimization mode to be used for route calculation. By default, it is <a href="../-traffic-optimization-mode/-t-i-m-e_-d-e-p-e-n-d-e-n-t/index.html">com.here.sdk.routing.TrafficOptimizationMode.TIME_DEPENDENT</a>, which enables traffic-aware routing.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>enable</span><wbr></wbr><span><span>Tolls</span></span></u></div></span></div><div><div class="title"><p class="paragraph">A flag that indicates whether the resulting route <a href="../-section/tolls.html">com.here.sdk.routing.Section.tolls</a> properties should contain tolls data. Defaults to <code class="lang-kotlin">false</code>.</p><p class="paragraph"><strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied. Consult your HERE representative to get more information on the related pricing schemes.</p><p class="paragraph"><strong>Note:</strong> For users of the <code class="lang-kotlin">OfflineRoutingEngine</code> this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. The <code class="lang-kotlin">OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code class="lang-kotlin">RoutingEngine</code> the feature is stable.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>optimize</span><wbr></wbr><span>Waypoints</span><wbr></wbr><span><span>Order</span></span></u></div></span></div><div><div class="title"><p class="paragraph">A flag that indicates whether the order of waypoints that is passed to <code class="lang-kotlin">calculateRoute()</code> should be optimized in the best order. The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="../-optimization-mode/index.html">com.here.sdk.routing.OptimizationMode</a>. The starting and destination <a href="../-waypoint/index.html">com.here.sdk.routing.Waypoint</a> are not reordered. If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize). The resulting order of waypoints can be identified by their waypoint indices in the route sections (see <a href="../-route/sections.html">com.here.sdk.routing.Route.sections</a>, <a href="../-section/departure-place.html">com.here.sdk.routing.Section.departurePlace</a>, <a href="../-section/arrival-place.html">com.here.sdk.routing.Section.arrivalPlace</a>, <a href="../-route-place/waypoint-index.html">com.here.sdk.routing.RoutePlace.waypointIndex</a>). Currently, the waypoints order optimization is available only when using the <code class="lang-kotlin">OfflineRoutingEngine</code> (only available for the Navigate license). Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>enable</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Labels</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Specifies whether route labels should be included in the route response. Route labels identify major highways or road names along the route. By default, this is set to <code class="lang-kotlin">false</code>.</p></div></div></div></div></div></div></div>
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
