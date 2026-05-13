---
title: "lookAtDistance"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-keyframe-track-companion-look-at-distance"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- look-at-distance.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>lookAtDistance</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.mapview/MapCameraKeyframeTrack.Companion/lookAtDistance/#com.here.sdk.mapview.MapMeasure.Kind#kotlin.collections.List[com.here.sdk.animation.ScalarKeyframe]#com.here.sdk.animation.Easing#com.here.sdk.animation.KeyframeInterpolationMode/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="../index.html">MapCameraKeyframeTrack</a><span class="delimiter">/</span><a href="index.html">Companion</a><span class="delimiter">/</span><span class="current">lookAtDistance</span></div>
  <div class="cover ">
    <h1 class="cover"><span>look</span><wbr></wbr><span>At</span><wbr></wbr><span><span>Distance</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="look-at-distance.html"><span class="token function">lookAtDistance</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">distanceKind<span class="token operator">: </span><a href="../../-map-measure/-kind/index.html">MapMeasure.Kind</a><span class="token punctuation">, </span></span><span class="parameter ">keyframes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../../../com.here.sdk.animation/-scalar-keyframe/index.html">ScalarKeyframe</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">easing<span class="token operator">: </span><a href="../../../com.here.sdk.animation/-easing/index.html">Easing</a><span class="token punctuation">, </span></span><span class="parameter ">interpolationMode<span class="token operator">: </span><a href="../../../com.here.sdk.animation/-keyframe-interpolation-mode/index.html">KeyframeInterpolationMode</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../index.html">MapCameraKeyframeTrack</a></div><p class="paragraph">Creates a map camera look-at distance keyframe track. It enables animations of the distance from the map camera to the target point that the camera looks at. The measure kind of that distance can be specified. The values will be clamped according to the minimum and maximum zoom levels set for the map camera.</p><span class="kdoc-tag"><h4 class="">Return</h4><p class="paragraph">A keyframe track over the distance from the map camera to its target.</p></span><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>distance</span><wbr></wbr><span><span>Kind</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The kind of measure of distance between camera and target point.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>keyframes</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The list of keyframes that specify how the camera property is changed.     Keyframe time offsets are considered to be relative to the previous keyframe     in the list or relative to the start of the animation if the current keyframe     is first in the list.     Time offset of the first keyframe in the list should be 0, otherwise an error occurs     and creation of the keyframe track will fail.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>easing</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The easing to apply during keyframe interpolation.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>interpolation</span><wbr></wbr><span><span>Mode</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The type of interpolation done between keyframe values.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="../-instantiation-exception/index.html"><span>Map</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Keyframe</span><wbr></wbr><span>Track.</span><wbr></wbr><span>Instantiation</span><wbr></wbr><span><span>Exception</span></span></a></div></span></div><div><div class="title"><p class="paragraph">Indicates an instantiation issue.</p></div></div></div></div></div><hr><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="look-at-distance.html"><span class="token function"><strike>lookAtDistance</strike></span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">keyframes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../../../com.here.sdk.animation/-scalar-keyframe/index.html">ScalarKeyframe</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">easing<span class="token operator">: </span><a href="../../../com.here.sdk.animation/-easing/index.html">Easing</a><span class="token punctuation">, </span></span><span class="parameter ">interpolationMode<span class="token operator">: </span><a href="../../../com.here.sdk.animation/-keyframe-interpolation-mode/index.html">KeyframeInterpolationMode</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../index.html">MapCameraKeyframeTrack</a></div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.27.0. Use [com.here.sdk.mapview.MapCameraKeyframeTrack.lookAtDistance] instead.</p></div><p class="paragraph">Creates a map camera look-at distance keyframe track. It enables animations of the distance from the map camera to the target point that the camera looks at in meters. The values will be clamped according to the minimum and maximum zoom levels set for the map camera.</p><span class="kdoc-tag"><h4 class="">Return</h4><p class="paragraph">A keyframe track over the distance from the map camera to its target.</p></span><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>keyframes</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The list of keyframes that specify how the camera property is changed.     Keyframe time offsets are considered to be relative to the previous keyframe     in the list or relative to the start of the animation if the current keyframe     is first in the list.     Time offset of the first keyframe in the list should be 0, otherwise an error occurs     and creation of the keyframe track will fail.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>easing</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The easing to apply during keyframe interpolation.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>interpolation</span><wbr></wbr><span><span>Mode</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The type of interpolation done between keyframe values.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="../-instantiation-exception/index.html"><span>Map</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Keyframe</span><wbr></wbr><span>Track.</span><wbr></wbr><span>Instantiation</span><wbr></wbr><span><span>Exception</span></span></a></div></span></div><div><div class="title"><p class="paragraph">Indicates an instantiation issue.</p></div></div></div></div></div></div></div>
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
