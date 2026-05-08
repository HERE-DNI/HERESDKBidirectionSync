---
title: "Waypoint"
slug: "sdk-for-flutter-explore--waypoint"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- -waypoint.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>Waypoint</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.routing/Waypoint/Waypoint/#com.here.sdk.core.GeoCoordinates/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.routing</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">Waypoint</a><span class="delimiter">/</span><span class="current">Waypoint</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Waypoint</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">coordinates<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a new instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>coordinates</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The waypoint's geographic coordinates.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">coordinates<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">type<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WaypointType</a><span class="token punctuation">, </span></span><span class="parameter ">transitRadiusInMeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">headingInDegrees<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">sideOfStreetHint<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">minCourseDistanceInMeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">duration<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Duration</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a new instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>coordinates</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The waypoint's geographic coordinates.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>type</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Defines how a waypoint should be considered for route calculation. The default waypoint type is <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.WaypointType.STOPOVER</a>.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>transit</span><wbr></wbr><span>Radius</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The maximum allowed distance from the waypoint that the calculated route may pass through. For example, to drive past a city without necessarily going into the city center, you can specify the coordinates of the center and a transit radius of 5000m. The default transit radius is zero. If the route should pass the waypoint as close as possible, the default value should be kept. Note that the waypoint will be map-matched to a road. Non-zero values allow a greater tolerance. Note that <a href="sdk-for-flutter-explore-side-of-street-hint">com.here.sdk.routing.Waypoint.sideOfStreetHint</a> option is ignored if the user sets this option with a value greater than zero.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>heading</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Degrees</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Optional heading angle referenced by true North, clockwise specifying the direction of travel. The heading direction may help the routing algorithm to select the best direction, for example, when multiple directions are possible at a road junction. North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees. The value must be in the range \[0, 360\] when specified. By default, or when <code class="lang-kotlin">null</code> is set, heading is ignored for route calculation.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>side</span><wbr></wbr><span>Of</span><wbr></wbr><span>Street</span><wbr></wbr><span><span>Hint</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Optional coordinates to indicate which side of the street should be used to reach the waypoint. For example, if the location is to the left of the street, the router will prefer using that side in case the street has dividers. Note that this option is ignored if the user sets <a href="sdk-for-flutter-explore-transit-radius-in-meters">com.here.sdk.routing.Waypoint.transitRadiusInMeters</a> option with a value greater than zero.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>min</span><wbr></wbr><span>Course</span><wbr></wbr><span>Distance</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Optional distance in meters during which the user wants to avoid taking actions. For example, if the origin is set by a moving vehicle, the user might not have time to react to immediate actions such as a sharp right turn.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>duration</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The duration in seconds that should be spent at a waypoint of type <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.WaypointType.STOPOVER</a>. Impacts time-aware calculations. Ignored for waypoints of type <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.WaypointType.PASS_THROUGH</a>. The default duration is 0 seconds.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">coordinates<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">type<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WaypointType</a><span class="token punctuation">, </span></span><span class="parameter ">transitRadiusInMeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">headingInDegrees<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">sideOfStreetHint<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">minCourseDistanceInMeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">nameHint<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">duration<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Duration</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a new instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>coordinates</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The waypoint's geographic coordinates.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>type</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Defines how a waypoint should be considered for route calculation. The default waypoint type is <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.WaypointType.STOPOVER</a>.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>transit</span><wbr></wbr><span>Radius</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The maximum allowed distance from the waypoint that the calculated route may pass through. For example, to drive past a city without necessarily going into the city center, you can specify the coordinates of the center and a transit radius of 5000m. The default transit radius is zero. If the route should pass the waypoint as close as possible, the default value should be kept. Note that the waypoint will be map-matched to a road. Non-zero values allow a greater tolerance. Note that <a href="sdk-for-flutter-explore-side-of-street-hint">com.here.sdk.routing.Waypoint.sideOfStreetHint</a> option is ignored if the user sets this option with a value greater than zero.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>heading</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Degrees</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Optional heading angle referenced by true North, clockwise specifying the direction of travel. The heading direction may help the routing algorithm to select the best direction, for example, when multiple directions are possible at a road junction. North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees. The value must be in the range \[0, 360\] when specified. By default, or when <code class="lang-kotlin">null</code> is set, heading is ignored for route calculation.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>side</span><wbr></wbr><span>Of</span><wbr></wbr><span>Street</span><wbr></wbr><span><span>Hint</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Optional coordinates to indicate which side of the street should be used to reach the waypoint. For example, if the location is to the left of the street, the router will prefer using that side in case the street has dividers. Note that this option is ignored if the user sets <a href="sdk-for-flutter-explore-transit-radius-in-meters">com.here.sdk.routing.Waypoint.transitRadiusInMeters</a> option with a value greater than zero.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>min</span><wbr></wbr><span>Course</span><wbr></wbr><span>Distance</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Optional distance in meters during which the user wants to avoid taking actions. For example, if the origin is set by a moving vehicle, the user might not have time to react to immediate actions such as a sharp right turn.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>name</span><wbr></wbr><span><span>Hint</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Optional name hint causes the router to look for the place with the most similar name. This can e.g. include things like: <code class="lang-kotlin">North</code> being used to differentiate between interstates <code class="lang-kotlin">I66 North</code> and <code class="lang-kotlin">I66 South</code>, <code class="lang-kotlin">Downtown Avenue</code> being used to correctly select a residential street.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>duration</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The duration in seconds that should be spent at a waypoint of type <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.WaypointType.STOPOVER</a>. Impacts time-aware calculations. Ignored for waypoints of type <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.WaypointType.PASS_THROUGH</a>. The default duration is 0 seconds.</p></div></div></div></div></div></div></div>
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
