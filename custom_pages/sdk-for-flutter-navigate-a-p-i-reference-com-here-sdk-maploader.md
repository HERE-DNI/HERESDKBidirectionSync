---
title: "com.here.sdk.maploader"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-maploader"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>com.here.sdk.maploader</title>
    <link href="../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../";</script>
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
<script type="text/javascript" src="../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../styles/style.css" rel="Stylesheet">
<link href="../../styles/main.css" rel="Stylesheet">
<link href="../../styles/prism.css" rel="Stylesheet">
<link href="../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
</head>
<body>
    <div class="root">
    <nav class="navigation theme-dark" id="navigation-wrapper">
            <a class="library-name--link" href="../../index.html">
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
<div class="main-content" data-page-type="package" id="content" pageIds="API Reference::com.here.sdk.maploader////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../index.html">API Reference</a><span class="delimiter">/</span><span class="current">com.here.sdk.maploader</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Package-level</span></span> <span><span>declarations</span></span></h1>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="TYPE">Types</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-1774932618%2FClasslikes%2F1617540583" anchor-label="CatalogsUpdateInfoCallback" id="-1774932618%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-catalogs-update-info-callback/index.html"><span>Catalogs</span><wbr></wbr><span>Update</span><wbr></wbr><span>Info</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1774932618%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-catalogs-update-info-callback/index.html">CatalogsUpdateInfoCallback</a></div><div class="brief "><p class="paragraph">This method will be called on the main thread when <a href="-map-updater/retrieve-catalogs-update-info.html">com.here.sdk.maploader.MapUpdater.retrieveCatalogsUpdateInfo</a> has been completed. The first parameter indicates an error in case of a failure. The second parameter contains the results. Both parameters cannot be <code class="lang-kotlin">null</code> at the same time - or not <code class="lang-kotlin">null</code> at the same time. An empty <code class="lang-kotlin">CatalogUpdateInfo</code> list  represent no map updates.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1496530342%2FClasslikes%2F1617540583" anchor-label="CatalogUpdateInfo" id="1496530342%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-catalog-update-info/index.html"><span>Catalog</span><wbr></wbr><span>Update</span><wbr></wbr><span><span>Info</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1496530342%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-catalog-update-info/index.html">CatalogUpdateInfo</a></div><div class="brief "><p class="paragraph">Holds information for the catalog update intent. Provides information regarding installed catalog and its latest available version.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1940993229%2FClasslikes%2F1617540583" anchor-label="CatalogUpdateProgressListener" id="-1940993229%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-catalog-update-progress-listener/index.html"><span>Catalog</span><wbr></wbr><span>Update</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1940993229%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-catalog-update-progress-listener/index.html">CatalogUpdateProgressListener</a></div><div class="brief "><p class="paragraph">Interface to get notified on status updates when updating catalog, previously downloaded by <a href="-map-downloader/index.html">com.here.sdk.maploader.MapDownloader</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="395994813%2FClasslikes%2F1617540583" anchor-label="CatalogUpdateState" id="395994813%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-catalog-update-state/index.html"><span>Catalog</span><wbr></wbr><span>Update</span><wbr></wbr><span><span>State</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="395994813%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-catalog-update-state/index.html">CatalogUpdateState</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-catalog-update-state/index.html">CatalogUpdateState</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Represents the state of catalog map updates.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-960676689%2FClasslikes%2F1617540583" anchor-label="CatalogUpdateTask" id="-960676689%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-catalog-update-task/index.html"><span>Catalog</span><wbr></wbr><span>Update</span><wbr></wbr><span><span>Task</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-960676689%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-catalog-update-task/index.html">CatalogUpdateTask</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">A class to control the catalog update process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-783341535%2FClasslikes%2F1617540583" anchor-label="DeletedRegionsCallback" id="-783341535%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-deleted-regions-callback/index.html"><span>Deleted</span><wbr></wbr><span>Regions</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-783341535%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-deleted-regions-callback/index.html">DeletedRegionsCallback</a></div><div class="brief "><p class="paragraph">A method which is called on the main thread when <a href="-map-downloader/delete-regions.html">com.here.sdk.maploader.MapDownloader.deleteRegions</a> has been completed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-311648620%2FClasslikes%2F1617540583" anchor-label="DownloadableRegionsCallback" id="-311648620%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-downloadable-regions-callback/index.html"><span>Downloadable</span><wbr></wbr><span>Regions</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-311648620%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-downloadable-regions-callback/index.html">DownloadableRegionsCallback</a></div><div class="brief "><p class="paragraph">A method which is called on the main thread when <a href="-map-downloader/get-downloadable-regions.html">com.here.sdk.maploader.MapDownloader.getDownloadableRegions</a> has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be <code class="lang-kotlin">null</code> at the same time - or not <code class="lang-kotlin">null</code> at the same time.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-718644263%2FClasslikes%2F1617540583" anchor-label="DownloadRegionsStatusListener" id="-718644263%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-download-regions-status-listener/index.html"><span>Download</span><wbr></wbr><span>Regions</span><wbr></wbr><span>Status</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-718644263%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-download-regions-status-listener/index.html">DownloadRegionsStatusListener</a></div><div class="brief "><p class="paragraph">Interface to get notified on status updates when downloading map regions.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1841280941%2FClasslikes%2F1617540583" anchor-label="InstalledCatalog" id="1841280941%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-installed-catalog/index.html"><span>Installed</span><wbr></wbr><span><span>Catalog</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1841280941%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-installed-catalog/index.html">InstalledCatalog</a></div><div class="brief "><p class="paragraph">Represents installed catalog.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1981824088%2FClasslikes%2F1617540583" anchor-label="InstalledRegion" id="-1981824088%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-installed-region/index.html"><span>Installed</span><wbr></wbr><span><span>Region</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1981824088%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-installed-region/index.html">InstalledRegion</a></div><div class="brief "><p class="paragraph">Represents a region, from persistent map storage.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2126523030%2FClasslikes%2F1617540583" anchor-label="InstalledRegionStatus" id="2126523030%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-installed-region-status/index.html"><span>Installed</span><wbr></wbr><span>Region</span><wbr></wbr><span><span>Status</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2126523030%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-installed-region-status/index.html">InstalledRegionStatus</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-installed-region-status/index.html">InstalledRegionStatus</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Represents download status of region in the persistent map storage.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1236577371%2FClasslikes%2F1617540583" anchor-label="MapDownloader" id="-1236577371%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-downloader/index.html"><span>Map</span><wbr></wbr><span><span>Downloader</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1236577371%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-map-downloader/index.html">MapDownloader</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">A class for downloading and managing map data for various regions worldwide. Downloaded map data is permanently stored on disk, enabling maps at all zoom levels, search, routing, and other features without an active data connection. Users can query available regions, download them to disk, or delete them. An instance of this class can be created using <a href="-map-downloader/-companion/from-engine-async.html">com.here.sdk.maploader.MapDownloader.fromEngineAsync</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1844537841%2FClasslikes%2F1617540583" anchor-label="MapDownloaderConstructionCallback" id="-1844537841%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-downloader-construction-callback/index.html"><span>Map</span><wbr></wbr><span>Downloader</span><wbr></wbr><span>Construction</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1844537841%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-map-downloader-construction-callback/index.html">MapDownloaderConstructionCallback</a></div><div class="brief "><p class="paragraph">A method which is called on the main thread when <a href="-map-downloader/-companion/from-engine-async.html">com.here.sdk.maploader.MapDownloader.fromEngineAsync</a> has been completed. The <code class="lang-kotlin">MapDownloader</code> instance is created on a background thread to not block the calling thread.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-862813280%2FClasslikes%2F1617540583" anchor-label="MapDownloaderTask" id="-862813280%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-downloader-task/index.html"><span>Map</span><wbr></wbr><span>Downloader</span><wbr></wbr><span><span>Task</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-862813280%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-map-downloader-task/index.html">MapDownloaderTask</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">A class to control map download process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-959439821%2FClasslikes%2F1617540583" anchor-label="MapLoaderError" id="-959439821%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-loader-error/index.html"><span>Map</span><wbr></wbr><span>Loader</span><wbr></wbr><span><span>Error</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-959439821%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-map-loader-error/index.html">MapLoaderError</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-map-loader-error/index.html">MapLoaderError</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies possible errors that may result from map downloading/prefetching.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-69577012%2FClasslikes%2F1617540583" anchor-label="MapLoaderException" id="-69577012%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-loader-exception/index.html"><span>Map</span><wbr></wbr><span>Loader</span><wbr></wbr><span><span>Exception</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-69577012%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-map-loader-exception/index.html">MapLoaderException</a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span class="token keyword">val </span>error<span class="token operator">: </span><a href="-map-loader-error/index.html">MapLoaderError</a></span></span><span class="token punctuation">)</span> : <a href="https://developer.android.com/reference/kotlin/java/lang/Exception.html">Exception</a></div><div class="brief "><p class="paragraph">Error occurred during map operation. <code class="lang-kotlin">sdk.maploader.MapLoaderError</code> represents possible errors.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1029639696%2FClasslikes%2F1617540583" anchor-label="MapUpdateProgressListener" id="1029639696%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-update-progress-listener/index.html"><span>Map</span><wbr></wbr><span>Update</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1029639696%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-map-update-progress-listener/index.html">MapUpdateProgressListener</a></div><div class="brief "><p class="paragraph">Interface to get notified on status updates when updating map data, previously downloaded by <a href="-map-downloader/index.html">com.here.sdk.maploader.MapDownloader</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1562672353%2FClasslikes%2F1617540583" anchor-label="MapUpdater" id="-1562672353%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-updater/index.html"><span>Map</span><wbr></wbr><span><span>Updater</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1562672353%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-map-updater/index.html">MapUpdater</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">A class for updating regions previously downloaded using the <a href="-map-downloader/index.html">com.here.sdk.maploader.MapDownloader</a>. First, updates for the regions are downloaded. Once the download is complete, the update process begins, installing the new content. It is recommended to regularly call <a href="-map-updater/retrieve-catalogs-update-info.html">com.here.sdk.maploader.MapUpdater.retrieveCatalogsUpdateInfo</a> to check for available updates for any downloaded regions.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1399438199%2FClasslikes%2F1617540583" anchor-label="MapUpdaterConstructionCallback" id="-1399438199%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-updater-construction-callback/index.html"><span>Map</span><wbr></wbr><span>Updater</span><wbr></wbr><span>Construction</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1399438199%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-map-updater-construction-callback/index.html">MapUpdaterConstructionCallback</a></div><div class="brief "><p class="paragraph">A method which is called on the main thread when <a href="-map-updater/-companion/from-engine-async.html">com.here.sdk.maploader.MapUpdater.fromEngineAsync</a> has been completed. Construction requires the online configuration to be fetched, which in case of sync API, would block the calling thread. When configuration is cached, it is enough to read it from the disk, this operation still takes relatively big time.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1356669708%2FClasslikes%2F1617540583" anchor-label="MapUpdateTask" id="1356669708%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-update-task/index.html"><span>Map</span><wbr></wbr><span>Update</span><wbr></wbr><span><span>Task</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1356669708%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-map-update-task/index.html">MapUpdateTask</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">A class to control the map update process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1363468648%2FClasslikes%2F1617540583" anchor-label="MapVersionHandle" id="1363468648%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-version-handle/index.html"><span>Map</span><wbr></wbr><span>Version</span><wbr></wbr><span><span>Handle</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1363468648%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-map-version-handle/index.html">MapVersionHandle</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Represents version of the map.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1640717321%2FClasslikes%2F1617540583" anchor-label="NavigabilityType" id="1640717321%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-navigability-type/index.html"><span>Navigability</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1640717321%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-navigability-type/index.html">NavigabilityType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-navigability-type/index.html">NavigabilityType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Represents the navigability level of a map region. This enum defines whether a region can be used for navigation purposes. It helps categorize regions based on their usability in routing and map operations.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1429953682%2FClasslikes%2F1617540583" anchor-label="OfflineStorageSizeCallback" id="-1429953682%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-offline-storage-size-callback/index.html"><span>Offline</span><wbr></wbr><span>Storage</span><wbr></wbr><span>Size</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1429953682%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-offline-storage-size-callback/index.html">OfflineStorageSizeCallback</a></div><div class="brief "><p class="paragraph">A method which is called on the main thread when <a href="-map-downloader/get-offline-maps-storage-size-in-bytes.html">com.here.sdk.maploader.MapDownloader.getOfflineMapsStorageSizeInBytes</a> has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be <code class="lang-kotlin">null</code> at the same time - or not <code class="lang-kotlin">null</code> at the same time.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1319579178%2FClasslikes%2F1617540583" anchor-label="PersistentMapRepairError" id="-1319579178%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-persistent-map-repair-error/index.html"><span>Persistent</span><wbr></wbr><span>Map</span><wbr></wbr><span>Repair</span><wbr></wbr><span><span>Error</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1319579178%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-persistent-map-repair-error/index.html">PersistentMapRepairError</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-persistent-map-repair-error/index.html">PersistentMapRepairError</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies possible errors that may result after a map repair operation has been completed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1198040255%2FClasslikes%2F1617540583" anchor-label="PersistentMapStatus" id="1198040255%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-persistent-map-status/index.html"><span>Persistent</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Status</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1198040255%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-persistent-map-status/index.html">PersistentMapStatus</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-persistent-map-status/index.html">PersistentMapStatus</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies possible statuses of the already downloaded map regions as a whole. Note: This can be valid only for a single region in case of a <a href="-persistent-map-status/-c-o-r-r-u-p-t-e-d/index.html">com.here.sdk.maploader.PersistentMapStatus.CORRUPTED</a> state.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="556990296%2FClasslikes%2F1617540583" anchor-label="Region" id="556990296%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-region/index.html"><span><span>Region</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="556990296%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-region/index.html">Region</a></div><div class="brief "><p class="paragraph">Defines an area, especially part of a country or the world that can be downloaded.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2102423363%2FClasslikes%2F1617540583" anchor-label="RegionId" id="-2102423363%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-region-id/index.html"><span>Region</span><wbr></wbr><span><span>Id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2102423363%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-region-id/index.html">RegionId</a></div><div class="brief "><p class="paragraph">Specify a unique identifier for Region.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1421976327%2FClasslikes%2F1617540583" anchor-label="RepairPersistentMapCallback" id="-1421976327%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-repair-persistent-map-callback/index.html"><span>Repair</span><wbr></wbr><span>Persistent</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1421976327%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-repair-persistent-map-callback/index.html">RepairPersistentMapCallback</a></div><div class="brief "><p class="paragraph">A method which is called on the main thread when <a href="-map-downloader/repair-persistent-map.html">com.here.sdk.maploader.MapDownloader.repairPersistentMap</a> has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be <code class="lang-kotlin">null</code> at the same time - or not <code class="lang-kotlin">null</code> at the same time.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1720203940%2FClasslikes%2F1617540583" anchor-label="SDKCache" id="1720203940%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-d-k-cache/index.html"><span><span>SDKCache</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1720203940%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-s-d-k-cache/index.html">SDKCache</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">A class to manage SDK Cache. Path for SDKCache is specified via <a href="../com.here.sdk.core.engine/-s-d-k-options/cache-path.html">com.here.sdk.core.engine.SDKOptions.cachePath</a>. SDKCache manages temporary downloaded map data during map interaction and follows LRU (least recently used) strategy to delete map data when cache size exceeds the specified <a href="../com.here.sdk.core.engine/-s-d-k-options/cache-size-in-bytes.html">com.here.sdk.core.engine.SDKOptions.cacheSizeInBytes</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1410998561%2FClasslikes%2F1617540583" anchor-label="SDKCacheCallback" id="-1410998561%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-d-k-cache-callback/index.html"><span>SDKCache</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1410998561%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-s-d-k-cache-callback/index.html">SDKCacheCallback</a></div><div class="brief "><p class="paragraph">A method which is called on the main thread when <a href="-s-d-k-cache/clear-cache.html">com.here.sdk.maploader.SDKCache.clearCache</a> has been completed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1743127744%2FClasslikes%2F1617540583" anchor-label="UpdateStatistics" id="1743127744%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-update-statistics/index.html"><span>Update</span><wbr></wbr><span><span>Statistics</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1743127744%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-update-statistics/index.html">UpdateStatistics</a></div><div class="brief "><p class="paragraph">Defines statistics related to the success or failure of patched bundles. It can be used to monitor and analyze the reliability of binary patch updates.</p></div></div></div>
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
