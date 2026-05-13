---
title: "setMarker3dModel"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapview-location-indicator-set-marker3d-model"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- set-marker3d-model.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>setMarker3dModel</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.mapview/LocationIndicator/setMarker3dModel/#com.here.sdk.mapview.MapMarker3DModel#kotlin.Double#com.here.sdk.mapview.LocationIndicator.MarkerType#com.here.sdk.mapview.RenderSize.Unit/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="index.html">LocationIndicator</a><span class="delimiter">/</span><span class="current">setMarker3dModel</span></div>
  <div class="cover ">
    <h1 class="cover"><span>set</span><wbr></wbr><span>Marker3d</span><wbr></wbr><span><span>Model</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-marker3d-model.html"><span class="token function">setMarker3dModel</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">model<span class="token operator">: </span><a href="../-map-marker3-d-model/index.html">MapMarker3DModel</a><span class="token punctuation">, </span></span><span class="parameter ">scale<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">type<span class="token operator">: </span><a href="-marker-type/index.html">LocationIndicator.MarkerType</a><span class="token punctuation">, </span></span><span class="parameter ">renderSizeUnit<span class="token operator">: </span><a href="../-render-size/-unit/index.html">RenderSize.Unit</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Sets the <a href="../-map-marker3-d-model/index.html">com.here.sdk.mapview.MapMarker3DModel</a> asset to be displayed as location indicator for a specified type. The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only <a href="../-map-marker3-d-model/index.html">com.here.sdk.mapview.MapMarker3DModel</a> created from <code class="lang-kotlin">obj</code> files are supported. Models created from Mesh will be ignored.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>model</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The <a href="../-map-marker3-d-model/index.html">com.here.sdk.mapview.MapMarker3DModel</a> object to be displayed for the specified type. Only models     created from <code class="lang-kotlin">obj</code> files are supported. Those created from mesh will be ignored.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>scale</span></span></u></div></span></div><div><div class="title"><p class="paragraph">A scale factor applied to the marker model.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>type</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The type of location marker for which the marker 3d model should be replaced.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>render</span><wbr></wbr><span>Size</span><wbr></wbr><span><span>Unit</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The <a href="../-render-size/-unit/index.html">com.here.sdk.mapview.RenderSize.Unit</a> specifying how the vertex coordinates of the     3D model are being interpreted. It specifies whether the 3D model is placed in world or     screen coordinate space.</p><div class="sample-container"><pre><code class="block lang-kotlin" theme="idea">[com.here.sdk.mapview.RenderSize.Unit.METERS] will make the 3D model use world
coordinate space, meaning that it will change size together with the map
when it is zoomed in and out. A simple 10 by 10 by 10 (in model space) cube
will have a size of 10 by 10 by 10 meters in world space.

[com.here.sdk.mapview.RenderSize.Unit.PIXELS] makes the 3D model use screen coordinate space,
meaning that it will have constant size on the screen regardless
of how the map zoom changes. A simple 10 by 10 (in model space) rectangle
will have a size of 10 by 10 pixels on the screen.

[com.here.sdk.mapview.RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS] is similar to pixels,
but the resulting size will take into account the pixel density of the
display, meaning that physical size on the screen will be approximately
the same regardless of the size or resolution of the display.</code></pre><span class="top-right-position"><span class="copy-icon"></span><div class="copy-popup-wrapper popup-to-left"><span class="copy-popup-icon"></span><span>Content copied to clipboard</span></div></span></div></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-marker3d-model.html"><span class="token function"><strike>setMarker3dModel</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">model<span class="token operator">: </span><a href="../-map-marker3-d-model/index.html">MapMarker3DModel</a><span class="token punctuation">, </span></span><span class="parameter ">scale<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">type<span class="token operator">: </span><a href="-marker-type/index.html">LocationIndicator.MarkerType</a></span></span><span class="token punctuation">)</span></div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.27.0. Please use the overloaded method with [com.here.sdk.mapview.RenderSize.Unit] instead.</p></div><p class="paragraph">Sets the MapMarker3DModel asset to be displayed as location indicator for a specified type. The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only MapMarker3DModel created from *.obj files are supported. Models created from Mesh will be ignored.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>model</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The MapMarker3DModel object to be displayed for the specified type. Only models     created from obj files are supported. Those created from mesh will be ignored.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>scale</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The scaling which will be applied to the marker model. As the size of the     location marker should be aligned on devices with different resolutions the     scale factor is applied relative to the ppi value and thus differs from the     scale which is passed to <a href="../-map-marker3-d/index.html">com.here.sdk.mapview.MapMarker3D</a> objects.     Meter is used for the unit of the map marker 3d model coordinate system.     For historical reason, the scale factor is internally devided by 6.     To display a unit qube of 1x1x1 meter as is, please use a scale value of 6.0.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>type</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The type of location marker for which the marker 3d model should be replaced.</p></div></div></div></div></div></div></div>
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
