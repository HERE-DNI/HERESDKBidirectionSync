---
title: "Venue"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>Venue</title>
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
            <a class="library-name--link" href="sdk-for-flutter-explore-index">
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.venue.control/Venue///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.venue.control</a><span class="delimiter">/</span><span class="current">Venue</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Venue</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Venue</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><p class="paragraph">Controls the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueModel</a> inside the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.control.VenueMap</a> object. The venue controls the selection of the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueDrawing</a> and the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueLevel</a> of the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueModel</a>. It provides the possibility to customize styles for the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueGeometry</a>. Objects of this class can only be created using methods <a href="sdk-for-flutter-explore-add-venue-async">com.here.sdk.venue.control.VenueMap.addVenueAsync</a> and <a href="sdk-for-flutter-explore-select-venue-async">com.here.sdk.venue.control.VenueMap.selectVenueAsync</a>.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1714558810%2FClasslikes%2F1617540583" anchor-label="Companion" id="1714558810%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1714558810%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="988802490%2FProperties%2F1617540583" anchor-label="isTopologyVisible" id="988802490%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-topology-visible"><span>is</span><wbr></wbr><span>Topology</span><wbr></wbr><span><span>Visible</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="988802490%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-topology-visible">isTopologyVisible</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Returns true if topology is visible. It can be used to check the status of topology visibility.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1714717168%2FProperties%2F1617540583" anchor-label="selectedDrawing" id="1714717168%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-selected-drawing"><span>selected</span><wbr></wbr><span><span>Drawing</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1714717168%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-selected-drawing">selectedDrawing</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VenueDrawing</a></div><div class="brief "><p class="paragraph">The selected drawing. Only the selected drawing will be visible as active on the map. All others will be hidden or displayed without details, depending on the implementation of the renderer.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="572524938%2FProperties%2F1617540583" anchor-label="selectedLevel" id="572524938%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-selected-level"><span>selected</span><wbr></wbr><span><span>Level</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="572524938%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-selected-level">selectedLevel</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VenueLevel</a></div><div class="brief "><p class="paragraph">The selected level. Only the selected level will be visible as active on the map. All others will be hidden or displayed without details, depending on a renderer implementation. If the level doesn't belong to the currently selected drawing, it can not be selected.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1008047714%2FProperties%2F1617540583" anchor-label="selectedLevelIndex" id="-1008047714%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-selected-level-index"><span>selected</span><wbr></wbr><span>Level</span><wbr></wbr><span><span>Index</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1008047714%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-selected-level-index">selectedLevelIndex</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The index of the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueLevel</a> selected from the level array of the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueDrawing</a>. Unlike the Z index, it can't have a negative value.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-708397518%2FProperties%2F1617540583" anchor-label="selectedLevelZIndex" id="-708397518%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-selected-level-z-index"><span>selected</span><wbr></wbr><span>Level</span><wbr></wbr><span><span>ZIndex</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-708397518%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-selected-level-z-index">selectedLevelZIndex</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The Z index value of the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueLevel</a> selected. Z index 0 represents the ground level, negative values represent underground levels, positive values - levels above the ground. Z index can also be taken from <a href="sdk-for-flutter-explore-z-index">com.here.sdk.venue.data.VenueLevel.zIndex</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="194726765%2FProperties%2F1617540583" anchor-label="venueModel" id="194726765%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-venue-model"><span>venue</span><wbr></wbr><span><span>Model</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="194726765%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-venue-model">venueModel</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VenueModel</a></div><div class="brief "><p class="paragraph">The <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueModel</a> controlled by this object. It can be used to get the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueModel</a> belonging to this object, like a building or a complex of buildings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="597856741%2FProperties%2F1617540583" anchor-label="venueStyle" id="597856741%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-venue-style"><span>venue</span><wbr></wbr><span><span>Style</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="597856741%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-venue-style">venueStyle</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VenueStyle</a></div><div class="brief "><p class="paragraph">The <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.style.VenueStyle</a> associated with the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueModel</a> controlled by this object. It can be used to get the style of the venue. Contains the information about the geometry and label styles available for the venue.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="644387840%2FFunctions%2F1617540583" anchor-label="setCustomStyle" id="644387840%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-custom-style"><span>set</span><wbr></wbr><span>Custom</span><wbr></wbr><span><span>Style</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="644387840%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-custom-style"><span class="token function">setCustomStyle</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">topologies<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">VenueTopology</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">style<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VenueGeometryStyle</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets a custom style for topologies.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-custom-style"><span class="token function">setCustomStyle</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">geometries<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">VenueGeometry</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">style<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VenueGeometryStyle</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">labelStyle<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VenueLabelStyle</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets a custom style for geometries and related labels.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="812546809%2FFunctions%2F1617540583" anchor-label="setCustomStyleToCrosswalk" id="812546809%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-custom-style-to-crosswalk"><span>set</span><wbr></wbr><span>Custom</span><wbr></wbr><span>Style</span><wbr></wbr><span>To</span><wbr></wbr><span><span>Crosswalk</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="812546809%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-custom-style-to-crosswalk"><span class="token function">setCustomStyleToCrosswalk</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">crosswalks<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">Crosswalk</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">style<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VenueGeometryStyle</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets a custom style for crosswalk.</p></div></div></div>
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
`}</HTMLBlock>
