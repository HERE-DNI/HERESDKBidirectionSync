---
title: "MapDownloader"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-maploader-map-downloader"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapDownloader</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.maploader/MapDownloader///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.maploader</a><span class="delimiter">/</span><span class="current">MapDownloader</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span><span>Downloader</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">MapDownloader</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">A class for downloading and managing map data for various regions worldwide. Downloaded map data is permanently stored on disk, enabling maps at all zoom levels, search, routing, and other features without an active data connection. Users can query available regions, download them to disk, or delete them. An instance of this class can be created using <a href="-companion/from-engine-async.html">com.here.sdk.maploader.MapDownloader.fromEngineAsync</a>.</p><p class="paragraph">The storage path for downloaded maps can be specified via <a href="../../com.here.sdk.core.engine/-s-d-k-options/persistent-map-storage-path.html">com.here.sdk.core.engine.SDKOptions.persistentMapStoragePath</a>.</p><p class="paragraph">To control the type of content included in a map download, use <code class="lang-kotlin">LayerConfiguration</code>. Once applied, it affects both the map cache and offline maps. Satellite-based map schemes are not included in the downloaded region data.</p><p class="paragraph"><strong>Note:</strong> During turn-by-turn navigation, while a map download or update is in progress, navigation may not function as expected, and the app may be blocked until the operation is completed. Ensure that all pending map operations are finished before starting navigation. This applies only to <code class="lang-kotlin">MapDownloader</code> and <code class="lang-kotlin">MapUpdater</code>. <code class="lang-kotlin">RoutePrefetcher</code> operations are not affected.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-724998681%2FClasslikes%2F1617540583" anchor-label="Companion" id="-724998681%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-724998681%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="907300182%2FProperties%2F1617540583" anchor-label="taskCount" id="907300182%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="task-count.html"><span>task</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="907300182%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="task-count.html">taskCount</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a></div><div class="brief "><p class="paragraph">The number of concurrent tasks for downloading a map. A valid task count is between 1 to 64. When the value set is outside the valid range, then it is clamped to a valid range:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1732218028%2FFunctions%2F1617540583" anchor-label="clearPersistentMapStorage" id="-1732218028%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="clear-persistent-map-storage.html"><span>clear</span><wbr></wbr><span>Persistent</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Storage</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1732218028%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="clear-persistent-map-storage.html"><span class="token function">clearPersistentMapStorage</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">callback<span class="token operator">: </span><a href="../-s-d-k-cache-callback/index.html">SDKCacheCallback</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Performs an asynchronous operation to clear the persistent map storage from all data. All downloaded regions will be removed. Note: Must be called only when no other region operation is ongoing. Returns an error if there is any active operation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-697877185%2FFunctions%2F1617540583" anchor-label="deleteRegions" id="-697877185%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="delete-regions.html"><span>delete</span><wbr></wbr><span><span>Regions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-697877185%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="delete-regions.html"><span class="token function">deleteRegions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">regions<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-region-id/index.html">RegionId</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-deleted-regions-callback/index.html">DeletedRegionsCallback</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Performs an asynchronous operation to delete map data for regions specified by a list of <a href="../-region-id/index.html">com.here.sdk.maploader.RegionId</a>. Note: Deleting a region when there is a pending download returns error <a href="../-map-loader-error/-i-n-t-e-r-n-a-l_-e-r-r-o-r/index.html">com.here.sdk.maploader.MapLoaderError.INTERNAL_ERROR</a>. Also, deleting a region when there is an ongoing download returns error <a href="../-map-loader-error/-p-a-r-a-l-l-e-l_-r-e-q-u-e-s-t/index.html">com.here.sdk.maploader.MapLoaderError.PARALLEL_REQUEST</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1590913676%2FFunctions%2F1617540583" anchor-label="downloadArea" id="-1590913676%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="download-area.html"><span>download</span><wbr></wbr><span><span>Area</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1590913676%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="download-area.html"><span class="token function">downloadArea</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">area<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-polygon/index.html">GeoPolygon</a><span class="token punctuation">, </span></span><span class="parameter ">statusListener<span class="token operator">: </span><a href="../-download-regions-status-listener/index.html">DownloadRegionsStatusListener</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-map-downloader-task/index.html">MapDownloaderTask</a></div><div class="brief "><p class="paragraph">Performs an asynchronous request to download map data for area specified by a GeoPolygon. com.here.sdk.maploader.MapDownloader.downloadArea.statusListener is receiving notifications until <a href="../-download-regions-status-listener/on-download-regions-complete.html">com.here.sdk.maploader.DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called. Returned <a href="../-map-downloader-task/index.html">com.here.sdk.maploader.MapDownloaderTask</a> should be used to pause or resume started download, by invoking <a href="../-map-downloader-task/pause.html">com.here.sdk.maploader.MapDownloaderTask.pause</a> or <a href="../-map-downloader-task/resume.html">com.here.sdk.maploader.MapDownloaderTask.resume</a>. Request can be cancelled by calling <a href="../-map-downloader-task/cancel.html">com.here.sdk.maploader.MapDownloaderTask.cancel</a> on returned <a href="../-map-downloader-task/index.html">com.here.sdk.maploader.MapDownloaderTask</a> object, afterwards <a href="../-download-regions-status-listener/on-download-regions-complete.html">com.here.sdk.maploader.DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called with error <a href="../-map-loader-error/-o-p-e-r-a-t-i-o-n_-c-a-n-c-e-l-l-e-d/index.html">com.here.sdk.maploader.MapLoaderError.OPERATION_CANCELLED</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1794048066%2FFunctions%2F1617540583" anchor-label="downloadRegions" id="-1794048066%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="download-regions.html"><span>download</span><wbr></wbr><span><span>Regions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1794048066%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="download-regions.html"><span class="token function">downloadRegions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">regions<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-region-id/index.html">RegionId</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">statusListener<span class="token operator">: </span><a href="../-download-regions-status-listener/index.html">DownloadRegionsStatusListener</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-map-downloader-task/index.html">MapDownloaderTask</a></div><div class="brief "><p class="paragraph">Performs an asynchronous request to download map data for regions specified by a list of <a href="../-region-id/index.html">com.here.sdk.maploader.RegionId</a> instances. com.here.sdk.maploader.MapDownloader.downloadRegions.statusListener receives notifications until <a href="../-download-regions-status-listener/on-download-regions-complete.html">com.here.sdk.maploader.DownloadRegionsStatusListener.onDownloadRegionsComplete</a> is called. The returned <a href="../-map-downloader-task/index.html">com.here.sdk.maploader.MapDownloaderTask</a> can be used to pause or resume the download using <a href="../-map-downloader-task/pause.html">com.here.sdk.maploader.MapDownloaderTask.pause</a> or <a href="../-map-downloader-task/resume.html">com.here.sdk.maploader.MapDownloaderTask.resume</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1609112474%2FFunctions%2F1617540583" anchor-label="getDownloadableRegions" id="-1609112474%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-downloadable-regions.html"><span>get</span><wbr></wbr><span>Downloadable</span><wbr></wbr><span><span>Regions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1609112474%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-downloadable-regions.html"><span class="token function">getDownloadableRegions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">callback<span class="token operator">: </span><a href="../-downloadable-regions-callback/index.html">DownloadableRegionsCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous request to fetch a list of <a href="../-region/index.html">com.here.sdk.maploader.Region</a> objects for downloading map data in a separate request.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-downloadable-regions.html"><span class="token function">getDownloadableRegions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">languageCode<span class="token operator">: </span><a href="../../com.here.sdk.core/-language-code/index.html">LanguageCode</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-downloadable-regions-callback/index.html">DownloadableRegionsCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous request to fetch a list of <a href="../-region/index.html">com.here.sdk.maploader.Region</a> objects with <a href="../-region/name.html">com.here.sdk.maploader.Region.name</a> in given com.here.sdk.maploader.MapDownloader.getDownloadableRegions.languageCode, that can be used to download the actual map data in a separate request.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1329873001%2FFunctions%2F1617540583" anchor-label="getInitialPersistentMapStatus" id="-1329873001%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-initial-persistent-map-status.html"><span>get</span><wbr></wbr><span>Initial</span><wbr></wbr><span>Persistent</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Status</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1329873001%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-initial-persistent-map-status.html"><span class="token function">getInitialPersistentMapStatus</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-persistent-map-status/index.html">PersistentMapStatus</a></div><div class="brief "><p class="paragraph">Gets the initial status of the already downloaded regions at start-up time of the app. It is not recommended to download or to upload map data while an app is running in background. However, it can happen, that an app gets shut down during an ongoing operation, for example, due to a crash. In such a case, some or all of the downloaded map data may be in a corrupted state. Refer to the <a href="../-persistent-map-status/index.html">com.here.sdk.maploader.PersistentMapStatus</a> for exact healing procedure for specific status. Note: This value will not change during the lifetime of an app.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2113971877%2FFunctions%2F1617540583" anchor-label="getInstalledRegions" id="2113971877%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-installed-regions.html"><span>get</span><wbr></wbr><span>Installed</span><wbr></wbr><span><span>Regions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2113971877%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-installed-regions.html"><span class="token function">getInstalledRegions</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-installed-region/index.html">InstalledRegion</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Method to get a list of map regions that are currently installed on the device. Throws if it's not possible to return list of installed regions. Returned list contains:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1970835436%2FFunctions%2F1617540583" anchor-label="getOfflineMapsStorageSizeInBytes" id="-1970835436%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-offline-maps-storage-size-in-bytes.html"><span>get</span><wbr></wbr><span>Offline</span><wbr></wbr><span>Maps</span><wbr></wbr><span>Storage</span><wbr></wbr><span>Size</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Bytes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1970835436%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-offline-maps-storage-size-in-bytes.html"><span class="token function">getOfflineMapsStorageSizeInBytes</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-offline-maps-storage-size-in-bytes.html"><span class="token function">getOfflineMapsStorageSizeInBytes</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">callback<span class="token operator">: </span><a href="../-offline-storage-size-callback/index.html">OfflineStorageSizeCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Get the total size of all downloaded regions currently persisted on disk at the location that is specified via <a href="../../com.here.sdk.core.engine/-s-d-k-options/persistent-map-storage-path.html">com.here.sdk.core.engine.SDKOptions.persistentMapStoragePath</a>. This includes also data that is currently being downloaded.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1046433084%2FFunctions%2F1617540583" anchor-label="onEnterForeground" id="-1046433084%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-enter-foreground.html"><span>on</span><wbr></wbr><span>Enter</span><wbr></wbr><span><span>Foreground</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1046433084%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="on-enter-foreground.html"><span class="token function"><strike>onEnterForeground</strike></span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">To enable background map downloads for iOS, this method must be invoked when the application moves from the foreground to the background, usually triggered when the user switches to another application or when the device's screen is turned off. Please note that this method is only relevant to the iOS platform. Robust handling of online requests finished while in the background depends on the integration with AppDelegate. How to integrate it see <code class="lang-kotlin">sdk.maploader.BackgroundMapOperationContext</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1783675503%2FFunctions%2F1617540583" anchor-label="repairPersistentMap" id="1783675503%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="repair-persistent-map.html"><span>repair</span><wbr></wbr><span>Persistent</span><wbr></wbr><span><span>Map</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1783675503%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="repair-persistent-map.html"><span class="token function">repairPersistentMap</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">callback<span class="token operator">: </span><a href="../-repair-persistent-map-callback/index.html">RepairPersistentMapCallback</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Tries to repair already downloaded regions that are in a corrupted state (see <a href="get-initial-persistent-map-status.html">com.here.sdk.maploader.MapDownloader.getInitialPersistentMapStatus</a>).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
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
