---
title: "RoutingError"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-routing-error"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>RoutingError</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.routing/RoutingError///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.routing</a><span class="delimiter">/</span><span class="current">RoutingError</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Routing</span><wbr></wbr><span><span>Error</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="index.html">RoutingError</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="index.html">RoutingError</a><span class="token operator">&gt; </span></div><p class="paragraph">Specifies possible errors that may result from the calculation of a route.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
    <div class="tabs-section-body">
      <div data-togglable="ENTRY">
        <h2 class="">Entries</h2>
        <div class="table"><a data-name="-217918792%2FClasslikes%2F1617540583" anchor-label="INTERNAL_ERROR" id="-217918792%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-n-t-e-r-n-a-l_-e-r-r-o-r/index.html">INTERNAL_ERROR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-217918792%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-n-t-e-r-n-a-l_-e-r-r-o-r/index.html">INTERNAL_ERROR</a></div></div><div class="brief "><p class="paragraph">Generic internal error.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1084038775%2FClasslikes%2F1617540583" anchor-label="INVALID_PARAMETER" id="1084038775%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-n-v-a-l-i-d_-p-a-r-a-m-e-t-e-r/index.html">INVALID_PARAMETER</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1084038775%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-n-v-a-l-i-d_-p-a-r-a-m-e-t-e-r/index.html">INVALID_PARAMETER</a></div></div><div class="brief "><p class="paragraph">An invalid input parameter.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1458098698%2FClasslikes%2F1617540583" anchor-label="SERVER_UNREACHABLE" id="1458098698%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-e-r-v-e-r_-u-n-r-e-a-c-h-a-b-l-e/index.html">SERVER_UNREACHABLE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1458098698%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-e-r-v-e-r_-u-n-r-e-a-c-h-a-b-l-e/index.html">SERVER_UNREACHABLE</a></div></div><div class="brief "><p class="paragraph">Routing server is unreachable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1582374403%2FClasslikes%2F1617540583" anchor-label="HTTP_ERROR" id="1582374403%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-t-t-p_-e-r-r-o-r/index.html">HTTP_ERROR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1582374403%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-t-t-p_-e-r-r-o-r/index.html">HTTP_ERROR</a></div></div><div class="brief "><p class="paragraph">A general network request error.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="431922938%2FClasslikes%2F1617540583" anchor-label="AUTHENTICATION_FAILED" id="431922938%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-a-u-t-h-e-n-t-i-c-a-t-i-o-n_-f-a-i-l-e-d/index.html">AUTHENTICATION_FAILED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="431922938%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-a-u-t-h-e-n-t-i-c-a-t-i-o-n_-f-a-i-l-e-d/index.html">AUTHENTICATION_FAILED</a></div></div><div class="brief "><p class="paragraph">Routing operation is not authenticated. Check your credentials.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1833918673%2FClasslikes%2F1617540583" anchor-label="FORBIDDEN" id="-1833918673%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-f-o-r-b-i-d-d-e-n/index.html">FORBIDDEN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1833918673%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-f-o-r-b-i-d-d-e-n/index.html">FORBIDDEN</a></div></div><div class="brief "><p class="paragraph">The provided credentials don't give access to the requested resource.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="474940803%2FClasslikes%2F1617540583" anchor-label="EXCEEDED_USAGE_LIMIT" id="474940803%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-x-c-e-e-d-e-d_-u-s-a-g-e_-l-i-m-i-t/index.html">EXCEEDED_USAGE_LIMIT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="474940803%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-x-c-e-e-d-e-d_-u-s-a-g-e_-l-i-m-i-t/index.html">EXCEEDED_USAGE_LIMIT</a></div></div><div class="brief "><p class="paragraph">Credentials exceeded the allowed requests limit.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="216251855%2FClasslikes%2F1617540583" anchor-label="PARSING_ERROR" id="216251855%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-a-r-s-i-n-g_-e-r-r-o-r/index.html">PARSING_ERROR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="216251855%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-a-r-s-i-n-g_-e-r-r-o-r/index.html">PARSING_ERROR</a></div></div><div class="brief "><p class="paragraph">Error while parsing route data. This is not expected to happen. Try updating to the newest version of the SDK. If the problem persists, please report a bug in the SDK.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1646779616%2FClasslikes%2F1617540583" anchor-label="NO_ROUTE_FOUND" id="-1646779616%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o_-r-o-u-t-e_-f-o-u-n-d/index.html">NO_ROUTE_FOUND</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1646779616%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o_-r-o-u-t-e_-f-o-u-n-d/index.html">NO_ROUTE_FOUND</a></div></div><div class="brief "><p class="paragraph">No route can be calculated for the given input.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="879089820%2FClasslikes%2F1617540583" anchor-label="TIMED_OUT" id="879089820%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-i-m-e-d_-o-u-t/index.html">TIMED_OUT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="879089820%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-i-m-e-d_-o-u-t/index.html">TIMED_OUT</a></div></div><div class="brief "><p class="paragraph">The request timed out.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-421799911%2FClasslikes%2F1617540583" anchor-label="OFFLINE" id="-421799911%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-f-f-l-i-n-e/index.html">OFFLINE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-421799911%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-f-f-l-i-n-e/index.html">OFFLINE</a></div></div><div class="brief "><p class="paragraph">The device has no internet connection.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-69440816%2FClasslikes%2F1617540583" anchor-label="NO_ISOLINE_FOUND" id="-69440816%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o_-i-s-o-l-i-n-e_-f-o-u-n-d/index.html">NO_ISOLINE_FOUND</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-69440816%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o_-i-s-o-l-i-n-e_-f-o-u-n-d/index.html">NO_ISOLINE_FOUND</a></div></div><div class="brief "><p class="paragraph">No isoline can be calculated for the given input.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1888488786%2FClasslikes%2F1617540583" anchor-label="NO_ROUTE_HANDLE" id="1888488786%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o_-r-o-u-t-e_-h-a-n-d-l-e/index.html">NO_ROUTE_HANDLE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1888488786%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o_-r-o-u-t-e_-h-a-n-d-l-e/index.html">NO_ROUTE_HANDLE</a></div></div><div class="brief "><p class="paragraph">The route has no <a href="../-route/route-handle.html">com.here.sdk.routing.Route.routeHandle</a>, but it was used for a feature that requires one. Consider to recalculate the route with a route handle. See <a href="../-route-options/enable-route-handle.html">com.here.sdk.routing.RouteOptions.enableRouteHandle</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2008907023%2FClasslikes%2F1617540583" anchor-label="OPERATION_CANCELLED" id="2008907023%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-p-e-r-a-t-i-o-n_-c-a-n-c-e-l-l-e-d/index.html">OPERATION_CANCELLED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2008907023%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-p-e-r-a-t-i-o-n_-c-a-n-c-e-l-l-e-d/index.html">OPERATION_CANCELLED</a></div></div><div class="brief "><p class="paragraph">Operation cancelled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1053621184%2FClasslikes%2F1617540583" anchor-label="COULD_NOT_MATCH_DESTINATION" id="1053621184%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-c-o-u-l-d_-n-o-t_-m-a-t-c-h_-d-e-s-t-i-n-a-t-i-o-n/index.html">COULD_NOT_MATCH_DESTINATION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1053621184%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-c-o-u-l-d_-n-o-t_-m-a-t-c-h_-d-e-s-t-i-n-a-t-i-o-n/index.html">COULD_NOT_MATCH_DESTINATION</a></div></div><div class="brief "><p class="paragraph">Destination waypoint could not be matched to a road network. Either this waypoint is far from road network or not enough data has been downloaded. When both, origin and destination, cannot be matched, then the origin waypoint error will take precedence.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="444757180%2FClasslikes%2F1617540583" anchor-label="COULD_NOT_MATCH_ORIGIN" id="444757180%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-c-o-u-l-d_-n-o-t_-m-a-t-c-h_-o-r-i-g-i-n/index.html">COULD_NOT_MATCH_ORIGIN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="444757180%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-c-o-u-l-d_-n-o-t_-m-a-t-c-h_-o-r-i-g-i-n/index.html">COULD_NOT_MATCH_ORIGIN</a></div></div><div class="brief "><p class="paragraph">Origin waypoint could not be matched to a road network. Either this waypoint is far from road network or not enough data has been downloaded. When both, origin and destination, cannot be matched, then the origin waypoint error will take precedence.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-28505904%2FClasslikes%2F1617540583" anchor-label="FAILED_ROUTE_HANDLE_CREATION" id="-28505904%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-f-a-i-l-e-d_-r-o-u-t-e_-h-a-n-d-l-e_-c-r-e-a-t-i-o-n/index.html">FAILED_ROUTE_HANDLE_CREATION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-28505904%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-f-a-i-l-e-d_-r-o-u-t-e_-h-a-n-d-l-e_-c-r-e-a-t-i-o-n/index.html">FAILED_ROUTE_HANDLE_CREATION</a></div></div><div class="brief "><p class="paragraph">No RouteHandle was created.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1808475117%2FClasslikes%2F1617540583" anchor-label="IMPORT_FAILED" id="1808475117%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-m-p-o-r-t_-f-a-i-l-e-d/index.html">IMPORT_FAILED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1808475117%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-m-p-o-r-t_-f-a-i-l-e-d/index.html">IMPORT_FAILED</a></div></div><div class="brief "><p class="paragraph">No route section was found for imported waypoints.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-388395505%2FClasslikes%2F1617540583" anchor-label="NO_REACHABLE_CHARGING_STATION_FOUND" id="-388395505%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o_-r-e-a-c-h-a-b-l-e_-c-h-a-r-g-i-n-g_-s-t-a-t-i-o-n_-f-o-u-n-d/index.html">NO_REACHABLE_CHARGING_STATION_FOUND</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-388395505%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o_-r-e-a-c-h-a-b-l-e_-c-h-a-r-g-i-n-g_-s-t-a-t-i-o-n_-f-o-u-n-d/index.html">NO_REACHABLE_CHARGING_STATION_FOUND</a></div></div><div class="brief "><p class="paragraph">Initial charge is not enough to reach any known charging stations.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="808531067%2FClasslikes%2F1617540583" anchor-label="ROUTE_CALCULATION_FAILED" id="808531067%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-o-u-t-e_-c-a-l-c-u-l-a-t-i-o-n_-f-a-i-l-e-d/index.html">ROUTE_CALCULATION_FAILED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="808531067%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-o-u-t-e_-c-a-l-c-u-l-a-t-i-o-n_-f-a-i-l-e-d/index.html">ROUTE_CALCULATION_FAILED</a></div></div><div class="brief "><p class="paragraph">Calculation did not succeed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1383198576%2FClasslikes%2F1617540583" anchor-label="ROUTE_LENGTH_LIMIT_EXCEEDED" id="1383198576%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-o-u-t-e_-l-e-n-g-t-h_-l-i-m-i-t_-e-x-c-e-e-d-e-d/index.html">ROUTE_LENGTH_LIMIT_EXCEEDED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1383198576%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-o-u-t-e_-l-e-n-g-t-h_-l-i-m-i-t_-e-x-c-e-e-d-e-d/index.html">ROUTE_LENGTH_LIMIT_EXCEEDED</a></div></div><div class="brief "><p class="paragraph">Distance between waypoints is too large for current options.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1405035187%2FClasslikes%2F1617540583" anchor-label="VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING" id="-1405035187%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-v-i-o-l-a-t-e-d_-t-r-a-n-s-p-o-r-t_-m-o-d-e_-i-n_-r-o-u-t-e_-h-a-n-d-l-e_-d-e-c-o-d-i-n-g/index.html">VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1405035187%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-v-i-o-l-a-t-e-d_-t-r-a-n-s-p-o-r-t_-m-o-d-e_-i-n_-r-o-u-t-e_-h-a-n-d-l-e_-d-e-c-o-d-i-n-g/index.html">VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING</a></div></div><div class="brief "><p class="paragraph">Route handle decoding failed due to forbidden segments for the specified transport mode.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1296010743%2FClasslikes%2F1617540583" anchor-label="PROXY_AUTHENTICATION_FAILED" id="-1296010743%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-o-x-y_-a-u-t-h-e-n-t-i-c-a-t-i-o-n_-f-a-i-l-e-d/index.html">PROXY_AUTHENTICATION_FAILED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1296010743%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-o-x-y_-a-u-t-h-e-n-t-i-c-a-t-i-o-n_-f-a-i-l-e-d/index.html">PROXY_AUTHENTICATION_FAILED</a></div></div><div class="brief "><p class="paragraph">Proxy is not authenticated. Check your proxy credentials.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1106022053%2FClasslikes%2F1617540583" anchor-label="PROXY_SERVER_UNREACHABLE" id="-1106022053%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-o-x-y_-s-e-r-v-e-r_-u-n-r-e-a-c-h-a-b-l-e/index.html">PROXY_SERVER_UNREACHABLE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1106022053%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-o-x-y_-s-e-r-v-e-r_-u-n-r-e-a-c-h-a-b-l-e/index.html">PROXY_SERVER_UNREACHABLE</a></div></div><div class="brief "><p class="paragraph">Proxy server unreachable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="610530395%2FClasslikes%2F1617540583" anchor-label="ACTIVE_MAP_UPDATE" id="610530395%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-a-c-t-i-v-e_-m-a-p_-u-p-d-a-t-e/index.html">ACTIVE_MAP_UPDATE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="610530395%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-a-c-t-i-v-e_-m-a-p_-u-p-d-a-t-e/index.html">ACTIVE_MAP_UPDATE</a></div></div><div class="brief "><p class="paragraph">Route cannot be calculated due to active map update. Please, repeat the request after map update is finished successfully.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-17288724%2FProperties%2F1617540583" anchor-label="entries" id="-17288724%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="entries.html"><span><span>entries</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-17288724%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="entries.html">entries</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="token operator">&lt;</span><a href="index.html">RoutingError</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2122262549%2FProperties%2F1617540583" anchor-label="value" id="-2122262549%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value.html"><span><span>value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2122262549%2FProperties%2F1617540583"></span>
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
        <div class="table"><a data-name="-1109316816%2FFunctions%2F1617540583" anchor-label="valueOf" id="-1109316816%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value-of.html"><span>value</span><wbr></wbr><span><span>Of</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1109316816%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="value-of.html"><span class="token function">valueOf</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">RoutingError</a></div><div class="brief "><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="200625212%2FFunctions%2F1617540583" anchor-label="values" id="200625212%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="values.html"><span><span>values</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="200625212%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="values.html"><span class="token function">values</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="token operator">&lt;</span><a href="index.html">RoutingError</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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
