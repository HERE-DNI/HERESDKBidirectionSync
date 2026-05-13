---
title: "RefreshRouteOptions"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-routing-refresh-route-options"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.routing/RefreshRouteOptions///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.routing</a><span class="delimiter">/</span><span class="current">RefreshRouteOptions</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Refresh</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Options</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html"><strike>RefreshRouteOptions</strike></a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.28.0. Use the `RoutingOptions` class instead.</p></div><p class="paragraph">The options to specify how to refresh an already calculated route identified by a <a href="../-route-handle/index.html">com.here.sdk.routing.RouteHandle</a>. All the options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored: <a href="../-route-options/alternatives.html">com.here.sdk.routing.RouteOptions.alternatives</a>, <a href="../-route-options/arrival-time.html">com.here.sdk.routing.RouteOptions.arrivalTime</a>, and <a href="../-route-options/optimization-mode.html">com.here.sdk.routing.RouteOptions.optimizationMode</a>. If new <a href="../-avoidance-options/index.html">com.here.sdk.routing.AvoidanceOptions</a> are specified, they are ignored as well and instead new <a href="../-section-notice/index.html">com.here.sdk.routing.SectionNotice</a>'s are generated that indicate where the requested <a href="../-avoidance-options/index.html">com.here.sdk.routing.AvoidanceOptions</a> are violated. Note that when <a href="../-e-v-car-options/ensure-reachability.html">com.here.sdk.routing.EVCarOptions.ensureReachability</a> is set to true, the route refresh request will fail as this option is incompatible with a fixed route shape. If any of the ignored options are important, consider calculating a new route instead.</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="217179754%2FConstructors%2F1617540583" anchor-label="RefreshRouteOptions" id="217179754%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-refresh-route-options.html"><span>Refresh</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="217179754%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportMode<span class="token operator">: </span><a href="../../com.here.sdk.transport/-transport-mode/index.html">TransportMode</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="../../com.here.sdk.transport/-transport-mode/index.html">com.here.sdk.transport.TransportMode</a>.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">carOptions<span class="token operator">: </span><a href="../-car-options/index.html">CarOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="../-car-options/index.html">com.here.sdk.routing.CarOptions</a>.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">truckOptions<span class="token operator">: </span><a href="../-truck-options/index.html">TruckOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="../-truck-options/index.html">com.here.sdk.routing.TruckOptions</a>.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">pedestrianOptions<span class="token operator">: </span><a href="../-pedestrian-options/index.html">PedestrianOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="../-pedestrian-options/index.html">com.here.sdk.routing.PedestrianOptions</a>.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">scooterOptions<span class="token operator">: </span><a href="../-scooter-options/index.html">ScooterOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="../-scooter-options/index.html">com.here.sdk.routing.ScooterOptions</a>.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">taxiOptions<span class="token operator">: </span><a href="../-taxi-options/index.html">TaxiOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="../-taxi-options/index.html">com.here.sdk.routing.TaxiOptions</a>.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">evCarOptions<span class="token operator">: </span><a href="../-e-v-car-options/index.html">EVCarOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="../-e-v-car-options/index.html">com.here.sdk.routing.EVCarOptions</a>.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">evTruckOptions<span class="token operator">: </span><a href="../-e-v-truck-options/index.html">EVTruckOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="../-e-v-truck-options/index.html">com.here.sdk.routing.EVTruckOptions</a>.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">bicycleOptions<span class="token operator">: </span><a href="../-bicycle-options/index.html">BicycleOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="../-bicycle-options/index.html">com.here.sdk.routing.BicycleOptions</a>.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">busOptions<span class="token operator">: </span><a href="../-bus-options/index.html">BusOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="../-bus-options/index.html">com.here.sdk.routing.BusOptions</a>.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">privateBusOptions<span class="token operator">: </span><a href="../-private-bus-options/index.html">PrivateBusOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs a RefreshRouteOptions object with <a href="../-private-bus-options/index.html">com.here.sdk.routing.PrivateBusOptions</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-913361935%2FClasslikes%2F1617540583" anchor-label="Companion" id="-913361935%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-913361935%2FClasslikes%2F1617540583"></span>
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
