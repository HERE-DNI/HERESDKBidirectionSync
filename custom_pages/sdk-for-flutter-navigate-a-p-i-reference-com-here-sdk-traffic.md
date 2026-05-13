---
title: "com.here.sdk.traffic"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-traffic"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>com.here.sdk.traffic</title>
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
<div class="main-content" data-page-type="package" id="content" pageIds="API Reference::com.here.sdk.traffic////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../index.html">API Reference</a><span class="delimiter">/</span><span class="current">com.here.sdk.traffic</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Package-level</span></span> <span><span>declarations</span></span></h1>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="TYPE">Types</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-771767758%2FClasslikes%2F1617540583" anchor-label="JunctionsTraversability" id="-771767758%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-junctions-traversability/index.html"><span>Junctions</span><wbr></wbr><span><span>Traversability</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-771767758%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-junctions-traversability/index.html">JunctionsTraversability</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-junctions-traversability/index.html">JunctionsTraversability</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Junctions traversability of some traffic incident or flow section.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1517412240%2FClasslikes%2F1617540583" anchor-label="TrafficDataProvider" id="1517412240%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-data-provider/index.html"><span>Traffic</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Provider</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1517412240%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-traffic-data-provider/index.html">TrafficDataProvider</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">This interface provides traffic information from radio signals to other HERE SDK modules. For now, only the <code class="lang-kotlin">OfflineRoutingEngine</code> is supported.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="732274281%2FClasslikes%2F1617540583" anchor-label="TrafficEngine" id="732274281%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-engine/index.html"><span>Traffic</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="732274281%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-traffic-engine/index.html">TrafficEngine</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Use the TrafficEngine to get information about current traffic flow and incidents in an area specified by <a href="../com.here.sdk.core/-geo-box/index.html">com.here.sdk.core.GeoBox</a>, <a href="../com.here.sdk.core/-geo-circle/index.html">com.here.sdk.core.GeoCircle</a>, or <a href="../com.here.sdk.core/-geo-corridor/index.html">com.here.sdk.core.GeoCorridor</a>. Provides optional parameters given in <a href="-traffic-incidents-query-options/index.html">com.here.sdk.traffic.TrafficIncidentsQueryOptions</a> and <a href="-traffic-flow-query-options/index.html">com.here.sdk.traffic.TrafficFlowQueryOptions</a> to filter the result.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="377798525%2FClasslikes%2F1617540583" anchor-label="TrafficFlow" id="377798525%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-flow/index.html"><span>Traffic</span><wbr></wbr><span><span>Flow</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="377798525%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-traffic-flow/index.html">TrafficFlow</a> : <a href="../com.here/-native-base/index.html">NativeBase</a>, <a href="-traffic-flow-base/index.html">TrafficFlowBase</a></div><div class="brief "><p class="paragraph">This class provides details about traffic flow along a <a href="../com.here.sdk.core/-geo-corridor/index.html">com.here.sdk.core.GeoCorridor</a>, inside a <a href="../com.here.sdk.core/-geo-circle/index.html">com.here.sdk.core.GeoCircle</a> or a <a href="../com.here.sdk.core/-geo-box/index.html">com.here.sdk.core.GeoBox</a>, that represents particular path of the road network.<br/> Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.<br/> For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1699495852%2FClasslikes%2F1617540583" anchor-label="TrafficFlowBase" id="1699495852%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-flow-base/index.html"><span>Traffic</span><wbr></wbr><span>Flow</span><wbr></wbr><span><span>Base</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1699495852%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-traffic-flow-base/index.html">TrafficFlowBase</a></div><div class="brief "><p class="paragraph">This interface provides details about a traffic flow.<br/> For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="372227064%2FClasslikes%2F1617540583" anchor-label="TrafficFlowQueryCallback" id="372227064%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-flow-query-callback/index.html"><span>Traffic</span><wbr></wbr><span>Flow</span><wbr></wbr><span>Query</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="372227064%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-traffic-flow-query-callback/index.html">TrafficFlowQueryCallback</a></div><div class="brief "><p class="paragraph">Callback passed to following functions: <a href="-traffic-engine/query-for-flow.html">com.here.sdk.traffic.TrafficEngine.queryForFlow</a> <a href="-traffic-engine/query-for-flow.html">com.here.sdk.traffic.TrafficEngine.queryForFlow</a> The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is <code class="lang-kotlin">null</code> for an operation that succeeds. The second argument is the list of flow items in the case of the success. It is <code class="lang-kotlin">null</code> in case of an error.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2022326631%2FClasslikes%2F1617540583" anchor-label="TrafficFlowQueryOptions" id="2022326631%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-flow-query-options/index.html"><span>Traffic</span><wbr></wbr><span>Flow</span><wbr></wbr><span>Query</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2022326631%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-traffic-flow-query-options/index.html">TrafficFlowQueryOptions</a></div><div class="brief "><p class="paragraph">The options to specify how traffic flow data should be queried.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="669003609%2FClasslikes%2F1617540583" anchor-label="TrafficIncident" id="669003609%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-incident/index.html"><span>Traffic</span><wbr></wbr><span><span>Incident</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="669003609%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-traffic-incident/index.html">TrafficIncident</a> : <a href="../com.here/-native-base/index.html">NativeBase</a>, <a href="-traffic-incident-base/index.html">TrafficIncidentBase</a></div><div class="brief "><p class="paragraph">TrafficIncident provides details about a traffic incident.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2037670280%2FClasslikes%2F1617540583" anchor-label="TrafficIncidentBase" id="2037670280%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-incident-base/index.html"><span>Traffic</span><wbr></wbr><span>Incident</span><wbr></wbr><span><span>Base</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2037670280%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-traffic-incident-base/index.html">TrafficIncidentBase</a></div><div class="brief "><p class="paragraph">TrafficIncident provides details about a traffic incident.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="456378035%2FClasslikes%2F1617540583" anchor-label="TrafficIncidentImpact" id="456378035%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-incident-impact/index.html"><span>Traffic</span><wbr></wbr><span>Incident</span><wbr></wbr><span><span>Impact</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="456378035%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-traffic-incident-impact/index.html">TrafficIncidentImpact</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-traffic-incident-impact/index.html">TrafficIncidentImpact</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Impact of a traffic incident.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2105464378%2FClasslikes%2F1617540583" anchor-label="TrafficIncidentLookupCallback" id="2105464378%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-incident-lookup-callback/index.html"><span>Traffic</span><wbr></wbr><span>Incident</span><wbr></wbr><span>Lookup</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2105464378%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-traffic-incident-lookup-callback/index.html">TrafficIncidentLookupCallback</a></div><div class="brief "><p class="paragraph">Callback passed to <a href="-traffic-engine/lookup-incident.html">com.here.sdk.traffic.TrafficEngine.lookupIncident</a>. The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is <code class="lang-kotlin">null</code> for an operation that succeeds. The second argument is the incident in the case of the success. It is <code class="lang-kotlin">null</code> in case of an error.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1246898459%2FClasslikes%2F1617540583" anchor-label="TrafficIncidentLookupOptions" id="-1246898459%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-incident-lookup-options/index.html"><span>Traffic</span><wbr></wbr><span>Incident</span><wbr></wbr><span>Lookup</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1246898459%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-traffic-incident-lookup-options/index.html">TrafficIncidentLookupOptions</a></div><div class="brief "><p class="paragraph">All the options to specify how a single incident should be queried.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1660776223%2FClasslikes%2F1617540583" anchor-label="TrafficIncidentsQueryCallback" id="1660776223%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-incidents-query-callback/index.html"><span>Traffic</span><wbr></wbr><span>Incidents</span><wbr></wbr><span>Query</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1660776223%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-traffic-incidents-query-callback/index.html">TrafficIncidentsQueryCallback</a></div><div class="brief "><p class="paragraph">Callback passed to <a href="-traffic-engine/query-for-incidents.html">com.here.sdk.traffic.TrafficEngine.queryForIncidents</a>. The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is <code class="lang-kotlin">null</code> for an operation that succeeds. The second argument is the list of incidents in the case of the success. It is <code class="lang-kotlin">null</code> in case of an error.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1094061408%2FClasslikes%2F1617540583" anchor-label="TrafficIncidentsQueryOptions" id="1094061408%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-incidents-query-options/index.html"><span>Traffic</span><wbr></wbr><span>Incidents</span><wbr></wbr><span>Query</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1094061408%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-traffic-incidents-query-options/index.html">TrafficIncidentsQueryOptions</a></div><div class="brief "><p class="paragraph">The options to specify how incidents should be queried.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1220014399%2FClasslikes%2F1617540583" anchor-label="TrafficIncidentType" id="1220014399%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-incident-type/index.html"><span>Traffic</span><wbr></wbr><span>Incident</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1220014399%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-traffic-incident-type/index.html">TrafficIncidentType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-traffic-incident-type/index.html">TrafficIncidentType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Category of a traffic incident.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1431451178%2FClasslikes%2F1617540583" anchor-label="TrafficLocation" id="-1431451178%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-location/index.html"><span>Traffic</span><wbr></wbr><span><span>Location</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1431451178%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-traffic-location/index.html">TrafficLocation</a></div><div class="brief "><p class="paragraph">The location reference to the traffic incident.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1004690251%2FClasslikes%2F1617540583" anchor-label="TrafficQueryError" id="1004690251%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-query-error/index.html"><span>Traffic</span><wbr></wbr><span>Query</span><wbr></wbr><span><span>Error</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1004690251%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-traffic-query-error/index.html">TrafficQueryError</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-traffic-query-error/index.html">TrafficQueryError</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Represents various errors that could occur from a traffic queries.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1062616707%2FClasslikes%2F1617540583" anchor-label="Traversability" id="1062616707%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traversability/index.html"><span><span>Traversability</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1062616707%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-traversability/index.html">Traversability</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-traversability/index.html">Traversability</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Junctions traversability of some traffic incident or flow section.</p></div></div></div>
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
