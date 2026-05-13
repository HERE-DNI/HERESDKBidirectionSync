---
title: "setIndexOptions"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-search-offline-search-engine-companion-set-index-options"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- set-index-options.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>setIndexOptions</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.search/OfflineSearchEngine.Companion/setIndexOptions/#com.here.sdk.core.engine.SDKNativeEngine#com.here.sdk.search.OfflineSearchIndex.Options#com.here.sdk.search.OfflineSearchIndexListener/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../../index.html">com.here.sdk.search</a><span class="delimiter">/</span><a href="../index.html">OfflineSearchEngine</a><span class="delimiter">/</span><a href="index.html">Companion</a><span class="delimiter">/</span><span class="current">setIndexOptions</span></div>
  <div class="cover ">
    <h1 class="cover"><span>set</span><wbr></wbr><span>Index</span><wbr></wbr><span><span>Options</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-index-options.html"><span class="token function">setIndexOptions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">sdkEngine<span class="token operator">: </span><a href="../../../com.here.sdk.core.engine/-s-d-k-native-engine/index.html">SDKNativeEngine</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../../-offline-search-index/-options/index.html">OfflineSearchIndex.Options</a><span class="token punctuation">, </span></span><span class="parameter ">listener<span class="token operator">: </span><a href="../../-offline-search-index-listener/index.html">OfflineSearchIndexListener</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../-offline-search-index/-error/index.html">OfflineSearchIndex.Error</a><span class="token operator">?</span></div><p class="paragraph">Enables or disables indexing. When indexing is enabled, HERE SDK will create a detailed index over persistent map data and update it as needed. A detailed index enables finding data faster and over entire persistent map. Creating an index takes time, but usually no more than a few seconds up to a couple of minutes, depending on persistent map size. As the feature is improved, the indexing time will improve. Also please note that this is a heavy processing task. The stored index increases the space taken by offline maps by around 2-5%. This may also improve in future versions.</p><p class="paragraph">Indexing is disabled by default. If you want it enabled, make sure to call setIndexOptions with <code class="lang-kotlin">OfflineSearchIndex.Options.enabled</code> as <code class="lang-kotlin">true</code> before any operations in <code class="lang-kotlin">MapDownloader</code> or <code class="lang-kotlin">MapUpdater</code> that modify the persistent map. Calling setIndexOptions may also create or remove map index to match the previously installed map regions. If the matching index for installed map regions is found, then indexing is skipped. While a new index is being created, <code class="lang-kotlin">OfflineSearchEngine</code> functionality can still be used. However, without a valid index in place yet, it operates as though indexing is disabled. If <code class="lang-kotlin">SDKNativeEngine</code> is disposed during indexing (for example, by closing the app), the indexing is cancelled. Recreating <code class="lang-kotlin">SDKNativeEngine</code> and enabling indexing will ensure that index is created.</p><p class="paragraph">Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p><span class="kdoc-tag"><h4 class="">Return</h4><p class="paragraph">An error in case there was one. It's <code class="lang-kotlin">null</code> if the indexing listener could be     configured successfully.</p></span><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>sdk</span><wbr></wbr><span><span>Engine</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Indexing is enabled and disabled per SDKNativeEngine instance.     The index is created inside the related <a href="../../../com.here.sdk.core.engine/-s-d-k-options/persistent-map-storage-path.html">com.here.sdk.core.engine.SDKOptions.persistentMapStoragePath</a>.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>options</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Sets indexing options.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>listener</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The listener that will receive updates about indexing process.     When <code class="lang-kotlin">OfflineSearchIndex.Options.enabled</code> is true, SDK would store listener and the listener will receive updates     about indexing progress every time it is performed.     When <code class="lang-kotlin">OfflineSearchIndex.Options.enabled</code> is false, SDK would report indexing removal progress to the listener     one last time and remove storage of listener.</p></div></div></div></div></div></div></div>
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
