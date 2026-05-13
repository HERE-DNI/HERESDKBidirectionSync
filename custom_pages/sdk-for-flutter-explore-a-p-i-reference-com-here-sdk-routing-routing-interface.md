---
title: "RoutingInterface"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-interface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>RoutingInterface</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.routing/RoutingInterface///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.routing</a><span class="delimiter">/</span><span class="current">RoutingInterface</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Routing</span><wbr></wbr><span><span>Interface</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="index.html">RoutingInterface</a></div><p class="paragraph">Provides the interface for the online and offline routing engines.</p><p class="paragraph"><strong>Note</strong>: Clients need to explicitly call <a href="dispose.html">com.here.sdk.routing.RoutingInterface.dispose</a> in order to prevent a possible, though unlikely, deadlock on destruction.</p><h4 class="">Inheritors</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="../-routing-engine/index.html">RoutingEngine</a></div></span></div><div></div></div></div></div></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="845384302%2FFunctions%2F1617540583" anchor-label="calculateRoute" id="845384302%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="calculate-route.html"><span>calculate</span><wbr></wbr><span><span>Route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="845384302%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">bicycleOptions<span class="token operator">: </span><a href="../-bicycle-options/index.html">BicycleOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a bicycle route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">busOptions<span class="token operator">: </span><a href="../-bus-options/index.html">BusOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a bus route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">carOptions<span class="token operator">: </span><a href="../-car-options/index.html">CarOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a car route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">evCarOptions<span class="token operator">: </span><a href="../-e-v-car-options/index.html">EVCarOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates an electric car route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">evTruckOptions<span class="token operator">: </span><a href="../-e-v-truck-options/index.html">EVTruckOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates an electic truck route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">pedestrianOptions<span class="token operator">: </span><a href="../-pedestrian-options/index.html">PedestrianOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a pedestrian route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">privateBusOptions<span class="token operator">: </span><a href="../-private-bus-options/index.html">PrivateBusOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a private bus route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function">calculateRoute</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-routing-options/index.html">RoutingOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">scooterOptions<span class="token operator">: </span><a href="../-scooter-options/index.html">ScooterOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a scooter route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">taxiOptions<span class="token operator">: </span><a href="../-taxi-options/index.html">TaxiOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a taxi route from one point to another, passing through the given waypoints in the given order.</p></div><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="calculate-route.html"><span class="token function"><strike>calculateRoute</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">waypoints<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-waypoint/index.html">Waypoint</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">truckOptions<span class="token operator">: </span><a href="../-truck-options/index.html">TruckOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a truck route from one point to another, passing through the given waypoints in the given order.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="482140716%2FFunctions%2F1617540583" anchor-label="dispose" id="482140716%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="dispose.html"><span><span>dispose</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="482140716%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="dispose.html"><span class="token function">dispose</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Cancels pending requests and closes the background worker thread. <strong>Note:</strong> This method should be called from main thread.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-590574508%2FFunctions%2F1617540583" anchor-label="returnToRoute" id="-590574508%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="return-to-route.html"><span>return</span><wbr></wbr><span>To</span><wbr></wbr><span><span>Route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-590574508%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="return-to-route.html"><span class="token function">returnToRoute</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">route<span class="token operator">: </span><a href="../-route/index.html">Route</a><span class="token punctuation">, </span></span><span class="parameter ">startingPoint<span class="token operator">: </span><a href="../-waypoint/index.html">Waypoint</a><span class="token punctuation">, </span></span><span class="parameter ">lastTraveledSectionIndex<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">traveledDistanceOnLastSectionInMeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-calculate-route-callback/index.html">CalculateRouteCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously calculates a new route that leads back to the original route. The part of the original route which was already traveled by the user is ignored.</p></div></div></div>
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
