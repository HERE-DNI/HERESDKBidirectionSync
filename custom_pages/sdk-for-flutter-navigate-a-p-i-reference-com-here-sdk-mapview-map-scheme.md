---
title: "MapScheme"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapview-map-scheme"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapScheme</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapScheme///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MapScheme</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span><span>Scheme</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="index.html">MapScheme</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="index.html">MapScheme</a><span class="token operator">&gt; </span></div><p class="paragraph">Represents the preconfigured map schemes bundled with the SDK.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
    <div class="tabs-section-body">
      <div data-togglable="ENTRY">
        <h2 class="">Entries</h2>
        <div class="table"><a data-name="752554712%2FClasslikes%2F1617540583" anchor-label="NORMAL_DAY" id="752554712%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o-r-m-a-l_-d-a-y/index.html">NORMAL_DAY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="752554712%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o-r-m-a-l_-d-a-y/index.html">NORMAL_DAY</a></div></div><div class="brief "><p class="paragraph">Normal map for day.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2031522900%2FClasslikes%2F1617540583" anchor-label="NORMAL_NIGHT" id="2031522900%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o-r-m-a-l_-n-i-g-h-t/index.html">NORMAL_NIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2031522900%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o-r-m-a-l_-n-i-g-h-t/index.html">NORMAL_NIGHT</a></div></div><div class="brief "><p class="paragraph">Normal map for night.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-876187313%2FClasslikes%2F1617540583" anchor-label="SATELLITE" id="-876187313%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-a-t-e-l-l-i-t-e/index.html">SATELLITE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-876187313%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-a-t-e-l-l-i-t-e/index.html">SATELLITE</a></div></div><div class="brief "><p class="paragraph">Satellite imagery.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2093189459%2FClasslikes%2F1617540583" anchor-label="HYBRID_DAY" id="-2093189459%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-y-b-r-i-d_-d-a-y/index.html">HYBRID_DAY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2093189459%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-y-b-r-i-d_-d-a-y/index.html">HYBRID_DAY</a></div></div><div class="brief "><p class="paragraph">Day version of hybrid scheme combining satellite data with vector street network, map labels and POI information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1129425175%2FClasslikes%2F1617540583" anchor-label="HYBRID_NIGHT" id="-1129425175%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-y-b-r-i-d_-n-i-g-h-t/index.html">HYBRID_NIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1129425175%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-y-b-r-i-d_-n-i-g-h-t/index.html">HYBRID_NIGHT</a></div></div><div class="brief "><p class="paragraph">Night version of hybrid scheme combining satellite data with vector street network, map labels and POI information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-69743393%2FClasslikes%2F1617540583" anchor-label="LITE_DAY" id="-69743393%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-i-t-e_-d-a-y/index.html">LITE_DAY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-69743393%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-i-t-e_-d-a-y/index.html">LITE_DAY</a></div></div><div class="brief "><p class="paragraph">The day version of lite scheme is a simplified version of the <a href="-n-o-r-m-a-l_-d-a-y/index.html">com.here.sdk.mapview.MapScheme.NORMAL_DAY</a>, featuring fewer map elements and a more limited color palette.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2077026459%2FClasslikes%2F1617540583" anchor-label="LITE_NIGHT" id="2077026459%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-i-t-e_-n-i-g-h-t/index.html">LITE_NIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2077026459%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-i-t-e_-n-i-g-h-t/index.html">LITE_NIGHT</a></div></div><div class="brief "><p class="paragraph">The night version of lite scheme is a simplified version of the <a href="-n-o-r-m-a-l_-n-i-g-h-t/index.html">com.here.sdk.mapview.MapScheme.NORMAL_NIGHT</a>, featuring fewer map elements and a more limited color palette.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-830395682%2FClasslikes%2F1617540583" anchor-label="LITE_HYBRID_DAY" id="-830395682%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-i-t-e_-h-y-b-r-i-d_-d-a-y/index.html">LITE_HYBRID_DAY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-830395682%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-i-t-e_-h-y-b-r-i-d_-d-a-y/index.html">LITE_HYBRID_DAY</a></div></div><div class="brief "><p class="paragraph">The day version of lite hybrid scheme is a simplified version of the <a href="-h-y-b-r-i-d_-d-a-y/index.html">com.here.sdk.mapview.MapScheme.HYBRID_DAY</a>, featuring fewer map elements and a more limited color palette.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1234617050%2FClasslikes%2F1617540583" anchor-label="LITE_HYBRID_NIGHT" id="1234617050%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-i-t-e_-h-y-b-r-i-d_-n-i-g-h-t/index.html">LITE_HYBRID_NIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1234617050%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-i-t-e_-h-y-b-r-i-d_-n-i-g-h-t/index.html">LITE_HYBRID_NIGHT</a></div></div><div class="brief "><p class="paragraph">The night version of lite hybrid scheme is a simplified version of the <a href="-h-y-b-r-i-d_-n-i-g-h-t/index.html">com.here.sdk.mapview.MapScheme.HYBRID_NIGHT</a>, featuring fewer map elements and a more limited color palette.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1044592476%2FClasslikes%2F1617540583" anchor-label="LOGISTICS_DAY" id="-1044592476%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-o-g-i-s-t-i-c-s_-d-a-y/index.html">LOGISTICS_DAY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1044592476%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-o-g-i-s-t-i-c-s_-d-a-y/index.html">LOGISTICS_DAY</a></div></div><div class="brief "><p class="paragraph">The day version of the logistics map scheme catering to the needs of dispatchers, fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1549928224%2FClasslikes%2F1617540583" anchor-label="LOGISTICS_NIGHT" id="1549928224%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-o-g-i-s-t-i-c-s_-n-i-g-h-t/index.html">LOGISTICS_NIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1549928224%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-o-g-i-s-t-i-c-s_-n-i-g-h-t/index.html">LOGISTICS_NIGHT</a></div></div><div class="brief "><p class="paragraph">The night version of the logistics map scheme catering to the needs of dispatchers, fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="392386425%2FClasslikes%2F1617540583" anchor-label="LOGISTICS_HYBRID_DAY" id="392386425%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-o-g-i-s-t-i-c-s_-h-y-b-r-i-d_-d-a-y/index.html">LOGISTICS_HYBRID_DAY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="392386425%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-o-g-i-s-t-i-c-s_-h-y-b-r-i-d_-d-a-y/index.html">LOGISTICS_HYBRID_DAY</a></div></div><div class="brief "><p class="paragraph">The day version of the logistics hybrid map scheme catering to the needs of dispatchers, fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-492817227%2FClasslikes%2F1617540583" anchor-label="LOGISTICS_HYBRID_NIGHT" id="-492817227%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-o-g-i-s-t-i-c-s_-h-y-b-r-i-d_-n-i-g-h-t/index.html">LOGISTICS_HYBRID_NIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-492817227%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-o-g-i-s-t-i-c-s_-h-y-b-r-i-d_-n-i-g-h-t/index.html">LOGISTICS_HYBRID_NIGHT</a></div></div><div class="brief "><p class="paragraph">The night version of the logistics hybrid map scheme catering to the needs of dispatchers, fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1487729696%2FClasslikes%2F1617540583" anchor-label="ROAD_NETWORK_DAY" id="-1487729696%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-o-a-d_-n-e-t-w-o-r-k_-d-a-y/index.html">ROAD_NETWORK_DAY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1487729696%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-o-a-d_-n-e-t-w-o-r-k_-d-a-y/index.html">ROAD_NETWORK_DAY</a></div></div><div class="brief "><p class="paragraph">The day version of a scheme highlighting roads without showing other content such as labels or buildings. It is designed for usage as an additional zoomed-in mini-maps display to help drivers to orientate during navigation and to focus on the maneuver arrows which can be highlighted on top of this map scheme.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="896822108%2FClasslikes%2F1617540583" anchor-label="ROAD_NETWORK_NIGHT" id="896822108%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-o-a-d_-n-e-t-w-o-r-k_-n-i-g-h-t/index.html">ROAD_NETWORK_NIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="896822108%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-o-a-d_-n-e-t-w-o-r-k_-n-i-g-h-t/index.html">ROAD_NETWORK_NIGHT</a></div></div><div class="brief "><p class="paragraph">The night version of a scheme highlighting roads without showing other content such as labels or buildings. It is designed for usage as an additional zoomed-in mini-maps display to help drivers to orientate during navigation and to focus on the maneuver arrows which can be highlighted on top of this map scheme.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-161172757%2FClasslikes%2F1617540583" anchor-label="TOPO_DAY" id="-161172757%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-o-p-o_-d-a-y/index.html">TOPO_DAY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-161172757%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-o-p-o_-d-a-y/index.html">TOPO_DAY</a></div></div><div class="brief "><p class="paragraph">The day version of a scheme highlighting geographic features such as elevation, landforms and natural landscapes to provide a clear representation of the terrain. It is best suited for applications related to hiking, biking, skiing or any outdoor activities.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="112753575%2FClasslikes%2F1617540583" anchor-label="TOPO_NIGHT" id="112753575%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-o-p-o_-n-i-g-h-t/index.html">TOPO_NIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="112753575%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-o-p-o_-n-i-g-h-t/index.html">TOPO_NIGHT</a></div></div><div class="brief "><p class="paragraph">The night version of a scheme highlighting geographic features such as elevation, landforms and natural landscapes to provide a clear representation of the terrain. It is best suited for applications related to hiking, biking, skiing or any outdoor activities.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="1675164494%2FProperties%2F1617540583" anchor-label="entries" id="1675164494%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="entries.html"><span><span>entries</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1675164494%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="entries.html">entries</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="token operator">&lt;</span><a href="index.html">MapScheme</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1097372109%2FProperties%2F1617540583" anchor-label="value" id="1097372109%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value.html"><span><span>value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1097372109%2FProperties%2F1617540583"></span>
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
        <div class="table"><a data-name="-550096626%2FFunctions%2F1617540583" anchor-label="valueOf" id="-550096626%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value-of.html"><span>value</span><wbr></wbr><span><span>Of</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-550096626%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="value-of.html"><span class="token function">valueOf</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapScheme</a></div><div class="brief "><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1225051802%2FFunctions%2F1617540583" anchor-label="values" id="1225051802%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="values.html"><span><span>values</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1225051802%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="values.html"><span class="token function">values</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="token operator">&lt;</span><a href="index.html">MapScheme</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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
