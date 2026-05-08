---
title: "MapMarker3D"
slug: "sdk-for-flutter-explore--map-marker3-d"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- -map-marker3-d.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapMarker3D</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.mapview/MapMarker3D/MapMarker3D/#com.here.sdk.core.GeoCoordinates#com.here.sdk.mapview.MapMarker3DModel/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapMarker3D</a><span class="delimiter">/</span><span class="current">MapMarker3D</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span><span>Marker3D</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">at<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">model<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMarker3DModel</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates an instance of a 3D marker.</p><p class="paragraph">The origin of the 3D model's local coordinate system is placed at the specified geographical coordinates.</p><p class="paragraph">Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>at</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The geographical coordinates where the 3D marker is placed corresponding to origin of the     3D model's local coordinate system.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>model</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The 3D model used to draw 3D marker.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">at<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">image<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapImage</a><span class="token punctuation">, </span></span><span class="parameter ">scale<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">unit<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RenderSize.Unit</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a flat marker from provided map image.</p><p class="paragraph">Such map marker is a flat 3D marker of rectangular shape textured with given image. Aspect ratio of the flat marker is determined by aspect ratio of the image.</p><p class="paragraph">Only bitmap images are supported, using a <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapImage</a> created from SVG data will result in distorted rendering of the flat marker.</p><p class="paragraph">Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.</p><p class="paragraph">Size of the rendered flat marker can be specified in either world or screen coordinate space.</p><p class="paragraph">For <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit.PIXELS</a>, the flat marker will cover com.here.sdk.mapview.MapMarker3D.MapMarker3D.scale * image's width pixels horizontally and com.here.sdk.mapview.MapMarker3D.MapMarker3D.scale * image's height pixels vertically. The size of the flat marker remains constant on the screen.</p><p class="paragraph">For <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS</a> the flat marker will cover com.here.sdk.mapview.MapMarker3D.MapMarker3D.scale * image's width density independent pixels horizontally and com.here.sdk.mapview.MapMarker3D.MapMarker3D.scale * image's height density independent pixels vertically. The size of the flat marker remains constant on the screen.</p><p class="paragraph">For <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit.METERS</a> the flat marker will cover com.here.sdk.mapview.MapMarker3D.MapMarker3D.scale * image's width meters horizontally and com.here.sdk.mapview.MapMarker3D.MapMarker3D.scale * image's height meters vertically. Unlike with pixels or density independent pixels the size of the flat marker will grow and shrink together with regular map content like streets or buildings.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>at</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The geographical coordinates where the flat marker is placed corresponding to center of the     provided map image.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>image</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The MapImage containing the texture data of the flat marker. SVG images are not supported.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>scale</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Scale factor applied to the dimensions of the image.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>unit</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Determines whether the size of the flat marker is represented in world or in screen space.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">at<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">model<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMarker3DModel</a><span class="token punctuation">, </span></span><span class="parameter ">scale<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates an instance of a 3D marker with scale factor.</p><p class="paragraph">One unit of the 3D marker model will cover com.here.sdk.mapview.MapMarker3D.MapMarker3D.scale pixels. The size of the 3D marker remains constant on the screen.</p><p class="paragraph">The origin of the 3D model's local coordinate system is placed at the specified geographical coordinates.</p><p class="paragraph">Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>at</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The geographical coordinates where the 3D marker is placed corresponding to origin of the     3D model's local coordinate system.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>model</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The 3D model used to render the 3D marker.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>scale</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Scale factor to apply to the 3D model.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">at<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">model<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMarker3DModel</a><span class="token punctuation">, </span></span><span class="parameter ">scale<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">unit<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RenderSize.Unit</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates a new 3D marker at given world coordinates, using the supplied 3D model.</p><p class="paragraph">The unit specifies how the 3D geometry of the model is interpreted (meters for world space, pixels or density independent pixels for screen space), while scale determines its relative size.</p><p class="paragraph">For <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit.PIXELS</a> one unit of the 3D marker model will cover com.here.sdk.mapview.MapMarker3D.MapMarker3D.scale pixels. The size of the 3D marker remains constant on the screen.</p><p class="paragraph">For <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS</a> one unit of the 3D marker model will cover com.here.sdk.mapview.MapMarker3D.MapMarker3D.scale density independent pixels. The size of the 3D marker remains constant on the screen.</p><p class="paragraph">For <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit.METERS</a> one unit of the 3D marker model will cover com.here.sdk.mapview.MapMarker3D.MapMarker3D.scale meters in the real world. Unlike with pixels or density-independent pixels the size of the 3D marker will grow and shrink together with regular map content like streets or buildings.</p><p class="paragraph">The origin of the 3D model's local coordinate system is placed at the specified geographical coordinates.</p><p class="paragraph">Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>at</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The geographical coordinates where the 3D marker is placed corresponding to origin of the     3D model's local coordinate system.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>model</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The 3D model used to render the 3D marker.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>scale</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Scale factor to apply to the 3D model.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>unit</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Determines the unit of the model vertices and whether the size of the 3D marker     is expressed in world or screen space.</p></div></div></div></div></div></div></div>
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
