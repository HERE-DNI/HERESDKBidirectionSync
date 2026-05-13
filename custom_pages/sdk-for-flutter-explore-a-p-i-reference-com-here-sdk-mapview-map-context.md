---
title: "MapContext"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapContext</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapContext///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MapContext</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span><span>Context</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">MapContext</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">MapContext is the rendering engine and the context in which virtual geographic maps get rendered.</p><p class="paragraph">It runs the render loop or offers the means for the user to run a custom one.</p><p class="paragraph">Data sources, assets and virtual maps can be attached to the context. A virtual map can only render data from sources attached to the same context.</p><p class="paragraph">The graphics backend to be used by the engine can be choosen by the user or a platform suitable one can be automatically selected internally. Only one graphics backend can be active and once selected it cannot be changed.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-264068339%2FClasslikes%2F1617540583" anchor-label="Companion" id="-264068339%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-264068339%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1267443982%2FClasslikes%2F1617540583" anchor-label="FreeResourceSeverity" id="-1267443982%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-free-resource-severity/index.html"><span>Free</span><wbr></wbr><span>Resource</span><wbr></wbr><span><span>Severity</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1267443982%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-free-resource-severity/index.html">FreeResourceSeverity</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-free-resource-severity/index.html">MapContext.FreeResourceSeverity</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">The severity of a free resource request.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1779198463%2FClasslikes%2F1617540583" anchor-label="MemoryManagementOptions" id="1779198463%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-memory-management-options/index.html"><span>Memory</span><wbr></wbr><span>Management</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1779198463%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-memory-management-options/index.html">MemoryManagementOptions</a></div><div class="brief "><p class="paragraph">Memory management options.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1605183112%2FClasslikes%2F1617540583" anchor-label="MemoryManagementResult" id="1605183112%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-memory-management-result/index.html"><span>Memory</span><wbr></wbr><span>Management</span><wbr></wbr><span><span>Result</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1605183112%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-memory-management-result/index.html">MemoryManagementResult</a></div><div class="brief "><p class="paragraph">Memory management result.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2139257243%2FClasslikes%2F1617540583" anchor-label="MemoryManagementResultCode" id="2139257243%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-memory-management-result-code/index.html"><span>Memory</span><wbr></wbr><span>Management</span><wbr></wbr><span>Result</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2139257243%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-memory-management-result-code/index.html">MemoryManagementResultCode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-memory-management-result-code/index.html">MapContext.MemoryManagementResultCode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">The memory management result code.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1846899442%2FClasslikes%2F1617540583" anchor-label="MemoryManagementStrategy" id="1846899442%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-memory-management-strategy/index.html"><span>Memory</span><wbr></wbr><span>Management</span><wbr></wbr><span><span>Strategy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1846899442%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-memory-management-strategy/index.html">MemoryManagementStrategy</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-memory-management-strategy/index.html">MapContext.MemoryManagementStrategy</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">The memory management strategy. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2145310879%2FClasslikes%2F1617540583" anchor-label="ResourceType" id="-2145310879%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-resource-type/index.html"><span>Resource</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2145310879%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-resource-type/index.html">ResourceType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-resource-type/index.html">MapContext.ResourceType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Types of system resources used by <a href="index.html">com.here.sdk.mapview.MapContext</a> or any of the entities attached to it, like <a href="../-here-map/index.html">com.here.sdk.mapview.HereMap</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="367903724%2FClasslikes%2F1617540583" anchor-label="SetMemoryManagementOptionsCallback" id="367903724%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-set-memory-management-options-callback/index.html"><span>Set</span><wbr></wbr><span>Memory</span><wbr></wbr><span>Management</span><wbr></wbr><span>Options</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="367903724%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-set-memory-management-options-callback/index.html">SetMemoryManagementOptionsCallback</a></div><div class="brief "><p class="paragraph">Callback to handle the memory management result.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-734694986%2FFunctions%2F1617540583" anchor-label="freeResource" id="-734694986%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="free-resource.html"><span>free</span><wbr></wbr><span><span>Resource</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-734694986%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="free-resource.html"><span class="token function">freeResource</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">type<span class="token operator">: </span><a href="-resource-type/index.html">MapContext.ResourceType</a><span class="token punctuation">, </span></span><span class="parameter ">severity<span class="token operator">: </span><a href="-free-resource-severity/index.html">MapContext.FreeResourceSeverity</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Frees a system resource held by the <a href="index.html">com.here.sdk.mapview.MapContext</a> and all entities attached to it, like <a href="../-here-map/index.html">com.here.sdk.mapview.HereMap</a>. This function is intended for use when a system resource availability becomes low. For example, some memory can be freed when the application transitions to the background state.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="958183344%2FFunctions%2F1617540583" anchor-label="getMemoryManagementOptions" id="958183344%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-memory-management-options.html"><span>get</span><wbr></wbr><span>Memory</span><wbr></wbr><span>Management</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="958183344%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-memory-management-options.html"><span class="token function">getMemoryManagementOptions</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="-memory-management-options/index.html">MapContext.MemoryManagementOptions</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-948576577%2FFunctions%2F1617540583" anchor-label="setMemoryManagementOptions" id="-948576577%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-memory-management-options.html"><span>set</span><wbr></wbr><span>Memory</span><wbr></wbr><span>Management</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-948576577%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-memory-management-options.html"><span class="token function">setMemoryManagementOptions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">memoryManagementOptions<span class="token operator">: </span><a href="-memory-management-options/index.html">MapContext.MemoryManagementOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="-set-memory-management-options-callback/index.html">MapContext.SetMemoryManagementOptionsCallback</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets memory management options for controlling tile cache and video memory usage. In <a href="-memory-management-options/index.html">com.here.sdk.mapview.MapContext.MemoryManagementOptions</a> optional parameters with <code class="lang-kotlin">null</code> or non positive values will be ignored, preserving their existing settings.</p></div></div></div>
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
