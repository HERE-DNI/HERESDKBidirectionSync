---
title: "ChargingStation"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-routing-charging-station-charging-station"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -charging-station.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>ChargingStation</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.routing/ChargingStation/ChargingStation/#kotlin.String?#kotlin.String?#com.here.sdk.routing.ChargingConnectorAttributes?/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.routing</a><span class="delimiter">/</span><a href="index.html">ChargingStation</a><span class="delimiter">/</span><span class="current">ChargingStation</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Charging</span><wbr></wbr><span><span>Station</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">id<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">connectorAttributes<span class="token operator">: </span><a href="../-charging-connector-attributes/index.html">ChargingConnectorAttributes</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a new instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>id</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>name</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Human readable name of this charging station. It can be null when there is no name associated with the station.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>connector</span><wbr></wbr><span><span>Attributes</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Details of the connector suggested to be used.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">id<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">connectorAttributes<span class="token operator">: </span><a href="../-charging-connector-attributes/index.html">ChargingConnectorAttributes</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">brand<span class="token operator">: </span><a href="../../com.here.sdk.core/-name-i-d/index.html">NameID</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">chargePointOperator<span class="token operator">: </span><a href="../../com.here.sdk.core/-name-i-d/index.html">NameID</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">matchingEMobilityServiceProviders<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../../com.here.sdk.core/-name-i-d/index.html">NameID</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a new instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>id</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>name</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Human readable name of this charging station. It can be null when there is no name associated with the station.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>connector</span><wbr></wbr><span><span>Attributes</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Details of the connector suggested to be used.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>brand</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Charging station brand. <a href="../../com.here.sdk.core/-name-i-d/name.html">com.here.sdk.core.NameID.name</a> reflect to charging station brand name. <a href="../../com.here.sdk.core/-name-i-d/id.html">com.here.sdk.core.NameID.id</a> reflect to charging station brand unique ID.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>charge</span><wbr></wbr><span>Point</span><wbr></wbr><span><span>Operator</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Charging station charge-point-operator. <a href="../../com.here.sdk.core/-name-i-d/name.html">com.here.sdk.core.NameID.name</a> reflect to charge-point-operator name. <a href="../../com.here.sdk.core/-name-i-d/id.html">com.here.sdk.core.NameID.id</a> reflect to charge-point-operator ID.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>matching</span><wbr></wbr><span>EMobility</span><wbr></wbr><span>Service</span><wbr></wbr><span><span>Providers</span></span></u></div></span></div><div><div class="title"><p class="paragraph">List of matched E-Mobility Service Providers. Populated only when <a href="../-electric-vehicle-options/ev-mobility-service-provider-preferences.html">com.here.sdk.routing.ElectricVehicleOptions.evMobilityServiceProviderPreferences</a> was set. This list reflects the subset of E-Mobility Service Providers supported by the charging station, from the list specified in the request parameter <a href="../-electric-vehicle-options/ev-mobility-service-provider-preferences.html">com.here.sdk.routing.ElectricVehicleOptions.evMobilityServiceProviderPreferences</a>. <a href="../../com.here.sdk.core/-name-i-d/name.html">com.here.sdk.core.NameID.name</a> in each list item reflect to E-Mobility Service Provider name. <a href="../../com.here.sdk.core/-name-i-d/id.html">com.here.sdk.core.NameID.id</a> in each list item reflect to E-Mobility Service Provider id.</p></div></div></div></div></div></div></div>
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
