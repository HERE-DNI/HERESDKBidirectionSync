---
title: "returnToRoute"
slug: "sdk-for-flutter-navigate-return-to-route"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- return-to-route.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>returnToRoute</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.routing/OfflineRoutingEngine/returnToRoute/#com.here.sdk.routing.Route#com.here.sdk.routing.Waypoint#kotlin.Int#kotlin.Int#com.here.sdk.routing.CalculateRouteCallback/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.routing</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">OfflineRoutingEngine</a><span class="delimiter">/</span><span class="current">returnToRoute</span></div>
  <div class="cover ">
    <h1 class="cover"><span>return</span><wbr></wbr><span>To</span><wbr></wbr><span><span>Route</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-return-to-route"><span class="token function">returnToRoute</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">route<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Route</a><span class="token punctuation">, </span></span><span class="parameter ">startingPoint<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Waypoint</a><span class="token punctuation">, </span></span><span class="parameter ">lastTraveledSectionIndex<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">traveledDistanceOnLastSectionInMeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TaskHandle</a></div><p class="paragraph">Asynchronously calculates a new route that leads back to the original route. The part of the original route which was already traveled by the user is ignored.</p><p class="paragraph"><strong>Note:</strong> Stopover waypoints are guaranteed to be visited. Pass-through waypoints will be ignored. Additionally, the following route options are ignored: <a href="sdk-for-flutter-explore-alternatives">com.here.sdk.routing.RouteOptions.alternatives</a>, <a href="sdk-for-flutter-explore-arrival-time">com.here.sdk.routing.RouteOptions.arrivalTime</a>, and <a href="sdk-for-flutter-explore-optimization-mode">com.here.sdk.routing.RouteOptions.optimizationMode</a>. Most route options are only applied to the newly calculated part back to the route.</p><p class="paragraph">An application may use this method to submit a new starting point for a previously calculated route. This method tries to avoid a costly route re-calculation as much as possible. In case returning to the route without re-calculation is not possible, a new route is calculated, while trying to salvage the previous route as much as possible. However, a completely new route containing no part of the previous route is possible, too.</p><p class="paragraph">Note that this function uses only a limited amount of map data around the new origin. Therefore, it may also work fine with temporarily cached map data. It may also copy some of the original route data into the new route.</p><p class="paragraph">A typical use case is to await at least 3 <code class="lang-kotlin">RouteDeviation</code> events before calling this method.</p><ul><li><p class="paragraph">Or alternatively, wait at least 10 seconds after getting the first deviation event.</p></li><li><p class="paragraph">On top, the user experience can be improved by checking if the vehicle has moved at least 50 meters since calling this method for the last time.</p></li><li><p class="paragraph">Optionally, it may make sense to verify if the vehicle was ever following the route by checking if <code class="lang-kotlin">RouteDeviation.lastLocationOnRoute</code> is set.</p></li></ul><p class="paragraph">Note that deviation events are sent each time a deviation is detected, i.e. for each new location update, regardless if the location has changed or not. More information can be found in the Developer Guide in the &quot;Handle route deviations&quot; section.</p><span class="kdoc-tag"><h4 class="">Return</h4><p class="paragraph">Handle that will be used to manipulate the execution of the task.</p></span><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>route</span></span></u></div></span></div><div><div class="title"><p class="paragraph">A <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.Route</a> calculated using the online or offline route engine. For the offline case, It     should not contain an indoor <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.Section</a> as such routes will fail. For the online case, it     should have <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteHandle</a>.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>starting</span><wbr></wbr><span><span>Point</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The current location, for example, provided by a <code class="lang-kotlin">RouteDeviation</code> event. The waypoint needs to be of     type <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.WaypointType.STOPOVER</a>. Otherwise, an <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RoutingError.INVALID_PARAMETER</a>     error is generated.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>last</span><wbr></wbr><span>Traveled</span><wbr></wbr><span>Section</span><wbr></wbr><span><span>Index</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Indicates the index of the last traveled route section. Traveled part of the route won't be reused.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>traveled</span><wbr></wbr><span>Distance</span><wbr></wbr><span>On</span><wbr></wbr><span>Last</span><wbr></wbr><span>Section</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Offset in meter to the last visited position on the route section defined by the last traveled section index.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>callback</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Callback object that will be invoked after route calculation.     It is always invoked on the main thread.</p></div></div></div></div></div></div></div>
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
