---
title: "setWatermarkLocation"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapview-map-surface-set-watermark-location"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- set-watermark-location.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>setWatermarkLocation</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.mapview/MapSurface/setWatermarkLocation/#com.here.sdk.core.Anchor2D#com.here.sdk.core.Point2D/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="index.html">MapSurface</a><span class="delimiter">/</span><span class="current">setWatermarkLocation</span></div>
  <div class="cover ">
    <h1 class="cover"><span>set</span><wbr></wbr><span>Watermark</span><wbr></wbr><span><span>Location</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="set-watermark-location.html"><span class="token function">setWatermarkLocation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>anchor<span class="token operator">: </span><a href="../../com.here.sdk.core/-anchor2-d/index.html">Anchor2D</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>offset<span class="token operator">: </span><a href="../../com.here.sdk.core/-point2-d/index.html">Point2D</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Sets the position of the HERE logo watermark within the map view. By default, the watermark is aligned to the bottom-right corner of the view: Anchor2D(1.0, 1.0) and Point2D(-watermarkSize.width / 2, -watermarkSize.height / 2). It is recommended to change the default position only if necessary to avoid overlapping UI elements. The watermark should always be fully visible within the view. The anchor point on the watermark is its center (width/2, height/2), around which it will be placed in the map view. For map views smaller than 250 dip in both width and height, the watermark will not be shown.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>anchor</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Anchor point in normalized view coordinates [0, 1]. Map view's origin at (0, 0) indicates a top-left corner of the map view. Out of boundary anchor point values will be clamped to the [0, 1] range.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>offset</span></span></u></div></span></div><div><div class="title"><p class="paragraph">A horizontal and vertical offset (expressed in positive/negative pixel coordinates) that allows shifting the watermark from the anchor point position in one or the other direction. For the quadrant of values expressing visible part of the map view negative offset shifts the watermark to the direction of the origin, positive - away from it. For example, the offset of (-10, 5) will shift the watermark 10px to the left and 5px to the bottom. If specified offset will result in watermark being completely or partially out-of-view the offset will be adjusted internally so that watermark is fully visible. Offset is not being scaled when the map view size changes.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html"><span>Illegal</span><wbr></wbr><span>State</span><wbr></wbr><span><span>Exception</span></span></a></div></span></div><div><div class="title"><p class="paragraph">if MapSurface object is not valid.</p></div></div></div></div></div></div></div>
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
