---
title: "SegmentDataLoaderOptions"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapdata-segment-data-loader-options"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>SegmentDataLoaderOptions</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapdata/SegmentDataLoaderOptions///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapdata</a><span class="delimiter">/</span><span class="current">SegmentDataLoaderOptions</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Segment</span><wbr></wbr><span>Data</span><wbr></wbr><span>Loader</span><wbr></wbr><span><span>Options</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">SegmentDataLoaderOptions</a></div><p class="paragraph">Specifies which data should be loaded by the <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> function.</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-715234980%2FConstructors%2F1617540583" anchor-label="SegmentDataLoaderOptions" id="-715234980%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-segment-data-loader-options.html"><span>Segment</span><wbr></wbr><span>Data</span><wbr></wbr><span>Loader</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-715234980%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="2025386829%2FProperties%2F1617540583" anchor-label="loadAdministrativeRules" id="2025386829%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-administrative-rules.html"><span>load</span><wbr></wbr><span>Administrative</span><wbr></wbr><span><span>Rules</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2025386829%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-administrative-rules.html">loadAdministrativeRules</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, <a href="../-segment-span-data/administrative-rules.html">com.here.sdk.mapdata.SegmentSpanData.administrativeRules</a> will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> is called. Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1661504729%2FProperties%2F1617540583" anchor-label="loadBaseSpeeds" id="-1661504729%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-base-speeds.html"><span>load</span><wbr></wbr><span>Base</span><wbr></wbr><span><span>Speeds</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1661504729%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-base-speeds.html">loadBaseSpeeds</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, <a href="../-segment-span-data/positive-direction-base-speed-in-meters-per-second.html">com.here.sdk.mapdata.SegmentSpanData.positiveDirectionBaseSpeedInMetersPerSecond</a>, <a href="../-segment-span-data/negative-direction-base-speed-in-meters-per-second.html">com.here.sdk.mapdata.SegmentSpanData.negativeDirectionBaseSpeedInMetersPerSecond</a> and <a href="../-segment-span-data/base-speed-in-meters-per-second.html">com.here.sdk.mapdata.SegmentSpanData.baseSpeedInMetersPerSecond</a> will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> is called.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-563468863%2FProperties%2F1617540583" anchor-label="loadFunctionalRoadClass" id="-563468863%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-functional-road-class.html"><span>load</span><wbr></wbr><span>Functional</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Class</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-563468863%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-functional-road-class.html">loadFunctionalRoadClass</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, the <a href="../-segment-span-data/functional-road-class.html">com.here.sdk.mapdata.SegmentSpanData.functionalRoadClass</a> will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> is called.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-68024681%2FProperties%2F1617540583" anchor-label="loadLocalRoadCharacteristics" id="-68024681%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-local-road-characteristics.html"><span>load</span><wbr></wbr><span>Local</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Characteristics</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-68024681%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-local-road-characteristics.html">loadLocalRoadCharacteristics</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, <a href="../-segment-span-data/local-road-characteristics.html">com.here.sdk.mapdata.SegmentSpanData.localRoadCharacteristics</a> will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> is called.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-707872368%2FProperties%2F1617540583" anchor-label="loadRailwayCrossings" id="-707872368%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-railway-crossings.html"><span>load</span><wbr></wbr><span>Railway</span><wbr></wbr><span><span>Crossings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-707872368%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-railway-crossings.html">loadRailwayCrossings</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, <a href="../-segment-data/railway-crossings.html">com.here.sdk.mapdata.SegmentData.railwayCrossings</a> will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> is called. Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1058647949%2FProperties%2F1617540583" anchor-label="loadRoadAttributes" id="1058647949%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-road-attributes.html"><span>load</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1058647949%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-road-attributes.html">loadRoadAttributes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, <a href="../-segment-span-data/physical-attributes.html">com.here.sdk.mapdata.SegmentSpanData.physicalAttributes</a> and <a href="../-segment-span-data/road-usages.html">com.here.sdk.mapdata.SegmentSpanData.roadUsages</a> will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> is called.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1694748544%2FProperties%2F1617540583" anchor-label="loadRoadSigns" id="-1694748544%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-road-signs.html"><span>load</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Signs</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1694748544%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-road-signs.html">loadRoadSigns</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, <a href="../-segment-data/road-signs.html">com.here.sdk.mapdata.SegmentData.roadSigns</a> will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> is called. Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1178943169%2FProperties%2F1617540583" anchor-label="loadSpecialSpeedSituations" id="1178943169%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-special-speed-situations.html"><span>load</span><wbr></wbr><span>Special</span><wbr></wbr><span>Speed</span><wbr></wbr><span><span>Situations</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1178943169%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-special-speed-situations.html">loadSpecialSpeedSituations</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, <a href="../-segment-span-data/special-speed-situations.html">com.here.sdk.mapdata.SegmentSpanData.specialSpeedSituations</a> will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> is called. <strong>Note:</strong> To get timezone offset and daylight saving time values for TimeRule, sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules must also be set to <code class="lang-kotlin">true</code>. Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="462124599%2FProperties%2F1617540583" anchor-label="loadSpeedLimits" id="462124599%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-speed-limits.html"><span>load</span><wbr></wbr><span>Speed</span><wbr></wbr><span><span>Limits</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="462124599%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-speed-limits.html">loadSpeedLimits</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, <a href="../-segment-span-data/positive-direction-speed-limit.html">com.here.sdk.mapdata.SegmentSpanData.positiveDirectionSpeedLimit</a>, <a href="../-segment-span-data/negative-direction-speed-limit.html">com.here.sdk.mapdata.SegmentSpanData.negativeDirectionSpeedLimit</a> and <a href="../-segment-span-data/speed-limit.html">com.here.sdk.mapdata.SegmentSpanData.speedLimit</a> will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> is called.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="175574718%2FProperties%2F1617540583" anchor-label="loadStreetNamesAndRoadNumbers" id="175574718%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-street-names-and-road-numbers.html"><span>load</span><wbr></wbr><span>Street</span><wbr></wbr><span>Names</span><wbr></wbr><span>And</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Numbers</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="175574718%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-street-names-and-road-numbers.html">loadStreetNamesAndRoadNumbers</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, <a href="../-segment-span-data/street-names.html">com.here.sdk.mapdata.SegmentSpanData.streetNames</a> and <a href="../-segment-span-data/road-numbers.html">com.here.sdk.mapdata.SegmentSpanData.roadNumbers</a> and will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> is called.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-358604922%2FProperties%2F1617540583" anchor-label="loadTollPoints" id="-358604922%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-toll-points.html"><span>load</span><wbr></wbr><span>Toll</span><wbr></wbr><span><span>Points</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-358604922%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-toll-points.html">loadTollPoints</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, <a href="../-segment-data/toll-points.html">com.here.sdk.mapdata.SegmentData.tollPoints</a> will be loaded when <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> is called. Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-717161994%2FProperties%2F1617540583" anchor-label="loadTrafficSignals" id="-717161994%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-traffic-signals.html"><span>load</span><wbr></wbr><span>Traffic</span><wbr></wbr><span><span>Signals</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-717161994%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-traffic-signals.html">loadTrafficSignals</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, <a href="../-segment-data/traffic-signals.html">com.here.sdk.mapdata.SegmentData.trafficSignals</a> will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> is called. Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-784644199%2FProperties%2F1617540583" anchor-label="loadTransportModesAccess" id="-784644199%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-transport-modes-access.html"><span>load</span><wbr></wbr><span>Transport</span><wbr></wbr><span>Modes</span><wbr></wbr><span><span>Access</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-784644199%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-transport-modes-access.html">loadTransportModesAccess</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, <a href="../-segment-span-data/allowed-transport-modes.html">com.here.sdk.mapdata.SegmentSpanData.allowedTransportModes</a> will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> is called.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2099273265%2FProperties%2F1617540583" anchor-label="loadTravelDirection" id="2099273265%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-travel-direction.html"><span>load</span><wbr></wbr><span>Travel</span><wbr></wbr><span><span>Direction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2099273265%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-travel-direction.html">loadTravelDirection</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, the <a href="../-segment-span-data/travel-direction.html">com.here.sdk.mapdata.SegmentSpanData.travelDirection</a> will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="../-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> is called.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1503947964%2FProperties%2F1617540583" anchor-label="loadUrban" id="-1503947964%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-urban.html"><span>load</span><wbr></wbr><span><span>Urban</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1503947964%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="load-urban.html">loadUrban</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If it is true, <a href="../-segment-span-data/is-urban.html">com.here.sdk.mapdata.SegmentSpanData.isUrban</a> will be loaded when <a href="../-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> is called. Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="1844152951%2FFunctions%2F1617540583" anchor-label="equals" id="1844152951%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="equals.html"><span><span>equals</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1844152951%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">operator override </span><span class="token keyword">fun </span><a href="equals.html"><span class="token function">equals</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">other<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1020810097%2FFunctions%2F1617540583" anchor-label="hashCode" id="-1020810097%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="hash-code.html"><span>hash</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1020810097%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">fun </span><a href="hash-code.html"><span class="token function">hashCode</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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
