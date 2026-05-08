---
title: "RefreshRouteOptions"
slug: "sdk-for-flutter-explore--refresh-route-options"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- -refresh-route-options.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>RefreshRouteOptions</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.routing/RefreshRouteOptions/RefreshRouteOptions/#com.here.sdk.transport.TransportMode/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.routing</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">RefreshRouteOptions</a><span class="delimiter">/</span><span class="current">RefreshRouteOptions</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Refresh</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Options</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TransportMode</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportMode</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>transport</span><wbr></wbr><span><span>Mode</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Updates the transport mode for the route.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">carOptions<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">CarOptions</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.CarOptions</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>car</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Converts the route to a car route, if a different transport mode was used for the     <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteHandle</a>. Note that in case this is not possible,     an <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RoutingError.NO_ROUTE_FOUND</a> error will be triggered.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">truckOptions<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TruckOptions</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.TruckOptions</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>truck</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Converts the route to a truck route, if a different transport mode was used for the     <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteHandle</a>. Note that in case this is not possible,     an <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RoutingError.NO_ROUTE_FOUND</a> error will be triggered.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">pedestrianOptions<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">PedestrianOptions</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.PedestrianOptions</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>pedestrian</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Converts the route to a pedestrian route, if a different transport mode was used for the     <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteHandle</a>. Note that in case this is not possible,     an <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RoutingError.NO_ROUTE_FOUND</a> error will be triggered.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">scooterOptions<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">ScooterOptions</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.ScooterOptions</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>scooter</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Converts the route to a scooter route, if a different transport mode was used for the     <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteHandle</a>. Note that in case this is not possible,     an <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RoutingError.NO_ROUTE_FOUND</a> error will be triggered.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">taxiOptions<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TaxiOptions</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.TaxiOptions</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>taxi</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Converts the route to a taxi route, if a different transport mode was used for the     <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteHandle</a>. Note that in case this is not possible,     an <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RoutingError.NO_ROUTE_FOUND</a> error will be triggered.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">evCarOptions<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">EVCarOptions</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.EVCarOptions</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>ev</span><wbr></wbr><span>Car</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Converts the route to an electric car route, if a different transport mode was used for the     <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteHandle</a>. Note that in case this is not possible,     an <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RoutingError.NO_ROUTE_FOUND</a> error will be triggered.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">evTruckOptions<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">EVTruckOptions</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.EVTruckOptions</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>ev</span><wbr></wbr><span>Truck</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Converts the route to an electric truck route, if a different transport mode was used for the     <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteHandle</a>. Note that in case this is not possible,     an <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RoutingError.NO_ROUTE_FOUND</a> error will be triggered.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">bicycleOptions<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">BicycleOptions</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.BicycleOptions</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>bicycle</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Converts the route to a bicycle route, if a different transport mode was used for the     <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteHandle</a>. Note that in case this is not possible,     an <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RoutingError.NO_ROUTE_FOUND</a> error will be triggered.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">busOptions<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">BusOptions</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.BusOptions</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>bus</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Converts the route to a bus route, if a different transport mode was used for the     <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteHandle</a>. Note that in case this is not possible,     an <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RoutingError.NO_ROUTE_FOUND</a> error will be triggered.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">privateBusOptions<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">PrivateBusOptions</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.PrivateBusOptions</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>private</span><wbr></wbr><span>Bus</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Converts the route to a private bus route, if a different transport mode was used for the     <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteHandle</a>. Note that in case this is not possible,     an <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RoutingError.NO_ROUTE_FOUND</a> error will be triggered.</p></div></div></div></div></div></div></div>
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
