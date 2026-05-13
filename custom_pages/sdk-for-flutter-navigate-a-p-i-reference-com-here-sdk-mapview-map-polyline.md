---
title: "MapPolyline"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapview-map-polyline"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapPolyline</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapPolyline///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MapPolyline</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span><span>Polyline</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">MapPolyline</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">A visual representation of a line on the map.</p><p class="paragraph">The geometry to be visualized is represented by an instance of <a href="../../com.here.sdk.core/-geo-polyline/index.html">com.here.sdk.core.GeoPolyline</a>.</p><p class="paragraph">Altitude component of <code class="lang-kotlin">GeoPolyline</code>'s vertices is ignored.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="990954598%2FConstructors%2F1617540583" anchor-label="MapPolyline" id="990954598%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-polyline.html"><span>Map</span><wbr></wbr><span><span>Polyline</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="990954598%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">geometry<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-polyline/index.html">GeoPolyline</a><span class="token punctuation">, </span></span><span class="parameter ">representation<span class="token operator">: </span><a href="-representation/index.html">MapPolyline.Representation</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new <code class="lang-kotlin">MapPolyline</code> instance with a specified visual representation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-1657422038%2FClasslikes%2F1617540583" anchor-label="Companion" id="-1657422038%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1657422038%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1270520160%2FClasslikes%2F1617540583" anchor-label="DashImageRepresentation" id="-1270520160%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-dash-image-representation/index.html"><span>Dash</span><wbr></wbr><span>Image</span><wbr></wbr><span><span>Representation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1270520160%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-dash-image-representation/index.html">DashImageRepresentation</a> : <a href="-representation/index.html">MapPolyline.Representation</a></div><div class="brief "><p class="paragraph">Represents a dash pattern for the map polyline consisting of images rendered with certain gaps from each other.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1630123309%2FClasslikes%2F1617540583" anchor-label="DashRepresentation" id="1630123309%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-dash-representation/index.html"><span>Dash</span><wbr></wbr><span><span>Representation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1630123309%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-dash-representation/index.html">DashRepresentation</a> : <a href="-representation/index.html">MapPolyline.Representation</a></div><div class="brief "><p class="paragraph">Represents a dash pattern for map polyline where the dash can be rendered as a colored line and the gap can be either empty or colored.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1954753889%2FClasslikes%2F1617540583" anchor-label="Representation" id="-1954753889%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-representation/index.html"><span><span>Representation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1954753889%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">class </span><a href="-representation/index.html">Representation</a> : <a href="../-map-item-representation/index.html">MapItemRepresentation</a></div><div class="brief "><p class="paragraph">Base class to represent the visual appearance of a <a href="index.html">com.here.sdk.mapview.MapPolyline</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1920165996%2FClasslikes%2F1617540583" anchor-label="SolidMultiColorRepresentation" id="-1920165996%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-solid-multi-color-representation/index.html"><span>Solid</span><wbr></wbr><span>Multi</span><wbr></wbr><span>Color</span><wbr></wbr><span><span>Representation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1920165996%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-solid-multi-color-representation/index.html">SolidMultiColorRepresentation</a> : <a href="-representation/index.html">MapPolyline.Representation</a></div><div class="brief "><p class="paragraph">Representation allows map polyline to be colored in multiple specified color segments.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1071675106%2FClasslikes%2F1617540583" anchor-label="SolidRepresentation" id="-1071675106%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-solid-representation/index.html"><span>Solid</span><wbr></wbr><span><span>Representation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1071675106%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-solid-representation/index.html">SolidRepresentation</a> : <a href="-representation/index.html">MapPolyline.Representation</a></div><div class="brief "><p class="paragraph">Representation for a solid line without outline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="1844888761%2FProperties%2F1617540583" anchor-label="drawOrder" id="1844888761%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="draw-order.html"><span>draw</span><wbr></wbr><span><span>Order</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1844888761%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="draw-order.html">drawOrder</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The draw order of the polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1182694559%2FProperties%2F1617540583" anchor-label="drawOrderType" id="1182694559%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="draw-order-type.html"><span>draw</span><wbr></wbr><span>Order</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1182694559%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="draw-order-type.html">drawOrderType</a><span class="token operator">: </span><a href="../-draw-order-type/index.html">DrawOrderType</a></div><div class="brief "><p class="paragraph">The draw order type of the polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1116305573%2FProperties%2F1617540583" anchor-label="geometry" id="1116305573%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="geometry.html"><span><span>geometry</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1116305573%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="geometry.html">geometry</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-polyline/index.html">GeoPolyline</a></div><div class="brief "><p class="paragraph">The list of vertices that represent the geometry of the polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="835516266%2FProperties%2F1617540583" anchor-label="mapContentCategoriesToBlock" id="835516266%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="map-content-categories-to-block.html"><span>map</span><wbr></wbr><span>Content</span><wbr></wbr><span>Categories</span><wbr></wbr><span>To</span><wbr></wbr><span><span>Block</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="835516266%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="map-content-categories-to-block.html">mapContentCategoriesToBlock</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-map-content-category/index.html">MapContentCategory</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">List of map content categories this polyline should block.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-746937208%2FProperties%2F1617540583" anchor-label="metadata" id="-746937208%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="metadata.html"><span><span>metadata</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-746937208%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="metadata.html">metadata</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-metadata/index.html">Metadata</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The <code class="lang-kotlin">Metadata</code> instance attached to this polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1064396982%2FProperties%2F1617540583" anchor-label="progress" id="-1064396982%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="progress.html"><span><span>progress</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1064396982%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="progress.html">progress</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">The progress from the polyline's starting point, as a ratio of its total length clamped to the range \[0, 1\].</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1156758931%2FProperties%2F1617540583" anchor-label="progressColor" id="-1156758931%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="progress-color.html"><span>progress</span><wbr></wbr><span><span>Color</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1156758931%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="progress-color.html">progressColor</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-color/index.html">Color</a></div><div class="brief "><p class="paragraph">The color used for the progress part of the polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1791476468%2FProperties%2F1617540583" anchor-label="progressGradientLength" id="1791476468%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="progress-gradient-length.html"><span>progress</span><wbr></wbr><span>Gradient</span><wbr></wbr><span><span>Length</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1791476468%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="progress-gradient-length.html">progressGradientLength</a><span class="token operator">: </span><a href="../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a></div><div class="brief "><p class="paragraph">The maximum gradient length between <code class="lang-kotlin">MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1882277513%2FProperties%2F1617540583" anchor-label="progressOutlineColor" id="1882277513%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="progress-outline-color.html"><span>progress</span><wbr></wbr><span>Outline</span><wbr></wbr><span><span>Color</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1882277513%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="progress-outline-color.html">progressOutlineColor</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-color/index.html">Color</a></div><div class="brief "><p class="paragraph">The color used for outline of the progress part of the polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1038402383%2FProperties%2F1617540583" anchor-label="visibilityRanges" id="1038402383%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="visibility-ranges.html"><span>visibility</span><wbr></wbr><span><span>Ranges</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1038402383%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="visibility-ranges.html">visibilityRanges</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-map-measure-range/index.html">MapMeasureRange</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of visibility ranges. The map polyline is visible only inside these map measure ranges.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="669505362%2FFunctions%2F1617540583" anchor-label="cancelAnimation" id="669505362%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="cancel-animation.html"><span>cancel</span><wbr></wbr><span><span>Animation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="669505362%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="cancel-animation.html"><span class="token function">cancelAnimation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">animation<span class="token operator">: </span><a href="../../com.here.sdk.animation/-map-polyline-animation/index.html">MapPolylineAnimation</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Cancels single ongoing animation of this map polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-931536227%2FFunctions%2F1617540583" anchor-label="setRepresentation" id="-931536227%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-representation.html"><span>set</span><wbr></wbr><span><span>Representation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-931536227%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-representation.html"><span class="token function">setRepresentation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">representation<span class="token operator">: </span><a href="-representation/index.html">MapPolyline.Representation</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Changes the appearance of the <code class="lang-kotlin">MapPolyline</code> instance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1267796416%2FFunctions%2F1617540583" anchor-label="startAnimation" id="-1267796416%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="start-animation.html"><span>start</span><wbr></wbr><span><span>Animation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1267796416%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="start-animation.html"><span class="token function">startAnimation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">animation<span class="token operator">: </span><a href="../../com.here.sdk.animation/-map-polyline-animation/index.html">MapPolylineAnimation</a><span class="token punctuation">, </span></span><span class="parameter ">listener<span class="token operator">: </span><a href="../../com.here.sdk.animation/-animation-listener/index.html">AnimationListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Starts an animation of this map polyline.</p></div></div></div>
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
