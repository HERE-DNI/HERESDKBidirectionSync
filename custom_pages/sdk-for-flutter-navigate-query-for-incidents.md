---
title: "queryForIncidents"
slug: "sdk-for-flutter-navigate-query-for-incidents"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- query-for-incidents.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>queryForIncidents</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.traffic/TrafficEngine/queryForIncidents/#com.here.sdk.core.GeoBox#com.here.sdk.traffic.TrafficIncidentsQueryOptions#com.here.sdk.traffic.TrafficIncidentsQueryCallback/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.traffic</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">TrafficEngine</a><span class="delimiter">/</span><span class="current">queryForIncidents</span></div>
  <div class="cover ">
    <h1 class="cover"><span>query</span><wbr></wbr><span>For</span><wbr></wbr><span><span>Incidents</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-query-for-incidents"><span class="token function">queryForIncidents</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">boxArea<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoBox</a><span class="token punctuation">, </span></span><span class="parameter ">queryOptions<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficIncidentsQueryOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficIncidentsQueryCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TaskHandle</a></div><p class="paragraph">Asynchronously queries for traffic incidents using a bounding box as a filter.</p><span class="kdoc-tag"><h4 class="">Return</h4><p class="paragraph">Handle that will be used to manipulate the execution of the task.</p></span><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>box</span><wbr></wbr><span><span>Area</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The bounding box area to search for traffic incidents.     The maximum width and height for a bounding box filter is 1 degree.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>query</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options which are specific for incidents query.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>callback</span></span></u></div></span></div><div><div class="title"><p class="paragraph">It is always invoked on the main thread.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-query-for-incidents"><span class="token function">queryForIncidents</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">circleArea<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCircle</a><span class="token punctuation">, </span></span><span class="parameter ">queryOptions<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficIncidentsQueryOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficIncidentsQueryCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TaskHandle</a></div><p class="paragraph">Asynchronously queries for traffic incidents using a circle as a filter.</p><span class="kdoc-tag"><h4 class="">Return</h4><p class="paragraph">Handle that will be used to manipulate the execution of the task.</p></span><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>circle</span><wbr></wbr><span><span>Area</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The circle area to search for traffic incidents.     The maximum radius of the circle filter is 50000 meters.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>query</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options which are specific for incidents query.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>callback</span></span></u></div></span></div><div><div class="title"><p class="paragraph">It is always invoked on the main thread.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-query-for-incidents"><span class="token function">queryForIncidents</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">corridorArea<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCorridor</a><span class="token punctuation">, </span></span><span class="parameter ">queryOptions<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficIncidentsQueryOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficIncidentsQueryCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TaskHandle</a></div><p class="paragraph">Asynchronously queries for traffic incidents by a corridor as a filter.</p><span class="kdoc-tag"><h4 class="">Return</h4><p class="paragraph">Handle that will be used to manipulate the execution of the task.</p></span><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>corridor</span><wbr></wbr><span><span>Area</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The corridor box to search for traffic incidents.     The maximum length for the corridor is 500000 meters and the maximum <code class="lang-kotlin">GeoCorridor.half_width_in_meters</code> is 5000 meters.     If the number of points in corridor is greater than 300 then request is split into smaller ones and results are     aggregated into single response, this will result in multiple requests to the backend. This process does not change a shape of the corridor.</p><div class="sample-container"><pre><code class="block lang-kotlin" theme="idea">To reduce number of points in the corridor use [com.here.sdk.core.PolylineSimplifier].

If no `GeoCorridor.half_width_in_meters` is specified, the default value is used. The default value is 30 meters.</code></pre><span class="top-right-position"><span class="copy-icon"></span><div class="copy-popup-wrapper popup-to-left"><span class="copy-popup-icon"></span><span>Content copied to clipboard</span></div></span></div></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>query</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options which are specific for incidents query.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>callback</span></span></u></div></span></div><div><div class="title"><p class="paragraph">It is always invoked on the main thread.</p></div></div></div></div></div></div></div>
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
