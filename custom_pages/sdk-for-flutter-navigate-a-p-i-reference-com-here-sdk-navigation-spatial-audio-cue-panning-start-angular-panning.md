---
title: "startAngularPanning"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-navigation-spatial-audio-cue-panning-start-angular-panning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- start-angular-panning.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>startAngularPanning</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.navigation/SpatialAudioCuePanning/startAngularPanning/#com.here.sdk.navigation.CustomPanningData?#com.here.sdk.navigation.SpatialAudioCuePanning.SpatialAzimuthCallback/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.navigation</a><span class="delimiter">/</span><a href="index.html">SpatialAudioCuePanning</a><span class="delimiter">/</span><span class="current">startAngularPanning</span></div>
  <div class="cover ">
    <h1 class="cover"><span>start</span><wbr></wbr><span>Angular</span><wbr></wbr><span><span>Panning</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="start-angular-panning.html"><span class="token function">startAngularPanning</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">nextCustomPanningData<span class="token operator">: </span><a href="../-custom-panning-data/index.html">CustomPanningData</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">azimuthCallback<span class="token operator">: </span><a href="-spatial-azimuth-callback/index.html">SpatialAudioCuePanning.SpatialAzimuthCallback</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">This method will retrieve a stream of azimuth values to be passed onto the spatial audio renderer. An optional custom value for <a href="../-custom-panning-data/estimated-audio-cue-duration.html">com.here.sdk.navigation.CustomPanningData.estimatedAudioCueDuration</a>, <a href="../-custom-panning-data/initial-azimuth-in-degrees.html">com.here.sdk.navigation.CustomPanningData.initialAzimuthInDegrees</a>,  or its <a href="../-custom-panning-data/sweep-azimuth-in-degrees.html">com.here.sdk.navigation.CustomPanningData.sweepAzimuthInDegrees</a> can be here defined if the default data does not fully match the utilized Language or TTS engine or angle expectations. If startAngularPanning is called to spatialize the audio cue of a new maneuver before the full completion of a previous spatial audio trajectory, then <a href="../-event-text-listener/index.html">com.here.sdk.navigation.EventTextListener</a> will retrieve the azimuth values of the new maneuver.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>next</span><wbr></wbr><span>Custom</span><wbr></wbr><span>Panning</span><wbr></wbr><span><span>Data</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Defines a new set of values related to spatial audio panning.     When <a href="../-custom-panning-data/index.html">com.here.sdk.navigation.CustomPanningData</a> is initialized as <code class="lang-kotlin">null</code>, the default set of values provided by HERE SDK     will be used instead.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>azimuth</span><wbr></wbr><span><span>Callback</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Callback that will signal the next azimuth required to complete a spatial audio trajectory     once the angular panning has started.     Azimuth angular values are retrieved individually until the full duration of the audio trajectory     has been reached,     or a new text message has started its angular panning.</p></div></div></div></div></div></div></div>
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
