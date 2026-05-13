---
title: "SolidMultiColorRepresentation"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapview-map-polyline-solid-multi-color-representation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>SolidMultiColorRepresentation</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapPolyline.SolidMultiColorRepresentation///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="../index.html">MapPolyline</a><span class="delimiter">/</span><span class="current">SolidMultiColorRepresentation</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Solid</span><wbr></wbr><span>Multi</span><wbr></wbr><span>Color</span><wbr></wbr><span><span>Representation</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">SolidMultiColorRepresentation</a> : <a href="../-representation/index.html">MapPolyline.Representation</a></div><p class="paragraph">Representation allows map polyline to be colored in multiple specified color segments.</p><p class="paragraph">Color segment is defined by color stops. Color stop is specified as a polyline length ratio (0.0 - start of the polyline, 1.0 - end of the polyline). Color stop represents a color change starting at that exact point up until either the next color stop (if one exists) or the end of the polyline.</p><p class="paragraph">Progress color <code class="lang-kotlin">MapPolyline.progressColor</code> overrides any of the multiple color.</p><p class="paragraph">Examples: The following configuration will color map polyline as follows:</p><ul><li><p class="paragraph">from the start to the middle of it at the 0.5 point - in Red</p></li><li><p class="paragraph">from the middle point 0.5 to the 0.7 point - in Green</p></li><li><p class="paragraph">from 0.7 to 1.0 - in Red 'colorStops: {0.0, 0.5, 0.7}, colorIndices: {0, 1, 0}, colors: {Red, Green}'</p></li></ul><p class="paragraph">Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="2073598289%2FConstructors%2F1617540583" anchor-label="SolidMultiColorRepresentation" id="2073598289%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-solid-multi-color-representation.html"><span>Solid</span><wbr></wbr><span>Multi</span><wbr></wbr><span>Color</span><wbr></wbr><span><span>Representation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2073598289%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">lineWidth<span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">capShape<span class="token operator">: </span><a href="../../-line-cap/index.html">LineCap</a><span class="token punctuation">, </span></span><span class="parameter ">colorStops<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">colorIndices<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">colors<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../../../com.here.sdk.core/-color/index.html">Color</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">gradientLength<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a representation for a multicolored line without an outline.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">lineWidth<span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">outlineWidth<span class="token operator">: </span><a href="../../-map-measure-dependent-render-size/index.html">MapMeasureDependentRenderSize</a><span class="token punctuation">, </span></span><span class="parameter ">outlineColor<span class="token operator">: </span><a href="../../../com.here.sdk.core/-color/index.html">Color</a><span class="token punctuation">, </span></span><span class="parameter ">capShape<span class="token operator">: </span><a href="../../-line-cap/index.html">LineCap</a><span class="token punctuation">, </span></span><span class="parameter ">colorStops<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">colorIndices<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">colors<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../../../com.here.sdk.core/-color/index.html">Color</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">gradientLength<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a representation for a multicolored line with an outline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="722848534%2FClasslikes%2F1617540583" anchor-label="Companion" id="722848534%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="722848534%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="1678778327%2FFunctions%2F1617540583" anchor-label="setMultiColorGradientLength" id="1678778327%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-multi-color-gradient-length.html"><span>set</span><wbr></wbr><span>Multi</span><wbr></wbr><span>Color</span><wbr></wbr><span>Gradient</span><wbr></wbr><span><span>Length</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1678778327%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-multi-color-gradient-length.html"><span class="token function">setMultiColorGradientLength</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">length<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Sets the multiple color segment gradient length.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2098660190%2FFunctions%2F1617540583" anchor-label="setMultiColors" id="2098660190%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-multi-colors.html"><span>set</span><wbr></wbr><span>Multi</span><wbr></wbr><span><span>Colors</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2098660190%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-multi-colors.html"><span class="token function">setMultiColors</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">colorStops<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">colorIndices<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">colors<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../../../com.here.sdk.core/-color/index.html">Color</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Sets lists of colors and multiple color segment stops for the polyline to be colored in. When this representation is already set on any <code class="lang-kotlin">MapPolyline</code>, values will be applied on that <code class="lang-kotlin">MapPolyline</code> right away. If this representation is not set on any <code class="lang-kotlin">MapPolyline</code>, values will be applied once representation is set on a <code class="lang-kotlin">MapPolyline</code>.</p></div></div></div>
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
