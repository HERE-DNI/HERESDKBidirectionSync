---
title: "dataPath"
slug: "sdk-for-flutter-navigate-data-path"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- data-path.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>dataPath</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.core.engine/SDKOptions/dataPath/#/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">SDKOptions</a><span class="delimiter">/</span><span class="current">dataPath</span></div>
  <div class="cover ">
    <h1 class="cover"><span>data</span><wbr></wbr><span><span>Path</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-data-path">dataPath</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><p class="paragraph">Path used for storing application internal data, such as the offline search index and other essential data required for proper functionality.</p><p class="paragraph"><strong>Note:</strong> For common use cases, prefer <a href="sdk-for-flutter-explore-persistent-map-storage-path">com.here.sdk.core.engine.SDKOptions.persistentMapStoragePath</a>, or keep the default paths. Use <code class="lang-kotlin">dataPath</code> only as a fallback if <a href="sdk-for-flutter-explore-persistent-map-storage-path">com.here.sdk.core.engine.SDKOptions.persistentMapStoragePath</a> is not writable, for example, when you have an agreement with HERE to flash data at factory time.</p><p class="paragraph">By default, this returns an empty string. In this case, the same path as <a href="sdk-for-flutter-explore-persistent-map-storage-path">com.here.sdk.core.engine.SDKOptions.persistentMapStoragePath</a> will be used. If an absolute path is set, it will be used instead. If a relative path is set then directory <code class="lang-kotlin">Context.getFilesDir().getPath()</code> is used as parent path. Application must have read/write permissions to the given desired path. It is recommended that the application has exclusive access to this path. Avoid using shared or public directories such as <code class="lang-kotlin">Download</code> or <code class="lang-kotlin">Documents</code>. Using such directories may cause certain HERE SDK features to behave with limitations. For example, index creation for offline search may fail or not function as expected. It is recommended not to use the application cache paths like <code class="lang-kotlin">Context.getCacheDir().getPath()</code> , since operating system manages data in this location and data can be deleted if the device is low on storage space, which will result in application malfunction. The path can be on internal or external storage. The internal storage is recommended due to the file I/O speed. Note: If the <a href="sdk-for-flutter-explore-persistent-map-storage-path">com.here.sdk.core.engine.SDKOptions.persistentMapStoragePath</a> is writable, <code class="lang-kotlin">dataPath</code> can be left empty. If the <a href="sdk-for-flutter-explore-persistent-map-storage-path">com.here.sdk.core.engine.SDKOptions.persistentMapStoragePath</a> is not writable, <code class="lang-kotlin">dataPath</code> must be set and also be writable. Note that <code class="lang-kotlin">dataPath</code> is used to store essential HERE SDK data.</p><p class="paragraph"><strong>Important:</strong> There is no automatic migration of stored data between the <a href="sdk-for-flutter-explore-persistent-map-storage-path">com.here.sdk.core.engine.SDKOptions.persistentMapStoragePath</a> and the <code class="lang-kotlin">dataPath</code>. For ease of management, it's recommended to set the persistence path as writable and ignore <code class="lang-kotlin">dataPath</code>. If <code class="lang-kotlin">dataPath</code> is set differently from the <a href="sdk-for-flutter-explore-persistent-map-storage-path">com.here.sdk.core.engine.SDKOptions.persistentMapStoragePath</a>, some data that would typically be saved in the <a href="sdk-for-flutter-explore-persistent-map-storage-path">com.here.sdk.core.engine.SDKOptions.persistentMapStoragePath</a> will now be saved to <code class="lang-kotlin">dataPath</code>. If <code class="lang-kotlin">dataPath</code> is set and later unset, any data stored there will remain inaccessible and will not be migrated back.</p></div></div>
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
