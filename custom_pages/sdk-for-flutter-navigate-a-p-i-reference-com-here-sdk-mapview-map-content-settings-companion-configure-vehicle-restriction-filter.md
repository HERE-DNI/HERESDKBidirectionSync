---
title: "configureVehicleRestrictionFilter"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapview-map-content-settings-companion-configure-vehicle-restriction-filter"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- configure-vehicle-restriction-filter.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>configureVehicleRestrictionFilter</title>
    <link href="../../../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../../../";</script>
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
<script type="text/javascript" src="../../../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../../../styles/style.css" rel="Stylesheet">
<link href="../../../../styles/main.css" rel="Stylesheet">
<link href="../../../../styles/prism.css" rel="Stylesheet">
<link href="../../../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
</head>
<body>
    <div class="root">
    <nav class="navigation theme-dark" id="navigation-wrapper">
            <a class="library-name--link" href="../../../../index.html">
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.mapview/MapContentSettings.Companion/configureVehicleRestrictionFilter/#com.here.sdk.transport.TransportSpecification/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="../index.html">MapContentSettings</a><span class="delimiter">/</span><a href="index.html">Companion</a><span class="delimiter">/</span><span class="current">configureVehicleRestrictionFilter</span></div>
  <div class="cover ">
    <h1 class="cover"><span>configure</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span>Restriction</span><wbr></wbr><span><span>Filter</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="configure-vehicle-restriction-filter.html"><span class="token function">configureVehicleRestrictionFilter</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportSpecs<span class="token operator">: </span><a href="../../../com.here.sdk.transport/-transport-specification/index.html">TransportSpecification</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Configures a filter for <a href="../../-map-features/-companion/-v-e-h-i-c-l-e_-r-e-s-t-r-i-c-t-i-o-n-s.html">com.here.sdk.mapview.MapFeatures.VEHICLE_RESTRICTIONS</a> to show only the restrictions matching the transport specifications when the feature is enabled.</p><p class="paragraph">This method provides a unified way to configure vehicle restriction filters using a single <a href="../../../com.here.sdk.transport/-transport-specification/index.html">com.here.sdk.transport.TransportSpecification</a> parameter. This allows you to use the same transport configuration for both routing and map rendering, ensuring consistency between route calculation and the restrictions displayed on the map.</p><p class="paragraph">The method extracts the transport mode, vehicle specifications, hazardous materials, and tunnel category from the com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter.transportSpecs parameter and applies filtering according to the same rules described below.</p><h1 class="">Filtering rules for transport mode</h1><p class="paragraph">The transport mode is used to distinguish between truck and other transport modes. This distinction ensures consistency between the routing logic and the information displayed on the map. At present, this is primarily used to suppress the generic truck restriction icon for non-truck modes.</p><p class="paragraph">Currently, only vehicle-related restrictions are supported. For pedestrian, scooter, or taxi transport modes, the transport mode information is used, but no additional vehicle-specific restrictions are applied.</p><h1 class="">Filtering rules for vehicle specifications</h1><p class="paragraph">Only restrictions applicable to the vehicle specifications will be shown. The vehicle specifications include dimensions (height, width, length), weights (gross weight, weight per axle), and trailer count.</p><p class="paragraph">Examples:</p><ul><li><p class="paragraph">If the height in vehicle specifications is set to 200 cm, then height restrictions with a height greater than 200 cm will not be displayed.</p></li><li><p class="paragraph">If the trailer count in vehicle specifications is set to 2, then trailer restrictions for a count greater than 2 will not be displayed.</p></li></ul><h1 class="">Filtering rules for hazardous materials</h1><p class="paragraph">Only restrictions applicable to specified hazardous materials will be shown. Hazardous materials are specified within the <a href="../../../com.here.sdk.transport/-vehicle-specification/index.html">com.here.sdk.transport.VehicleSpecification</a> contained in the com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter.transportSpecs parameter.</p><p class="paragraph">If at least one hazardous material of any type is present in the list, all available tunnel category restrictions will be displayed. In order to filter-out non-applicable tunnel categories, a tunnel category that applies to the vehicle can be specified additionally.</p><p class="paragraph">Examples:</p><ul><li><p class="paragraph">If the hazardous materials list contains <a href="../../../com.here.sdk.transport/-hazardous-material/-p-o-i-s-o-n/index.html">com.here.sdk.transport.HazardousMaterial.POISON</a> and <a href="../../../com.here.sdk.transport/-hazardous-material/-g-a-s/index.html">com.here.sdk.transport.HazardousMaterial.GAS</a>, then only material restrictions for poison and gas will be displayed.</p></li><li><p class="paragraph">If the hazardous materials list is empty, then no material restrictions will be shown.</p></li><li><p class="paragraph">If the hazardous materials list is not supplied at all (is <code class="lang-kotlin">null</code>), then no material restrictions will be shown.</p></li><li><p class="paragraph">If the hazardous materials list contains at least one hazardous material of any type and tunnel category is <code class="lang-kotlin">null</code>, then only corresponding material restrictions will be displayed together with all available tunnel categories.</p></li></ul><h1 class="">Filtering rules for tunnel category</h1><p class="paragraph">Tunnel categories are labeled and rated based on the level of restriction they provide. The lowest level of restriction is <a href="../../../com.here.sdk.transport/-tunnel-category/-b/index.html">com.here.sdk.transport.TunnelCategory.B</a>, the highest and most restrictive one is <a href="../../../com.here.sdk.transport/-tunnel-category/-e/index.html">com.here.sdk.transport.TunnelCategory.E</a>.</p><p class="paragraph">The tunnel category is specified within the <a href="../../../com.here.sdk.transport/-vehicle-specification/index.html">com.here.sdk.transport.VehicleSpecification</a> contained in the com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter.transportSpecs parameter.</p><p class="paragraph">Specifying tunnel category means that:</p><ul><li><p class="paragraph">The vehicle carries goods which could cause only the additional dangerous effects described in specified tunnel category and other categories below it with lower level of restriction.</p></li><li><p class="paragraph">The vehicle does not carry goods that could cause the dangerous effects described in tunnel categories above with higher restriction levels than the one specified.</p></li></ul><p class="paragraph">Tunnel categories are closely related to hazardous materials.</p><p class="paragraph">Since the type of hazardous material alone does not define the exact level of danger, to ensure comprehensive coverage; the HERE SDK follows:</p><ul><li><p class="paragraph">If at least one hazardous material is specified but no tunnel category is provided, the SDK enables and displays <strong>all tunnel category restrictions</strong> to ensure that no relevant restrictions are omitted.</p></li><li><p class="paragraph">If both hazardous materials and a tunnel category are specified, the SDK <strong>strictly follows the given tunnel category parameter</strong> and displays only the applicable restrictions.</p></li></ul><p class="paragraph">Example: If tunnel category is set to <a href="../../../com.here.sdk.transport/-tunnel-category/-d/index.html">com.here.sdk.transport.TunnelCategory.D</a>, then restrictions for tunnel category <a href="../../../com.here.sdk.transport/-tunnel-category/-e/index.html">com.here.sdk.transport.TunnelCategory.E</a> and <a href="../../../com.here.sdk.transport/-tunnel-category/-d/index.html">com.here.sdk.transport.TunnelCategory.D</a> will be displayed, but not the categories <a href="../../../com.here.sdk.transport/-tunnel-category/-b/index.html">com.here.sdk.transport.TunnelCategory.B</a> and <a href="../../../com.here.sdk.transport/-tunnel-category/-c/index.html">com.here.sdk.transport.TunnelCategory.C</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>transport</span><wbr></wbr><span><span>Specs</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The transport specification containing the transport mode and vehicle specifications.     For vehicle modes (car, truck, bus), the <a href="../../../com.here.sdk.transport/-vehicle-specification/index.html">com.here.sdk.transport.VehicleSpecification</a> within     this parameter provides dimensions, weights, hazardous materials, and tunnel category     information used for filtering. The same <a href="../../../com.here.sdk.transport/-transport-specification/index.html">com.here.sdk.transport.TransportSpecification</a> object     can be used for both routing configuration and map rendering to ensure consistency.</p></div></div></div></div></div><hr><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="configure-vehicle-restriction-filter.html"><span class="token function"><strike>configureVehicleRestrictionFilter</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportMode<span class="token operator">: </span><a href="../../../com.here.sdk.transport/-transport-mode/index.html">TransportMode</a><span class="token punctuation">, </span></span><span class="parameter ">truckSpecifications<span class="token operator">: </span><a href="../../../com.here.sdk.transport/-truck-specifications/index.html">TruckSpecifications</a><span class="token punctuation">, </span></span><span class="parameter ">hazardousMaterials<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../../../com.here.sdk.transport/-hazardous-material/index.html">HazardousMaterial</a><span class="token operator">&gt;</span><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">tunnelCategory<span class="token operator">: </span><a href="../../../com.here.sdk.transport/-tunnel-category/index.html">TunnelCategory</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.28.0, use [com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter] instead.</p></div><p class="paragraph">Configure a filter for <a href="../../-map-features/-companion/-v-e-h-i-c-l-e_-r-e-s-t-r-i-c-t-i-o-n-s.html">com.here.sdk.mapview.MapFeatures.VEHICLE_RESTRICTIONS</a> to show only the restrictions matching the specified criteria when the feature is enabled.</p><h1 class="">Filtering rules for truck specifications</h1><p class="paragraph">Only restrictions applicable to the supplied truck specifications will be shown.</p><p class="paragraph">Examples:</p><ul><li><p class="paragraph">If the height in com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter.truckSpecifications is set to 200 cm, then height restrictions with a height greater than 200 cm will not be displayed.</p></li><li><p class="paragraph">If the trailer count in com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter.truckSpecifications is set to 2, then trailer restrictions for a count greater than 2 will not be displayed.</p></li></ul><h1 class="">Filtering rules for hazardous materials</h1><p class="paragraph">Only restrictions applicable to specified hazardous materials will be shown. If at least one hazardous material of any type is present in the list, all available tunnel category restrictions will be displayed. In order to filter-out non-applicable tunnel categories, a tunnel category, that applies to the vehicle, can be specified additionally.</p><p class="paragraph">Examples:</p><ul><li><p class="paragraph">If the com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials contains <a href="../../../com.here.sdk.transport/-hazardous-material/-p-o-i-s-o-n/index.html">com.here.sdk.transport.HazardousMaterial.POISON</a> and <a href="../../../com.here.sdk.transport/-hazardous-material/-g-a-s/index.html">com.here.sdk.transport.HazardousMaterial.GAS</a>, then only material restrictions for poison and gas will be displayed.</p></li><li><p class="paragraph">If the com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials list is empty, then no material restrictions will be shown.</p></li><li><p class="paragraph">If the com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials list is not supplied at all (is <code class="lang-kotlin">null</code>), then no material restrictions will be shown.</p></li><li><p class="paragraph">If the com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials contains at least one hazardous material of any type and com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory is <code class="lang-kotlin">null</code>, then only corresponding material restrictions will be displayed together with all available tunnel categories.</p></li></ul><h1 class="">Filtering rules for tunnel category</h1><p class="paragraph">Tunnel categories are labeled and rated based on the level of restriction they provide. The lowest level of restriction is <a href="../../../com.here.sdk.transport/-tunnel-category/-b/index.html">com.here.sdk.transport.TunnelCategory.B</a>, the highest and most restrictive one is <a href="../../../com.here.sdk.transport/-tunnel-category/-e/index.html">com.here.sdk.transport.TunnelCategory.E</a>.</p><p class="paragraph">Specifying tunnel category means that:</p><ul><li><p class="paragraph">The truck carries goods which could cause only the additional dangerous effects described in specified tunnel category and other categories below it with lower level of restriction.</p></li><li><p class="paragraph">The truck does not carry goods that could cause the dangerous effects described in tunnel categories above with higher restriction levels than the one specified.</p></li></ul><p class="paragraph">Tunnel categories are closely related to hazardous materials.</p><p class="paragraph">Since the type of hazardous material alone does not define the exact level of danger, to ensure comprehensive coverage; the HERE SDK follows:</p><ul><li><p class="paragraph">If at least one hazardous material is specified but no com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory is provided, the SDK enables and displays <strong>all tunnel category restrictions</strong> to ensure that no relevant restrictions are omitted.</p></li><li><p class="paragraph">If both hazardous materials and a com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory are specified, the SDK <strong>strictly follows the given tunnel category parameter</strong> and displays only the applicable restrictions.</p></li></ul><p class="paragraph">Example: If com.here.sdk.mapview.MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory is set to <a href="../../../com.here.sdk.transport/-tunnel-category/-d/index.html">com.here.sdk.transport.TunnelCategory.D</a>, then restrictions for tunnel category <a href="../../../com.here.sdk.transport/-tunnel-category/-e/index.html">com.here.sdk.transport.TunnelCategory.E</a> and <a href="../../../com.here.sdk.transport/-tunnel-category/-d/index.html">com.here.sdk.transport.TunnelCategory.D</a> will be displayed, but not the categories <a href="../../../com.here.sdk.transport/-tunnel-category/-b/index.html">com.here.sdk.transport.TunnelCategory.B</a> and <a href="../../../com.here.sdk.transport/-tunnel-category/-c/index.html">com.here.sdk.transport.TunnelCategory.C</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>transport</span><wbr></wbr><span><span>Mode</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Specifies the current transport type. Currently, it's used to distinguish     between truck and other transport modes. This distinction ensures consistency     between the routing logic and the information displayed on the map.     At present, this is primarily used to suppress the generic truck restriction icon.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>truck</span><wbr></wbr><span><span>Specifications</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The size, weight, type and trailer count specifications to filter for, so that only     restrictions which are relevant for the given specifications are displayed.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>hazardous</span><wbr></wbr><span><span>Materials</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The hazardous materials to filter for, so that only applicable restrictions are     displayed. When the list is <code class="lang-kotlin">null</code> or empty, then no material restrictions     will be displayed.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>tunnel</span><wbr></wbr><span><span>Category</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The tunnel category to filter for, so that only applicable restrictions are     displayed. If <code class="lang-kotlin">null</code>, then no tunnel category restrictions will be     displayed.</p></div></div></div></div></div></div></div>
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
