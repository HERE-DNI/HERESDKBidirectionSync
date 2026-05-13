---
title: "VenueMap"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-venue-control-venue-map"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>VenueMap</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.venue.control/VenueMap///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.venue.control</a><span class="delimiter">/</span><span class="current">VenueMap</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Venue</span><wbr></wbr><span><span>Map</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">VenueMap</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">Connects a map with venues. When the <a href="index.html">com.here.sdk.venue.control.VenueMap</a> is started, venues can be seen on the map as interactive models. The user can switch drawings and levels, change a visual style of geometries and related labels inside the venue etc. After constructing the <a href="index.html">com.here.sdk.venue.control.VenueMap</a>, for relevant events should be added to the object. <a href="index.html">com.here.sdk.venue.control.VenueMap</a> is an add-on to the base map functionality with its own content loading and cache. For this reason, in certain situations there may be a small delay before the venue is visible.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-421787792%2FClasslikes%2F1617540583" anchor-label="Companion" id="-421787792%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-421787792%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="1709063701%2FProperties%2F1617540583" anchor-label="selectedVenue" id="1709063701%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="selected-venue.html"><span>selected</span><wbr></wbr><span><span>Venue</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1709063701%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="selected-venue.html">selectedVenue</a><span class="token operator">: </span><a href="../-venue/index.html">Venue</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The selected venue or <code class="lang-kotlin">null</code> if no venue is selected. Use <code class="lang-kotlin">null</code> to deselect the venue.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1550345397%2FProperties%2F1617540583" anchor-label="venueService" id="-1550345397%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="venue-service.html"><span>venue</span><wbr></wbr><span><span>Service</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1550345397%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="venue-service.html">venueService</a><span class="token operator">: </span><a href="../../com.here.sdk.venue.service/-venue-service/index.html">VenueService</a></div><div class="brief "><p class="paragraph">The <code class="lang-kotlin">VenueService</code> object. It can be used to search and get the <a href="../../com.here.sdk.venue.data/-venue-model/index.html">com.here.sdk.venue.data.VenueModel</a> objects.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="531316818%2FFunctions%2F1617540583" anchor-label="add" id="531316818%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add.html"><span><span>add</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="531316818%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add.html"><span class="token function">add</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-drawing-selection-listener/index.html">VenueDrawingSelectionListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a drawing selection .</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add.html"><span class="token function">add</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-info-list-listener/index.html">VenueInfoListListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a listener to handle the completion of the asynchronous venue info list retrieval.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add.html"><span class="token function">add</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-level-selection-listener/index.html">VenueLevelSelectionListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a level selection .</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add.html"><span class="token function">add</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-lifecycle-listener/index.html">VenueLifecycleListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a venue lifecycle .</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add.html"><span class="token function">add</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-map-lifecycle-listener/index.html">VenueMapLifecycleListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a venue map lifecycle .</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add.html"><span class="token function">add</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-selection-listener/index.html">VenueSelectionListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a venue selection .</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1552585606%2FFunctions%2F1617540583" anchor-label="addVenueAsync" id="1552585606%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-venue-async.html"><span>add</span><wbr></wbr><span>Venue</span><wbr></wbr><span><span>Async</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1552585606%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-venue-async.html"><span class="token function">addVenueAsync</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">venueId<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-venue-async.html"><span class="token function">addVenueAsync</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">venueIdentifier<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-venue-async.html"><span class="token function">addVenueAsync</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">venueId<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-venue-load-error-callback/index.html">VenueLoadErrorCallback</a></span></span><span class="token punctuation">)</span></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-venue-async.html"><span class="token function">addVenueAsync</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">venueIdentifier<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-venue-load-error-callback/index.html">VenueLoadErrorCallback</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Downloads and adds a <a href="../-venue/index.html">com.here.sdk.venue.control.Venue</a> to the <a href="index.html">com.here.sdk.venue.control.VenueMap</a>. Method will do nothing if the venue already exists on the venue map.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1873856326%2FFunctions%2F1617540583" anchor-label="cancelVenueSelection" id="-1873856326%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="cancel-venue-selection.html"><span>cancel</span><wbr></wbr><span>Venue</span><wbr></wbr><span><span>Selection</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1873856326%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="cancel-venue-selection.html"><span class="token function">cancelVenueSelection</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Attempts to cancel venue loading and selection that may currently be in progress.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-158899830%2FFunctions%2F1617540583" anchor-label="getCrosswalk" id="-158899830%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-crosswalk.html"><span>get</span><wbr></wbr><span><span>Crosswalk</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-158899830%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-crosswalk.html"><span class="token function">getCrosswalk</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">position<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-coordinates/index.html">GeoCoordinates</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.venue.data/-crosswalk/index.html">Crosswalk</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Tries to find a <a href="../../com.here.sdk.venue.data/-crosswalk/index.html">com.here.sdk.venue.data.Crosswalk</a> at the specified geographic coordinates in the selected <a href="../-venue/index.html">com.here.sdk.venue.control.Venue</a> in the currently selected <a href="../../com.here.sdk.venue.data/-venue-level/index.html">com.here.sdk.venue.data.VenueLevel</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2006142445%2FFunctions%2F1617540583" anchor-label="getGeometry" id="2006142445%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-geometry.html"><span>get</span><wbr></wbr><span><span>Geometry</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2006142445%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-geometry.html"><span class="token function">getGeometry</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">position<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-coordinates/index.html">GeoCoordinates</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.venue.data/-venue-geometry/index.html">VenueGeometry</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Tries to find a <a href="../../com.here.sdk.venue.data/-venue-geometry/index.html">com.here.sdk.venue.data.VenueGeometry</a> at the specified geographic coordinates in the selected <a href="../-venue/index.html">com.here.sdk.venue.control.Venue</a> in the currently selected <a href="../../com.here.sdk.venue.data/-venue-level/index.html">com.here.sdk.venue.data.VenueLevel</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1183347056%2FFunctions%2F1617540583" anchor-label="getTopology" id="-1183347056%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-topology.html"><span>get</span><wbr></wbr><span><span>Topology</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1183347056%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-topology.html"><span class="token function">getTopology</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">position<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-coordinates/index.html">GeoCoordinates</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.venue.data/-venue-topology/index.html">VenueTopology</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Tries to find a <a href="../../com.here.sdk.venue.data/-venue-topology/index.html">com.here.sdk.venue.data.VenueTopology</a> at the specified geographic coordinates in the selected <a href="../-venue/index.html">com.here.sdk.venue.control.Venue</a> in the currently selected <a href="../../com.here.sdk.venue.data/-venue-level/index.html">com.here.sdk.venue.data.VenueLevel</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-102380316%2FFunctions%2F1617540583" anchor-label="getVenue" id="-102380316%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-venue.html"><span>get</span><wbr></wbr><span><span>Venue</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-102380316%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-venue.html"><span class="token function">getVenue</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">position<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-coordinates/index.html">GeoCoordinates</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-venue/index.html">Venue</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Tries to find a <a href="../-venue/index.html">com.here.sdk.venue.control.Venue</a> at the specified geographic coordinates.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1211362793%2FFunctions%2F1617540583" anchor-label="getVenueInfoList" id="1211362793%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-venue-info-list.html"><span>get</span><wbr></wbr><span>Venue</span><wbr></wbr><span>Info</span><wbr></wbr><span><span>List</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1211362793%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-venue-info-list.html"><span class="token function">getVenueInfoList</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../../com.here.sdk.venue.data/-venue-info/index.html">VenueInfo</a><span class="token operator">&gt;</span></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-venue-info-list.html"><span class="token function">getVenueInfoList</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">callback<span class="token operator">: </span><a href="../-venue-load-error-callback/index.html">VenueLoadErrorCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../../com.here.sdk.venue.data/-venue-info/index.html">VenueInfo</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of <a href="../../com.here.sdk.venue.data/-venue-info/index.html">com.here.sdk.venue.data.VenueInfo</a> contains venue id and name.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1534790621%2FFunctions%2F1617540583" anchor-label="getVenueInfoListAsync" id="1534790621%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-venue-info-list-async.html"><span>get</span><wbr></wbr><span>Venue</span><wbr></wbr><span>Info</span><wbr></wbr><span>List</span><wbr></wbr><span><span>Async</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1534790621%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-venue-info-list-async.html"><span class="token function">getVenueInfoListAsync</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-venue-info-list-async.html"><span class="token function">getVenueInfoListAsync</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">callback<span class="token operator">: </span><a href="../-venue-load-error-callback/index.html">VenueLoadErrorCallback</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">The list of <a href="../../com.here.sdk.venue.data/-venue-info/index.html">com.here.sdk.venue.data.VenueInfo</a> contains venue id and name. Downloads the list of <a href="../../com.here.sdk.venue.data/-venue-info/index.html">com.here.sdk.venue.data.VenueInfo</a> asynchronously.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1686242918%2FFunctions%2F1617540583" anchor-label="remove" id="1686242918%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove.html"><span><span>remove</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1686242918%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove.html"><span class="token function">remove</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-drawing-selection-listener/index.html">VenueDrawingSelectionListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a drawing selection .</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove.html"><span class="token function">remove</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-info-list-listener/index.html">VenueInfoListListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a listener for the asynchronous venue info list retrieval.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove.html"><span class="token function">remove</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-level-selection-listener/index.html">VenueLevelSelectionListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a level selection .</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove.html"><span class="token function">remove</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-lifecycle-listener/index.html">VenueLifecycleListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a venue lifecycle .</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove.html"><span class="token function">remove</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-map-lifecycle-listener/index.html">VenueMapLifecycleListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a venue map lifecycle .</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove.html"><span class="token function">remove</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-selection-listener/index.html">VenueSelectionListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a venue selection .</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1253971676%2FFunctions%2F1617540583" anchor-label="removeVenue" id="-1253971676%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-venue.html"><span>remove</span><wbr></wbr><span><span>Venue</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1253971676%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove-venue.html"><span class="token function">removeVenue</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">venue<span class="token operator">: </span><a href="../-venue/index.html">Venue</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a <a href="../-venue/index.html">com.here.sdk.venue.control.Venue</a> from the <a href="index.html">com.here.sdk.venue.control.VenueMap</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="893671532%2FFunctions%2F1617540583" anchor-label="selectVenueAsync" id="893671532%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="select-venue-async.html"><span>select</span><wbr></wbr><span>Venue</span><wbr></wbr><span><span>Async</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="893671532%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="select-venue-async.html"><span class="token function">selectVenueAsync</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">venueId<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="select-venue-async.html"><span class="token function">selectVenueAsync</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">venueIdentifier<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="select-venue-async.html"><span class="token function">selectVenueAsync</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">venueId<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-venue-load-error-callback/index.html">VenueLoadErrorCallback</a></span></span><span class="token punctuation">)</span></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="select-venue-async.html"><span class="token function">selectVenueAsync</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">venueIdentifier<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-venue-load-error-callback/index.html">VenueLoadErrorCallback</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Downloads a <a href="../../com.here.sdk.venue.data/-venue-model/index.html">com.here.sdk.venue.data.VenueModel</a> if needed and selects a <a href="../-venue/index.html">com.here.sdk.venue.control.Venue</a>.</p></div></div></div>
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
