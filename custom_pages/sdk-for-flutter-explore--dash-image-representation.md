---
title: "DashImageRepresentation"
slug: "sdk-for-flutter-explore--dash-image-representation"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- -dash-image-representation.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>DashImageRepresentation</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.mapview/MapPolyline.DashImageRepresentation/DashImageRepresentation/#com.here.sdk.mapview.MapMeasureDependentRenderSize#com.here.sdk.mapview.MapMeasureDependentRenderSize#com.here.sdk.mapview.MapImage/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapPolyline</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">DashImageRepresentation</a><span class="delimiter">/</span><span class="current">DashImageRepresentation</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Dash</span><wbr></wbr><span>Image</span><wbr></wbr><span><span>Representation</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">dashLength<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">dashWidth<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">image<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapImage</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a uniform dash pattern in which the length of a gap is the same as the length of a dash. Dashes are rendered as image.</p><p class="paragraph">This allows for patterns like <code class="lang-kotlin">' — — — —'</code> or <code class="lang-kotlin">'  ——  ——  ——'</code>.</p><p class="paragraph">For <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasureDependentRenderSize</a> supplied for <code class="lang-kotlin">dashLength</code> and <code class="lang-kotlin">dashWidth</code>, only <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL</a> is supported for <a href="sdk-for-flutter-explore-measure-kind">com.here.sdk.mapview.MapMeasureDependentRenderSize.measureKind</a> and only <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit.METERS</a> is supported for <a href="sdk-for-flutter-explore-size-unit">com.here.sdk.mapview.MapMeasureDependentRenderSize.sizeUnit</a>.</p><p class="paragraph">Only map measure values in range \[3-19\] are supported.</p><p class="paragraph">The value of the keys in <a href="sdk-for-flutter-explore-sizes">com.here.sdk.mapview.MapMeasureDependentRenderSize.sizes</a> is truncated to integer values, hence only a single value can be provided per zoom level.</p><p class="paragraph">The values are interpolated linearly between zoom levels.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>dash</span><wbr></wbr><span><span>Length</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The map measure dependent length of a dash, to which image width is stretched.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>dash</span><wbr></wbr><span><span>Width</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The map measure dependent width of a dash, to which image height is stretched.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>image</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Image to be rendered in place of dash space. It is stretched to match <code class="lang-kotlin">dashWidth</code> and <code class="lang-kotlin">dashLength</code>.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="sdk-for-flutter-explore-index"><span>Map</span><wbr></wbr><span>Polyline.</span><wbr></wbr><span>Representation.</span><wbr></wbr><span>Instantiation</span><wbr></wbr><span><span>Exception</span></span></a></div></span></div><div><div class="title"><p class="paragraph">In case of invalid input parameters.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">dashLength<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">gapLength<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">dashWidth<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">image<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapImage</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a simple dash pattern in which the lengths of a dash and gap can be different. Dashes are rendered as image.</p><p class="paragraph">This allows for patterns like <code class="lang-kotlin">'  —  —  —  —'</code> or <code class="lang-kotlin">' ——— ——— ———'</code>.</p><p class="paragraph">For <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasureDependentRenderSize</a> supplied for <code class="lang-kotlin">dashLength</code>, <code class="lang-kotlin">gapLength</code> and <code class="lang-kotlin">dashWidth</code>, only <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL</a> is supported for <a href="sdk-for-flutter-explore-measure-kind">com.here.sdk.mapview.MapMeasureDependentRenderSize.measureKind</a> and only <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit.METERS</a> is supported for <a href="sdk-for-flutter-explore-size-unit">com.here.sdk.mapview.MapMeasureDependentRenderSize.sizeUnit</a>.</p><p class="paragraph">Only map measure values in range \[3-19\] are supported.</p><p class="paragraph">The value of the keys in <a href="sdk-for-flutter-explore-sizes">com.here.sdk.mapview.MapMeasureDependentRenderSize.sizes</a> is truncated to integer values, hence only a single value can be provided per zoom level.</p><p class="paragraph">The values are interpolated linearly between zoom levels.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>dash</span><wbr></wbr><span><span>Length</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The map measure dependent length of a dash, to which image width is stretched.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>gap</span><wbr></wbr><span><span>Length</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The map measure dependent length of a gap between dash images.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>dash</span><wbr></wbr><span><span>Width</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The map measure dependent width of a dash, to which image height is stretched.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>image</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Image to be rendered in place of dash space. It is stretched to match <code class="lang-kotlin">dashWidth</code> and <code class="lang-kotlin">dashLength</code>.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="sdk-for-flutter-explore-index"><span>Map</span><wbr></wbr><span>Polyline.</span><wbr></wbr><span>Representation.</span><wbr></wbr><span>Instantiation</span><wbr></wbr><span><span>Exception</span></span></a></div></span></div><div><div class="title"><p class="paragraph">In case of invalid input parameters.</p></div></div></div></div></div></div></div>
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
