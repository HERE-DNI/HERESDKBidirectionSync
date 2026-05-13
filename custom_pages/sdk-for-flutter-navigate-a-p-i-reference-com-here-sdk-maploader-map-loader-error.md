---
title: "MapLoaderError"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-maploader-map-loader-error"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapLoaderError</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.maploader/MapLoaderError///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.maploader</a><span class="delimiter">/</span><span class="current">MapLoaderError</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span>Loader</span><wbr></wbr><span><span>Error</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="index.html">MapLoaderError</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="index.html">MapLoaderError</a><span class="token operator">&gt; </span></div><p class="paragraph">Specifies possible errors that may result from map downloading/prefetching.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
    <div class="tabs-section-body">
      <div data-togglable="ENTRY">
        <h2 class="">Entries</h2>
        <div class="table"><a data-name="1784415465%2FClasslikes%2F1617540583" anchor-label="RESOURCE_NOT_FOUND" id="1784415465%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-e-s-o-u-r-c-e_-n-o-t_-f-o-u-n-d/index.html">RESOURCE_NOT_FOUND</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1784415465%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-e-s-o-u-r-c-e_-n-o-t_-f-o-u-n-d/index.html">RESOURCE_NOT_FOUND</a></div></div><div class="brief "><p class="paragraph">The requested resource is not found.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="702988315%2FClasslikes%2F1617540583" anchor-label="NOT_READY" id="702988315%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o-t_-r-e-a-d-y/index.html">NOT_READY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="702988315%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o-t_-r-e-a-d-y/index.html">NOT_READY</a></div></div><div class="brief "><p class="paragraph">There's a problem with an ongoing download or update: If an operation is in a paused state, you can resume or cancel it. If no operation is in a paused state: Either wait for active downloads to finish, or cancel existing <code class="lang-kotlin">sdk.maploader.MapDownloader</code> requests and call <code class="lang-kotlin">sdk.maploader.MapDownloader.get_initial_persistent_map_status</code>. If there is a problem, call <code class="lang-kotlin">sdk.maploader.MapDownloader.repair_persistent_map</code> to repair before continuing with other <code class="lang-kotlin">sdk.maploader.MapDownloader</code> operations. This error may occur when an on-going or paused operation prevents the requested task.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1891397929%2FClasslikes%2F1617540583" anchor-label="INVALID_ARGUMENT" id="1891397929%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-n-v-a-l-i-d_-a-r-g-u-m-e-n-t/index.html">INVALID_ARGUMENT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1891397929%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-n-v-a-l-i-d_-a-r-g-u-m-e-n-t/index.html">INVALID_ARGUMENT</a></div></div><div class="brief "><p class="paragraph">The request passed invalid arguments.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2034536413%2FClasslikes%2F1617540583" anchor-label="OPERATION_CANCELLED" id="2034536413%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-p-e-r-a-t-i-o-n_-c-a-n-c-e-l-l-e-d/index.html">OPERATION_CANCELLED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2034536413%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-p-e-r-a-t-i-o-n_-c-a-n-c-e-l-l-e-d/index.html">OPERATION_CANCELLED</a></div></div><div class="brief "><p class="paragraph">The request was cancelled (usually by the user).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-675774921%2FClasslikes%2F1617540583" anchor-label="ALREADY_INSTALLED" id="-675774921%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-a-l-r-e-a-d-y_-i-n-s-t-a-l-l-e-d/index.html">ALREADY_INSTALLED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-675774921%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-a-l-r-e-a-d-y_-i-n-s-t-a-l-l-e-d/index.html">ALREADY_INSTALLED</a></div></div><div class="brief "><p class="paragraph">All tiles of requested regions were already installed, no need for any download.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="542426496%2FClasslikes%2F1617540583" anchor-label="TIME_OUT" id="542426496%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-i-m-e_-o-u-t/index.html">TIME_OUT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="542426496%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-i-m-e_-o-u-t/index.html">TIME_OUT</a></div></div><div class="brief "><p class="paragraph">The request exceeded the timeout limit.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="358361194%2FClasslikes%2F1617540583" anchor-label="SERVICE_UNAVAILABLE" id="358361194%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-e-r-v-i-c-e_-u-n-a-v-a-i-l-a-b-l-e/index.html">SERVICE_UNAVAILABLE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="358361194%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-e-r-v-i-c-e_-u-n-a-v-a-i-l-a-b-l-e/index.html">SERVICE_UNAVAILABLE</a></div></div><div class="brief "><p class="paragraph">The requested service is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1777606074%2FClasslikes%2F1617540583" anchor-label="ACCESS_DENIED" id="1777606074%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-a-c-c-e-s-s_-d-e-n-i-e-d/index.html">ACCESS_DENIED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1777606074%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-a-c-c-e-s-s_-d-e-n-i-e-d/index.html">ACCESS_DENIED</a></div></div><div class="brief "><p class="paragraph">The access is denied due to invalid credentials.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1238593442%2FClasslikes%2F1617540583" anchor-label="REQUEST_LIMIT_REACHED" id="1238593442%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-e-q-u-e-s-t_-l-i-m-i-t_-r-e-a-c-h-e-d/index.html">REQUEST_LIMIT_REACHED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1238593442%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-e-q-u-e-s-t_-l-i-m-i-t_-r-e-a-c-h-e-d/index.html">REQUEST_LIMIT_REACHED</a></div></div><div class="brief "><p class="paragraph">Request limit reached for set a credentials for a particular period of time.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="300335388%2FClasslikes%2F1617540583" anchor-label="NETWORK_CONNECTION_ERROR" id="300335388%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-e-t-w-o-r-k_-c-o-n-n-e-c-t-i-o-n_-e-r-r-o-r/index.html">NETWORK_CONNECTION_ERROR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="300335388%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-e-t-w-o-r-k_-c-o-n-n-e-c-t-i-o-n_-e-r-r-o-r/index.html">NETWORK_CONNECTION_ERROR</a></div></div><div class="brief "><p class="paragraph">A network connection error has happened.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1935424381%2FClasslikes%2F1617540583" anchor-label="FORBIDDEN" id="1935424381%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-f-o-r-b-i-d-d-e-n/index.html">FORBIDDEN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1935424381%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-f-o-r-b-i-d-d-e-n/index.html">FORBIDDEN</a></div></div><div class="brief "><p class="paragraph">The operation is forbidden, make sure your credentials grant the necessary permissions.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1054321350%2FClasslikes%2F1617540583" anchor-label="MAP_DATA_ERROR" id="-1054321350%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-m-a-p_-d-a-t-a_-e-r-r-o-r/index.html">MAP_DATA_ERROR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1054321350%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-m-a-p_-d-a-t-a_-e-r-r-o-r/index.html">MAP_DATA_ERROR</a></div></div><div class="brief "><p class="paragraph">Downloaded map data is invalid or a <code class="lang-kotlin">sdk.maploader.RegionId</code> passed to the method <code class="lang-kotlin">sdk.maploader.MapDownloader.delete_regions</code> is incorrect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="294014291%2FClasslikes%2F1617540583" anchor-label="UNEXPECTED_SERVER_RESPONSE" id="294014291%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-u-n-e-x-p-e-c-t-e-d_-s-e-r-v-e-r_-r-e-s-p-o-n-s-e/index.html">UNEXPECTED_SERVER_RESPONSE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="294014291%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-u-n-e-x-p-e-c-t-e-d_-s-e-r-v-e-r_-r-e-s-p-o-n-s-e/index.html">UNEXPECTED_SERVER_RESPONSE</a></div></div><div class="brief "><p class="paragraph">Received unexpected response from the backend. It means the response is malformed or server returned an internal error. Try repeating the request.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2029976343%2FClasslikes%2F1617540583" anchor-label="MAP_MANAGER_ERROR" id="2029976343%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-m-a-p_-m-a-n-a-g-e-r_-e-r-r-o-r/index.html">MAP_MANAGER_ERROR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2029976343%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-m-a-p_-m-a-n-a-g-e-r_-e-r-r-o-r/index.html">MAP_MANAGER_ERROR</a></div></div><div class="brief "><p class="paragraph">Error occurred inside the map manager and might be related to network issues. Try repeating the request.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1728756209%2FClasslikes%2F1617540583" anchor-label="INCOMPLETE_DATA" id="-1728756209%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-n-c-o-m-p-l-e-t-e_-d-a-t-a/index.html">INCOMPLETE_DATA</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1728756209%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-n-c-o-m-p-l-e-t-e_-d-a-t-a/index.html">INCOMPLETE_DATA</a></div></div><div class="brief "><p class="paragraph">The data to process is incomplete, failed decoding the tile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-140632014%2FClasslikes%2F1617540583" anchor-label="SERVICE_ACCESS_FAILED" id="-140632014%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-e-r-v-i-c-e_-a-c-c-e-s-s_-f-a-i-l-e-d/index.html">SERVICE_ACCESS_FAILED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-140632014%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-e-r-v-i-c-e_-a-c-c-e-s-s_-f-a-i-l-e-d/index.html">SERVICE_ACCESS_FAILED</a></div></div><div class="brief "><p class="paragraph">The conditions to access the service are not satisfied. Check if correct <code class="lang-kotlin">sdk.maploader.RegionId</code> was passed to <code class="lang-kotlin">sdk.maploader.MapDownloader.download_regions</code> or download for passed <code class="lang-kotlin">sdk.maploader.RegionId</code> already started. Further control for started download must be performed through <code class="lang-kotlin">sdk.maploader.MapDownloaderTask</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2119350058%2FClasslikes%2F1617540583" anchor-label="INTERNAL_ERROR" id="2119350058%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-n-t-e-r-n-a-l_-e-r-r-o-r/index.html">INTERNAL_ERROR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2119350058%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-n-t-e-r-n-a-l_-e-r-r-o-r/index.html">INTERNAL_ERROR</a></div></div><div class="brief "><p class="paragraph">Internal error occurred.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="918433767%2FClasslikes%2F1617540583" anchor-label="OFFLINE" id="918433767%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-f-f-l-i-n-e/index.html">OFFLINE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="918433767%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-f-f-l-i-n-e/index.html">OFFLINE</a></div></div><div class="brief "><p class="paragraph">Online operation is not permitted because offline mode is enabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1806164112%2FClasslikes%2F1617540583" anchor-label="CACHE_IO_ERROR" id="1806164112%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-c-a-c-h-e_-i-o_-e-r-r-o-r/index.html">CACHE_IO_ERROR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1806164112%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-c-a-c-h-e_-i-o_-e-r-r-o-r/index.html">CACHE_IO_ERROR</a></div></div><div class="brief "><p class="paragraph">A cache IO error occurred.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1660382434%2FClasslikes%2F1617540583" anchor-label="PROTECTED_CACHE_CORRUPTED" id="1660382434%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-o-t-e-c-t-e-d_-c-a-c-h-e_-c-o-r-r-u-p-t-e-d/index.html">PROTECTED_CACHE_CORRUPTED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1660382434%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-o-t-e-c-t-e-d_-c-a-c-h-e_-c-o-r-r-u-p-t-e-d/index.html">PROTECTED_CACHE_CORRUPTED</a></div></div><div class="brief "><p class="paragraph">Protected cache is corrupted. It can be a result of downloading the map in the background and the OS killing the application at that time. Use method <code class="lang-kotlin">sdk.maploader.MapDownloader.get_initial_persistent_map_status</code> to get the status of the map and method repair_persistent_map in the MapDownloader to try to fix the cache if it is broken.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1603838764%2FClasslikes%2F1617540583" anchor-label="MIGRATION_REQUIRED" id="-1603838764%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-m-i-g-r-a-t-i-o-n_-r-e-q-u-i-r-e-d/index.html">MIGRATION_REQUIRED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1603838764%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-m-i-g-r-a-t-i-o-n_-r-e-q-u-i-r-e-d/index.html">MIGRATION_REQUIRED</a></div></div><div class="brief "><p class="paragraph">Operation on the protected cache cannot be done due to required migration. Call <code class="lang-kotlin">sdk.maploader.MapDownloader.repair_persistent_map</code> to perform migration.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1975436312%2FClasslikes%2F1617540583" anchor-label="OPERATION_AFTER_DISPOSE" id="-1975436312%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-p-e-r-a-t-i-o-n_-a-f-t-e-r_-d-i-s-p-o-s-e/index.html">OPERATION_AFTER_DISPOSE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1975436312%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-p-e-r-a-t-i-o-n_-a-f-t-e-r_-d-i-s-p-o-s-e/index.html">OPERATION_AFTER_DISPOSE</a></div></div><div class="brief "><p class="paragraph">Method is invoked on object connected to the disposed SDKNativeEngine.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="475223965%2FClasslikes%2F1617540583" anchor-label="CATALOG_CONFIGURATION_ERROR" id="475223965%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-c-a-t-a-l-o-g_-c-o-n-f-i-g-u-r-a-t-i-o-n_-e-r-r-o-r/index.html">CATALOG_CONFIGURATION_ERROR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="475223965%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-c-a-t-a-l-o-g_-c-o-n-f-i-g-u-r-a-t-i-o-n_-e-r-r-o-r/index.html">CATALOG_CONFIGURATION_ERROR</a></div></div><div class="brief "><p class="paragraph">Misconfiguration of catalogs. This error may occur when <code class="lang-kotlin">sdk.core.engine.CatalogConfiguration</code> is misconfigured and cannot be used for any operation with <code class="lang-kotlin">MapDownloader</code> or <code class="lang-kotlin">MapUpdater</code>. Verify <a href="../../com.here.sdk.core.engine/-s-d-k-options/catalog-configurations.html">com.here.sdk.core.engine.SDKOptions.catalogConfigurations</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-83766123%2FClasslikes%2F1617540583" anchor-label="PENDING_UPDATE" id="-83766123%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-e-n-d-i-n-g_-u-p-d-a-t-e/index.html">PENDING_UPDATE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-83766123%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-e-n-d-i-n-g_-u-p-d-a-t-e/index.html">PENDING_UPDATE</a></div></div><div class="brief "><p class="paragraph">Map regions update was interrupted. Indicates that the cache state is wrong after an update that was finished not in correct way (e.g sudden app shutdown). Prefetching or removing of map regions are blocked until the update has been completed successfully.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-800411717%2FClasslikes%2F1617540583" anchor-label="UPDATE_BLOCKED_AS_ANOTHER_PENDING" id="-800411717%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-u-p-d-a-t-e_-b-l-o-c-k-e-d_-a-s_-a-n-o-t-h-e-r_-p-e-n-d-i-n-g/index.html">UPDATE_BLOCKED_AS_ANOTHER_PENDING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-800411717%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-u-p-d-a-t-e_-b-l-o-c-k-e-d_-a-s_-a-n-o-t-h-e-r_-p-e-n-d-i-n-g/index.html">UPDATE_BLOCKED_AS_ANOTHER_PENDING</a></div></div><div class="brief "><p class="paragraph">Catalog update cannot proceed as another catalog update is in PENDING_UPDATE state. Update the catalog in PENDING_UPDATE state first, before trying to update another catalog.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-319120745%2FClasslikes%2F1617540583" anchor-label="BROKEN_UPDATE" id="-319120745%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-b-r-o-k-e-n_-u-p-d-a-t-e/index.html">BROKEN_UPDATE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-319120745%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-b-r-o-k-e-n_-u-p-d-a-t-e/index.html">BROKEN_UPDATE</a></div></div><div class="brief "><p class="paragraph">Unrecoverable error during construction of pending update parameters. Operations such as catalog updates or region downloads will fail. The healing procedure is to clean persistent map with <code class="lang-kotlin">sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1501156795%2FClasslikes%2F1617540583" anchor-label="PARALLEL_REQUEST" id="1501156795%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-a-r-a-l-l-e-l_-r-e-q-u-e-s-t/index.html">PARALLEL_REQUEST</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1501156795%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-a-r-a-l-l-e-l_-r-e-q-u-e-s-t/index.html">PARALLEL_REQUEST</a></div></div><div class="brief "><p class="paragraph">Parallel request is already running and conflicting with the current one (e.g updating map and deleting map regions)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1546049239%2FClasslikes%2F1617540583" anchor-label="PROXY_AUTHENTICATION_FAILED" id="1546049239%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-o-x-y_-a-u-t-h-e-n-t-i-c-a-t-i-o-n_-f-a-i-l-e-d/index.html">PROXY_AUTHENTICATION_FAILED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1546049239%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-o-x-y_-a-u-t-h-e-n-t-i-c-a-t-i-o-n_-f-a-i-l-e-d/index.html">PROXY_AUTHENTICATION_FAILED</a></div></div><div class="brief "><p class="paragraph">Proxy is not authenticated. Check your proxy credentials.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1347555507%2FClasslikes%2F1617540583" anchor-label="PROXY_SERVER_UNREACHABLE" id="-1347555507%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-o-x-y_-s-e-r-v-e-r_-u-n-r-e-a-c-h-a-b-l-e/index.html">PROXY_SERVER_UNREACHABLE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1347555507%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-o-x-y_-s-e-r-v-e-r_-u-n-r-e-a-c-h-a-b-l-e/index.html">PROXY_SERVER_UNREACHABLE</a></div></div><div class="brief "><p class="paragraph">Proxy server unreachable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2055675929%2FClasslikes%2F1617540583" anchor-label="NOT_ENOUGH_SPACE" id="-2055675929%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o-t_-e-n-o-u-g-h_-s-p-a-c-e/index.html">NOT_ENOUGH_SPACE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2055675929%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o-t_-e-n-o-u-g-h_-s-p-a-c-e/index.html">NOT_ENOUGH_SPACE</a></div></div><div class="brief "><p class="paragraph">There's no sufficient space on the disk to finish operation. For offline maps operation (download or update), it means that there's not enough space on the device. For prefetch operations, it means that there's not enough space in the mutable cache to store the prefetched data.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="963724306%2FClasslikes%2F1617540583" anchor-label="ONLINE_NAVIGATE_ONLY" id="963724306%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-n-l-i-n-e_-n-a-v-i-g-a-t-e_-o-n-l-y/index.html">ONLINE_NAVIGATE_ONLY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="963724306%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-n-l-i-n-e_-n-a-v-i-g-a-t-e_-o-n-l-y/index.html">ONLINE_NAVIGATE_ONLY</a></div></div><div class="brief "><p class="paragraph">This version of HERE SDK does not support the ability to download maps. Contact the sales team to get access to the full version.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="351570270%2FProperties%2F1617540583" anchor-label="entries" id="351570270%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="entries.html"><span><span>entries</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="351570270%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="entries.html">entries</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="token operator">&lt;</span><a href="index.html">MapLoaderError</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-986684451%2FProperties%2F1617540583" anchor-label="value" id="-986684451%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value.html"><span><span>value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-986684451%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="value.html">value</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="900594942%2FFunctions%2F1617540583" anchor-label="valueOf" id="900594942%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value-of.html"><span>value</span><wbr></wbr><span><span>Of</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="900594942%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="value-of.html"><span class="token function">valueOf</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapLoaderError</a></div><div class="brief "><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1043807882%2FFunctions%2F1617540583" anchor-label="values" id="1043807882%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="values.html"><span><span>values</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1043807882%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="values.html"><span class="token function">values</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="token operator">&lt;</span><a href="index.html">MapLoaderError</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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
