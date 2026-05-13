---
title: "SolidRepresentation"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-solid-representation-solid-representation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -solid-representation.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>SolidRepresentation</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.mapview/MapPolyline.SolidRepresentation/SolidRepresentation/#com.here.sdk.mapview.MapMeasureDependentRenderSize#com.here.sdk.core.Color#com.here.sdk.mapview.LineCap/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="../index.html">MapPolyline</a><span class="delimiter">/</span><a href="index.html">SolidRepresentation</a><span class="delimiter">/</span><span class="current">SolidRepresentation</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Solid</span><wbr></wbr><span><span>Representation</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">lineWidth<span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">color<span class="token operator">: </span><a href="../../../com.here.sdk.core/-color/index.html">Color</a><span class="token punctuation">, </span></span><span class="parameter ">capShape<span class="token operator">: </span><a href="../../-line-cap/index.html">LineCap</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a representation for a solid line without outline.</p><p class="paragraph">At map measures smaller than smallest map measure in the <code class="lang-kotlin">lineWidth</code> line width is constant and equal to the width given for the smallest map measure in the <code class="lang-kotlin">lineWidth</code>.</p><p class="paragraph">At map measures bigger than biggest map measure in the <code class="lang-kotlin">lineWidth</code> line width is constant and equal to the width given for the biggest map measure in the <code class="lang-kotlin">lineWidth</code>.</p><p class="paragraph">At map measures between two nearest given map measures line width is linearly interpolated between width values given for these map measures.</p><p class="paragraph">For <a href="../../-map-measure/-kind/index.html">com.here.sdk.mapview.MapMeasure.Kind</a> only <a href="../../-map-measure/-kind/-z-o-o-m_-l-e-v-e-l/index.html">com.here.sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL</a> is supported.</p><p class="paragraph">For <a href="../../-render-size/-unit/index.html">com.here.sdk.mapview.RenderSize.Unit</a> only <a href="../../-render-size/-unit/-p-i-x-e-l-s/index.html">com.here.sdk.mapview.RenderSize.Unit.PIXELS</a> is supported.</p><p class="paragraph"><code class="lang-kotlin">lineWidth</code> must not be 0 (<code class="lang-kotlin">lineWidth.sizes</code> with all values set to 0.0).</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>line</span><wbr></wbr><span><span>Width</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The width of the polyline depending on the map measure.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>color</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The color of the polyline.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>cap</span><wbr></wbr><span><span>Shape</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The cap shape applied to both ends of the polyline.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="../-representation/-instantiation-exception/index.html"><span>Map</span><wbr></wbr><span>Polyline.</span><wbr></wbr><span>Representation.</span><wbr></wbr><span>Instantiation</span><wbr></wbr><span><span>Exception</span></span></a></div></span></div><div><div class="title"><p class="paragraph">In case of invalid input parameters.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">lineWidth<span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">color<span class="token operator">: </span><a href="../../../com.here.sdk.core/-color/index.html">Color</a><span class="token punctuation">, </span></span><span class="parameter ">outlineWidth<span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">outlineColor<span class="token operator">: </span><a href="../../../com.here.sdk.core/-color/index.html">Color</a><span class="token punctuation">, </span></span><span class="parameter ">capShape<span class="token operator">: </span><a href="../../-line-cap/index.html">LineCap</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a representation for a solid line with outline.</p><p class="paragraph">The total width of the polyline is <code class="lang-kotlin">line width + 2 * outline width</code>.</p><p class="paragraph">At map measures smaller than smallest map measure in the <code class="lang-kotlin">lineWidth</code> and <code class="lang-kotlin">outlineWidth</code>, the value is constant and equal to the width given for the smallest map measure in the <code class="lang-kotlin">lineWidth</code> and <code class="lang-kotlin">outlineWidth</code>.</p><p class="paragraph">At map measures bigger than biggest map measure in the <code class="lang-kotlin">lineWidth</code> and <code class="lang-kotlin">outlineWidth</code>, the value is constant and equal to the width given for the biggest map measure in the <code class="lang-kotlin">lineWidth</code> and <code class="lang-kotlin">outlineWidth</code>.</p><p class="paragraph">At map measures between two nearest given map measure is linearly interpolated between width values given for these map measures.</p><p class="paragraph">For <a href="../../-map-measure/-kind/index.html">com.here.sdk.mapview.MapMeasure.Kind</a> only <a href="../../-map-measure/-kind/-z-o-o-m_-l-e-v-e-l/index.html">com.here.sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL</a> is supported.</p><p class="paragraph">For <a href="../../-render-size/-unit/index.html">com.here.sdk.mapview.RenderSize.Unit</a> only <a href="../../-render-size/-unit/-p-i-x-e-l-s/index.html">com.here.sdk.mapview.RenderSize.Unit.PIXELS</a> is supported.</p><p class="paragraph"><code class="lang-kotlin">lineWidth</code> must not be 0 (<code class="lang-kotlin">lineWidth.sizes</code> with all values set to 0.0).</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>line</span><wbr></wbr><span><span>Width</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The width of the polyline depending on the map measure.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>color</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The color of the polyline.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>outline</span><wbr></wbr><span><span>Width</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The width of the outline on one side of the polyline depending on     the map measure.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>outline</span><wbr></wbr><span><span>Color</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The outline color of the polyline.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>cap</span><wbr></wbr><span><span>Shape</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The cap shape applied to both ends of the polyline.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="../-representation/-instantiation-exception/index.html"><span>Map</span><wbr></wbr><span>Polyline.</span><wbr></wbr><span>Representation.</span><wbr></wbr><span>Instantiation</span><wbr></wbr><span><span>Exception</span></span></a></div></span></div><div><div class="title"><p class="paragraph">In case of invalid input parameters.</p></div></div></div></div></div></div></div>
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
