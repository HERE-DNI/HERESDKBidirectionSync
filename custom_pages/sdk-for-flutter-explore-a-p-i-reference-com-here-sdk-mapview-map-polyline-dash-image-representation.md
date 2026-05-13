---
title: "DashImageRepresentation"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>DashImageRepresentation</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapPolyline.DashImageRepresentation///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="../index.html">MapPolyline</a><span class="delimiter">/</span><span class="current">DashImageRepresentation</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Dash</span><wbr></wbr><span>Image</span><wbr></wbr><span><span>Representation</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">DashImageRepresentation</a> : <a href="../-representation/index.html">MapPolyline.Representation</a></div><p class="paragraph">Represents a dash pattern for the map polyline consisting of images rendered with certain gaps from each other.</p><p class="paragraph">This dash pattern representation consists only of images rendered at certain points along the polyline. For rendering them without any distortions, polyline gets sliced into series of straight segments that are multiple of sum of dash and gap lengths. For this reason, the new polyline geometry might not align fully with original geometry.</p><p class="paragraph">The <a href="dash-image.html">com.here.sdk.mapview.MapPolyline.DashImageRepresentation.dashImage</a> is stretched according to <a href="dash-length.html">com.here.sdk.mapview.MapPolyline.DashImageRepresentation.dashLength</a> and <a href="dash-width.html">com.here.sdk.mapview.MapPolyline.DashImageRepresentation.dashWidth</a>, with image's width matched to <code class="lang-kotlin">dashLength</code> and image's height matched to <code class="lang-kotlin">dashWidth</code>. The image is oriented so that its bottom is on the left-hand side between vertices <code class="lang-kotlin">n</code> and <code class="lang-kotlin">n+1</code>.</p><p class="paragraph">The spacing between images is specified by <a href="gap-length.html">com.here.sdk.mapview.MapPolyline.DashImageRepresentation.gapLength</a>.</p><p class="paragraph">Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-1126388875%2FConstructors%2F1617540583" anchor-label="DashImageRepresentation" id="-1126388875%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-dash-image-representation.html"><span>Dash</span><wbr></wbr><span>Image</span><wbr></wbr><span><span>Representation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1126388875%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">dashLength<span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">dashWidth<span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">image<span class="token operator">: </span><a href="../../-map-image/index.html">MapImage</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a uniform dash pattern in which the length of a gap is the same as the length of a dash. Dashes are rendered as image.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">dashLength<span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">gapLength<span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">dashWidth<span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">image<span class="token operator">: </span><a href="../../-map-image/index.html">MapImage</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a simple dash pattern in which the lengths of a dash and gap can be different. Dashes are rendered as image.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="856701730%2FClasslikes%2F1617540583" anchor-label="Companion" id="856701730%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="856701730%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="-1211572974%2FProperties%2F1617540583" anchor-label="dashImage" id="-1211572974%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="dash-image.html"><span>dash</span><wbr></wbr><span><span>Image</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1211572974%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="dash-image.html">dashImage</a><span class="token operator">: </span><a href="../../-map-image/index.html">MapImage</a></div><div class="brief "><p class="paragraph">Image to be rendered in place of dash space. It is stretched to fill whole polyline width and length of each dash.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="947579719%2FProperties%2F1617540583" anchor-label="dashLength" id="947579719%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="dash-length.html"><span>dash</span><wbr></wbr><span><span>Length</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="947579719%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="dash-length.html">dashLength</a><span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a></div><div class="brief "><p class="paragraph">The map measure dependent length of a dash, to which image width is stretched.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-585656569%2FProperties%2F1617540583" anchor-label="dashWidth" id="-585656569%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="dash-width.html"><span>dash</span><wbr></wbr><span><span>Width</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-585656569%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="dash-width.html">dashWidth</a><span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a></div><div class="brief "><p class="paragraph">The map measure dependent width of a dash, to which image height is stretched.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1558457343%2FProperties%2F1617540583" anchor-label="gapLength" id="1558457343%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="gap-length.html"><span>gap</span><wbr></wbr><span><span>Length</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1558457343%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="gap-length.html">gapLength</a><span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a></div><div class="brief "><p class="paragraph">The map measure dependent length of a gap between dash images.</p></div></div></div>
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
