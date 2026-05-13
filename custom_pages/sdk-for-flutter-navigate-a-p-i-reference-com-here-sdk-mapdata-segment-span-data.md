---
title: "SegmentSpanData"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapdata-segment-span-data"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>SegmentSpanData</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapdata/SegmentSpanData///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapdata</a><span class="delimiter">/</span><span class="current">SegmentSpanData</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Segment</span><wbr></wbr><span>Span</span><wbr></wbr><span><span>Data</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">SegmentSpanData</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">Contains attributes that are not necessarily constant on a full segment. A Span is a portion of a Segment where the requested attributes are constant.</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-51823238%2FClasslikes%2F1617540583" anchor-label="Companion" id="-51823238%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-51823238%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="-1968241558%2FProperties%2F1617540583" anchor-label="administrativeRules" id="-1968241558%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="administrative-rules.html"><span>administrative</span><wbr></wbr><span><span>Rules</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1968241558%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="administrative-rules.html">administrativeRules</a><span class="token operator">: </span><a href="../-administrative-rules/index.html">AdministrativeRules</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The <a href="../-administrative-rules/index.html">com.here.sdk.mapdata.AdministrativeRules</a> for the segment, containing information about country code, state code, unit system, tolls, pre-trip planning and other administrative information. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-administrative-rules.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadAdministrativeRules</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1903770428%2FProperties%2F1617540583" anchor-label="allowedTransportModes" id="-1903770428%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="allowed-transport-modes.html"><span>allowed</span><wbr></wbr><span>Transport</span><wbr></wbr><span><span>Modes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1903770428%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="allowed-transport-modes.html">allowedTransportModes</a><span class="token operator">: </span><a href="../-allowed-transport-modes/index.html">AllowedTransportModes</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The <a href="../-allowed-transport-modes/index.html">com.here.sdk.mapdata.AllowedTransportModes</a> object representing the allowed transport modes. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-transport-modes-access.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadTransportModesAccess</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1631816773%2FProperties%2F1617540583" anchor-label="baseSpeedInMetersPerSecond" id="-1631816773%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="base-speed-in-meters-per-second.html"><span>base</span><wbr></wbr><span>Speed</span><wbr></wbr><span>In</span><wbr></wbr><span>Meters</span><wbr></wbr><span>Per</span><wbr></wbr><span><span>Second</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1631816773%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="base-speed-in-meters-per-second.html">baseSpeedInMetersPerSecond</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The average speed expected for this segment span with a car or a similar vehicle. Will be loaded if <a href="../-segment-data-loader-options/load-base-speeds.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadBaseSpeeds</a> is <code class="lang-kotlin">true</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-262129954%2FProperties%2F1617540583" anchor-label="functionalRoadClass" id="-262129954%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="functional-road-class.html"><span>functional</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Class</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-262129954%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="functional-road-class.html">functionalRoadClass</a><span class="token operator">: </span><a href="../../com.here.sdk.routing/-functional-road-class/index.html">FunctionalRoadClass</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The <a href="../../com.here.sdk.routing/-functional-road-class/index.html">com.here.sdk.routing.FunctionalRoadClass</a> object representing the polyline of this segment. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-functional-road-class.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadFunctionalRoadClass</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-483206805%2FProperties%2F1617540583" anchor-label="isUrban" id="-483206805%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-urban.html"><span>is</span><wbr></wbr><span><span>Urban</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-483206805%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="is-urban.html">isUrban</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The urban attribute of the segment. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-urban.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadUrban</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-409264230%2FProperties%2F1617540583" anchor-label="localRoadCharacteristics" id="-409264230%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="local-road-characteristics.html"><span>local</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Characteristics</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-409264230%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="local-road-characteristics.html">localRoadCharacteristics</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-local-road-characteristic/index.html">LocalRoadCharacteristic</a><span class="token operator">&gt;</span><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The local road characteristics of the segment: frontage, parking lot road, or POI access road. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-local-road-characteristics.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadLocalRoadCharacteristics</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-458457795%2FProperties%2F1617540583" anchor-label="negativeDirectionBaseSpeedInMetersPerSecond" id="-458457795%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="negative-direction-base-speed-in-meters-per-second.html"><span>negative</span><wbr></wbr><span>Direction</span><wbr></wbr><span>Base</span><wbr></wbr><span>Speed</span><wbr></wbr><span>In</span><wbr></wbr><span>Meters</span><wbr></wbr><span>Per</span><wbr></wbr><span><span>Second</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-458457795%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="negative-direction-base-speed-in-meters-per-second.html">negativeDirectionBaseSpeedInMetersPerSecond</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The average speed expected for this segment in negative direction with a car or a similar vehicle. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-base-speeds.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadBaseSpeeds</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="199039573%2FProperties%2F1617540583" anchor-label="negativeDirectionSpeedLimit" id="199039573%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="negative-direction-speed-limit.html"><span>negative</span><wbr></wbr><span>Direction</span><wbr></wbr><span>Speed</span><wbr></wbr><span><span>Limit</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="199039573%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="negative-direction-speed-limit.html">negativeDirectionSpeedLimit</a><span class="token operator">: </span><a href="../-segment-speed-limit/index.html">SegmentSpeedLimit</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The <a href="../-segment-speed-limit/index.html">com.here.sdk.mapdata.SegmentSpeedLimit</a> object representing the speed limit of this segment span in the negative travel direction. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-speed-limits.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadSpeedLimits</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="731133497%2FProperties%2F1617540583" anchor-label="physicalAttributes" id="731133497%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="physical-attributes.html"><span>physical</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="731133497%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="physical-attributes.html">physicalAttributes</a><span class="token operator">: </span><a href="../-physical-attributes/index.html">PhysicalAttributes</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The physical attributes of the segment. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-road-attributes.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadRoadAttributes</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="458059009%2FProperties%2F1617540583" anchor-label="positiveDirectionBaseSpeedInMetersPerSecond" id="458059009%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="positive-direction-base-speed-in-meters-per-second.html"><span>positive</span><wbr></wbr><span>Direction</span><wbr></wbr><span>Base</span><wbr></wbr><span>Speed</span><wbr></wbr><span>In</span><wbr></wbr><span>Meters</span><wbr></wbr><span>Per</span><wbr></wbr><span><span>Second</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="458059009%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="positive-direction-base-speed-in-meters-per-second.html">positiveDirectionBaseSpeedInMetersPerSecond</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The average speed expected for this segment in positive direction with a car or a similar vehicle. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-base-speeds.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadBaseSpeeds</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1530794521%2FProperties%2F1617540583" anchor-label="positiveDirectionSpeedLimit" id="1530794521%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="positive-direction-speed-limit.html"><span>positive</span><wbr></wbr><span>Direction</span><wbr></wbr><span>Speed</span><wbr></wbr><span><span>Limit</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1530794521%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="positive-direction-speed-limit.html">positiveDirectionSpeedLimit</a><span class="token operator">: </span><a href="../-segment-speed-limit/index.html">SegmentSpeedLimit</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The <a href="../-segment-speed-limit/index.html">com.here.sdk.mapdata.SegmentSpeedLimit</a> object representing the speed limit of this segment span in the positive tavel direction. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-speed-limits.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadSpeedLimits</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1412457193%2FProperties%2F1617540583" anchor-label="roadNumbers" id="1412457193%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="road-numbers.html"><span>road</span><wbr></wbr><span><span>Numbers</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1412457193%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="road-numbers.html">roadNumbers</a><span class="token operator">: </span><a href="../../com.here.sdk.routing/-localized-road-numbers/index.html">LocalizedRoadNumbers</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The road numbers on the span enriched with information specific to <i>route numbers</i> of a road such as I-10, US-50, or A3. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-street-names-and-road-numbers.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="211131413%2FProperties%2F1617540583" anchor-label="roadUsages" id="211131413%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="road-usages.html"><span>road</span><wbr></wbr><span><span>Usages</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="211131413%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="road-usages.html">roadUsages</a><span class="token operator">: </span><a href="../-road-usages/index.html">RoadUsages</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The road usages of the segment. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-road-attributes.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadRoadAttributes</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1551017368%2FProperties%2F1617540583" anchor-label="spanLengthInMeters" id="-1551017368%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="span-length-in-meters.html"><span>span</span><wbr></wbr><span>Length</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1551017368%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="span-length-in-meters.html">spanLengthInMeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The length of this span in meters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1884732548%2FProperties%2F1617540583" anchor-label="specialSpeedSituations" id="1884732548%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="special-speed-situations.html"><span>special</span><wbr></wbr><span>Speed</span><wbr></wbr><span><span>Situations</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1884732548%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="special-speed-situations.html">specialSpeedSituations</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-segment-special-speed-situation/index.html">SegmentSpecialSpeedSituation</a><span class="token operator">&gt;</span><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The special speed situations of the segment. Will be loaded if <a href="../-segment-data-loader-options/load-special-speed-situations.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadSpecialSpeedSituations</a> is <code class="lang-kotlin">true</code>. <strong>Note:</strong> To get timezone offset and daylight saving time values for TimeRule, sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules must also be set to <code class="lang-kotlin">true</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="636865747%2FProperties%2F1617540583" anchor-label="speedLimit" id="636865747%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="speed-limit.html"><span>speed</span><wbr></wbr><span><span>Limit</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="636865747%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="speed-limit.html">speedLimit</a><span class="token operator">: </span><a href="../-segment-speed-limit/index.html">SegmentSpeedLimit</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The <a href="../-segment-speed-limit/index.html">com.here.sdk.mapdata.SegmentSpeedLimit</a> object representing the speed limit of this segment span. Will be loaded if <a href="../-segment-data-loader-options/load-speed-limits.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadSpeedLimits</a> is <code class="lang-kotlin">true</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="482398959%2FProperties%2F1617540583" anchor-label="startOffsetInMeters" id="482398959%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="start-offset-in-meters.html"><span>start</span><wbr></wbr><span>Offset</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="482398959%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="start-offset-in-meters.html">startOffsetInMeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">Start offset. The offset in meters from the beginning of the segment to the start of the span in positive direction or from the end of the segment to the start of the span in negative direction.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-566377138%2FProperties%2F1617540583" anchor-label="streetNames" id="-566377138%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="street-names.html"><span>street</span><wbr></wbr><span><span>Names</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-566377138%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="street-names.html">streetNames</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-localized-texts/index.html">LocalizedTexts</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The street names on the span. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-street-names-and-road-numbers.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-950172210%2FProperties%2F1617540583" anchor-label="travelDirection" id="-950172210%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="travel-direction.html"><span>travel</span><wbr></wbr><span><span>Direction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-950172210%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="travel-direction.html">travelDirection</a><span class="token operator">: </span><a href="../../com.here.sdk.routing/-travel-direction/index.html">TravelDirection</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The <a href="../../com.here.sdk.routing/-travel-direction/index.html">com.here.sdk.routing.TravelDirection</a> object representing the allowed travel directions. Gets the <a href="../../com.here.sdk.routing/-travel-direction/index.html">com.here.sdk.routing.TravelDirection</a> object for the portion of the segment. Returns <code class="lang-kotlin">null</code> if <a href="../-segment-data-loader-options/load-travel-direction.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadTravelDirection</a> is set to <code class="lang-kotlin">false</code>.</p></div></div></div>
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
