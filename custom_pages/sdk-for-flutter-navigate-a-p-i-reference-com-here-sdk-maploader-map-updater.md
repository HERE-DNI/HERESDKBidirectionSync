---
title: "MapUpdater"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-maploader-map-updater"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapUpdater</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.maploader/MapUpdater///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.maploader</a><span class="delimiter">/</span><span class="current">MapUpdater</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span><span>Updater</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">MapUpdater</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">A class for updating regions previously downloaded using the <a href="../-map-downloader/index.html">com.here.sdk.maploader.MapDownloader</a>. First, updates for the regions are downloaded. Once the download is complete, the update process begins, installing the new content. It is recommended to regularly call <a href="retrieve-catalogs-update-info.html">com.here.sdk.maploader.MapUpdater.retrieveCatalogsUpdateInfo</a> to check for available updates for any downloaded regions.</p><p class="paragraph">If updates are available, regions can be updated asynchronously using <a href="update-catalog.html">com.here.sdk.maploader.MapUpdater.updateCatalog</a>. The <a href="../-map-update-progress-listener/index.html">com.here.sdk.maploader.MapUpdateProgressListener</a> provides update progress for each region.</p><p class="paragraph">Incremental map updates are supported, by default: Instead of downloading an entire region, only the parts that have changed will be installed. This results in a faster update process. MapUpdater also aligns previously downloaded content with <code class="lang-kotlin">LayerConfiguration</code> changes made via <code class="lang-kotlin">SDKOptions</code>.</p><p class="paragraph">Note that patching (also called &quot;incremental updates&quot;) is only supported for up to 8 versions. For example, if an update started with version x.y.0 then it will be supported till x.y.8 and stopped starting with x.y.9. Usually, OCM updates are released weekly. Incremental updates will stop after 2 months and a full update is performed instead.</p><p class="paragraph">In case of an error, the previous map data remains available for use. It is only replaced after new map data has been successfully downloaded. Regions that fail to update must be retried in a new call. Paused updates can be resumed later.</p><p class="paragraph">During the update process, <a href="index.html">com.here.sdk.maploader.MapUpdater</a> internally retries failed downloads until a timeout occurs. If this happens, it is reported via <a href="../-map-update-progress-listener/index.html">com.here.sdk.maploader.MapUpdateProgressListener</a>.</p><p class="paragraph">If the user cancels the update process during the update phase, it is ignored. The update phase begins after all content has been downloaded, then the HERE SDK installs and replaces the existing regions. Cancellation is only possible during the download phase, and a successful cancellation is indicated via <a href="../-map-update-progress-listener/on-complete.html">com.here.sdk.maploader.MapUpdateProgressListener.onComplete</a>.</p><p class="paragraph">Note that a <a href="../-map-loader-error/-n-o-t_-r-e-a-d-y/index.html">com.here.sdk.maploader.MapLoaderError.NOT_READY</a> occurs when the <a href="../-map-downloader/index.html">com.here.sdk.maploader.MapDownloader</a> is used in parallel. In general, background updates are not supported explicitly, as the OS can abort background processes. In addition, the OfflineSearchEngine and the OfflineRoutingEngine cannot be used while a map update is in progress and it will be indicated by a <a href="../-map-loader-error/index.html">com.here.sdk.maploader.MapLoaderError</a>.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1059587297%2FClasslikes%2F1617540583" anchor-label="Companion" id="1059587297%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1059587297%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1094084807%2FClasslikes%2F1617540583" anchor-label="MapUpdateVersionCommitPolicy" id="-1094084807%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-update-version-commit-policy/index.html"><span>Map</span><wbr></wbr><span>Update</span><wbr></wbr><span>Version</span><wbr></wbr><span>Commit</span><wbr></wbr><span><span>Policy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1094084807%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-map-update-version-commit-policy/index.html">MapUpdateVersionCommitPolicy</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-map-update-version-commit-policy/index.html">MapUpdater.MapUpdateVersionCommitPolicy</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Defines if installed regions and subregions are updated one-by-one or if all regions are updated only once the updates for all installed regions have been downloaded entirely. This influences the required size of the storage during an update. Regardless of the set policy, during an update, the previous region data is kept until the new region data is committed successfully to the persisted storage. This allows to revert to the previous version in case the update fails. With <a href="-map-update-version-commit-policy/-o-n_-c-o-m-p-l-e-t-e/index.html">com.here.sdk.maploader.MapUpdater.MapUpdateVersionCommitPolicy.ON_COMPLETE</a>, more data has to be kept until the update process finishes, while <a href="-map-update-version-commit-policy/-o-n_-f-i-r-s-t_-r-e-g-i-o-n/index.html">com.here.sdk.maploader.MapUpdater.MapUpdateVersionCommitPolicy.ON_FIRST_REGION</a> allows to make faster use of the downloaded region and requires less disk space as only the currently updated region is kept until the process completes. However, with an <a href="-map-update-version-commit-policy/-o-n_-f-i-r-s-t_-r-e-g-i-o-n/index.html">com.here.sdk.maploader.MapUpdater.MapUpdateVersionCommitPolicy.ON_FIRST_REGION</a> policy the overall process can be less reliable and bears a higher risk of errors.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-1603081136%2FProperties%2F1617540583" anchor-label="taskCount" id="-1603081136%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="task-count.html"><span>task</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1603081136%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="task-count.html">taskCount</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a></div><div class="brief "><p class="paragraph">The number of concurrent tasks for downloading a map. A valid task count is between 1 to 64. When the value set is outside the valid range, then it is clamped to a valid range:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1481363444%2FProperties%2F1617540583" anchor-label="updateStatistics" id="1481363444%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="update-statistics.html"><span>update</span><wbr></wbr><span><span>Statistics</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1481363444%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="update-statistics.html">updateStatistics</a><span class="token operator">: </span><a href="../-update-statistics/index.html">UpdateStatistics</a></div><div class="brief "><p class="paragraph">Map update statistics for the current application session. In the event of binary updates, patches are downloaded and applied. This property helps to  determine the success or failure rate of applied patches.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="788424481%2FFunctions%2F1617540583" anchor-label="getCurrentMapVersion" id="788424481%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-current-map-version.html"><span>get</span><wbr></wbr><span>Current</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Version</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="788424481%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-current-map-version.html"><span class="token function">getCurrentMapVersion</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-map-version-handle/index.html">MapVersionHandle</a></div><div class="brief "><p class="paragraph">Returns a handle that contains the map version of the already downloaded and installed regions. This information is only needed for debugging purposes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1745202635%2FFunctions%2F1617540583" anchor-label="retrieveCatalogsUpdateInfo" id="-1745202635%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="retrieve-catalogs-update-info.html"><span>retrieve</span><wbr></wbr><span>Catalogs</span><wbr></wbr><span>Update</span><wbr></wbr><span><span>Info</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1745202635%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="retrieve-catalogs-update-info.html"><span class="token function">retrieveCatalogsUpdateInfo</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">callback<span class="token operator">: </span><a href="../-catalogs-update-info-callback/index.html">CatalogsUpdateInfoCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Retrieves information of all catalogs that have newer version available. This method can also be used to query catalog information like HRN, current installed version and newer available version on server. An empty list in <a href="../-catalogs-update-info-callback/index.html">com.here.sdk.maploader.CatalogsUpdateInfoCallback</a> represent no map updates.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-80006104%2FFunctions%2F1617540583" anchor-label="setVersionCommitPolicy" id="-80006104%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-version-commit-policy.html"><span>set</span><wbr></wbr><span>Version</span><wbr></wbr><span>Commit</span><wbr></wbr><span><span>Policy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-80006104%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-version-commit-policy.html"><span class="token function">setVersionCommitPolicy</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">versionCommitPolicy<span class="token operator">: </span><a href="-map-update-version-commit-policy/index.html">MapUpdater.MapUpdateVersionCommitPolicy</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets the map update version policy. Defaults to <a href="-map-update-version-commit-policy/-o-n_-c-o-m-p-l-e-t-e/index.html">com.here.sdk.maploader.MapUpdater.MapUpdateVersionCommitPolicy.ON_COMPLETE</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="760731010%2FFunctions%2F1617540583" anchor-label="updateCatalog" id="760731010%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="update-catalog.html"><span>update</span><wbr></wbr><span><span>Catalog</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="760731010%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="update-catalog.html"><span class="token function">updateCatalog</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">catalogInfo<span class="token operator">: </span><a href="../-catalog-update-info/index.html">CatalogUpdateInfo</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-catalog-update-progress-listener/index.html">CatalogUpdateProgressListener</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-catalog-update-task/index.html">CatalogUpdateTask</a></div><div class="brief "><p class="paragraph">Performs an asynchronous request for each catalog to update map data to the latest available version. This applies to all previously installed <a href="../-region/index.html">com.here.sdk.maploader.Region</a> map data and any incomplete downloads in a pending state.</p></div></div></div>
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
