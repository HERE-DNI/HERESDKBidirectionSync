---
title: "com.here.sdk.mapview.datasource"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-datasource"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>com.here.sdk.mapview.datasource</title>
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
<div class="main-content" data-page-type="package" id="content" pageIds="API Reference::com.here.sdk.mapview.datasource////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../index.html">API Reference</a><span class="delimiter">/</span><span class="current">com.here.sdk.mapview.datasource</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Package-level</span></span> <span><span>declarations</span></span></h1>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="TYPE">Types</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1726312408%2FClasslikes%2F1617540583" anchor-label="DataAttributes" id="1726312408%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-data-attributes/index.html"><span>Data</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1726312408%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-data-attributes/index.html">DataAttributes</a> : <a href="../com.here/-native-base/index.html">NativeBase</a>, <a href="-data-attributes-base/index.html">DataAttributesBase</a></div><div class="brief "><p class="paragraph">Data attributes collection.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="95202385%2FClasslikes%2F1617540583" anchor-label="DataAttributesAccessor" id="95202385%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-data-attributes-accessor/index.html"><span>Data</span><wbr></wbr><span>Attributes</span><wbr></wbr><span><span>Accessor</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="95202385%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-data-attributes-accessor/index.html">DataAttributesAccessor</a> : <a href="../com.here/-native-base/index.html">NativeBase</a>, <a href="-data-attributes-base/index.html">DataAttributesBase</a></div><div class="brief "><p class="paragraph">Accessor used for manipulating data attributes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="987187847%2FClasslikes%2F1617540583" anchor-label="DataAttributesBase" id="987187847%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-data-attributes-base/index.html"><span>Data</span><wbr></wbr><span>Attributes</span><wbr></wbr><span><span>Base</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="987187847%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-data-attributes-base/index.html">DataAttributesBase</a></div><div class="brief "><p class="paragraph">Interface for a collection of data attributes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="513387407%2FClasslikes%2F1617540583" anchor-label="DataAttributesBuilder" id="513387407%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-data-attributes-builder/index.html"><span>Data</span><wbr></wbr><span>Attributes</span><wbr></wbr><span><span>Builder</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="513387407%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-data-attributes-builder/index.html">DataAttributesBuilder</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Data attributes collection builder.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-208537670%2FClasslikes%2F1617540583" anchor-label="DataAttributeValue" id="-208537670%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-data-attribute-value/index.html"><span>Data</span><wbr></wbr><span>Attribute</span><wbr></wbr><span><span>Value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-208537670%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-data-attribute-value/index.html">DataAttributeValue</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Encapsulates a data attribute value. Supports basic types and arrays of basic types.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1070262107%2FClasslikes%2F1617540583" anchor-label="LineData" id="1070262107%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-line-data/index.html"><span>Line</span><wbr></wbr><span><span>Data</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1070262107%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-line-data/index.html">LineData</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Represents a geodetic line with custom attributes. Can be created using a <a href="-line-data-builder/index.html">com.here.sdk.mapview.datasource.LineDataBuilder</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-667946796%2FClasslikes%2F1617540583" anchor-label="LineDataAccessor" id="-667946796%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-line-data-accessor/index.html"><span>Line</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Accessor</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-667946796%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-line-data-accessor/index.html">LineDataAccessor</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Line data accessor used for manipulating polylines that are part of a LineDataSource.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1042959020%2FClasslikes%2F1617540583" anchor-label="LineDataBuilder" id="1042959020%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-line-data-builder/index.html"><span>Line</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Builder</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1042959020%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-line-data-builder/index.html">LineDataBuilder</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Builder of <a href="-line-data/index.html">com.here.sdk.mapview.datasource.LineData</a> instances.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2094582784%2FClasslikes%2F1617540583" anchor-label="LineDataSource" id="-2094582784%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-line-data-source/index.html"><span>Line</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2094582784%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-line-data-source/index.html">LineDataSource</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Polyline data source allows the rendering engine access to the user provided polylines geometry and their attributes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2000524697%2FClasslikes%2F1617540583" anchor-label="LineDataSourceBuilder" id="-2000524697%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-line-data-source-builder/index.html"><span>Line</span><wbr></wbr><span>Data</span><wbr></wbr><span>Source</span><wbr></wbr><span><span>Builder</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2000524697%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-line-data-source-builder/index.html">LineDataSourceBuilder</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Builder of lines data source.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1570672754%2FClasslikes%2F1617540583" anchor-label="LineTileDataSource" id="1570672754%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-line-tile-data-source/index.html"><span>Line</span><wbr></wbr><span>Tile</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1570672754%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-line-tile-data-source/index.html">LineTileDataSource</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Line tile data source allows the rendering engine access to user managed data sets of geodetic lines and their attributes through a <a href="-line-tile-source/index.html">com.here.sdk.mapview.datasource.LineTileSource</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="196374652%2FClasslikes%2F1617540583" anchor-label="LineTileSource" id="196374652%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-line-tile-source/index.html"><span>Line</span><wbr></wbr><span>Tile</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="196374652%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-line-tile-source/index.html">LineTileSource</a> : <a href="-tile-source/index.html">TileSource</a></div><div class="brief "><p class="paragraph">A source of geodetic line tiles. Lines provided by an implementation must be clipped to the boundaries of the requested tile. The implementations must be thread-safe.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1645455855%2FClasslikes%2F1617540583" anchor-label="PointData" id="1645455855%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-point-data/index.html"><span>Point</span><wbr></wbr><span><span>Data</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1645455855%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-point-data/index.html">PointData</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Represents a geodetic point with custom attributes. Can be created using a <a href="-point-data-builder/index.html">com.here.sdk.mapview.datasource.PointDataBuilder</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-970530968%2FClasslikes%2F1617540583" anchor-label="PointDataAccessor" id="-970530968%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-point-data-accessor/index.html"><span>Point</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Accessor</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-970530968%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-point-data-accessor/index.html">PointDataAccessor</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Point data accessor used for manipulating points that are part of a PointDataSource.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="756103576%2FClasslikes%2F1617540583" anchor-label="PointDataBuilder" id="756103576%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-point-data-builder/index.html"><span>Point</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Builder</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="756103576%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-point-data-builder/index.html">PointDataBuilder</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Builder of <a href="-point-data/index.html">com.here.sdk.mapview.datasource.PointData</a> instances.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-579815532%2FClasslikes%2F1617540583" anchor-label="PointDataSource" id="-579815532%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-point-data-source/index.html"><span>Point</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-579815532%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-point-data-source/index.html">PointDataSource</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Point data source allows the rendering engine access to the user provided geographical locations and their attributes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="41777235%2FClasslikes%2F1617540583" anchor-label="PointDataSourceBuilder" id="41777235%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-point-data-source-builder/index.html"><span>Point</span><wbr></wbr><span>Data</span><wbr></wbr><span>Source</span><wbr></wbr><span><span>Builder</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="41777235%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-point-data-source-builder/index.html">PointDataSourceBuilder</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Builder of points data source.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1449907706%2FClasslikes%2F1617540583" anchor-label="PointTileDataSource" id="-1449907706%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-point-tile-data-source/index.html"><span>Point</span><wbr></wbr><span>Tile</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1449907706%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-point-tile-data-source/index.html">PointTileDataSource</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Point tile data source allows the rendering engine access to user managed data sets of geographical locations and their attributes through a <a href="-point-tile-source/index.html">com.here.sdk.mapview.datasource.PointTileSource</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1711141904%2FClasslikes%2F1617540583" anchor-label="PointTileSource" id="1711141904%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-point-tile-source/index.html"><span>Point</span><wbr></wbr><span>Tile</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1711141904%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-point-tile-source/index.html">PointTileSource</a> : <a href="-tile-source/index.html">TileSource</a></div><div class="brief "><p class="paragraph">A source of geodetic point tiles. The implementations must be thread-safe.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1422496635%2FClasslikes%2F1617540583" anchor-label="PolygonData" id="-1422496635%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-polygon-data/index.html"><span>Polygon</span><wbr></wbr><span><span>Data</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1422496635%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-polygon-data/index.html">PolygonData</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Represents a geodetic polygon with custom attributes. Can be created using a <a href="-polygon-data-builder/index.html">com.here.sdk.mapview.datasource.PolygonDataBuilder</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1988056066%2FClasslikes%2F1617540583" anchor-label="PolygonDataAccessor" id="-1988056066%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-polygon-data-accessor/index.html"><span>Polygon</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Accessor</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1988056066%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-polygon-data-accessor/index.html">PolygonDataAccessor</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Polygon data accessor used for manipulating polygons that are part of a PolygonDataSource.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1000374850%2FClasslikes%2F1617540583" anchor-label="PolygonDataBuilder" id="1000374850%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-polygon-data-builder/index.html"><span>Polygon</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Builder</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1000374850%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-polygon-data-builder/index.html">PolygonDataBuilder</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Builder of <a href="-polygon-data/index.html">com.here.sdk.mapview.datasource.PolygonData</a> instances.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1126125142%2FClasslikes%2F1617540583" anchor-label="PolygonDataSource" id="-1126125142%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-polygon-data-source/index.html"><span>Polygon</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1126125142%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-polygon-data-source/index.html">PolygonDataSource</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Polygon data source allows the rendering engine access to the user provided polygons geometry and their attributes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1957029507%2FClasslikes%2F1617540583" anchor-label="PolygonDataSourceBuilder" id="-1957029507%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-polygon-data-source-builder/index.html"><span>Polygon</span><wbr></wbr><span>Data</span><wbr></wbr><span>Source</span><wbr></wbr><span><span>Builder</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1957029507%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-polygon-data-source-builder/index.html">PolygonDataSourceBuilder</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Builder of the polygons data source.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-38983396%2FClasslikes%2F1617540583" anchor-label="PolygonTileDataSource" id="-38983396%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-polygon-tile-data-source/index.html"><span>Polygon</span><wbr></wbr><span>Tile</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-38983396%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-polygon-tile-data-source/index.html">PolygonTileDataSource</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Polygon tile data source allows the rendering engine access to user managed data sets of geodetic polygons and their attributes through a <a href="-polygon-tile-source/index.html">com.here.sdk.mapview.datasource.PolygonTileSource</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1164832294%2FClasslikes%2F1617540583" anchor-label="PolygonTileSource" id="1164832294%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-polygon-tile-source/index.html"><span>Polygon</span><wbr></wbr><span>Tile</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1164832294%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-polygon-tile-source/index.html">PolygonTileSource</a> : <a href="-tile-source/index.html">TileSource</a></div><div class="brief "><p class="paragraph">A source of geodetic polygon tiles. Polygons provided by an implementation must be clipped to the boundaries of the requested tile. The implementations must be thread-safe.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1473470423%2FClasslikes%2F1617540583" anchor-label="RasterDataSource" id="1473470423%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-raster-data-source/index.html"><span>Raster</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1473470423%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-raster-data-source/index.html">RasterDataSource</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Data source to load map layers using a raster image format (jpg, png). The example below illustrates how to create a raster data source and how to link it to a newly created map layer.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2099117515%2FClasslikes%2F1617540583" anchor-label="RasterDataSourceConfiguration" id="-2099117515%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-raster-data-source-configuration/index.html"><span>Raster</span><wbr></wbr><span>Data</span><wbr></wbr><span>Source</span><wbr></wbr><span><span>Configuration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2099117515%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-raster-data-source-configuration/index.html">RasterDataSourceConfiguration</a></div><div class="brief "><p class="paragraph">Called on the main thread after <code class="lang-kotlin">fromJsonFile()</code> method finishes loading the configuration.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2084441492%2FClasslikes%2F1617540583" anchor-label="RasterDataSourceConfigurationUpdate" id="-2084441492%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-raster-data-source-configuration-update/index.html"><span>Raster</span><wbr></wbr><span>Data</span><wbr></wbr><span>Source</span><wbr></wbr><span>Configuration</span><wbr></wbr><span><span>Update</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2084441492%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-raster-data-source-configuration-update/index.html">RasterDataSourceConfigurationUpdate</a></div><div class="brief "><p class="paragraph">Configuration update for a RasterDataSource.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1252259683%2FClasslikes%2F1617540583" anchor-label="RasterDataSourceError" id="1252259683%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-raster-data-source-error/index.html"><span>Raster</span><wbr></wbr><span>Data</span><wbr></wbr><span>Source</span><wbr></wbr><span><span>Error</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1252259683%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-raster-data-source-error/index.html">RasterDataSourceError</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-raster-data-source-error/index.html">RasterDataSourceError</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Raster data source error codes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="198772611%2FClasslikes%2F1617540583" anchor-label="RasterDataSourceListener" id="198772611%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-raster-data-source-listener/index.html"><span>Raster</span><wbr></wbr><span>Data</span><wbr></wbr><span>Source</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="198772611%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-raster-data-source-listener/index.html">RasterDataSourceListener</a></div><div class="brief "><p class="paragraph">Listener for RasterDataSource events.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-530539437%2FClasslikes%2F1617540583" anchor-label="RasterTileSource" id="-530539437%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-raster-tile-source/index.html"><span>Raster</span><wbr></wbr><span>Tile</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-530539437%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-raster-tile-source/index.html">RasterTileSource</a> : <a href="-tile-source/index.html">TileSource</a></div><div class="brief "><p class="paragraph">A source of raster tiles. The implementations must be thread-safe. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-806614577%2FClasslikes%2F1617540583" anchor-label="TileGeoBoundsCalculator" id="-806614577%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-tile-geo-bounds-calculator/index.html"><span>Tile</span><wbr></wbr><span>Geo</span><wbr></wbr><span>Bounds</span><wbr></wbr><span><span>Calculator</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-806614577%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-tile-geo-bounds-calculator/index.html">TileGeoBoundsCalculator</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">A calculator of geodetic bounds for tiles identified by keys generated in a particular tiling scheme (<a href="-tiling-scheme/index.html">com.here.sdk.mapview.datasource.TilingScheme</a>).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1687390296%2FClasslikes%2F1617540583" anchor-label="TileKey" id="1687390296%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-tile-key/index.html"><span>Tile</span><wbr></wbr><span><span>Key</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1687390296%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-tile-key/index.html">TileKey</a></div><div class="brief "><p class="paragraph">Key of a data source tile. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-731934448%2FClasslikes%2F1617540583" anchor-label="TileSource" id="-731934448%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-tile-source/index.html"><span>Tile</span><wbr></wbr><span><span>Source</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-731934448%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-tile-source/index.html">TileSource</a></div><div class="brief "><p class="paragraph">A source of tiles. The implementations must be thread-safe.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-183367534%2FClasslikes%2F1617540583" anchor-label="TileUrlProviderCallback" id="-183367534%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-tile-url-provider-callback/index.html"><span>Tile</span><wbr></wbr><span>Url</span><wbr></wbr><span>Provider</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-183367534%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-tile-url-provider-callback/index.html">TileUrlProviderCallback</a></div><div class="brief "><p class="paragraph">Provides the URL as String for the given tile coordinates and storage level.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="943497377%2FClasslikes%2F1617540583" anchor-label="TileUrlProviderFactory" id="943497377%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-tile-url-provider-factory/index.html"><span>Tile</span><wbr></wbr><span>Url</span><wbr></wbr><span>Provider</span><wbr></wbr><span><span>Factory</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="943497377%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-tile-url-provider-factory/index.html">TileUrlProviderFactory</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Factory for generating a <a href="-tile-url-provider-callback/index.html">com.here.sdk.mapview.datasource.TileUrlProviderCallback</a> utilized in creating a tile URL.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="612562921%2FClasslikes%2F1617540583" anchor-label="TilingScheme" id="612562921%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-tiling-scheme/index.html"><span>Tiling</span><wbr></wbr><span><span>Scheme</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="612562921%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-tiling-scheme/index.html">TilingScheme</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-tiling-scheme/index.html">TilingScheme</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">List of available data tiling schemes. X axis has the origin at -180 longitude and is increasing in east direction. Y axis has the origin at max latitude and is increasing in south direction. For half quad tree schemes, only the uppper half of the tree is used.</p></div></div></div>
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
