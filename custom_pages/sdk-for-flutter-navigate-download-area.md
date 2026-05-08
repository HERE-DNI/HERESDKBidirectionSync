---
title: "downloadArea"
slug: "sdk-for-flutter-navigate-download-area"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- download-area.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>downloadArea</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.maploader/MapDownloader/downloadArea/#com.here.sdk.core.GeoPolygon#com.here.sdk.maploader.DownloadRegionsStatusListener/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.maploader</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapDownloader</a><span class="delimiter">/</span><span class="current">downloadArea</span></div>
  <div class="cover ">
    <h1 class="cover"><span>download</span><wbr></wbr><span><span>Area</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-download-area"><span class="token function">downloadArea</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">area<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoPolygon</a><span class="token punctuation">, </span></span><span class="parameter ">statusListener<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">DownloadRegionsStatusListener</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapDownloaderTask</a></div><p class="paragraph">Performs an asynchronous request to download map data for area specified by a GeoPolygon. com.here.sdk.maploader.MapDownloader.downloadArea.statusListener is receiving notifications until <a href="sdk-for-flutter-explore-on-download-regions-complete">com.here.sdk.maploader.DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called. Returned <a href="sdk-for-flutter-explore-index">com.here.sdk.maploader.MapDownloaderTask</a> should be used to pause or resume started download, by invoking <a href="sdk-for-flutter-explore-pause">com.here.sdk.maploader.MapDownloaderTask.pause</a> or <a href="sdk-for-flutter-explore-resume">com.here.sdk.maploader.MapDownloaderTask.resume</a>. Request can be cancelled by calling <a href="sdk-for-flutter-explore-cancel">com.here.sdk.maploader.MapDownloaderTask.cancel</a> on returned <a href="sdk-for-flutter-explore-index">com.here.sdk.maploader.MapDownloaderTask</a> object, afterwards <a href="sdk-for-flutter-explore-on-download-regions-complete">com.here.sdk.maploader.DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called with error <a href="sdk-for-flutter-explore-index">com.here.sdk.maploader.MapLoaderError.OPERATION_CANCELLED</a>.</p><p class="paragraph"><a href="sdk-for-flutter-explore-index">com.here.sdk.maploader.MapDownloaderTask</a> remains operational until <a href="sdk-for-flutter-explore-on-download-regions-complete">com.here.sdk.maploader.DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called.</p><p class="paragraph">Downloaded area will be associated to a unique id that will be reported via <a href="sdk-for-flutter-explore-index">com.here.sdk.maploader.DownloadRegionsStatusListener</a>.</p><p class="paragraph">Simultaneous download of the same region twice is not supported. When such condition occurs then <a href="sdk-for-flutter-explore-on-download-regions-complete">com.here.sdk.maploader.DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called with error <a href="sdk-for-flutter-explore-index">com.here.sdk.maploader.MapLoaderError.SERVICE_ACCESS_FAILED</a> for a new request, while previous one continues uninterrupted.</p><p class="paragraph">If indexing is enabled through <code class="lang-kotlin">OfflineSearchEngine.setIndexOptions</code>, then after the requested regions have been downloaded, the corresponding index will be created. The index is used by <code class="lang-kotlin">OfflineSearchEngine</code> to find better results. Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p><p class="paragraph">To control list of map content features for area download, use <a href="sdk-for-flutter-explore-enabled-features">com.here.sdk.core.engine.LayerConfiguration.enabledFeatures</a>.</p><br>
Note: If an application is forcefully closed or crashes during a map download operation, then this
method can be called again to resume the download. For example, if a download was interrupted at 60%,
then the next call to download the same region will load the remaining 40%.
<br>
Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected
region three times before giving up. A connection will be timed out after one minute.
<br>
Note: If user try to re-download same GeoPolygon the status will be reported as per the
state of previous download operation.
<span class="kdoc-tag"><h4 class="">Return</h4><p class="paragraph">Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p></span><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>area</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Area to download.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>status</span><wbr></wbr><span><span>Listener</span></span></u></div></span></div><div><div class="title"><p class="paragraph">Notifies on the download progress.</p></div></div></div></div></div></div></div>
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
