---
title: "IsolineOptions"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-isoline-options"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>IsolineOptions</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.routing/IsolineOptions///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.routing</a><span class="delimiter">/</span><span class="current">IsolineOptions</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Isoline</span><wbr></wbr><span><span>Options</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">IsolineOptions</a></div><p class="paragraph">Specifies options for isolines calculation.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="1119746191%2FConstructors%2F1617540583" anchor-label="IsolineOptions" id="1119746191%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-isoline-options.html"><span>Isoline</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1119746191%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">calculationOptions<span class="token operator">: </span><a href="-calculation/index.html">IsolineOptions.Calculation</a><span class="token punctuation">, </span></span><span class="parameter ">carOptions<span class="token operator">: </span><a href="../-car-options/index.html">CarOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and car routing options.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">calculationOptions<span class="token operator">: </span><a href="-calculation/index.html">IsolineOptions.Calculation</a><span class="token punctuation">, </span></span><span class="parameter ">truckOptions<span class="token operator">: </span><a href="../-truck-options/index.html">TruckOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and truck routing options.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">calculationOptions<span class="token operator">: </span><a href="-calculation/index.html">IsolineOptions.Calculation</a><span class="token punctuation">, </span></span><span class="parameter ">evCarOptions<span class="token operator">: </span><a href="../-e-v-car-options/index.html">EVCarOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and electric car routing options.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">calculationOptions<span class="token operator">: </span><a href="-calculation/index.html">IsolineOptions.Calculation</a><span class="token punctuation">, </span></span><span class="parameter ">evTruckOptions<span class="token operator">: </span><a href="../-e-v-truck-options/index.html">EVTruckOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and electric truck routing options.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">calculationOptions<span class="token operator">: </span><a href="-calculation/index.html">IsolineOptions.Calculation</a><span class="token punctuation">, </span></span><span class="parameter ">routingOptions<span class="token operator">: </span><a href="../-routing-options/index.html">RoutingOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and routing options. <strong>Notes</strong></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-1493181117%2FClasslikes%2F1617540583" anchor-label="Calculation" id="-1493181117%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-calculation/index.html"><span><span>Calculation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1493181117%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-calculation/index.html">Calculation</a></div><div class="brief "><p class="paragraph">Specifies isoline parameters. Setting at least one limit to <a href="-calculation/range-values.html">com.here.sdk.routing.IsolineOptions.Calculation.rangeValues</a> is mandatory or the calculation will fail.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="553667872%2FClasslikes%2F1617540583" anchor-label="Companion" id="553667872%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="553667872%2FClasslikes%2F1617540583"></span>
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
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-1081003732%2FProperties%2F1617540583" anchor-label="calculationOptions" id="-1081003732%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="calculation-options.html"><span>calculation</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1081003732%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="calculation-options.html">calculationOptions</a><span class="token operator">: </span><a href="-calculation/index.html">IsolineOptions.Calculation</a></div><div class="brief "><p class="paragraph">Specifies isoline parameters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1181321783%2FProperties%2F1617540583" anchor-label="carOptions" id="1181321783%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="car-options.html"><span>car</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1181321783%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="car-options.html"><strike>carOptions</strike></a><span class="token operator">: </span><a href="../-car-options/index.html">CarOptions</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Specifies options for calculation of isolines for car. Mutually exclusive with <a href="truck-options.html">com.here.sdk.routing.IsolineOptions.truckOptions</a>, <a href="ev-car-options.html">com.here.sdk.routing.IsolineOptions.evCarOptions</a>, <a href="ev-truck-options.html">com.here.sdk.routing.IsolineOptions.evTruckOptions</a> and <a href="routing-options.html">com.here.sdk.routing.IsolineOptions.routingOptions</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1250866886%2FProperties%2F1617540583" anchor-label="evCarOptions" id="1250866886%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="ev-car-options.html"><span>ev</span><wbr></wbr><span>Car</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1250866886%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="ev-car-options.html"><strike>evCarOptions</strike></a><span class="token operator">: </span><a href="../-e-v-car-options/index.html">EVCarOptions</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Specifies options for calculation of isolines for electric car. Mutually exclusive with <a href="car-options.html">com.here.sdk.routing.IsolineOptions.carOptions</a>, <a href="truck-options.html">com.here.sdk.routing.IsolineOptions.truckOptions</a>, <a href="ev-truck-options.html">com.here.sdk.routing.IsolineOptions.evTruckOptions</a> and <a href="routing-options.html">com.here.sdk.routing.IsolineOptions.routingOptions</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1336039057%2FProperties%2F1617540583" anchor-label="evTruckOptions" id="1336039057%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="ev-truck-options.html"><span>ev</span><wbr></wbr><span>Truck</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1336039057%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="ev-truck-options.html"><strike>evTruckOptions</strike></a><span class="token operator">: </span><a href="../-e-v-truck-options/index.html">EVTruckOptions</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Specifies options for calculation of isolines for electric truck. Mutually exclusive with <a href="car-options.html">com.here.sdk.routing.IsolineOptions.carOptions</a>, <a href="truck-options.html">com.here.sdk.routing.IsolineOptions.truckOptions</a>, <a href="ev-car-options.html">com.here.sdk.routing.IsolineOptions.evCarOptions</a> and <a href="routing-options.html">com.here.sdk.routing.IsolineOptions.routingOptions</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="593678633%2FProperties%2F1617540583" anchor-label="routingOptions" id="593678633%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="routing-options.html"><span>routing</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="593678633%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="routing-options.html">routingOptions</a><span class="token operator">: </span><a href="../-routing-options/index.html">RoutingOptions</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Specifies options for calculation of isolines for any vehicle type. Mutually exclusive with <a href="car-options.html">com.here.sdk.routing.IsolineOptions.carOptions</a>, <a href="truck-options.html">com.here.sdk.routing.IsolineOptions.truckOptions</a>, <a href="ev-car-options.html">com.here.sdk.routing.IsolineOptions.evCarOptions</a> and <a href="ev-truck-options.html">com.here.sdk.routing.IsolineOptions.evTruckOptions</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1072295486%2FProperties%2F1617540583" anchor-label="truckOptions" id="-1072295486%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="truck-options.html"><span>truck</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1072295486%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="truck-options.html"><strike>truckOptions</strike></a><span class="token operator">: </span><a href="../-truck-options/index.html">TruckOptions</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Specifies options for calculation of isolines for truck. Mutually exclusive with <a href="car-options.html">com.here.sdk.routing.IsolineOptions.carOptions</a>, <a href="ev-car-options.html">com.here.sdk.routing.IsolineOptions.evCarOptions</a>, <a href="ev-truck-options.html">com.here.sdk.routing.IsolineOptions.evTruckOptions</a> and <a href="routing-options.html">com.here.sdk.routing.IsolineOptions.routingOptions</a>.</p></div></div></div>
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
