---
title: "start"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-trafficawarenavigation-dynamic-routing-engine-start"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- start.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>start</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.trafficawarenavigation/DynamicRoutingEngine/start/#com.here.sdk.routing.Route#com.here.sdk.trafficawarenavigation.DynamicRoutingListener/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.trafficawarenavigation</a><span class="delimiter">/</span><a href="index.html">DynamicRoutingEngine</a><span class="delimiter">/</span><span class="current">start</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>start</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="start.html"><span class="token function">start</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">route<span class="token operator">: </span><a href="../../com.here.sdk.routing/-route/index.html">Route</a><span class="token punctuation">, </span></span><span class="parameter ">listener<span class="token operator">: </span><a href="../-dynamic-routing-listener/index.html">DynamicRoutingListener</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Starts polling the HERE backend services to find a better route, as defined by the DynamicRoutingEngineOptions.</p><p class="paragraph"><strong>Note:</strong> The engine will be internally stopped, if it was started before. Therefore, it is not necessary to stop the engine before starting it again.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>route</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The route to be refreshed. The route must contain a <a href="../../com.here.sdk.routing/-route-handle/index.html">com.here.sdk.routing.RouteHandle</a>,     therefore the route must have been requested with     <a href="../../com.here.sdk.routing/-route-options/enable-route-handle.html">com.here.sdk.routing.RouteOptions.enableRouteHandle</a> set to <code class="lang-kotlin">true</code>.     The information to calculate new routes will be extracted from the provided route parameter.     If more information from the original waypoints is important besides their location,     consider to use one of the overloaded methods instead.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>listener</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The listener to receive the events.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="-start-exception/index.html"><span>Dynamic</span><wbr></wbr><span>Routing</span><wbr></wbr><span>Engine.</span><wbr></wbr><span>Start</span><wbr></wbr><span><span>Exception</span></span></a></div></span></div><div><div class="title"><p class="paragraph">when the passed parameter are invalid.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="start.html"><span class="token function">start</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">routeHandle<span class="token operator">: </span><a href="../../com.here.sdk.routing/-route-handle/index.html">RouteHandle</a><span class="token punctuation">, </span></span><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../../com.here.sdk.routing/-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">routingOptions<span class="token operator">: </span><a href="../../com.here.sdk.routing/-routing-options/index.html">RoutingOptions</a><span class="token punctuation">, </span></span><span class="parameter ">listener<span class="token operator">: </span><a href="../-dynamic-routing-listener/index.html">DynamicRoutingListener</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Starts polling the HERE backend services to find a better route, as defined by the <a href="../-dynamic-routing-engine-options/index.html">com.here.sdk.trafficawarenavigation.DynamicRoutingEngineOptions</a>.</p><p class="paragraph"><strong>Note:</strong> The engine will be internally stopped, if it was started before. Therefore, it is not necessary to stop the engine before starting it again.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>route</span><wbr></wbr><span><span>Handle</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The route handle from the HERE routing backend.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>waypoints</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Allows to specify detailed information on the waypoints of the route.     This parameter can be useful, when additional information needs to be     specified besides the coordinates - as the coordinates can be retrieved     from the contained <a href="../../com.here.sdk.routing/-route-place/index.html">com.here.sdk.routing.RoutePlace</a> that are already contained in     the <a href="../../com.here.sdk.routing/-route-handle/index.html">com.here.sdk.routing.RouteHandle</a> parameter.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>routing</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options for the route calculation.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>listener</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The listener to receive the events.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="-start-exception/index.html"><span>Dynamic</span><wbr></wbr><span>Routing</span><wbr></wbr><span>Engine.</span><wbr></wbr><span>Start</span><wbr></wbr><span><span>Exception</span></span></a></div></span></div><div><div class="title"><p class="paragraph">when the passed parameter are invalid.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="start.html"><span class="token function"><strike>start</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">routeHandle<span class="token operator">: </span><a href="../../com.here.sdk.routing/-route-handle/index.html">RouteHandle</a><span class="token punctuation">, </span></span><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../../com.here.sdk.routing/-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">refreshRouteOptions<span class="token operator">: </span><a href="../../com.here.sdk.routing/-refresh-route-options/index.html">RefreshRouteOptions</a><span class="token punctuation">, </span></span><span class="parameter ">listener<span class="token operator">: </span><a href="../-dynamic-routing-listener/index.html">DynamicRoutingListener</a></span></span><span class="token punctuation">)</span></div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.28.0. Use the `start()` method with RoutingOptions parameter instead.</p></div><p class="paragraph">Starts polling the HERE backend services to find a better route, as defined by the <a href="../-dynamic-routing-engine-options/index.html">com.here.sdk.trafficawarenavigation.DynamicRoutingEngineOptions</a>.</p><p class="paragraph"><strong>Note:</strong> The engine will be internally stopped, if it was started before. Therefore, it is not necessary to stop the engine before starting it again.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>route</span><wbr></wbr><span><span>Handle</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The route handle from the HERE routing backend.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>waypoints</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Allows to specify detailed information on the waypoints of the route.     This parameter can be useful, when additional information needs to be     specified besides the coordinates - as the coordinates can be retrieved     from the contained <a href="../../com.here.sdk.routing/-route-place/index.html">com.here.sdk.routing.RoutePlace</a> that are already contained in     the <a href="../../com.here.sdk.routing/-route-handle/index.html">com.here.sdk.routing.RouteHandle</a> parameter.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>refresh</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options for the route calculation.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>listener</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The listener to receive the events.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="-start-exception/index.html"><span>Dynamic</span><wbr></wbr><span>Routing</span><wbr></wbr><span>Engine.</span><wbr></wbr><span>Start</span><wbr></wbr><span><span>Exception</span></span></a></div></span></div><div><div class="title"><p class="paragraph">when the passed parameter are invalid.</p></div></div></div></div></div></div></div>
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
