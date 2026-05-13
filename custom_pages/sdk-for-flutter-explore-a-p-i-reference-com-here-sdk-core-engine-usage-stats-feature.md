---
title: "Feature"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-usage-stats-feature"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>Feature</title>
    <link href="../../../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../../../";</script>
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
<script type="text/javascript" src="../../../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../../../styles/style.css" rel="Stylesheet">
<link href="../../../../styles/main.css" rel="Stylesheet">
<link href="../../../../styles/prism.css" rel="Stylesheet">
<link href="../../../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
</head>
<body>
    <div class="root">
    <nav class="navigation theme-dark" id="navigation-wrapper">
            <a class="library-name--link" href="../../../../index.html">
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.core.engine/UsageStats.Feature///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../../index.html">com.here.sdk.core.engine</a><span class="delimiter">/</span><a href="../index.html">UsageStats</a><span class="delimiter">/</span><span class="current">Feature</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Feature</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="index.html">Feature</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="index.html">UsageStats.Feature</a><span class="token operator">&gt; </span></div><p class="paragraph">Represents the feature enum associated with the gathered usage stats.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
    <div class="tabs-section-body">
      <div data-togglable="ENTRY">
        <h2 class="">Entries</h2>
        <div class="table"><a data-name="726973526%2FClasslikes%2F1617540583" anchor-label="DETAILED_RENDERING" id="726973526%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-d-e-t-a-i-l-e-d_-r-e-n-d-e-r-i-n-g/index.html">DETAILED_RENDERING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="726973526%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-d-e-t-a-i-l-e-d_-r-e-n-d-e-r-i-n-g/index.html">DETAILED_RENDERING</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the <a href="../../-layer-configuration/-feature/-d-e-t-a-i-l_-r-e-n-d-e-r-i-n-g/index.html">com.here.sdk.core.engine.LayerConfiguration.Feature.DETAIL_RENDERING</a> layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1724911849%2FClasslikes%2F1617540583" anchor-label="EV_RENDERING" id="-1724911849%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-v_-r-e-n-d-e-r-i-n-g/index.html">EV_RENDERING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1724911849%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-v_-r-e-n-d-e-r-i-n-g/index.html">EV_RENDERING</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the &quot;ev_charging_station_rendering_premium&quot; layer group, enabled with <a href="../../-layer-configuration/-feature/-e-v/index.html">com.here.sdk.core.engine.LayerConfiguration.Feature.EV</a>. Note, that <a href="../../-layer-configuration/-feature/-e-v/index.html">com.here.sdk.core.engine.LayerConfiguration.Feature.EV</a> also enables &quot;ev_charging_station_search_premium&quot; layer group, which is represented with <a href="-e-v_-s-e-a-r-c-h/index.html">UsageStats.Feature.EV_SEARCH</a>. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1083562875%2FClasslikes%2F1617540583" anchor-label="EV_SEARCH" id="-1083562875%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-v_-s-e-a-r-c-h/index.html">EV_SEARCH</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1083562875%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-v_-s-e-a-r-c-h/index.html">EV_SEARCH</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the &quot;ev_charging_station_search_premium&quot; layer group, enabled with <a href="../../-layer-configuration/-feature/-e-v/index.html">com.here.sdk.core.engine.LayerConfiguration.Feature.EV</a>. Note, that <a href="../../-layer-configuration/-feature/-e-v/index.html">com.here.sdk.core.engine.LayerConfiguration.Feature.EV</a> also enables &quot;ev_charging_station_rendering_premium&quot; layer group, which is represented with <a href="-e-v_-r-e-n-d-e-r-i-n-g/index.html">UsageStats.Feature.EV_RENDERING</a>. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-169832563%2FClasslikes%2F1617540583" anchor-label="NAVIGATION" id="-169832563%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-a-v-i-g-a-t-i-o-n/index.html">NAVIGATION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-169832563%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-a-v-i-g-a-t-i-o-n/index.html">NAVIGATION</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the &quot;adas&quot;, &quot;ehorizon&quot;, &quot;interop&quot;, &quot;isa&quot; OCM layers. In addition, it is also tracking the following layer configurations:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1946861125%2FClasslikes%2F1617540583" anchor-label="PLACES" id="1946861125%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-l-a-c-e-s/index.html">PLACES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1946861125%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-l-a-c-e-s/index.html">PLACES</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for places search. This is legacy statistic which is now replaced by <a href="-s-e-a-r-c-h_-o-n-l-i-n-e/index.html">com.here.sdk.core.engine.UsageStats.Feature.SEARCH_ONLINE</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="897669902%2FClasslikes%2F1617540583" anchor-label="RDS_TRAFFIC" id="897669902%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-d-s_-t-r-a-f-f-i-c/index.html">RDS_TRAFFIC</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="897669902%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-d-s_-t-r-a-f-f-i-c/index.html">RDS_TRAFFIC</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the <a href="../../-layer-configuration/-feature/-r-d-s_-t-r-a-f-f-i-c/index.html">com.here.sdk.core.engine.LayerConfiguration.Feature.RDS_TRAFFIC</a> layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2033535867%2FClasslikes%2F1617540583" anchor-label="RENDERING" id="2033535867%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-e-n-d-e-r-i-n-g/index.html">RENDERING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2033535867%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-e-n-d-e-r-i-n-g/index.html">RENDERING</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the <a href="../../-layer-configuration/-feature/-r-e-n-d-e-r-i-n-g/index.html">com.here.sdk.core.engine.LayerConfiguration.Feature.RENDERING</a> layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1818699646%2FClasslikes%2F1617540583" anchor-label="ROUTER" id="-1818699646%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-o-u-t-e-r/index.html">ROUTER</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1818699646%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-o-u-t-e-r/index.html">ROUTER</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the <code class="lang-kotlin">RoutingEngine</code>. Includes the following transaction counts and APIs:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1994279669%2FClasslikes%2F1617540583" anchor-label="ROUTING" id="1994279669%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-o-u-t-i-n-g/index.html">ROUTING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1994279669%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-o-u-t-i-n-g/index.html">ROUTING</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the following layer configurations:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1156975343%2FClasslikes%2F1617540583" anchor-label="SATELLITES" id="-1156975343%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-a-t-e-l-l-i-t-e-s/index.html">SATELLITES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1156975343%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-a-t-e-l-l-i-t-e-s/index.html">SATELLITES</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics to show satellite map scheme. This includes a <strong>Raster Tile Base</strong> transaction count with HRN <code class="lang-kotlin">hrn:here:service::olp-here:rendering-raster-tiles-3:base</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1996176735%2FClasslikes%2F1617540583" anchor-label="SEARCH" id="-1996176735%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-e-a-r-c-h/index.html">SEARCH</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1996176735%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-e-a-r-c-h/index.html">SEARCH</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the &quot;search&quot;, &quot;ev_charging_station_search_premium&quot;, &quot;fueling_station_premium&quot; OCM layers. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1413308377%2FClasslikes%2F1617540583" anchor-label="SEARCH_ONLINE" id="1413308377%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-e-a-r-c-h_-o-n-l-i-n-e/index.html">SEARCH_ONLINE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1413308377%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-e-a-r-c-h_-o-n-l-i-n-e/index.html">SEARCH_ONLINE</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the <code class="lang-kotlin">SearchEngine</code>. Includes the following transaction counts and APIs:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2035880126%2FClasslikes%2F1617540583" anchor-label="TRANSIT" id="-2035880126%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-r-a-n-s-i-t/index.html">TRANSIT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2035880126%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-r-a-n-s-i-t/index.html">TRANSIT</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the &quot;transit&quot; OCM layer. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-771513664%2FClasslikes%2F1617540583" anchor-label="TRANSIT_ROUTING_ENGINE" id="-771513664%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-r-a-n-s-i-t_-r-o-u-t-i-n-g_-e-n-g-i-n-e/index.html">TRANSIT_ROUTING_ENGINE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-771513664%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-r-a-n-s-i-t_-r-o-u-t-i-n-g_-e-n-g-i-n-e/index.html">TRANSIT_ROUTING_ENGINE</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the <code class="lang-kotlin">TransitRoutingEngine</code>. This includes a <strong>Public Transit</strong> transaction count with HRN: <code class="lang-kotlin">hrn:here:service::olp-here:transit-8</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1323336212%2FClasslikes%2F1617540583" anchor-label="TRAFFIC" id="-1323336212%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-r-a-f-f-i-c/index.html">TRAFFIC</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1323336212%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-r-a-f-f-i-c/index.html">TRAFFIC</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the calls of <code class="lang-kotlin">TrafficEngine</code>. All calls to <code class="lang-kotlin">TrafficEngine</code> result in transaction counts for HRN <code class="lang-kotlin">hrn:here:service::olp-here:traffic-api-7:standard</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1104531068%2FClasslikes%2F1617540583" anchor-label="TRAFFIC_VECTOR_TILES" id="-1104531068%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-r-a-f-f-i-c_-v-e-c-t-o-r_-t-i-l-e-s/index.html">TRAFFIC_VECTOR_TILES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1104531068%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-r-a-f-f-i-c_-v-e-c-t-o-r_-t-i-l-e-s/index.html">TRAFFIC_VECTOR_TILES</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for traffic vector tiles. This includes a <strong>Traffic vector tile</strong> transaction count with HRN: <code class="lang-kotlin">hrn:here:service::olp-here:traffic-vector-tiles-2</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1831221134%2FClasslikes%2F1617540583" anchor-label="TRUCK" id="1831221134%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-r-u-c-k/index.html">TRUCK</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1831221134%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-r-u-c-k/index.html">TRUCK</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the <a href="../../-layer-configuration/-feature/-t-r-u-c-k/index.html">com.here.sdk.core.engine.LayerConfiguration.Feature.TRUCK</a> layer configuration. Counted when data for the corresponding layer is requested by the application by performing one of the following actions:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1747679970%2FClasslikes%2F1617540583" anchor-label="VECTOR_TILES" id="1747679970%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-v-e-c-t-o-r_-t-i-l-e-s/index.html">VECTOR_TILES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1747679970%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-v-e-c-t-o-r_-t-i-l-e-s/index.html">VECTOR_TILES</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for online usage corresponding to the vector tiles. This includes a <strong>Vector tile</strong> transaction count with HRN: <code class="lang-kotlin">hrn:here:service::olp-here:rendering-vector-tiles-2</code>. This statistic is only counted for the HERE SDK (Explore) when showing the map view.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1482908287%2FClasslikes%2F1617540583" anchor-label="OTHER" id="1482908287%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-t-h-e-r/index.html">OTHER</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1482908287%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-t-h-e-r/index.html">OTHER</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for feature that doesn't fit into other categories. Some examples include:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-280303736%2FClasslikes%2F1617540583" anchor-label="POSITIONING" id="-280303736%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-o-s-i-t-i-o-n-i-n-g/index.html">POSITIONING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-280303736%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-o-s-i-t-i-o-n-i-n-g/index.html">POSITIONING</a></div></div><div class="brief "><p class="paragraph">Represents network traffic statistics for Here Positioning. This includes a <strong>Network Positioning</strong> transaction count with HRN <code class="lang-kotlin">hrn:here:service::olp-here:positioning-2</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="74412819%2FProperties%2F1617540583" anchor-label="entries" id="74412819%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="entries.html"><span><span>entries</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="74412819%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="entries.html">entries</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="token operator">&lt;</span><a href="index.html">UsageStats.Feature</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1851012818%2FProperties%2F1617540583" anchor-label="value" id="1851012818%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value.html"><span><span>value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1851012818%2FProperties%2F1617540583"></span>
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
        <div class="table"><a data-name="1254441321%2FFunctions%2F1617540583" anchor-label="valueOf" id="1254441321%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value-of.html"><span>value</span><wbr></wbr><span><span>Of</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1254441321%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="value-of.html"><span class="token function">valueOf</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">UsageStats.Feature</a></div><div class="brief "><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1181889995%2FFunctions%2F1617540583" anchor-label="values" id="-1181889995%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="values.html"><span><span>values</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1181889995%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="values.html"><span class="token function">values</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="token operator">&lt;</span><a href="index.html">UsageStats.Feature</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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
