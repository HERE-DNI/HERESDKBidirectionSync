---
title: "TrafficQueryError"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-traffic-traffic-query-error"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>TrafficQueryError</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.traffic/TrafficQueryError///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.traffic</a><span class="delimiter">/</span><span class="current">TrafficQueryError</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Traffic</span><wbr></wbr><span>Query</span><wbr></wbr><span><span>Error</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="index.html">TrafficQueryError</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="index.html">TrafficQueryError</a><span class="token operator">&gt; </span></div><p class="paragraph">Represents various errors that could occur from a traffic queries.</p><p class="paragraph">Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
    <div class="tabs-section-body">
      <div data-togglable="ENTRY">
        <h2 class="">Entries</h2>
        <div class="table"><a data-name="622857674%2FClasslikes%2F1617540583" anchor-label="FAILED_TO_RETRIEVE_RESULT" id="622857674%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-f-a-i-l-e-d_-t-o_-r-e-t-r-i-e-v-e_-r-e-s-u-l-t/index.html">FAILED_TO_RETRIEVE_RESULT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="622857674%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-f-a-i-l-e-d_-t-o_-r-e-t-r-i-e-v-e_-r-e-s-u-l-t/index.html">FAILED_TO_RETRIEVE_RESULT</a></div></div><div class="brief "><p class="paragraph">Failed to retrieve result since the server has returned an error or invalid result that couldn't be processed correctly.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-564238288%2FClasslikes%2F1617540583" anchor-label="AUTHENTICATION_FAILED" id="-564238288%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-a-u-t-h-e-n-t-i-c-a-t-i-o-n_-f-a-i-l-e-d/index.html">AUTHENTICATION_FAILED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-564238288%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-a-u-t-h-e-n-t-i-c-a-t-i-o-n_-f-a-i-l-e-d/index.html">AUTHENTICATION_FAILED</a></div></div><div class="brief "><p class="paragraph">Incident query/flow operation is not authenticated. Check your credentials.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1619261083%2FClasslikes%2F1617540583" anchor-label="FORBIDDEN" id="-1619261083%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-f-o-r-b-i-d-d-e-n/index.html">FORBIDDEN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1619261083%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-f-o-r-b-i-d-d-e-n/index.html">FORBIDDEN</a></div></div><div class="brief "><p class="paragraph">The provided credentials don't give access to the requested resource.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1859290260%2FClasslikes%2F1617540583" anchor-label="SERVER_UNREACHABLE" id="1859290260%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-e-r-v-e-r_-u-n-r-e-a-c-h-a-b-l-e/index.html">SERVER_UNREACHABLE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1859290260%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-e-r-v-e-r_-u-n-r-e-a-c-h-a-b-l-e/index.html">SERVER_UNREACHABLE</a></div></div><div class="brief "><p class="paragraph">Server unreachable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1093747410%2FClasslikes%2F1617540583" anchor-label="TIMED_OUT" id="1093747410%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-i-m-e-d_-o-u-t/index.html">TIMED_OUT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1093747410%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-i-m-e-d_-o-u-t/index.html">TIMED_OUT</a></div></div><div class="brief "><p class="paragraph">The request timed out.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1127721009%2FClasslikes%2F1617540583" anchor-label="OFFLINE" id="-1127721009%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-f-f-l-i-n-e/index.html">OFFLINE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1127721009%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-f-f-l-i-n-e/index.html">OFFLINE</a></div></div><div class="brief "><p class="paragraph">The device has no internet connection.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-353174899%2FClasslikes%2F1617540583" anchor-label="HTTP_ERROR" id="-353174899%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-t-t-p_-e-r-r-o-r/index.html">HTTP_ERROR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-353174899%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-t-t-p_-e-r-r-o-r/index.html">HTTP_ERROR</a></div></div><div class="brief "><p class="paragraph">Network request error.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1455839575%2FClasslikes%2F1617540583" anchor-label="INVALID_IN" id="-1455839575%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-n-v-a-l-i-d_-i-n/index.html">INVALID_IN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1455839575%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-n-v-a-l-i-d_-i-n/index.html">INVALID_IN</a></div></div><div class="brief "><p class="paragraph">Invalid &quot;in&quot; parameter: wrong type, missing or invalid &quot;in&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1916399926%2FClasslikes%2F1617540583" anchor-label="INVALID_GEOMETRY" id="1916399926%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-n-v-a-l-i-d_-g-e-o-m-e-t-r-y/index.html">INVALID_GEOMETRY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1916399926%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-n-v-a-l-i-d_-g-e-o-m-e-t-r-y/index.html">INVALID_GEOMETRY</a></div></div><div class="brief "><p class="paragraph">Invalid geometry: bounding box, circle, or corridor.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1730069910%2FClasslikes%2F1617540583" anchor-label="INVALID_INCIDENT" id="1730069910%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-n-v-a-l-i-d_-i-n-c-i-d-e-n-t/index.html">INVALID_INCIDENT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1730069910%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-n-v-a-l-i-d_-i-n-c-i-d-e-n-t/index.html">INVALID_INCIDENT</a></div></div><div class="brief "><p class="paragraph">Invalid incident ID, type, earliestStartTime or latestEndTime.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1622839819%2FClasslikes%2F1617540583" anchor-label="INCIDENT_ID_NOT_FOUND" id="1622839819%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-n-c-i-d-e-n-t_-i-d_-n-o-t_-f-o-u-n-d/index.html">INCIDENT_ID_NOT_FOUND</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1622839819%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-n-c-i-d-e-n-t_-i-d_-n-o-t_-f-o-u-n-d/index.html">INCIDENT_ID_NOT_FOUND</a></div></div><div class="brief "><p class="paragraph">Incident ID is not found in the system.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1847472827%2FClasslikes%2F1617540583" anchor-label="INVALID_FILTER_OPTIONS" id="1847472827%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-n-v-a-l-i-d_-f-i-l-t-e-r_-o-p-t-i-o-n-s/index.html">INVALID_FILTER_OPTIONS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1847472827%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-n-v-a-l-i-d_-f-i-l-t-e-r_-o-p-t-i-o-n-s/index.html">INVALID_FILTER_OPTIONS</a></div></div><div class="brief "><p class="paragraph">One or several filter options are invalid.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-288492883%2FClasslikes%2F1617540583" anchor-label="INVALID_PARAMETER" id="-288492883%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-n-v-a-l-i-d_-p-a-r-a-m-e-t-e-r/index.html">INVALID_PARAMETER</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-288492883%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-n-v-a-l-i-d_-p-a-r-a-m-e-t-e-r/index.html">INVALID_PARAMETER</a></div></div><div class="brief "><p class="paragraph">One or more input parameters in the query is not valid.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1794071106%2FClasslikes%2F1617540583" anchor-label="INTERNAL_ERROR" id="1794071106%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-n-t-e-r-n-a-l_-e-r-r-o-r/index.html">INTERNAL_ERROR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1794071106%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-n-t-e-r-n-a-l_-e-r-r-o-r/index.html">INTERNAL_ERROR</a></div></div><div class="brief "><p class="paragraph">Internal error.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1560943557%2FClasslikes%2F1617540583" anchor-label="OPERATION_CANCELLED" id="1560943557%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-p-e-r-a-t-i-o-n_-c-a-n-c-e-l-l-e-d/index.html">OPERATION_CANCELLED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1560943557%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-p-e-r-a-t-i-o-n_-c-a-n-c-e-l-l-e-d/index.html">OPERATION_CANCELLED</a></div></div><div class="brief "><p class="paragraph">Operation cancelled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="825621183%2FClasslikes%2F1617540583" anchor-label="PROXY_AUTHENTICATION_FAILED" id="825621183%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-o-x-y_-a-u-t-h-e-n-t-i-c-a-t-i-o-n_-f-a-i-l-e-d/index.html">PROXY_AUTHENTICATION_FAILED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="825621183%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-o-x-y_-a-u-t-h-e-n-t-i-c-a-t-i-o-n_-f-a-i-l-e-d/index.html">PROXY_AUTHENTICATION_FAILED</a></div></div><div class="brief "><p class="paragraph">Proxy is not authenticated. Check your proxy credentials.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="478909541%2FClasslikes%2F1617540583" anchor-label="PROXY_SERVER_UNREACHABLE" id="478909541%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-o-x-y_-s-e-r-v-e-r_-u-n-r-e-a-c-h-a-b-l-e/index.html">PROXY_SERVER_UNREACHABLE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="478909541%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-o-x-y_-s-e-r-v-e-r_-u-n-r-e-a-c-h-a-b-l-e/index.html">PROXY_SERVER_UNREACHABLE</a></div></div><div class="brief "><p class="paragraph">Proxy server unreachable. Error indicates a problem with a proxy server's accessibility or connectivity.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-277815647%2FClasslikes%2F1617540583" anchor-label="BAD_REQUEST" id="-277815647%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-b-a-d_-r-e-q-u-e-s-t/index.html">BAD_REQUEST</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-277815647%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-b-a-d_-r-e-q-u-e-s-t/index.html">BAD_REQUEST</a></div></div><div class="brief "><p class="paragraph">Bad request. Error indicates server could not understand or process the request made by the client because the request itself was malformed or incorrect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-822423707%2FClasslikes%2F1617540583" anchor-label="TOO_MANY_REQUESTS" id="-822423707%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-o-o_-m-a-n-y_-r-e-q-u-e-s-t-s/index.html">TOO_MANY_REQUESTS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-822423707%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-o-o_-m-a-n-y_-r-e-q-u-e-s-t-s/index.html">TOO_MANY_REQUESTS</a></div></div><div class="brief "><p class="paragraph">Server has received an excessive number of requests from client within a specific timeframe and client should slow down or wait before sending more requests.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="365047926%2FProperties%2F1617540583" anchor-label="entries" id="365047926%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="entries.html"><span><span>entries</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="365047926%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="entries.html">entries</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="token operator">&lt;</span><a href="index.html">TrafficQueryError</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1122824437%2FProperties%2F1617540583" anchor-label="value" id="1122824437%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value.html"><span><span>value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1122824437%2FProperties%2F1617540583"></span>
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
        <div class="table"><a data-name="-2058183450%2FFunctions%2F1617540583" anchor-label="valueOf" id="-2058183450%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value-of.html"><span>value</span><wbr></wbr><span><span>Of</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2058183450%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="value-of.html"><span class="token function">valueOf</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">TrafficQueryError</a></div><div class="brief "><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2014073970%2FFunctions%2F1617540583" anchor-label="values" id="2014073970%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="values.html"><span><span>values</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2014073970%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="values.html"><span class="token function">values</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="token operator">&lt;</span><a href="index.html">TrafficQueryError</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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
