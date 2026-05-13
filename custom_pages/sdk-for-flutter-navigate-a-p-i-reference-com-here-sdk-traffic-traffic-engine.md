---
title: "TrafficEngine"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-traffic-traffic-engine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>TrafficEngine</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.traffic/TrafficEngine///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.traffic</a><span class="delimiter">/</span><span class="current">TrafficEngine</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Traffic</span><wbr></wbr><span><span>Engine</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">TrafficEngine</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">Use the TrafficEngine to get information about current traffic flow and incidents in an area specified by <a href="../../com.here.sdk.core/-geo-box/index.html">com.here.sdk.core.GeoBox</a>, <a href="../../com.here.sdk.core/-geo-circle/index.html">com.here.sdk.core.GeoCircle</a>, or <a href="../../com.here.sdk.core/-geo-corridor/index.html">com.here.sdk.core.GeoCorridor</a>. Provides optional parameters given in <a href="../-traffic-incidents-query-options/index.html">com.here.sdk.traffic.TrafficIncidentsQueryOptions</a> and <a href="../-traffic-flow-query-options/index.html">com.here.sdk.traffic.TrafficFlowQueryOptions</a> to filter the result.</p><p class="paragraph">By default, incidents are localized based on their geographical location. You can override that behavior by specifying the desired language that should be used for the incidents description and summary.</p><p class="paragraph">The resulting traffic data contains information on incident types such as congestion, construction for road works, road hazard, road closure, weather updates for road condition, lane restriction and others.</p><p class="paragraph">Traffic data is fetched online to get the most precise and freshest data available. In offline mode, live traffic data can be fetched using the traffic pass-through features. See <a href="../../com.here.sdk.core.engine/-s-d-k-native-engine/pass-through-features.html">com.here.sdk.core.engine.SDKNativeEngine.passThroughFeatures</a></p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-1818046149%2FConstructors%2F1617540583" anchor-label="TrafficEngine" id="-1818046149%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-engine.html"><span>Traffic</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1818046149%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">sdkEngine<span class="token operator">: </span><a href="../../com.here.sdk.core.engine/-s-d-k-native-engine/index.html">SDKNativeEngine</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-60290133%2FClasslikes%2F1617540583" anchor-label="Companion" id="-60290133%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-60290133%2FClasslikes%2F1617540583"></span>
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
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1336384619%2FFunctions%2F1617540583" anchor-label="lookupIncident" id="-1336384619%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="lookup-incident.html"><span>lookup</span><wbr></wbr><span><span>Incident</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1336384619%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="lookup-incident.html"><span class="token function">lookupIncident</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">originalId<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">lookupOptions<span class="token operator">: </span><a href="../-traffic-incident-lookup-options/index.html">TrafficIncidentLookupOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-traffic-incident-lookup-callback/index.html">TrafficIncidentLookupCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously queries for traffic incident by the original id. See <a href="../-traffic-incident/original-id.html">com.here.sdk.traffic.TrafficIncident.originalId</a> for more information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1653310548%2FFunctions%2F1617540583" anchor-label="queryForFlow" id="1653310548%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="query-for-flow.html"><span>query</span><wbr></wbr><span>For</span><wbr></wbr><span><span>Flow</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1653310548%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="query-for-flow.html"><span class="token function">queryForFlow</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">boxArea<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-box/index.html">GeoBox</a><span class="token punctuation">, </span></span><span class="parameter ">queryOptions<span class="token operator">: </span><a href="../-traffic-flow-query-options/index.html">TrafficFlowQueryOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-traffic-flow-query-callback/index.html">TrafficFlowQueryCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously queries for traffic flow using a bounding box as a filter.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="query-for-flow.html"><span class="token function">queryForFlow</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">circleArea<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-circle/index.html">GeoCircle</a><span class="token punctuation">, </span></span><span class="parameter ">queryOptions<span class="token operator">: </span><a href="../-traffic-flow-query-options/index.html">TrafficFlowQueryOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-traffic-flow-query-callback/index.html">TrafficFlowQueryCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously queries for traffic flow using a circle as a filter.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="query-for-flow.html"><span class="token function">queryForFlow</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">corridorArea<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-corridor/index.html">GeoCorridor</a><span class="token punctuation">, </span></span><span class="parameter ">queryOptions<span class="token operator">: </span><a href="../-traffic-flow-query-options/index.html">TrafficFlowQueryOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-traffic-flow-query-callback/index.html">TrafficFlowQueryCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously queries for traffic flow by a corridor as a filter.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="236008499%2FFunctions%2F1617540583" anchor-label="queryForIncidents" id="236008499%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="query-for-incidents.html"><span>query</span><wbr></wbr><span>For</span><wbr></wbr><span><span>Incidents</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="236008499%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="query-for-incidents.html"><span class="token function">queryForIncidents</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">boxArea<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-box/index.html">GeoBox</a><span class="token punctuation">, </span></span><span class="parameter ">queryOptions<span class="token operator">: </span><a href="../-traffic-incidents-query-options/index.html">TrafficIncidentsQueryOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-traffic-incidents-query-callback/index.html">TrafficIncidentsQueryCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously queries for traffic incidents using a bounding box as a filter.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="query-for-incidents.html"><span class="token function">queryForIncidents</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">circleArea<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-circle/index.html">GeoCircle</a><span class="token punctuation">, </span></span><span class="parameter ">queryOptions<span class="token operator">: </span><a href="../-traffic-incidents-query-options/index.html">TrafficIncidentsQueryOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-traffic-incidents-query-callback/index.html">TrafficIncidentsQueryCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously queries for traffic incidents using a circle as a filter.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="query-for-incidents.html"><span class="token function">queryForIncidents</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">corridorArea<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-corridor/index.html">GeoCorridor</a><span class="token punctuation">, </span></span><span class="parameter ">queryOptions<span class="token operator">: </span><a href="../-traffic-incidents-query-options/index.html">TrafficIncidentsQueryOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-traffic-incidents-query-callback/index.html">TrafficIncidentsQueryCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Asynchronously queries for traffic incidents by a corridor as a filter.</p></div></div></div>
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
