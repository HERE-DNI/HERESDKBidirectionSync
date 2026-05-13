---
title: "SegmentData"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapdata-segment-data"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>SegmentData</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapdata/SegmentData///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapdata</a><span class="delimiter">/</span><span class="current">SegmentData</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Segment</span><wbr></wbr><span><span>Data</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">SegmentData</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">Contains the requested information for a segment</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-2128748124%2FClasslikes%2F1617540583" anchor-label="Companion" id="-2128748124%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2128748124%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="-527592408%2FProperties%2F1617540583" anchor-label="lengthInMeters" id="-527592408%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="length-in-meters.html"><span>length</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-527592408%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="length-in-meters.html">lengthInMeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The length of this segment in meters. This information is based on map data. It can differ from the length of <a href="polyline.html">com.here.sdk.mapdata.SegmentData.polyline</a> due to approximations of the polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1047449128%2FProperties%2F1617540583" anchor-label="ocmSegmentId" id="1047449128%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="ocm-segment-id.html"><span>ocm</span><wbr></wbr><span>Segment</span><wbr></wbr><span><span>Id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1047449128%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="ocm-segment-id.html">ocmSegmentId</a><span class="token operator">: </span><a href="../-o-c-m-segment-id/index.html">OCMSegmentId</a></div><div class="brief "><p class="paragraph">The <a href="../-o-c-m-segment-id/index.html">com.here.sdk.mapdata.OCMSegmentId</a> object representing the segment</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-637462179%2FProperties%2F1617540583" anchor-label="polyline" id="-637462179%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="polyline.html"><span><span>polyline</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-637462179%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="polyline.html">polyline</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-polyline/index.html">GeoPolyline</a></div><div class="brief "><p class="paragraph">The <a href="../../com.here.sdk.core/-geo-polyline/index.html">com.here.sdk.core.GeoPolyline</a> object representing the polyline of this segment.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="942849577%2FProperties%2F1617540583" anchor-label="railwayCrossings" id="942849577%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="railway-crossings.html"><span>railway</span><wbr></wbr><span><span>Crossings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="942849577%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="railway-crossings.html">railwayCrossings</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-railway-crossing/index.html">RailwayCrossing</a><span class="token operator">&gt;</span><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The list of <a href="../-railway-crossing/index.html">com.here.sdk.mapdata.RailwayCrossing</a> of the given segment. Returns an empty list if no data is found. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-railway-crossings.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadRailwayCrossings</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="165099015%2FProperties%2F1617540583" anchor-label="roadSigns" id="165099015%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="road-signs.html"><span>road</span><wbr></wbr><span><span>Signs</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="165099015%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="road-signs.html">roadSigns</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../../com.here.sdk.navigation/-road-sign/index.html">RoadSign</a><span class="token operator">&gt;</span><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The list of <a href="../../com.here.sdk.navigation/-road-sign/index.html">com.here.sdk.navigation.RoadSign</a> of the given segment. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-road-signs.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadRoadSigns</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="288378053%2FProperties%2F1617540583" anchor-label="segmentReference" id="288378053%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="segment-reference.html"><span>segment</span><wbr></wbr><span><span>Reference</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="288378053%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="segment-reference.html">segmentReference</a><span class="token operator">: </span><a href="../../com.here.sdk.routing/-segment-reference/index.html">SegmentReference</a></div><div class="brief "><p class="paragraph">The <a href="../../com.here.sdk.routing/-segment-reference/index.html">com.here.sdk.routing.SegmentReference</a> object representing the segment</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-943798764%2FProperties%2F1617540583" anchor-label="spans" id="-943798764%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="spans.html"><span><span>spans</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-943798764%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="spans.html">spans</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-segment-span-data/index.html">SegmentSpanData</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of <a href="../-segment-span-data/index.html">com.here.sdk.mapdata.SegmentSpanData</a> of the given segment for the requested attributes <strong>Note:</strong> If no span attributes is requested, the list will be empty.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1462094559%2FProperties%2F1617540583" anchor-label="tollPoints" id="1462094559%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="toll-points.html"><span>toll</span><wbr></wbr><span><span>Points</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1462094559%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="toll-points.html">tollPoints</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-toll-point/index.html">TollPoint</a><span class="token operator">&gt;</span><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The list of <a href="../-toll-point/index.html">com.here.sdk.mapdata.TollPoint</a> of the given segment. Returns an empty list if no data is found. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-toll-points.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadTollPoints</a> is set to <code class="lang-kotlin">false</code> or the <a href="index.html">com.here.sdk.mapdata.SegmentData</a> is not initialized using <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-438349617%2FProperties%2F1617540583" anchor-label="trafficSignals" id="-438349617%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="traffic-signals.html"><span>traffic</span><wbr></wbr><span><span>Signals</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-438349617%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="traffic-signals.html">trafficSignals</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-traffic-signal/index.html">TrafficSignal</a><span class="token operator">&gt;</span><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The list of <a href="../-traffic-signal/index.html">com.here.sdk.mapdata.TrafficSignal</a> of the given segment. Returns an empty list if no data is found. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-traffic-signals.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadTrafficSignals</a> is set to <code class="lang-kotlin">false</code>. The <a href="../-traffic-signal-location/index.html">com.here.sdk.mapdata.TrafficSignalLocation</a> indicates the location of a single traffic signal, which can be any combination of left, right and overhead. The <a href="../-traffic-signal/offset-in-meters.html">com.here.sdk.mapdata.TrafficSignal.offsetInMeters</a> is the location along the segment, while the traffic signal location have details on how the traffic signal is display/deploy in that specific location in the segment.</p></div></div></div>
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
