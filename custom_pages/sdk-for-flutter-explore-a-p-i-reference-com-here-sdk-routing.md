---
title: "com.here.sdk.routing"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>com.here.sdk.routing</title>
    <link href="../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../";</script>
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
<script type="text/javascript" src="../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../styles/style.css" rel="Stylesheet">
<link href="../../styles/main.css" rel="Stylesheet">
<link href="../../styles/prism.css" rel="Stylesheet">
<link href="../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
</head>
<body>
    <div class="root">
    <nav class="navigation theme-dark" id="navigation-wrapper">
            <a class="library-name--link" href="../../index.html">
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
<div class="main-content" data-page-type="package" id="content" pageIds="API Reference::com.here.sdk.routing////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../index.html">API Reference</a><span class="delimiter">/</span><span class="current">com.here.sdk.routing</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Package-level</span></span> <span><span>declarations</span></span></h1>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="TYPE">Types</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1052402408%2FClasslikes%2F1617540583" anchor-label="AccessAttributes" id="1052402408%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-access-attributes/index.html"><span>Access</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1052402408%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-access-attributes/index.html">AccessAttributes</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-access-attributes/index.html">AccessAttributes</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Types of access attributes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1633145218%2FClasslikes%2F1617540583" anchor-label="Agency" id="-1633145218%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-agency/index.html"><span><span>Agency</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1633145218%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-agency/index.html">Agency</a></div><div class="brief "><p class="paragraph">Holds all the agency information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1655625746%2FClasslikes%2F1617540583" anchor-label="AllowOptions" id="-1655625746%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-allow-options/index.html"><span>Allow</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1655625746%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-allow-options/index.html">AllowOptions</a></div><div class="brief "><p class="paragraph">The options explicitly allowed by user for route calculations.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-716223200%2FClasslikes%2F1617540583" anchor-label="Attribution" id="-716223200%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-attribution/index.html"><span><span>Attribution</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-716223200%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-attribution/index.html">Attribution</a></div><div class="brief "><p class="paragraph">Holds all the data on a URL address to an external resource.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1246024582%2FClasslikes%2F1617540583" anchor-label="AttributionType" id="1246024582%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-attribution-type/index.html"><span>Attribution</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1246024582%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-attribution-type/index.html">AttributionType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-attribution-type/index.html">AttributionType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Attribution link type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1498032105%2FClasslikes%2F1617540583" anchor-label="AvoidanceOptions" id="1498032105%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-avoidance-options/index.html"><span>Avoidance</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1498032105%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-avoidance-options/index.html">AvoidanceOptions</a></div><div class="brief "><p class="paragraph">The options to specify restrictions for route calculations.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1256255616%2FClasslikes%2F1617540583" anchor-label="AvoidBoundingBoxAreaOptions" id="1256255616%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-avoid-bounding-box-area-options/index.html"><span>Avoid</span><wbr></wbr><span>Bounding</span><wbr></wbr><span>Box</span><wbr></wbr><span>Area</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1256255616%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-avoid-bounding-box-area-options/index.html">AvoidBoundingBoxAreaOptions</a></div><div class="brief "><p class="paragraph">The options to specify rectangular shape which routes must not cross.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="769424721%2FClasslikes%2F1617540583" anchor-label="AvoidCorridorAreaOptions" id="769424721%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-avoid-corridor-area-options/index.html"><span>Avoid</span><wbr></wbr><span>Corridor</span><wbr></wbr><span>Area</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="769424721%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-avoid-corridor-area-options/index.html">AvoidCorridorAreaOptions</a></div><div class="brief "><p class="paragraph">Area of corridor shape which routes must not cross and exceptions for this area.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="943083315%2FClasslikes%2F1617540583" anchor-label="AvoidPolygonAreaOptions" id="943083315%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-avoid-polygon-area-options/index.html"><span>Avoid</span><wbr></wbr><span>Polygon</span><wbr></wbr><span>Area</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="943083315%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-avoid-polygon-area-options/index.html">AvoidPolygonAreaOptions</a></div><div class="brief "><p class="paragraph">The options to specify polygon shape which routes must not cross.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1687767390%2FClasslikes%2F1617540583" anchor-label="BatterySpecifications" id="-1687767390%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-battery-specifications/index.html"><span>Battery</span><wbr></wbr><span><span>Specifications</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1687767390%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-battery-specifications/index.html">BatterySpecifications</a></div><div class="brief "><p class="paragraph">Parameters related to the electric vehicle's battery.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="592005412%2FClasslikes%2F1617540583" anchor-label="BicycleOptions" id="592005412%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-bicycle-options/index.html"><span>Bicycle</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="592005412%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-bicycle-options/index.html"><strike>BicycleOptions</strike></a></div><div class="brief "><p class="paragraph">All the options to specify how a bicycle route should be calculated.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-518878299%2FClasslikes%2F1617540583" anchor-label="BusOptions" id="-518878299%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-bus-options/index.html"><span>Bus</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-518878299%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-bus-options/index.html"><strike>BusOptions</strike></a></div><div class="brief "><p class="paragraph">All the options to specify how a bus route should be calculated.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="952227915%2FClasslikes%2F1617540583" anchor-label="CalculateIsolineCallback" id="952227915%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-calculate-isoline-callback/index.html"><span>Calculate</span><wbr></wbr><span>Isoline</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="952227915%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-calculate-isoline-callback/index.html">CalculateIsolineCallback</a></div><div class="brief "><p class="paragraph">A function which is called by the RoutingEngine after isoline calculation has completed. It is always called on the main thread. The first argument is the error in case of a failure. It is <code class="lang-kotlin">null</code> for an operation that succeeds. The second argument holds a list of calculated isolines. The list is <code class="lang-kotlin">null</code> in case of an error. The size of the list matches the size of the provided sdk.routing.IsolineOptions.range_values: For each range limit, one isoline is calculated.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2060485637%2FClasslikes%2F1617540583" anchor-label="CalculateRouteCallback" id="-2060485637%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-calculate-route-callback/index.html"><span>Calculate</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2060485637%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-calculate-route-callback/index.html">CalculateRouteCallback</a></div><div class="brief "><p class="paragraph">A function which is called by the RoutingEngine after route calculation has completed. It is always called on the main thread. The first argument is the error in case of a failure. It is <code class="lang-kotlin">null</code> for an operation that succeeds. The second argument is the calculated routes. It is <code class="lang-kotlin">null</code> in case of an error.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-889846937%2FClasslikes%2F1617540583" anchor-label="CalculateTrafficOnRouteCallback" id="-889846937%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-calculate-traffic-on-route-callback/index.html"><span>Calculate</span><wbr></wbr><span>Traffic</span><wbr></wbr><span>On</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-889846937%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-calculate-traffic-on-route-callback/index.html">CalculateTrafficOnRouteCallback</a></div><div class="brief "><p class="paragraph">A function which is called by the RoutingEngine after route traffic calculation has completed. It is always called on the main thread. The first argument is the error in case of a failure. It is <code class="lang-kotlin">null</code> for an operation that succeeds. The second argument is the calculated route traffic. It is <code class="lang-kotlin">null</code> in case of an error.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="60308729%2FClasslikes%2F1617540583" anchor-label="CarOptions" id="60308729%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-car-options/index.html"><span>Car</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="60308729%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-car-options/index.html"><strike>CarOptions</strike></a></div><div class="brief "><p class="paragraph">All the options to specify how a car route should be calculated.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="569941860%2FClasslikes%2F1617540583" anchor-label="ChargingActionDetails" id="569941860%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-charging-action-details/index.html"><span>Charging</span><wbr></wbr><span>Action</span><wbr></wbr><span><span>Details</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="569941860%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-charging-action-details/index.html">ChargingActionDetails</a></div><div class="brief "><p class="paragraph">Parameters related to the electric vehicle's charging action.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-327412532%2FClasslikes%2F1617540583" anchor-label="ChargingConnectorAttributes" id="-327412532%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-charging-connector-attributes/index.html"><span>Charging</span><wbr></wbr><span>Connector</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-327412532%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-charging-connector-attributes/index.html">ChargingConnectorAttributes</a></div><div class="brief "><p class="paragraph">Details of the connector that is suggested to be used in the section's <a href="-post-action/index.html">com.here.sdk.routing.PostAction</a>'s for charging.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1709668809%2FClasslikes%2F1617540583" anchor-label="ChargingConnectorType" id="1709668809%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-charging-connector-type/index.html"><span>Charging</span><wbr></wbr><span>Connector</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1709668809%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-charging-connector-type/index.html">ChargingConnectorType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-charging-connector-type/index.html">ChargingConnectorType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Available charging connector types.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-892334692%2FClasslikes%2F1617540583" anchor-label="ChargingStation" id="-892334692%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-charging-station/index.html"><span>Charging</span><wbr></wbr><span><span>Station</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-892334692%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-charging-station/index.html">ChargingStation</a></div><div class="brief "><p class="paragraph">Data for an electric vehicle charging station.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1602489008%2FClasslikes%2F1617540583" anchor-label="ChargingStop" id="1602489008%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-charging-stop/index.html"><span>Charging</span><wbr></wbr><span><span>Stop</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1602489008%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-charging-stop/index.html">ChargingStop</a></div><div class="brief "><p class="paragraph">The options to specify a user-planned charging stop. <strong>Note:</strong> In order to specify this <a href="-charging-stop/index.html">com.here.sdk.routing.ChargingStop</a>, it is also required to set sdk.routing.BatterySpecifications.total_capacity_in_kilowatt_hours, sdk.routing.BatterySpecifications.initial_charge_in_kilowatt_hours, and sdk.routing.BatterySpecifications.charging_curve. Without all of them, the route calculation will fail as an invalid parameter error.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="916856585%2FClasslikes%2F1617540583" anchor-label="ChargingSupplyType" id="916856585%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-charging-supply-type/index.html"><span>Charging</span><wbr></wbr><span>Supply</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="916856585%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-charging-supply-type/index.html">ChargingSupplyType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-charging-supply-type/index.html">ChargingSupplyType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Available charging supply types.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2056903411%2FClasslikes%2F1617540583" anchor-label="DynamicSpeedInfo" id="-2056903411%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-dynamic-speed-info/index.html"><span>Dynamic</span><wbr></wbr><span>Speed</span><wbr></wbr><span><span>Info</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2056903411%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-dynamic-speed-info/index.html">DynamicSpeedInfo</a></div><div class="brief "><p class="paragraph">Provides estimated speed information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1406009996%2FClasslikes%2F1617540583" anchor-label="ElectricVehicleOptions" id="-1406009996%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-electric-vehicle-options/index.html"><span>Electric</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1406009996%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-electric-vehicle-options/index.html">ElectricVehicleOptions</a></div><div class="brief "><p class="paragraph">These options define the parameters of the electric vehicle. <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1497659931%2FClasslikes%2F1617540583" anchor-label="EmpiricalConsumptionModel" id="1497659931%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-empirical-consumption-model/index.html"><span>Empirical</span><wbr></wbr><span>Consumption</span><wbr></wbr><span><span>Model</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1497659931%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-empirical-consumption-model/index.html">EmpiricalConsumptionModel</a></div><div class="brief "><p class="paragraph">This model defines a data-driven energy consumption model for electric vehicles.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1462271448%2FClasslikes%2F1617540583" anchor-label="EVCarOptions" id="-1462271448%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-v-car-options/index.html"><span>EVCar</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1462271448%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-e-v-car-options/index.html"><strike>EVCarOptions</strike></a></div><div class="brief "><p class="paragraph">All the options to specify how a route for an electric car should be calculated. At minimum, a valid <a href="-e-v-consumption-model/index.html">com.here.sdk.routing.EVConsumptionModel</a> must be set or the route calculation will fail. <br> Note: <a href="-e-v-car-options/ensure-reachability.html">com.here.sdk.routing.EVCarOptions.ensureReachability</a> must be <code class="lang-kotlin">true</code> to make sure that all stopovers are reachable. For this, charging stations may be added to the route. If <a href="-e-v-car-options/ensure-reachability.html">com.here.sdk.routing.EVCarOptions.ensureReachability</a> is true, you need to specify the required route options and battery specifications that include the current charge level of the battery (<a href="-battery-specifications/initial-charge-in-kilowatt-hours.html">com.here.sdk.routing.BatterySpecifications.initialChargeInKilowattHours</a>). See the parameter description below for more details.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="947391940%2FClasslikes%2F1617540583" anchor-label="EVConsumptionModel" id="947391940%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-v-consumption-model/index.html"><span>EVConsumption</span><wbr></wbr><span><span>Model</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="947391940%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-e-v-consumption-model/index.html">EVConsumptionModel</a></div><div class="brief "><p class="paragraph">Parameters specific for the electric vehicle, which are then used to calculate energy consumption on a given route. At minimum, you must provide <a href="-e-v-consumption-model/ascent-consumption-in-watt-hours-per-meter.html">com.here.sdk.routing.EVConsumptionModel.ascentConsumptionInWattHoursPerMeter</a>, <a href="-e-v-consumption-model/descent-recovery-in-watt-hours-per-meter.html">com.here.sdk.routing.EVConsumptionModel.descentRecoveryInWattHoursPerMeter</a> and a <a href="-e-v-consumption-model/free-flow-speed-table.html">com.here.sdk.routing.EVConsumptionModel.freeFlowSpeedTable</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1170262357%2FClasslikes%2F1617540583" anchor-label="EVMobilityServiceProviderPreferences" id="1170262357%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-v-mobility-service-provider-preferences/index.html"><span>EVMobility</span><wbr></wbr><span>Service</span><wbr></wbr><span>Provider</span><wbr></wbr><span><span>Preferences</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1170262357%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-e-v-mobility-service-provider-preferences/index.html">EVMobilityServiceProviderPreferences</a></div><div class="brief "><p class="paragraph">Defines preference level per known E-Mobility Service Provider. The E-Mobility Service Provider ID partner id as received from https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html An alternative way to get <code class="lang-kotlin">partnerId</code> is the <code class="lang-kotlin">eMobilityServiceProviders.partnerId</code> as part of <code class="lang-kotlin">HERE SDK Search</code>. Maximum number of E-Mobility Service Providers is limited to 10 across all preference. Defaults to using all available providers with no prioritization.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-121069965%2FClasslikes%2F1617540583" anchor-label="EVTruckOptions" id="-121069965%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-v-truck-options/index.html"><span>EVTruck</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-121069965%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-e-v-truck-options/index.html"><strike>EVTruckOptions</strike></a></div><div class="brief "><p class="paragraph">All the options to specify how a route for an electric truck should be calculated.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="530892533%2FClasslikes%2F1617540583" anchor-label="Fare" id="530892533%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-fare/index.html"><span><span>Fare</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="530892533%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-fare/index.html">Fare</a></div><div class="brief "><p class="paragraph">Holds all the fare data.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="878979153%2FClasslikes%2F1617540583" anchor-label="FarePassValidityPeriod" id="878979153%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-fare-pass-validity-period/index.html"><span>Fare</span><wbr></wbr><span>Pass</span><wbr></wbr><span>Validity</span><wbr></wbr><span><span>Period</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="878979153%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-fare-pass-validity-period/index.html">FarePassValidityPeriod</a></div><div class="brief "><p class="paragraph">Specifies a temporal validity period for a pass</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="270970423%2FClasslikes%2F1617540583" anchor-label="FarePassValidityPeriodType" id="270970423%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-fare-pass-validity-period-type/index.html"><span>Fare</span><wbr></wbr><span>Pass</span><wbr></wbr><span>Validity</span><wbr></wbr><span>Period</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="270970423%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-fare-pass-validity-period-type/index.html">FarePassValidityPeriodType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-fare-pass-validity-period-type/index.html">FarePassValidityPeriodType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies validity periods.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2080927460%2FClasslikes%2F1617540583" anchor-label="FarePrice" id="2080927460%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-fare-price/index.html"><span>Fare</span><wbr></wbr><span><span>Price</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2080927460%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-fare-price/index.html">FarePrice</a></div><div class="brief "><p class="paragraph">Price of a fare.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-934317238%2FClasslikes%2F1617540583" anchor-label="FarePriceType" id="-934317238%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-fare-price-type/index.html"><span>Fare</span><wbr></wbr><span>Price</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-934317238%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-fare-price-type/index.html">FarePriceType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-fare-price-type/index.html">FarePriceType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Type of price represented by a <a href="-fare-price/index.html">com.here.sdk.routing.FarePrice</a> object.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="398056977%2FClasslikes%2F1617540583" anchor-label="FareReason" id="398056977%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-fare-reason/index.html"><span>Fare</span><wbr></wbr><span><span>Reason</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="398056977%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-fare-reason/index.html">FareReason</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-fare-reason/index.html">FareReason</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Reason for the cost.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1733531882%2FClasslikes%2F1617540583" anchor-label="FunctionalRoadClass" id="1733531882%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-functional-road-class/index.html"><span>Functional</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Class</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1733531882%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-functional-road-class/index.html">FunctionalRoadClass</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-functional-road-class/index.html">FunctionalRoadClass</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Types of function road class.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1388116%2FClasslikes%2F1617540583" anchor-label="IndoorLevelChangeData" id="1388116%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-indoor-level-change-data/index.html"><span>Indoor</span><wbr></wbr><span>Level</span><wbr></wbr><span>Change</span><wbr></wbr><span><span>Data</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1388116%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-indoor-level-change-data/index.html">IndoorLevelChangeData</a></div><div class="brief "><p class="paragraph">Represents the level change data for an indoor maneuver.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-318413151%2FClasslikes%2F1617540583" anchor-label="IndoorLevelChangeFeatures" id="-318413151%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-indoor-level-change-features/index.html"><span>Indoor</span><wbr></wbr><span>Level</span><wbr></wbr><span>Change</span><wbr></wbr><span><span>Features</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-318413151%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-indoor-level-change-features/index.html">IndoorLevelChangeFeatures</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-indoor-level-change-features/index.html">IndoorLevelChangeFeatures</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indoor route features.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1711443735%2FClasslikes%2F1617540583" anchor-label="IndoorManeuver" id="1711443735%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-indoor-maneuver/index.html"><span>Indoor</span><wbr></wbr><span><span>Maneuver</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1711443735%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-indoor-maneuver/index.html">IndoorManeuver</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Represents a maneuver within an indoor section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="324096078%2FClasslikes%2F1617540583" anchor-label="IndoorManeuverActions" id="324096078%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-indoor-maneuver-actions/index.html"><span>Indoor</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span><span>Actions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="324096078%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-indoor-maneuver-actions/index.html">IndoorManeuverActions</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-indoor-maneuver-actions/index.html">IndoorManeuverActions</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Defines the types of actions for indoor maneuvers.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="650203794%2FClasslikes%2F1617540583" anchor-label="IndoorRoutePlace" id="650203794%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-indoor-route-place/index.html"><span>Indoor</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Place</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="650203794%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-indoor-route-place/index.html">IndoorRoutePlace</a></div><div class="brief "><p class="paragraph">Represents a place within an indoor route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2121060499%2FClasslikes%2F1617540583" anchor-label="IndoorSectionDetails" id="2121060499%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-indoor-section-details/index.html"><span>Indoor</span><wbr></wbr><span>Section</span><wbr></wbr><span><span>Details</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2121060499%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-indoor-section-details/index.html">IndoorSectionDetails</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Provides additional details for an indoor <a href="-section/index.html">com.here.sdk.routing.Section</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2125975646%2FClasslikes%2F1617540583" anchor-label="IndoorSpaceData" id="-2125975646%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-indoor-space-data/index.html"><span>Indoor</span><wbr></wbr><span>Space</span><wbr></wbr><span><span>Data</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2125975646%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-indoor-space-data/index.html">IndoorSpaceData</a></div><div class="brief "><p class="paragraph">Represents the space data for an indoor maneuver.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="916067302%2FClasslikes%2F1617540583" anchor-label="Isoline" id="916067302%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-isoline/index.html"><span><span>Isoline</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="916067302%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-isoline/index.html">Isoline</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Represents an isoline polygon around a center point. Any possible route between the center and any point on the edges of the polygon can be travelled within the given range restriction. The edges of the polygon are not guaranteed to be on the road as all reachable road endpoints are smoothened to fit into one polygon shape. This process can be influenced by setting <a href="-isoline-options/-calculation/max-points.html">com.here.sdk.routing.IsolineOptions.Calculation.maxPoints</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="89956720%2FClasslikes%2F1617540583" anchor-label="IsolineCalculationMode" id="89956720%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-isoline-calculation-mode/index.html"><span>Isoline</span><wbr></wbr><span>Calculation</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="89956720%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-isoline-calculation-mode/index.html">IsolineCalculationMode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-isoline-calculation-mode/index.html">IsolineCalculationMode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies how isoline calculation is optimized.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1468415518%2FClasslikes%2F1617540583" anchor-label="IsolineOptions" id="1468415518%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-isoline-options/index.html"><span>Isoline</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1468415518%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-isoline-options/index.html">IsolineOptions</a></div><div class="brief "><p class="paragraph">Specifies options for isolines calculation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1758227963%2FClasslikes%2F1617540583" anchor-label="IsolineRangeType" id="-1758227963%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-isoline-range-type/index.html"><span>Isoline</span><wbr></wbr><span>Range</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1758227963%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-isoline-range-type/index.html">IsolineRangeType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-isoline-range-type/index.html">IsolineRangeType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies the type of one or more range values to be included in the isoline. This value defines the restriction that is used to calculate the reachable area.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-64789228%2FClasslikes%2F1617540583" anchor-label="IsolineRoutingEngine" id="-64789228%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-isoline-routing-engine/index.html"><span>Isoline</span><wbr></wbr><span>Routing</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-64789228%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-isoline-routing-engine/index.html">IsolineRoutingEngine</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Use the IsolineRoutingEngine to calculate a reachable area from a center point. The calculation is done asynchronously and requires an online connection.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-853837093%2FClasslikes%2F1617540583" anchor-label="LocalizedRoadNumber" id="-853837093%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-localized-road-number/index.html"><span>Localized</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Number</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-853837093%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-localized-road-number/index.html">LocalizedRoadNumber</a></div><div class="brief "><p class="paragraph">Used to represent road number localized to specific language with optional direction and route type information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-780264012%2FClasslikes%2F1617540583" anchor-label="LocalizedRoadNumbers" id="-780264012%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-localized-road-numbers/index.html"><span>Localized</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Numbers</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-780264012%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-localized-road-numbers/index.html">LocalizedRoadNumbers</a></div><div class="brief "><p class="paragraph">The list of multiple names or titles for the same entity, possibly in different languages.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1848158500%2FClasslikes%2F1617540583" anchor-label="LocalizedTextPreference" id="-1848158500%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-localized-text-preference/index.html"><span>Localized</span><wbr></wbr><span>Text</span><wbr></wbr><span><span>Preference</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1848158500%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-localized-text-preference/index.html">LocalizedTextPreference</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-localized-text-preference/index.html">LocalizedTextPreference</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates the option of localized text usage.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1452883114%2FClasslikes%2F1617540583" anchor-label="Maneuver" id="1452883114%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-maneuver/index.html"><span><span>Maneuver</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1452883114%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-maneuver/index.html">Maneuver</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">This class provides all the information for a maneuver. The directional information (e.g. road names, road numbers and signpost direction) is stored in <a href="-maneuver/road-texts.html">com.here.sdk.routing.Maneuver.roadTexts</a> and <a href="-maneuver/next-road-texts.html">com.here.sdk.routing.Maneuver.nextRoadTexts</a> attributes. As for the motorway exit information, it can be obtained from <a href="-maneuver/exit-sign-texts.html">com.here.sdk.routing.Maneuver.exitSignTexts</a> attribute.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="729776212%2FClasslikes%2F1617540583" anchor-label="ManeuverAction" id="729776212%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-maneuver-action/index.html"><span>Maneuver</span><wbr></wbr><span><span>Action</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="729776212%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-maneuver-action/index.html">ManeuverAction</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-maneuver-action/index.html">ManeuverAction</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Maneuver action type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1507895788%2FClasslikes%2F1617540583" anchor-label="MapMatchedCoordinates" id="1507895788%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-matched-coordinates/index.html"><span>Map</span><wbr></wbr><span>Matched</span><wbr></wbr><span><span>Coordinates</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1507895788%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-map-matched-coordinates/index.html">MapMatchedCoordinates</a></div><div class="brief "><p class="paragraph">Information about the user defined coordinates and where they match to the map.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="328293737%2FClasslikes%2F1617540583" anchor-label="MatchSideOfStreet" id="328293737%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-match-side-of-street/index.html"><span>Match</span><wbr></wbr><span>Side</span><wbr></wbr><span>Of</span><wbr></wbr><span><span>Street</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="328293737%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-match-side-of-street/index.html">MatchSideOfStreet</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-match-side-of-street/index.html">MatchSideOfStreet</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies how the location set by <a href="-waypoint/side-of-street-hint.html">com.here.sdk.routing.Waypoint.sideOfStreetHint</a> should be handled. This setting might affect the geometry of the resulting route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1383886976%2FClasslikes%2F1617540583" anchor-label="MaxAxleGroupWeight" id="-1383886976%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-max-axle-group-weight/index.html"><span>Max</span><wbr></wbr><span>Axle</span><wbr></wbr><span>Group</span><wbr></wbr><span><span>Weight</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1383886976%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-max-axle-group-weight/index.html">MaxAxleGroupWeight</a></div><div class="brief "><p class="paragraph"><code class="lang-kotlin">MaxAxleGroupWeight</code> contains all the restriction details violated by an axle group weight.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="17971470%2FClasslikes%2F1617540583" anchor-label="MaxSpeedOnSegment" id="17971470%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-max-speed-on-segment/index.html"><span>Max</span><wbr></wbr><span>Speed</span><wbr></wbr><span>On</span><wbr></wbr><span><span>Segment</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="17971470%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-max-speed-on-segment/index.html">MaxSpeedOnSegment</a></div><div class="brief "><p class="paragraph">New base speed for a segment. Affects route calculation and the ETA. Cannot increase base speed on segment.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1244671858%2FClasslikes%2F1617540583" anchor-label="NoticeSeverity" id="-1244671858%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-notice-severity/index.html"><span>Notice</span><wbr></wbr><span><span>Severity</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1244671858%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-notice-severity/index.html">NoticeSeverity</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-notice-severity/index.html">NoticeSeverity</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Describes the impact a notice has on the resource to which the notice is attached.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-688727629%2FClasslikes%2F1617540583" anchor-label="OptimizationMode" id="-688727629%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-optimization-mode/index.html"><span>Optimization</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-688727629%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-optimization-mode/index.html">OptimizationMode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-optimization-mode/index.html">OptimizationMode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Identifiers for different optimizations that can be used during the route calculation while trying to keep the quality of the route being calculated high. The route is considered to be of low quality if it gives the traveler an unpleasant experience, such as having difficult turns or having a lot of turns in general. For example, if there are two possible routes from A to B, one with a length of 1000m and 10 turns, and another with a length of 1050m and only one turn, the second one will be returned as the shortest, although it is 50m longer. Yet, it contains only one turn and it is therefore considered to provide a better traveler experience.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-676019510%2FClasslikes%2F1617540583" anchor-label="PassThroughWaypoint" id="-676019510%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-pass-through-waypoint/index.html"><span>Pass</span><wbr></wbr><span>Through</span><wbr></wbr><span><span>Waypoint</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-676019510%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-pass-through-waypoint/index.html">PassThroughWaypoint</a></div><div class="brief "><p class="paragraph">This structure provides all the information for a passthrough waypoint. The location information and offset of the waypoint are stored in <a href="-pass-through-waypoint/place.html">com.here.sdk.routing.PassThroughWaypoint.place</a> and <a href="-pass-through-waypoint/offset.html">com.here.sdk.routing.PassThroughWaypoint.offset</a> respectively.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="88635544%2FClasslikes%2F1617540583" anchor-label="PaymentMethod" id="88635544%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-payment-method/index.html"><span>Payment</span><wbr></wbr><span><span>Method</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="88635544%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-payment-method/index.html">PaymentMethod</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-payment-method/index.html">PaymentMethod</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Available payment methods.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1391629124%2FClasslikes%2F1617540583" anchor-label="PedestrianOptions" id="-1391629124%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-pedestrian-options/index.html"><span>Pedestrian</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1391629124%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-pedestrian-options/index.html"><strike>PedestrianOptions</strike></a></div><div class="brief "><p class="paragraph">All the options to specify how a pedestrian route should be calculated.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1415951038%2FClasslikes%2F1617540583" anchor-label="PhysicalConsumptionModel" id="1415951038%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-physical-consumption-model/index.html"><span>Physical</span><wbr></wbr><span>Consumption</span><wbr></wbr><span><span>Model</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1415951038%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-physical-consumption-model/index.html">PhysicalConsumptionModel</a></div><div class="brief "><p class="paragraph">Defines the physical consumption model for electric vehicles, using vehicle-specific parameters to calculate energy consumption along a route. <strong>Note:</strong> sdk.transport.VehicleSpecification.current_weight_in_kilograms must be set. <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="814651309%2FClasslikes%2F1617540583" anchor-label="PostAction" id="814651309%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-post-action/index.html"><span>Post</span><wbr></wbr><span><span>Action</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="814651309%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-post-action/index.html">PostAction</a></div><div class="brief "><p class="paragraph">An action that must be done after arrival, i.e. completing a section in the route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="143789971%2FClasslikes%2F1617540583" anchor-label="PostActionType" id="143789971%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-post-action-type/index.html"><span>Post</span><wbr></wbr><span>Action</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="143789971%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-post-action-type/index.html">PostActionType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-post-action-type/index.html">PostActionType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Identifies the action type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2135648166%2FClasslikes%2F1617540583" anchor-label="PreAction" id="2135648166%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-pre-action/index.html"><span>Pre</span><wbr></wbr><span><span>Action</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2135648166%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-pre-action/index.html">PreAction</a></div><div class="brief "><p class="paragraph">An action that must be done prior to the section, i.e. boarding a ferry.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="201603852%2FClasslikes%2F1617540583" anchor-label="PreActionType" id="201603852%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-pre-action-type/index.html"><span>Pre</span><wbr></wbr><span>Action</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="201603852%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-pre-action-type/index.html">PreActionType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-pre-action-type/index.html">PreActionType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Identifies the action type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1350720642%2FClasslikes%2F1617540583" anchor-label="PrivateBusOptions" id="-1350720642%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-private-bus-options/index.html"><span>Private</span><wbr></wbr><span>Bus</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1350720642%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-private-bus-options/index.html"><strike>PrivateBusOptions</strike></a></div><div class="brief "><p class="paragraph">All the options to specify how a private bus route should be calculated.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1854883375%2FClasslikes%2F1617540583" anchor-label="RefreshRouteOptions" id="1854883375%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-refresh-route-options/index.html"><span>Refresh</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1854883375%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-refresh-route-options/index.html"><strike>RefreshRouteOptions</strike></a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">The options to specify how to refresh an already calculated route identified by a <a href="-route-handle/index.html">com.here.sdk.routing.RouteHandle</a>. All the options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored: <a href="-route-options/alternatives.html">com.here.sdk.routing.RouteOptions.alternatives</a>, <a href="-route-options/arrival-time.html">com.here.sdk.routing.RouteOptions.arrivalTime</a>, and <a href="-route-options/optimization-mode.html">com.here.sdk.routing.RouteOptions.optimizationMode</a>. If new <a href="-avoidance-options/index.html">com.here.sdk.routing.AvoidanceOptions</a> are specified, they are ignored as well and instead new <a href="-section-notice/index.html">com.here.sdk.routing.SectionNotice</a>'s are generated that indicate where the requested <a href="-avoidance-options/index.html">com.here.sdk.routing.AvoidanceOptions</a> are violated. Note that when <a href="-e-v-car-options/ensure-reachability.html">com.here.sdk.routing.EVCarOptions.ensureReachability</a> is set to true, the route refresh request will fail as this option is incompatible with a fixed route shape. If any of the ignored options are important, consider calculating a new route instead.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1531398443%2FClasslikes%2F1617540583" anchor-label="RefreshRouteParameters" id="1531398443%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-refresh-route-parameters/index.html"><span>Refresh</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Parameters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1531398443%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-refresh-route-parameters/index.html">RefreshRouteParameters</a></div><div class="brief "><p class="paragraph">This class provides the necessary information for refreshing a route from a specific location on it.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1595223174%2FClasslikes%2F1617540583" anchor-label="RoadFeatures" id="1595223174%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-road-features/index.html"><span>Road</span><wbr></wbr><span><span>Features</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1595223174%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-road-features/index.html">RoadFeatures</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-road-features/index.html">RoadFeatures</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Road features or states.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="157093209%2FClasslikes%2F1617540583" anchor-label="RoadTexts" id="157093209%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-road-texts/index.html"><span>Road</span><wbr></wbr><span><span>Texts</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="157093209%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-road-texts/index.html">RoadTexts</a></div><div class="brief "><p class="paragraph">Textual attributes of road.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="786785558%2FClasslikes%2F1617540583" anchor-label="Route" id="786785558%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-route/index.html"><span><span>Route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="786785558%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-route/index.html">Route</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">A route is a path through a road network over which someone travels.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="229059598%2FClasslikes%2F1617540583" anchor-label="RouteHandle" id="229059598%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-route-handle/index.html"><span>Route</span><wbr></wbr><span><span>Handle</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="229059598%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-route-handle/index.html">RouteHandle</a></div><div class="brief "><p class="paragraph">Provides an opaque handle to the calculated <a href="-route/index.html">com.here.sdk.routing.Route</a>. A handle encodes the calculated route. The route can be decoded from a handle at a later point in time as long as the service uses the same map data which was used during encoding. Note that the <a href="-route/route-handle.html">com.here.sdk.routing.Route.routeHandle</a> is provided only if <a href="-route-options/enable-route-handle.html">com.here.sdk.routing.RouteOptions.enableRouteHandle</a> is set before route calculation. A <code class="lang-kotlin">RouteHandle</code> generated by the online <code class="lang-kotlin">RoutingEngine</code> is not compatible with the <code class="lang-kotlin">OfflineRoutingEngine</code>. Similarly, a <code class="lang-kotlin">RouteHandle</code> from the <code class="lang-kotlin">OfflineRoutingEngine</code> cannot be used with the online <code class="lang-kotlin">RoutingEngine</code>. Using an incompatible <code class="lang-kotlin">RouteHandle</code> results in a <a href="-routing-error/index.html">com.here.sdk.routing.RoutingError</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-207235560%2FClasslikes%2F1617540583" anchor-label="RouteLabel" id="-207235560%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-route-label/index.html"><span>Route</span><wbr></wbr><span><span>Label</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-207235560%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-route-label/index.html">RouteLabel</a></div><div class="brief "><p class="paragraph">The main street name or road number for a route. A route can contain more than one such street name or route number. To include route labels in the route response, enable it using <a href="-route-options/enable-route-labels.html">com.here.sdk.routing.RouteOptions.enableRouteLabels</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-675405698%2FClasslikes%2F1617540583" anchor-label="RouteLabelType" id="-675405698%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-route-label-type/index.html"><span>Route</span><wbr></wbr><span>Label</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-675405698%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-route-label-type/index.html">RouteLabelType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-route-label-type/index.html">RouteLabelType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Identifies the type of the route label.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-5721085%2FClasslikes%2F1617540583" anchor-label="RouteOffset" id="-5721085%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-route-offset/index.html"><span>Route</span><wbr></wbr><span><span>Offset</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-5721085%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-route-offset/index.html">RouteOffset</a></div><div class="brief "><p class="paragraph">Represents a specific location along the route. A <code class="lang-kotlin">RouteOffset</code> is a location on the route defined by the section index and the distance in meters from the start of that section to the specified location on the route. An offset in meters indicates the distance that needs to be traveled to reach a specific location along the route, such as a railway crossing. For the latter case, the location of a railway crossing can be retrieved from <code class="lang-kotlin">RouteRailwayCrossing.coordinates</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1044788974%2FClasslikes%2F1617540583" anchor-label="RouteOptions" id="1044788974%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-route-options/index.html"><span>Route</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1044788974%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-route-options/index.html">RouteOptions</a></div><div class="brief "><p class="paragraph">The options to specify how the route will be calculated.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1281550181%2FClasslikes%2F1617540583" anchor-label="RoutePlace" id="1281550181%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-route-place/index.html"><span>Route</span><wbr></wbr><span><span>Place</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1281550181%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-route-place/index.html">RoutePlace</a></div><div class="brief "><p class="paragraph">The location information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1142066946%2FClasslikes%2F1617540583" anchor-label="RoutePlaceDirection" id="-1142066946%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-route-place-direction/index.html"><span>Route</span><wbr></wbr><span>Place</span><wbr></wbr><span><span>Direction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1142066946%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-route-place-direction/index.html">RoutePlaceDirection</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-route-place-direction/index.html">RoutePlaceDirection</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies the direction to make distinction between departure and arrival cases.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2110243659%2FClasslikes%2F1617540583" anchor-label="RoutePlaceType" id="2110243659%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-route-place-type/index.html"><span>Route</span><wbr></wbr><span>Place</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2110243659%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-route-place-type/index.html">RoutePlaceType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-route-place-type/index.html">RoutePlaceType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Identifies the route place type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-726613811%2FClasslikes%2F1617540583" anchor-label="RouteRailwayCrossing" id="-726613811%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-route-railway-crossing/index.html"><span>Route</span><wbr></wbr><span>Railway</span><wbr></wbr><span><span>Crossing</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-726613811%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-route-railway-crossing/index.html">RouteRailwayCrossing</a></div><div class="brief "><p class="paragraph">Contains information about railway crossing.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="255502515%2FClasslikes%2F1617540583" anchor-label="RouteRailwayCrossingType" id="255502515%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-route-railway-crossing-type/index.html"><span>Route</span><wbr></wbr><span>Railway</span><wbr></wbr><span>Crossing</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="255502515%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-route-railway-crossing-type/index.html">RouteRailwayCrossingType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-route-railway-crossing-type/index.html">RouteRailwayCrossingType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Identify possible type of route railway crossing.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="941783220%2FClasslikes%2F1617540583" anchor-label="RouteStop" id="941783220%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-route-stop/index.html"><span>Route</span><wbr></wbr><span><span>Stop</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="941783220%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-route-stop/index.html">RouteStop</a></div><div class="brief "><p class="paragraph">Route stop that should be used together with import route functionality. It specifies location index within provided route locations track. Route stop can have additional stop delay, which will be included in expected time to arrival. During navigation the stop will be treated as stopover and will be reported as milestone when passing-by. Only available for the Navigate licence.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="616580795%2FClasslikes%2F1617540583" anchor-label="RouteTextOptions" id="616580795%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-route-text-options/index.html"><span>Route</span><wbr></wbr><span>Text</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="616580795%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-route-text-options/index.html">RouteTextOptions</a></div><div class="brief "><p class="paragraph">Specify how textual output should be provided.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1541361048%2FClasslikes%2F1617540583" anchor-label="RoutingConnectionSettings" id="1541361048%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-routing-connection-settings/index.html"><span>Routing</span><wbr></wbr><span>Connection</span><wbr></wbr><span><span>Settings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1541361048%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-routing-connection-settings/index.html">RoutingConnectionSettings</a></div><div class="brief "><p class="paragraph">Defines the settings for the retry logic when connecting to the HERE routing backend.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-483530857%2FClasslikes%2F1617540583" anchor-label="RoutingEngine" id="-483530857%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-routing-engine/index.html"><span>Routing</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-483530857%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-routing-engine/index.html">RoutingEngine</a> : <a href="../com.here/-native-base/index.html">NativeBase</a>, <a href="-routing-interface/index.html">RoutingInterface</a></div><div class="brief "><p class="paragraph">Use the RoutingEngine to calculate a route from A to B with a number of waypoints in between.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1431581377%2FClasslikes%2F1617540583" anchor-label="RoutingError" id="1431581377%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-routing-error/index.html"><span>Routing</span><wbr></wbr><span><span>Error</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1431581377%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-routing-error/index.html">RoutingError</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-routing-error/index.html">RoutingError</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies possible errors that may result from the calculation of a route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1937527984%2FClasslikes%2F1617540583" anchor-label="RoutingInterface" id="1937527984%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-routing-interface/index.html"><span>Routing</span><wbr></wbr><span><span>Interface</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1937527984%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-routing-interface/index.html">RoutingInterface</a></div><div class="brief "><p class="paragraph">Provides the interface for the online and offline routing engines.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-153309973%2FClasslikes%2F1617540583" anchor-label="RoutingOptions" id="-153309973%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-routing-options/index.html"><span>Routing</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-153309973%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-routing-options/index.html">RoutingOptions</a></div><div class="brief "><p class="paragraph">The options defines how a route should be calculated.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="575318550%2FClasslikes%2F1617540583" anchor-label="ScooterOptions" id="575318550%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-scooter-options/index.html"><span>Scooter</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="575318550%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-scooter-options/index.html"><strike>ScooterOptions</strike></a></div><div class="brief "><p class="paragraph">All the options to specify how a scooter route should be calculated.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-266488710%2FClasslikes%2F1617540583" anchor-label="Section" id="-266488710%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-section/index.html"><span><span>Section</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-266488710%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-section/index.html">Section</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">A section is a part of the route between two stopovers. A stopover is a location on the route where a stop is made.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-367501886%2FClasslikes%2F1617540583" anchor-label="SectionNotice" id="-367501886%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-section-notice/index.html"><span>Section</span><wbr></wbr><span><span>Notice</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-367501886%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-section-notice/index.html">SectionNotice</a></div><div class="brief "><p class="paragraph">Explains an issue encountered in a <a href="-section/index.html">com.here.sdk.routing.Section</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-424967211%2FClasslikes%2F1617540583" anchor-label="SectionNoticeCode" id="-424967211%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-section-notice-code/index.html"><span>Section</span><wbr></wbr><span>Notice</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-424967211%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-section-notice-code/index.html">SectionNoticeCode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-section-notice-code/index.html">SectionNoticeCode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Notice codes which point the issues encountered during processing of a <a href="-section/index.html">com.here.sdk.routing.Section</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1213778876%2FClasslikes%2F1617540583" anchor-label="SectionTransportMode" id="1213778876%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-section-transport-mode/index.html"><span>Section</span><wbr></wbr><span>Transport</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1213778876%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-section-transport-mode/index.html">SectionTransportMode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-section-transport-mode/index.html">SectionTransportMode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies the <a href="-section/index.html">com.here.sdk.routing.Section</a> mode of transport. A <a href="-section/index.html">com.here.sdk.routing.Section</a> may have a different transport mode than the one specified for route calculation. For example, a car route may have a section having ferry transport mode.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="875953675%2FClasslikes%2F1617540583" anchor-label="SegmentReference" id="875953675%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-segment-reference/index.html"><span>Segment</span><wbr></wbr><span><span>Reference</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="875953675%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-segment-reference/index.html">SegmentReference</a></div><div class="brief "><p class="paragraph">Reference to a segment id with a travel direction.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-480479073%2FClasslikes%2F1617540583" anchor-label="SideOfDestination" id="-480479073%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-side-of-destination/index.html"><span>Side</span><wbr></wbr><span>Of</span><wbr></wbr><span><span>Destination</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-480479073%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-side-of-destination/index.html">SideOfDestination</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-side-of-destination/index.html">SideOfDestination</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies the side of street on which the destination is located.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1061611226%2FClasslikes%2F1617540583" anchor-label="Signpost" id="-1061611226%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-signpost/index.html"><span><span>Signpost</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1061611226%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-signpost/index.html">Signpost</a></div><div class="brief "><p class="paragraph">Signpost information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-783275000%2FClasslikes%2F1617540583" anchor-label="SignpostLabel" id="-783275000%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-signpost-label/index.html"><span>Signpost</span><wbr></wbr><span><span>Label</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-783275000%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-signpost-label/index.html">SignpostLabel</a></div><div class="brief "><p class="paragraph">Details of a signpost representing a particular direction or destination.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1758159015%2FClasslikes%2F1617540583" anchor-label="Span" id="-1758159015%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-span/index.html"><span><span>Span</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1758159015%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-span/index.html">Span</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">A span is a part of the <a href="-section/index.html">com.here.sdk.routing.Section</a> which is traversable or navigable. Each span usually has some geometry associated with it.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="320506857%2FClasslikes%2F1617540583" anchor-label="StreetAttributes" id="320506857%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-street-attributes/index.html"><span>Street</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="320506857%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-street-attributes/index.html">StreetAttributes</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-street-attributes/index.html">StreetAttributes</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Types of street attributes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1499490847%2FClasslikes%2F1617540583" anchor-label="TaxiOptions" id="1499490847%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-taxi-options/index.html"><span>Taxi</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1499490847%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-taxi-options/index.html"><strike>TaxiOptions</strike></a></div><div class="brief "><p class="paragraph">All the options to specify how a taxi route should be calculated. See, <a href="../com.here.sdk.transport/-transport-mode/-t-a-x-i/index.html">com.here.sdk.transport.TransportMode.TAXI</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="14658585%2FClasslikes%2F1617540583" anchor-label="TextUsageOptions" id="14658585%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-text-usage-options/index.html"><span>Text</span><wbr></wbr><span>Usage</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="14658585%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-text-usage-options/index.html">TextUsageOptions</a></div><div class="brief "><p class="paragraph">Specify whether the text should be used when generating notification.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1115459208%2FClasslikes%2F1617540583" anchor-label="Toll" id="1115459208%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-toll/index.html"><span><span>Toll</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1115459208%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-toll/index.html">Toll</a></div><div class="brief "><p class="paragraph">This struct presents all the data for a toll.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1890708870%2FClasslikes%2F1617540583" anchor-label="TollFare" id="-1890708870%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-toll-fare/index.html"><span>Toll</span><wbr></wbr><span><span>Fare</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1890708870%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-toll-fare/index.html">TollFare</a></div><div class="brief "><p class="paragraph">This struct presents all the fare data for a toll.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1061869289%2FClasslikes%2F1617540583" anchor-label="TollFarePass" id="1061869289%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-toll-fare-pass/index.html"><span>Toll</span><wbr></wbr><span>Fare</span><wbr></wbr><span><span>Pass</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1061869289%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-toll-fare-pass/index.html">TollFarePass</a></div><div class="brief "><p class="paragraph"><a href="-toll-fare/index.html">com.here.sdk.routing.TollFare</a> multi-travel pass characteristics.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1790645956%2FClasslikes%2F1617540583" anchor-label="TollOptions" id="-1790645956%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-toll-options/index.html"><span>Toll</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1790645956%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-toll-options/index.html">TollOptions</a></div><div class="brief "><p class="paragraph">The option to specify how the tolls should be calculated. <strong>Note</strong> Not used for offline calculations.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-101246840%2FClasslikes%2F1617540583" anchor-label="TrafficIncidentOnRoute" id="-101246840%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-incident-on-route/index.html"><span>Traffic</span><wbr></wbr><span>Incident</span><wbr></wbr><span>On</span><wbr></wbr><span><span>Route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-101246840%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-traffic-incident-on-route/index.html">TrafficIncidentOnRoute</a> : <a href="../com.here/-native-base/index.html">NativeBase</a>, <a href="../com.here.sdk.traffic/-traffic-incident-base/index.html">TrafficIncidentBase</a></div><div class="brief "><p class="paragraph">Traffic incidents on a route. Use <a href="-section/traffic-incidents.html">com.here.sdk.routing.Section.trafficIncidents</a> to get a list of incidents on a route section. Use <a href="-span/traffic-incident-indexes.html">com.here.sdk.routing.Span.trafficIncidentIndexes</a> to associate incidents with spans. Each incident takes at least the whole geometry of matching spans. Also, an incident can take some place out of the built route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="80074390%2FClasslikes%2F1617540583" anchor-label="TrafficOnRoute" id="80074390%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-on-route/index.html"><span>Traffic</span><wbr></wbr><span>On</span><wbr></wbr><span><span>Route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="80074390%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-traffic-on-route/index.html">TrafficOnRoute</a></div><div class="brief "><p class="paragraph">Traffic information on a route. Information for the already traveled portion of the route is omitted.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-811088390%2FClasslikes%2F1617540583" anchor-label="TrafficOnSection" id="-811088390%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-on-section/index.html"><span>Traffic</span><wbr></wbr><span>On</span><wbr></wbr><span><span>Section</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-811088390%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-traffic-on-section/index.html">TrafficOnSection</a></div><div class="brief "><p class="paragraph">Traffic information on a section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="851443161%2FClasslikes%2F1617540583" anchor-label="TrafficOnSpan" id="851443161%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-on-span/index.html"><span>Traffic</span><wbr></wbr><span>On</span><wbr></wbr><span><span>Span</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="851443161%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-traffic-on-span/index.html">TrafficOnSpan</a></div><div class="brief "><p class="paragraph">Traffic information of a span along a route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-956383342%2FClasslikes%2F1617540583" anchor-label="TrafficOptimizationMode" id="-956383342%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-optimization-mode/index.html"><span>Traffic</span><wbr></wbr><span>Optimization</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-956383342%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-traffic-optimization-mode/index.html">TrafficOptimizationMode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-traffic-optimization-mode/index.html">TrafficOptimizationMode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Traffic optimization mode that defines whether and what kind of traffic information should be considered during route calculation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1438522590%2FClasslikes%2F1617540583" anchor-label="TransitDeparture" id="-1438522590%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transit-departure/index.html"><span>Transit</span><wbr></wbr><span><span>Departure</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1438522590%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-transit-departure/index.html">TransitDeparture</a></div><div class="brief "><p class="paragraph">This struct holds the transit departure or arrival information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1686587024%2FClasslikes%2F1617540583" anchor-label="TransitDepartureStatus" id="1686587024%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transit-departure-status/index.html"><span>Transit</span><wbr></wbr><span>Departure</span><wbr></wbr><span><span>Status</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1686587024%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-transit-departure-status/index.html">TransitDepartureStatus</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-transit-departure-status/index.html">TransitDepartureStatus</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Status of a departure.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1171266150%2FClasslikes%2F1617540583" anchor-label="TransitIncident" id="-1171266150%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transit-incident/index.html"><span>Transit</span><wbr></wbr><span><span>Incident</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1171266150%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-transit-incident/index.html">TransitIncident</a></div><div class="brief "><p class="paragraph">A transit incident describes disruptions on the transit network. Disruptions scale from delays to service cancellations.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1621190217%2FClasslikes%2F1617540583" anchor-label="TransitIncidentEffect" id="1621190217%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transit-incident-effect/index.html"><span>Transit</span><wbr></wbr><span>Incident</span><wbr></wbr><span><span>Effect</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1621190217%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-transit-incident-effect/index.html">TransitIncidentEffect</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-transit-incident-effect/index.html">TransitIncidentEffect</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Transit incident effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="600874752%2FClasslikes%2F1617540583" anchor-label="TransitIncidentType" id="600874752%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transit-incident-type/index.html"><span>Transit</span><wbr></wbr><span>Incident</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="600874752%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-transit-incident-type/index.html">TransitIncidentType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-transit-incident-type/index.html">TransitIncidentType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Transit incident type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-574454935%2FClasslikes%2F1617540583" anchor-label="TransitMode" id="-574454935%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transit-mode/index.html"><span>Transit</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-574454935%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-transit-mode/index.html">TransitMode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-transit-mode/index.html">TransitMode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Public transit mode</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1590608687%2FClasslikes%2F1617540583" anchor-label="TransitModeFilter" id="-1590608687%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transit-mode-filter/index.html"><span>Transit</span><wbr></wbr><span>Mode</span><wbr></wbr><span><span>Filter</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1590608687%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-transit-mode-filter/index.html">TransitModeFilter</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-transit-mode-filter/index.html">TransitModeFilter</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Filtering mode for public transit.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1162289609%2FClasslikes%2F1617540583" anchor-label="TransitRouteOptions" id="-1162289609%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transit-route-options/index.html"><span>Transit</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1162289609%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-transit-route-options/index.html">TransitRouteOptions</a></div><div class="brief "><p class="paragraph">All the options to specify how a public transit route should be calculated.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-183490194%2FClasslikes%2F1617540583" anchor-label="TransitRoutingEngine" id="-183490194%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transit-routing-engine/index.html"><span>Transit</span><wbr></wbr><span>Routing</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-183490194%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-transit-routing-engine/index.html">TransitRoutingEngine</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Use the TransitRoutingEngine to calculate a public transit route from A to B with a number of waypoints in between. Route calculation is done asynchronously and requires an online connection. The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1193786607%2FClasslikes%2F1617540583" anchor-label="TransitSectionDetails" id="1193786607%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transit-section-details/index.html"><span>Transit</span><wbr></wbr><span>Section</span><wbr></wbr><span><span>Details</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1193786607%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-transit-section-details/index.html">TransitSectionDetails</a></div><div class="brief "><p class="paragraph">Gives the details of a transit section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="344542698%2FClasslikes%2F1617540583" anchor-label="TransitStop" id="344542698%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transit-stop/index.html"><span>Transit</span><wbr></wbr><span><span>Stop</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="344542698%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-transit-stop/index.html">TransitStop</a></div><div class="brief "><p class="paragraph">A transit stop between the departure and destination of a transit section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-948704627%2FClasslikes%2F1617540583" anchor-label="TransitTransport" id="-948704627%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transit-transport/index.html"><span>Transit</span><wbr></wbr><span><span>Transport</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-948704627%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-transit-transport/index.html">TransitTransport</a></div><div class="brief "><p class="paragraph">Holds all the transit transport information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="200656203%2FClasslikes%2F1617540583" anchor-label="TransitWaypoint" id="200656203%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transit-waypoint/index.html"><span>Transit</span><wbr></wbr><span><span>Waypoint</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="200656203%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-transit-waypoint/index.html">TransitWaypoint</a></div><div class="brief "><p class="paragraph">Represents a transit waypoint, used as input for transit route calculation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1116238810%2FClasslikes%2F1617540583" anchor-label="TravelDirection" id="1116238810%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-travel-direction/index.html"><span>Travel</span><wbr></wbr><span><span>Direction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1116238810%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-travel-direction/index.html">TravelDirection</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-travel-direction/index.html">TravelDirection</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Travel direction.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1505367804%2FClasslikes%2F1617540583" anchor-label="TruckOptions" id="-1505367804%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-truck-options/index.html"><span>Truck</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1505367804%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-truck-options/index.html"><strike>TruckOptions</strike></a></div><div class="brief "><p class="paragraph">All the options to specify how a truck route should be calculated.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2049692771%2FClasslikes%2F1617540583" anchor-label="VehicleRestrictionMaxWeight" id="2049692771%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-vehicle-restriction-max-weight/index.html"><span>Vehicle</span><wbr></wbr><span>Restriction</span><wbr></wbr><span>Max</span><wbr></wbr><span><span>Weight</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2049692771%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-vehicle-restriction-max-weight/index.html">VehicleRestrictionMaxWeight</a></div><div class="brief "><p class="paragraph"><code class="lang-kotlin">VehicleRestrictionMaxWeight</code> contains max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1825177271%2FClasslikes%2F1617540583" anchor-label="VehicleRestrictionMaxWeightType" id="-1825177271%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-vehicle-restriction-max-weight-type/index.html"><span>Vehicle</span><wbr></wbr><span>Restriction</span><wbr></wbr><span>Max</span><wbr></wbr><span>Weight</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1825177271%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-vehicle-restriction-max-weight-type/index.html">VehicleRestrictionMaxWeightType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-vehicle-restriction-max-weight-type/index.html">VehicleRestrictionMaxWeightType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">This enum represents the specific type of the maximum permitted weight restriction. <strong>NOTES:</strong> A restriction of type <a href="-vehicle-restriction-max-weight-type/-u-n-k-n-o-w-n/index.html">com.here.sdk.routing.VehicleRestrictionMaxWeightType.UNKNOWN</a> may change to <a href="-vehicle-restriction-max-weight-type/-g-r-o-s-s/index.html">com.here.sdk.routing.VehicleRestrictionMaxWeightType.GROSS</a>, <a href="-vehicle-restriction-max-weight-type/-c-u-r-r-e-n-t/index.html">com.here.sdk.routing.VehicleRestrictionMaxWeightType.CURRENT</a> or <a href="-vehicle-restriction-max-weight-type/-e-m-p-t-y/index.html">com.here.sdk.routing.VehicleRestrictionMaxWeightType.EMPTY</a> when data becomes available in future. A restriction of type <a href="-vehicle-restriction-max-weight-type/-g-r-o-s-s/index.html">com.here.sdk.routing.VehicleRestrictionMaxWeightType.GROSS</a>, <a href="-vehicle-restriction-max-weight-type/-c-u-r-r-e-n-t/index.html">com.here.sdk.routing.VehicleRestrictionMaxWeightType.CURRENT</a> or <a href="-vehicle-restriction-max-weight-type/-e-m-p-t-y/index.html">com.here.sdk.routing.VehicleRestrictionMaxWeightType.EMPTY</a> may also change to a different type if actual regulation changes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1935633547%2FClasslikes%2F1617540583" anchor-label="ViolatedRestriction" id="-1935633547%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-violated-restriction/index.html"><span>Violated</span><wbr></wbr><span><span>Restriction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1935633547%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-violated-restriction/index.html">ViolatedRestriction</a></div><div class="brief "><p class="paragraph"><code class="lang-kotlin">ViolatedRestriction</code> contains all the violated restriction details for the planned trip.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="723790051%2FClasslikes%2F1617540583" anchor-label="WalkAttributes" id="723790051%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-walk-attributes/index.html"><span>Walk</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="723790051%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-walk-attributes/index.html">WalkAttributes</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-walk-attributes/index.html">WalkAttributes</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Types of walk attributes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="58855810%2FClasslikes%2F1617540583" anchor-label="Waypoint" id="58855810%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-waypoint/index.html"><span><span>Waypoint</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="58855810%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-waypoint/index.html">Waypoint</a></div><div class="brief "><p class="paragraph">Represents a waypoint, used as input for route calculation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-556099864%2FClasslikes%2F1617540583" anchor-label="WaypointType" id="-556099864%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-waypoint-type/index.html"><span>Waypoint</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-556099864%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-waypoint-type/index.html">WaypointType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-waypoint-type/index.html">WaypointType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Defines if the waypoint is a stop over, or a hint for a desired polyline of a route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="985275353%2FClasslikes%2F1617540583" anchor-label="ZoneCategory" id="985275353%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-zone-category/index.html"><span>Zone</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="985275353%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-zone-category/index.html">ZoneCategory</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-zone-category/index.html">ZoneCategory</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Identifies categories of zones which routes avoid going through when used in <a href="-avoidance-options/index.html">com.here.sdk.routing.AvoidanceOptions</a>.</p></div></div></div>
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
