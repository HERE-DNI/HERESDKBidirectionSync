---
title: "DataAttributesAccessor"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-datasource-data-attributes-accessor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>DataAttributesAccessor</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview.datasource/DataAttributesAccessor///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview.datasource</a><span class="delimiter">/</span><span class="current">DataAttributesAccessor</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Data</span><wbr></wbr><span>Attributes</span><wbr></wbr><span><span>Accessor</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">DataAttributesAccessor</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a>, <a href="../-data-attributes-base/index.html">DataAttributesBase</a></div><p class="paragraph">Accessor used for manipulating data attributes.</p><p class="paragraph">Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-972761197%2FClasslikes%2F1617540583" anchor-label="Companion" id="-972761197%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-972761197%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="1914439527%2FFunctions%2F1617540583" anchor-label="addOrReplace" id="1914439527%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-or-replace.html"><span>add</span><wbr></wbr><span>Or</span><wbr></wbr><span><span>Replace</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1914439527%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-or-replace.html"><span class="token function">addOrReplace</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">value<span class="token operator">: </span><a href="../../com.here.sdk.core/-color/index.html">Color</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds or replaces a color attribute.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-or-replace.html"><span class="token function">addOrReplace</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">value<span class="token operator">: </span><a href="../-data-attribute-value/index.html">DataAttributeValue</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds or replaces an attribute.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-or-replace.html"><span class="token function">addOrReplace</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds or replaces a boolean attribute.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-or-replace.html"><span class="token function">addOrReplace</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds or replaces a double precision floating decimal attribute.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-or-replace.html"><span class="token function">addOrReplace</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds or replaces a single precision floating decimal attribute.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-or-replace.html"><span class="token function">addOrReplace</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds or replaces a 64-bits integer attribute.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-or-replace.html"><span class="token function">addOrReplace</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds or replaces a string attribute.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="168334225%2FFunctions%2F1617540583" anchor-label="getAsString" id="168334225%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-as-string.html"><span>get</span><wbr></wbr><span>As</span><wbr></wbr><span><span>String</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="168334225%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="get-as-string.html"><span class="token function">getAsString</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Gets the value of an attribute as a string or <code class="lang-kotlin">null</code> if it is not contained.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="880132746%2FFunctions%2F1617540583" anchor-label="getAttributeNames" id="880132746%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-attribute-names.html"><span>get</span><wbr></wbr><span>Attribute</span><wbr></wbr><span><span>Names</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="880132746%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="get-attribute-names.html"><span class="token function">getAttributeNames</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns a list of attribute names.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1653442344%2FFunctions%2F1617540583" anchor-label="getBoolean" id="1653442344%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-boolean.html"><span>get</span><wbr></wbr><span><span>Boolean</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1653442344%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="get-boolean.html"><span class="token function">getBoolean</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Gets the value of a boolean attribute or <code class="lang-kotlin">null</code> if it is not contained or the type doesn't match.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-888277057%2FFunctions%2F1617540583" anchor-label="getDouble" id="-888277057%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-double.html"><span>get</span><wbr></wbr><span><span>Double</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-888277057%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="get-double.html"><span class="token function">getDouble</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Gets the value of a double precision floating decimal attribute or <code class="lang-kotlin">null</code> if it is not contained or the type doesn't match.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="748243100%2FFunctions%2F1617540583" anchor-label="getFloat" id="748243100%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-float.html"><span>get</span><wbr></wbr><span><span>Float</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="748243100%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="get-float.html"><span class="token function">getFloat</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Gets the value of a single precision floating decimal attribute or <code class="lang-kotlin">null</code> if it is not contained or the type doesn't match.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-939290515%2FFunctions%2F1617540583" anchor-label="getInt64" id="-939290515%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-int64.html"><span>get</span><wbr></wbr><span><span>Int64</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-939290515%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="get-int64.html"><span class="token function">getInt64</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Gets the value of a 64-bits integer attribute or <code class="lang-kotlin">null</code> if it is not contained or the type doesn't match.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1281446913%2FFunctions%2F1617540583" anchor-label="getString" id="-1281446913%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-string.html"><span>get</span><wbr></wbr><span><span>String</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1281446913%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="get-string.html"><span class="token function">getString</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Gets the value of a string attribute or <code class="lang-kotlin">null</code> if it is not contained or the type doesn't match.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1866547215%2FFunctions%2F1617540583" anchor-label="getValue" id="-1866547215%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-value.html"><span>get</span><wbr></wbr><span><span>Value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1866547215%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="get-value.html"><span class="token function">getValue</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-data-attribute-value/index.html">DataAttributeValue</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Gets the DataAttributeValue or <code class="lang-kotlin">null</code> if it is not contained.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1038574901%2FFunctions%2F1617540583" anchor-label="getValueType" id="-1038574901%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-value-type.html"><span>get</span><wbr></wbr><span>Value</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1038574901%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="get-value-type.html"><span class="token function">getValueType</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-data-attribute-value/-value-type/index.html">DataAttributeValue.ValueType</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns the value type of an attribute or <code class="lang-kotlin">null</code> if it is not contained.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1351525958%2FFunctions%2F1617540583" anchor-label="remove" id="-1351525958%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove.html"><span><span>remove</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1351525958%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove.html"><span class="token function">remove</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">name<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes an attribute by name.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-531246481%2FFunctions%2F1617540583" anchor-label="removeAll" id="-531246481%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-all.html"><span>remove</span><wbr></wbr><span><span>All</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-531246481%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove-all.html"><span class="token function">removeAll</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes all attributes.</p></div></div></div>
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
