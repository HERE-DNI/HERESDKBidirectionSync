---
title: "updateCatalog"
slug: "sdk-for-flutter-navigate-update-catalog"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- update-catalog.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>updateCatalog</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.maploader/MapUpdater/updateCatalog/#com.here.sdk.maploader.CatalogUpdateInfo#com.here.sdk.maploader.CatalogUpdateProgressListener/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.maploader</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapUpdater</a><span class="delimiter">/</span><span class="current">updateCatalog</span></div>
  <div class="cover ">
    <h1 class="cover"><span>update</span><wbr></wbr><span><span>Catalog</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-update-catalog"><span class="token function">updateCatalog</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">catalogInfo<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">CatalogUpdateInfo</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">CatalogUpdateProgressListener</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">CatalogUpdateTask</a></div><p class="paragraph">Performs an asynchronous request for each catalog to update map data to the latest available version. This applies to all previously installed <a href="sdk-for-flutter-explore-index">com.here.sdk.maploader.Region</a> map data and any incomplete downloads in a pending state.</p><p class="paragraph">If no regions are downloaded, this method updates only the map version. The map cache and persisted regions are always bound to the same map version.</p><p class="paragraph">If no updates are available, <a href="sdk-for-flutter-explore-index">com.here.sdk.maploader.CatalogsUpdateInfoCallback</a> from <a href="sdk-for-flutter-explore-retrieve-catalogs-update-info">com.here.sdk.maploader.MapUpdater.retrieveCatalogsUpdateInfo</a> returns an empty list. In this case, <a href="sdk-for-flutter-explore-on-complete">com.here.sdk.maploader.MapUpdateProgressListener.onComplete</a> is called immediately.</p><p class="paragraph">To check for available updates, use <a href="sdk-for-flutter-explore-retrieve-catalogs-update-info">com.here.sdk.maploader.MapUpdater.retrieveCatalogsUpdateInfo</a> to retrieve catalogs with newer versions. Individual catalogs can then be updated using this method. Ensure that the device has enough free disk space to perform a catalog update. Information about the required disk space is available in <a href="sdk-for-flutter-explore-disk-size-in-bytes">com.here.sdk.maploader.CatalogUpdateInfo.diskSizeInBytes</a>.</p><p class="paragraph">If there is not enough space to perform the catalog update with the default <a href="sdk-for-flutter-explore-index">com.here.sdk.maploader.MapUpdater.MapUpdateVersionCommitPolicy.ON_COMPLETE</a>, try using <a href="sdk-for-flutter-explore-index">com.here.sdk.maploader.MapUpdater.MapUpdateVersionCommitPolicy.ON_FIRST_REGION</a>. This option requires less space but follows a different strategy for handling errors during the map update.</p><p class="paragraph">If indexing is enabled through <code class="lang-kotlin">OfflineSearchEngine.setIndexOptions</code>, the index is rebuilt after the map is updated. The index helps <code class="lang-kotlin">OfflineSearchEngine</code> provide better search results.</p><p class="paragraph">Note: Indexing is a beta feature and may have bugs or unexpected behavior.</p><span class="kdoc-tag"><h4 class="">Return</h4><p class="paragraph">A handle that will be used to manipulate the execution of the task, for example, to cancel an ongoing request.</p></span><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>catalog</span><wbr></wbr><span><span>Info</span></span></u></div></span></div><div><div class="title"><p class="paragraph">catalog to update. CatalogUpdateInfo should be get from <a href="sdk-for-flutter-explore-retrieve-catalogs-update-info">com.here.sdk.maploader.MapUpdater.retrieveCatalogsUpdateInfo</a></p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>callback</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Callback which receives the result on the main thread.</p></div></div></div></div></div></div></div>
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
