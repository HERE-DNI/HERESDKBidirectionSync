---
title: "BatterySpecifications"
slug: "sdk-for-flutter-explore"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>BatterySpecifications</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.routing/BatterySpecifications///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.routing</a><span class="delimiter">/</span><span class="current">BatterySpecifications</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Battery</span><wbr></wbr><span><span>Specifications</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">BatterySpecifications</a></div><p class="paragraph">Parameters related to the electric vehicle's battery.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-1626525828%2FConstructors%2F1617540583" anchor-label="BatterySpecifications" id="-1626525828%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-battery-specifications"><span>Battery</span><wbr></wbr><span><span>Specifications</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1626525828%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html"><span class="token annotation builtin">JvmOverloads</span></a></div></div><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">totalCapacityInKilowattHours<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator"> = </span><span class="token constant">0.0</span><span class="token punctuation">, </span></span><span class="parameter ">initialChargeInKilowattHours<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator"> = </span><span class="token constant">0.0</span><span class="token punctuation">, </span></span><span class="parameter ">targetChargeInKilowattHours<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator"> = </span><span class="token constant">0.0</span><span class="token punctuation">, </span></span><span class="parameter ">chargingCurve<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">&gt;</span><span class="token operator"> = </span>mutableMapOf()<span class="token punctuation">, </span></span><span class="parameter ">connectorTypes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="sdk-for-flutter-explore-index">ChargingConnectorType</a><span class="token operator">&gt;</span><span class="token operator"> = </span>mutableListOf()<span class="token punctuation">, </span></span><span class="parameter ">minChargeAtChargingStationInKilowattHours<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator"> = </span><span class="token constant">0.0</span><span class="token punctuation">, </span></span><span class="parameter ">minChargeAtFirstChargingStationInKilowattHours<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span><span class="token operator"> = </span>null<span class="token punctuation">, </span></span><span class="parameter ">minChargeAtDestinationInKilowattHours<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator"> = </span><span class="token constant">0.0</span><span class="token punctuation">, </span></span><span class="parameter ">maxChargingVoltageInVolts<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span><span class="token operator"> = </span>null<span class="token punctuation">, </span></span><span class="parameter ">maxChargingCurrentInAmperes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span><span class="token operator"> = </span>null<span class="token punctuation">, </span></span><span class="parameter ">chargingSetupDuration<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Duration</a><span class="token operator"> = </span>Duration.ofSeconds(0L)<span class="token punctuation">, </span></span><span class="parameter ">maxPowerAtLowVoltageInKilowatts<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span><span class="token operator"> = </span>null</span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="1750776863%2FProperties%2F1617540583" anchor-label="chargingCurve" id="1750776863%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-charging-curve"><span>charging</span><wbr></wbr><span><span>Curve</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1750776863%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-charging-curve">chargingCurve</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \[0, <a href="sdk-for-flutter-explore-target-charge-in-kilowatt-hours">com.here.sdk.routing.BatterySpecifications.targetChargeInKilowattHours</a>\], otherwise the <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.BatterySpecifications</a> instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. <strong>Note:</strong> For a user-planned <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.ChargingStop</a>, this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1098003683%2FProperties%2F1617540583" anchor-label="chargingSetupDuration" id="-1098003683%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-charging-setup-duration"><span>charging</span><wbr></wbr><span>Setup</span><wbr></wbr><span><span>Duration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1098003683%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-charging-setup-duration">chargingSetupDuration</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Duration</a></div><div class="brief "><p class="paragraph">Time in seconds spent after arriving at a charging station, but before actually charging, e.g., time spent for payment processing. Defaults to 0 seconds.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="218569073%2FProperties%2F1617540583" anchor-label="connectorTypes" id="218569073%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-connector-types"><span>connector</span><wbr></wbr><span><span>Types</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="218569073%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-connector-types">connectorTypes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="sdk-for-flutter-explore-index">ChargingConnectorType</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">List of available charging connector types. It must be at least one charging connector type added, otherwise the <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.BatterySpecifications</a> instance is considered invalid. Defaults to an empty container.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1501739722%2FProperties%2F1617540583" anchor-label="initialChargeInKilowattHours" id="-1501739722%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-initial-charge-in-kilowatt-hours"><span>initial</span><wbr></wbr><span>Charge</span><wbr></wbr><span>In</span><wbr></wbr><span>Kilowatt</span><wbr></wbr><span><span>Hours</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1501739722%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-initial-charge-in-kilowatt-hours">initialChargeInKilowattHours</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of <a href="sdk-for-flutter-explore-total-capacity-in-kilowatt-hours">com.here.sdk.routing.BatterySpecifications.totalCapacityInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.BatterySpecifications</a> instance is considered invalid. Defaults to 0. <strong>Note:</strong> For a user-planned <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.ChargingStop</a>, this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1574646137%2FProperties%2F1617540583" anchor-label="maxChargingCurrentInAmperes" id="-1574646137%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-max-charging-current-in-amperes"><span>max</span><wbr></wbr><span>Charging</span><wbr></wbr><span>Current</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Amperes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1574646137%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-max-charging-current-in-amperes">maxChargingCurrentInAmperes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Maximum charging current supported by the vehicle's battery in Amperes. It must be positive. When omitted, the charging current is determined by the charging station attributes. Defaults to <code class="lang-kotlin">null</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="240075097%2FProperties%2F1617540583" anchor-label="maxChargingVoltageInVolts" id="240075097%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-max-charging-voltage-in-volts"><span>max</span><wbr></wbr><span>Charging</span><wbr></wbr><span>Voltage</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Volts</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="240075097%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-max-charging-voltage-in-volts">maxChargingVoltageInVolts</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Maximum charging voltage supported by the vehicle's battery in Volts. It must be positive. When omitted, the voltage is determined by the charging station attributes. Defaults to <code class="lang-kotlin">null</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="669441016%2FProperties%2F1617540583" anchor-label="maxPowerAtLowVoltageInKilowatts" id="669441016%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-max-power-at-low-voltage-in-kilowatts"><span>max</span><wbr></wbr><span>Power</span><wbr></wbr><span>At</span><wbr></wbr><span>Low</span><wbr></wbr><span>Voltage</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilowatts</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="669441016%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-max-power-at-low-voltage-in-kilowatts">maxPowerAtLowVoltageInKilowatts</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The maximum power in kilowatts at which a vehicle can charge under given these conditions:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="20994344%2FProperties%2F1617540583" anchor-label="minChargeAtChargingStationInKilowattHours" id="20994344%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-min-charge-at-charging-station-in-kilowatt-hours"><span>min</span><wbr></wbr><span>Charge</span><wbr></wbr><span>At</span><wbr></wbr><span>Charging</span><wbr></wbr><span>Station</span><wbr></wbr><span>In</span><wbr></wbr><span>Kilowatt</span><wbr></wbr><span><span>Hours</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="20994344%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-min-charge-at-charging-station-in-kilowatt-hours">minChargeAtChargingStationInKilowattHours</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">Minimum charge when arriving at a charging station in kWh. It must be non-negative and less than the value of <a href="sdk-for-flutter-explore-target-charge-in-kilowatt-hours">com.here.sdk.routing.BatterySpecifications.targetChargeInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.BatterySpecifications</a> instance is considered invalid. Defaults to 0.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1328497613%2FProperties%2F1617540583" anchor-label="minChargeAtDestinationInKilowattHours" id="-1328497613%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-min-charge-at-destination-in-kilowatt-hours"><span>min</span><wbr></wbr><span>Charge</span><wbr></wbr><span>At</span><wbr></wbr><span>Destination</span><wbr></wbr><span>In</span><wbr></wbr><span>Kilowatt</span><wbr></wbr><span><span>Hours</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1328497613%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-min-charge-at-destination-in-kilowatt-hours">minChargeAtDestinationInKilowattHours</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">Minimum charge at the final route destination in kWh. It must be non-negative and less than the value of <a href="sdk-for-flutter-explore-target-charge-in-kilowatt-hours">com.here.sdk.routing.BatterySpecifications.targetChargeInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.BatterySpecifications</a> instance is considered invalid. Defaults to 0.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-576692502%2FProperties%2F1617540583" anchor-label="minChargeAtFirstChargingStationInKilowattHours" id="-576692502%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-min-charge-at-first-charging-station-in-kilowatt-hours"><span>min</span><wbr></wbr><span>Charge</span><wbr></wbr><span>At</span><wbr></wbr><span>First</span><wbr></wbr><span>Charging</span><wbr></wbr><span>Station</span><wbr></wbr><span>In</span><wbr></wbr><span>Kilowatt</span><wbr></wbr><span><span>Hours</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-576692502%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-min-charge-at-first-charging-station-in-kilowatt-hours">minChargeAtFirstChargingStationInKilowattHours</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Minimum charge when arriving at first charging station in kWh. This overrides <a href="sdk-for-flutter-explore-min-charge-at-charging-station-in-kilowatt-hours">com.here.sdk.routing.BatterySpecifications.minChargeAtChargingStationInKilowattHours</a> for the first charging station. If not specified, <a href="sdk-for-flutter-explore-min-charge-at-charging-station-in-kilowatt-hours">com.here.sdk.routing.BatterySpecifications.minChargeAtChargingStationInKilowattHours</a> will be used for all charging stations, including the first one. Defaults to <code class="lang-kotlin">null</code>. When initialized, it must be non-negative and less than the value of <a href="sdk-for-flutter-explore-target-charge-in-kilowatt-hours">com.here.sdk.routing.BatterySpecifications.targetChargeInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.BatterySpecifications</a> instance is considered invalid. This is usually used when the current charge is too low to reach a charging station within <code class="lang-kotlin">minChargeAtChargingStation</code> limits.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-397569021%2FProperties%2F1617540583" anchor-label="targetChargeInKilowattHours" id="-397569021%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-target-charge-in-kilowatt-hours"><span>target</span><wbr></wbr><span>Charge</span><wbr></wbr><span>In</span><wbr></wbr><span>Kilowatt</span><wbr></wbr><span><span>Hours</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-397569021%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-target-charge-in-kilowatt-hours">targetChargeInKilowattHours</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of <a href="sdk-for-flutter-explore-total-capacity-in-kilowatt-hours">com.here.sdk.routing.BatterySpecifications.totalCapacityInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.BatterySpecifications</a> instance is considered invalid. Defaults to 0.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1018049596%2FProperties%2F1617540583" anchor-label="totalCapacityInKilowattHours" id="1018049596%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-total-capacity-in-kilowatt-hours"><span>total</span><wbr></wbr><span>Capacity</span><wbr></wbr><span>In</span><wbr></wbr><span>Kilowatt</span><wbr></wbr><span><span>Hours</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1018049596%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-total-capacity-in-kilowatt-hours">totalCapacityInKilowattHours</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. <strong>Note:</strong> For a user-planned <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.ChargingStop</a>, this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-82868220%2FFunctions%2F1617540583" anchor-label="equals" id="-82868220%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-equals"><span><span>equals</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-82868220%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">operator override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-equals"><span class="token function">equals</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">other<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="958319714%2FFunctions%2F1617540583" anchor-label="hashCode" id="958319714%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-hash-code"><span>hash</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="958319714%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-hash-code"><span class="token function">hashCode</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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
`}</HTMLBlock>
