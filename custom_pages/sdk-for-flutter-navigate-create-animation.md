---
title: "createAnimation"
slug: "sdk-for-flutter-navigate-create-animation"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- create-animation.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>createAnimation</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.mapview/MapCameraAnimationFactory.Companion/createAnimation/#com.here.sdk.mapview.MapCameraUpdate#com.here.time.Duration#com.here.sdk.animation.Easing/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapCameraAnimationFactory</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">Companion</a><span class="delimiter">/</span><span class="current">createAnimation</span></div>
  <div class="cover ">
    <h1 class="cover"><span>create</span><wbr></wbr><span><span>Animation</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-create-animation"><span class="token function">createAnimation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">cameraUpdate<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">duration<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Duration</a><span class="token punctuation">, </span></span><span class="parameter ">easing<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Easing</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraAnimation</a></div><p class="paragraph">Creates a <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapCameraAnimation</a> to gradually update the camera properties within a specified duration from its current values to the ones defined in the com.here.sdk.mapview.MapCameraAnimationFactory.createAnimation.cameraUpdate. <code class="lang-kotlin">MapCameraAnimation</code> instances created from <a href="sdk-for-flutter-explore-composite-update">com.here.sdk.mapview.MapCameraUpdateFactory.compositeUpdate</a> instances are not supported. An <a href="sdk-for-flutter-explore-index">com.here.sdk.animation.AnimationListener</a> will receive an <a href="sdk-for-flutter-explore-index">com.here.sdk.animation.AnimationState.CANCELLED</a> signal when trying to apply such animations.</p><span class="kdoc-tag"><h4 class="">Return</h4><p class="paragraph">MapCameraAnimation instance</p></span><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>camera</span><wbr></wbr><span><span>Update</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Update which should be applied to the map camera.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>duration</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Duration of the animation. Negative duration results in no camera change when applied.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>easing</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Easing to apply.</p></div></div></div></div></div><hr><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-create-animation"><span class="token function">createAnimation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">track<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraKeyframeTrack</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraAnimation</a></div><p class="paragraph">Creates a MapCameraAnimation for a movement defined by the supplied com.here.sdk.mapview.MapCameraAnimationFactory.createAnimation.track.</p><span class="kdoc-tag"><h4 class="">Return</h4><p class="paragraph">MapCameraAnimation instance</p></span><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>track</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The track</p></div></div></div></div></div><hr><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-create-animation"><span class="token function">createAnimation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">tracks<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MapCameraKeyframeTrack</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraAnimation</a></div><p class="paragraph">Creates a MapCameraAnimation for a movement defined by the supplied list of com.here.sdk.mapview.MapCameraAnimationFactory.createAnimation.tracks. Keyframe tracks specify how the map camera properties change during the animation. For the animation to be possible, no two different tracks can affect the same map camera property. The input tracks are validated with that in mind.</p><p class="paragraph">However, the following cases can only be detected at the time when animation is started:</p><ul><li><p class="paragraph">Changing altitude of camera position also changes camera look-at distance and at high altitudes, also camera look-at orientation.</p></li><li><p class="paragraph">Changing tilt of camera orientation also changes camera look-at distance and camera look-at target.</p></li><li><p class="paragraph">Changing bearing of camera orientation also changes camera look-at target if current tilt is not 0.</p></li><li><p class="paragraph">Changing tilt or bearing of camera look-at orientation also changes camera position.</p></li><li><p class="paragraph">Changing camera look-at orientation also changes camera look-at distance if tilt is not 0.</p></li></ul><span class="kdoc-tag"><h4 class="">Return</h4><p class="paragraph">MapCameraAnimation instance</p></span><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>tracks</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The list of tracks</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="sdk-for-flutter-explore-index"><span>Map</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Animation.</span><wbr></wbr><span>Instantiation</span><wbr></wbr><span><span>Exception</span></span></a></div></span></div><div><div class="title"><p class="paragraph">Indicates an instantiation issue.</p></div></div></div></div></div></div></div>
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
