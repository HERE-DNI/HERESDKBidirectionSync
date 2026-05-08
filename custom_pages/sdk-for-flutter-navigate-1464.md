---
title: "SolidRepresentation"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>SolidRepresentation</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapPolyline.SolidRepresentation///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapPolyline</a><span class="delimiter">/</span><span class="current">SolidRepresentation</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Solid</span><wbr></wbr><span><span>Representation</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SolidRepresentation</a> : <a href="sdk-for-flutter-explore-index">MapPolyline.Representation</a></div><p class="paragraph">Representation for a solid line without outline.</p><p class="paragraph">Can represent polylines that have constant width or width dependent on the map zoom.</p><p class="paragraph">To achieve constant width lines, use <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasureDependentRenderSize</a> with a single value.</p><p class="paragraph">To achieve line width dependent on map zoom, use <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasureDependentRenderSize</a> with multiple values.</p><p class="paragraph">For <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasure.Kind</a> only <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL</a> is supported.</p><p class="paragraph">For <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit</a> only <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.RenderSize.Unit.PIXELS</a> is supported.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-627444297%2FConstructors%2F1617540583" anchor-label="SolidRepresentation" id="-627444297%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-solid-representation"><span>Solid</span><wbr></wbr><span><span>Representation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-627444297%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">lineWidth<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">color<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Color</a><span class="token punctuation">, </span></span><span class="parameter ">capShape<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LineCap</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a representation for a solid line without outline.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">lineWidth<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">color<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Color</a><span class="token punctuation">, </span></span><span class="parameter ">outlineWidth<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">outlineColor<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Color</a><span class="token punctuation">, </span></span><span class="parameter ">capShape<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LineCap</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a representation for a solid line with outline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1589106720%2FClasslikes%2F1617540583" anchor-label="Companion" id="1589106720%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1589106720%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="815027474%2FProperties%2F1617540583" anchor-label="capShape" id="815027474%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-cap-shape"><span>cap</span><wbr></wbr><span><span>Shape</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="815027474%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-cap-shape">capShape</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LineCap</a></div><div class="brief "><p class="paragraph">The cap shape applied to both ends of the polyline and its outline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1570878954%2FProperties%2F1617540583" anchor-label="lineColor" id="1570878954%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-line-color"><span>line</span><wbr></wbr><span><span>Color</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1570878954%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-line-color">lineColor</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Color</a></div><div class="brief "><p class="paragraph">The color of the polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-120611609%2FProperties%2F1617540583" anchor-label="lineWidth" id="-120611609%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-line-width"><span>line</span><wbr></wbr><span><span>Width</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-120611609%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-line-width">lineWidth</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasureDependentRenderSize</a></div><div class="brief "><p class="paragraph">The width of the polyline depending on the map measure. At map measures smaller than smallest map measure in the <code class="lang-kotlin">lineWidth</code> line width is constant and equal to the width given for the smallest map measure in the <code class="lang-kotlin">lineWidth</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1676224000%2FProperties%2F1617540583" anchor-label="outlineColor" id="1676224000%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-outline-color"><span>outline</span><wbr></wbr><span><span>Color</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1676224000%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-outline-color">outlineColor</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Color</a></div><div class="brief "><p class="paragraph">The outline color of the polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-15266563%2FProperties%2F1617540583" anchor-label="outlineWidth" id="-15266563%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-outline-width"><span>outline</span><wbr></wbr><span><span>Width</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-15266563%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-outline-width">outlineWidth</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasureDependentRenderSize</a></div><div class="brief "><p class="paragraph">The width of the outline on one side of the polyline depending on the map measure. The total width of the polyline is <code class="lang-kotlin">line width + 2 * outline width</code>.</p></div></div></div>
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
