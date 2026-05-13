---
title: "IsolineOptions"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-isoline-options-isoline-options"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -isoline-options.html -->
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.routing/IsolineOptions/IsolineOptions/#com.here.sdk.routing.IsolineOptions.Calculation#com.here.sdk.routing.RoutingOptions/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.routing</a><span class="delimiter">/</span><a href="index.html">IsolineOptions</a><span class="delimiter">/</span><span class="current">IsolineOptions</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Isoline</span><wbr></wbr><span><span>Options</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">calculationOptions<span class="token operator">: </span><a href="-calculation/index.html">IsolineOptions.Calculation</a><span class="token punctuation">, </span></span><span class="parameter ">routingOptions<span class="token operator">: </span><a href="../-routing-options/index.html">RoutingOptions</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and routing options. <strong>Notes</strong></p><ul><li><p class="paragraph">By default all vehicle specifications from <a href="../-routing-options/transport-specification.html">com.here.sdk.routing.RoutingOptions.transportSpecification</a> are set to <code class="lang-kotlin">null</code> and the <a href="../../com.here.sdk.transport/-transport-specification/transport-mode.html">com.here.sdk.transport.TransportSpecification.transportMode</a> from <a href="../-routing-options/transport-specification.html">com.here.sdk.routing.RoutingOptions.transportSpecification</a> is set to <a href="../../com.here.sdk.transport/-transport-mode/-c-a-r/index.html">com.here.sdk.transport.TransportMode.CAR</a>.</p></li><li><p class="paragraph">A route can be calculated with only the <a href="../../com.here.sdk.transport/-transport-specification/transport-mode.html">com.here.sdk.transport.TransportSpecification.transportMode</a> from <a href="../-routing-options/transport-specification.html">com.here.sdk.routing.RoutingOptions.transportSpecification</a> set.</p></li></ul><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>calculation</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options to be used to calculate this isoline.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>routing</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options that should influence the possible routes within the isoline.     This determines also the transportation type.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">calculationOptions<span class="token operator">: </span><a href="-calculation/index.html">IsolineOptions.Calculation</a><span class="token punctuation">, </span></span><span class="parameter ">carOptions<span class="token operator">: </span><a href="../-car-options/index.html">CarOptions</a></span></span><span class="token punctuation">)</span></div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.</p></div><p class="paragraph">Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and car routing options.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>calculation</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options to be used to calculate this isoline.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>car</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options that should influence the possible routes within the isoline.     This determines also the transportation type.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">calculationOptions<span class="token operator">: </span><a href="-calculation/index.html">IsolineOptions.Calculation</a><span class="token punctuation">, </span></span><span class="parameter ">truckOptions<span class="token operator">: </span><a href="../-truck-options/index.html">TruckOptions</a></span></span><span class="token punctuation">)</span></div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.</p></div><p class="paragraph">Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and truck routing options.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>calculation</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options to be used to calculate this isoline.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>truck</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options that should influence the possible routes within the isoline.     This determines also the transportation type.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">calculationOptions<span class="token operator">: </span><a href="-calculation/index.html">IsolineOptions.Calculation</a><span class="token punctuation">, </span></span><span class="parameter ">evCarOptions<span class="token operator">: </span><a href="../-e-v-car-options/index.html">EVCarOptions</a></span></span><span class="token punctuation">)</span></div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.</p></div><p class="paragraph">Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and electric car routing options.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>calculation</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options to be used to calculate this isoline.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>ev</span><wbr></wbr><span>Car</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options that should influence the possible routes within the isoline.     This determines also the transportation type.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">calculationOptions<span class="token operator">: </span><a href="-calculation/index.html">IsolineOptions.Calculation</a><span class="token punctuation">, </span></span><span class="parameter ">evTruckOptions<span class="token operator">: </span><a href="../-e-v-truck-options/index.html">EVTruckOptions</a></span></span><span class="token punctuation">)</span></div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.</p></div><p class="paragraph">Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and electric truck routing options.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>calculation</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options to be used to calculate this isoline.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>ev</span><wbr></wbr><span>Truck</span><wbr></wbr><span><span>Options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The options that should influence the possible routes within the isoline.     This determines also the transportation type.</p></div></div></div></div></div></div></div>
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
