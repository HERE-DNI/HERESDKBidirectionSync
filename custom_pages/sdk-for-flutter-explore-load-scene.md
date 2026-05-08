---
title: "loadScene"
slug: "sdk-for-flutter-explore-load-scene"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- load-scene.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>loadScene</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.mapview/MapScene/loadScene/#com.here.sdk.mapview.MapScheme#com.here.sdk.mapview.MapScene.LoadSceneCallback?/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapScene</a><span class="delimiter">/</span><span class="current">loadScene</span></div>
  <div class="cover ">
    <h1 class="cover"><span>load</span><wbr></wbr><span><span>Scene</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-load-scene"><span class="token function">loadScene</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapScheme<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScheme</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScene.LoadSceneCallback</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><p class="paragraph">Asynchronously loads a map scene described by a specified map scheme. Any previous map scene config will be replaced. The loaded scene is cached and so any changes made to the scene files on disk might not get reflected on a successive call to this function. Instead the reloadScene API can handle such use-cases to force-update the scene.</p><p class="paragraph">Map features enabled or disabled using <a href="sdk-for-flutter-explore-enable-features">com.here.sdk.mapview.MapScene.enableFeatures</a> and <a href="sdk-for-flutter-explore-disable-features">com.here.sdk.mapview.MapScene.disableFeatures</a> will be reset to defaults for the new scene configuration.</p><p class="paragraph">The callback is called on the main thread. When recreating an activity following a device rotation, it is not necessary to call this method a second time. The map scheme that was loaded when the map view was initially created will continue to be used.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>map</span><wbr></wbr><span><span>Scheme</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Map scheme.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>callback</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Optional callback that will receive the result of this operation.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-load-scene"><span class="token function">loadScene</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">configurationFile<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScene.LoadSceneCallback</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><p class="paragraph">Asynchronously loads a map scene described by a specified file in one of the supported formats. Any previous map scene config will be replaced.</p><p class="paragraph">When loading the same file again, consider to call <code class="lang-kotlin">reloadScene()</code> instead.</p><p class="paragraph">Map features enabled or disabled using <a href="sdk-for-flutter-explore-enable-features">com.here.sdk.mapview.MapScene.enableFeatures</a> and <a href="sdk-for-flutter-explore-disable-features">com.here.sdk.mapview.MapScene.disableFeatures</a> will be reset to defaults for the new scene configuration.</p><p class="paragraph">The callback is called on the main thread. When recreating an activity following a device rotation, it is not necessary to call this method a second time. The map scheme that was loaded when the map view was initially created will continue to be used.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>configuration</span><wbr></wbr><span><span>File</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Map scheme configuration file. It must contain the whole scene configuration.     In case it contains references to other files, they have to be reachable under     the paths specified in the main configuration file.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>callback</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Optional callback that will receive the result of this operation.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-load-scene"><span class="token function">loadScene</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">configurationFile<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">watermarkStyle<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WatermarkStyle</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScene.LoadSceneCallback</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><p class="paragraph">Asynchronously loads a map scene described by a specified file in one of the supported formats. The style of the HERE watermark matching the map scheme is specified. Any previous map scene config will be replaced.</p><p class="paragraph">When loading the same file again, consider to call <code class="lang-kotlin">reloadScene()</code> instead.</p><p class="paragraph">Map features enabled or disabled using <a href="sdk-for-flutter-explore-enable-features">com.here.sdk.mapview.MapScene.enableFeatures</a> and <a href="sdk-for-flutter-explore-disable-features">com.here.sdk.mapview.MapScene.disableFeatures</a> will be reset to defaults for the new scene configuration.</p><p class="paragraph">The callback is called on the main thread. When recreating an activity following a device rotation, it is not necessary to call this method a second time. The map scheme that was loaded when the map view was initially created will continue to be used.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>configuration</span><wbr></wbr><span><span>File</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Map scheme configuration file. It must contain the whole scene configuration.     In case it contains references to other files, they have to be reachable under     the paths specified in the main configuration file.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>watermark</span><wbr></wbr><span><span>Style</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The style for the HERE watermark, see <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.WatermarkStyle</a>.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>callback</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Optional callback that will receive the result of this operation.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-load-scene"><span class="token function">loadScene</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">options<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapSceneLoadOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScene.LoadSceneCallback</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><p class="paragraph">Asynchronously loads a map scene using MapSceneLoadOptions.</p><p class="paragraph">This is an unified API that supports loading from either a map scheme or configuration file, with optional feature and watermark configuration. It's more efficient to load the scene with this function by specifying the list of enabled features and disabled features, compared to loading the scene first and enabling or disabling map features in the scene loading callback function.</p><p class="paragraph">Configuration defaults are used for features that are not part of the enabled features or disabled features parameters. When a feature is in both the enabled and disabled lists, the feature is considered as requested to be enabled. If the same feature is present multiple times in the enabled list with different modes, then the feature is considered as requested to be enabled, but with an unspecified mode (any of the many specified in the enabled list).</p><p class="paragraph">Any previous map scene config will be replaced. The callback is called on the main thread.</p><p class="paragraph">When recreating an activity following a device rotation, it is not necessary to call this method a second time. The map scheme that was loaded when the map view was initially created will continue to be used.</p><p class="paragraph">Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Scene configuration options created using MapSceneLoadOptionsBuilder.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>callback</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Optional callback that will receive the result of this operation.</p></div></div></div></div></div></div></div>
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
