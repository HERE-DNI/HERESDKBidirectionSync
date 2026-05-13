---
title: "MapSurface"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-surface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapSurface</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapSurface///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MapSurface</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span><span>Surface</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">class </span><a href="index.html">MapSurface</a> : <a href="../-map-view-base/index.html">MapViewBase</a></div><p class="paragraph">Provides the ability to render a map into a provided rendering surface. This enables the possibility to render a map into external displays like Android Auto. If you want to use the map for a regular use case please use the <a href="../-map-view/index.html">com.here.sdk.mapview.MapView</a> instead.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="1840272719%2FConstructors%2F1617540583" anchor-label="MapSurface" id="1840272719%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-surface.html"><span>Map</span><wbr></wbr><span><span>Surface</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1840272719%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief ">Creates a new instance.</div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">options<span class="token operator">: </span><a href="../-map-view-options/index.html">MapViewOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Creates a new instance.</div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">context<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Creates a new instance.</div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">context<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-map-view-options/index.html">MapViewOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Creates a new instance.</div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="2069071005%2FClasslikes%2F1617540583" anchor-label="RenderListener" id="2069071005%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-render-listener/index.html"><span>Render</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2069071005%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-render-listener/index.html">RenderListener</a></div><div class="brief ">Listener of MapSurface render events.</div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="1996445278%2FFunctions%2F1617540583" anchor-label="addLifecycleListener" id="1996445278%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-lifecycle-listener.html"><span>add</span><wbr></wbr><span>Lifecycle</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1996445278%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="add-lifecycle-listener.html"><span class="token function">addLifecycleListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>lifecycleListener<span class="token operator">: </span><a href="../-map-view-lifecycle-listener/index.html">MapViewLifecycleListener</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Adds a <a href="../-map-view-lifecycle-listener/index.html">com.here.sdk.mapview.MapViewLifecycleListener</a> to this map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1880809150%2FFunctions%2F1617540583" anchor-label="attachSurface" id="1880809150%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="attach-surface.html"><span>attach</span><wbr></wbr><span><span>Surface</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1880809150%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="attach-surface.html"><span class="token function">attachSurface</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">context<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a><span class="token punctuation">, </span></span><span class="parameter ">surface<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/view/Surface.html">Surface</a><span class="token punctuation">, </span></span><span class="parameter ">width<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">height<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span></div><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="attach-surface.html"><span class="token function">attachSurface</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">context<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a><span class="token punctuation">, </span></span><span class="parameter ">surface<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/view/Surface.html">Surface</a><span class="token punctuation">, </span></span><span class="parameter ">width<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">height<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>renderListener<span class="token operator">: </span><a href="-render-listener/index.html">MapSurface.RenderListener</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Sets the surface on which the map will be rendered.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="740609550%2FFunctions%2F1617540583" anchor-label="destroy" id="740609550%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="destroy.html"><span><span>destroy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="740609550%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="destroy.html"><span class="token function">destroy</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief ">Destroys the map renderer and render surface, making this <code class="lang-kotlin">MapSurface</code> invalid.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1133719647%2FFunctions%2F1617540583" anchor-label="destroySurface" id="1133719647%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="destroy-surface.html"><span>destroy</span><wbr></wbr><span><span>Surface</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1133719647%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="destroy-surface.html"><span class="token function">destroySurface</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief ">Destroys the rendering surface.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-621944652%2FFunctions%2F1617540583" anchor-label="geoToViewCoordinates" id="-621944652%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="geo-to-view-coordinates.html"><span>geo</span><wbr></wbr><span>To</span><wbr></wbr><span>View</span><wbr></wbr><span><span>Coordinates</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-621944652%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html"><span class="token annotation builtin">Nullable</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="geo-to-view-coordinates.html"><span class="token function">geoToViewCoordinates</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>geoCoordinates<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-coordinates/index.html">GeoCoordinates</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core/-point2-d/index.html">Point2D</a></div><div class="brief ">Converts geographical coordinates to view coordinates (in pixels).</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="394979405%2FFunctions%2F1617540583" anchor-label="getCamera" id="394979405%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-camera.html"><span>get</span><wbr></wbr><span><span>Camera</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="394979405%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="get-camera.html"><span class="token function">getCamera</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-map-camera/index.html">MapCamera</a></div><div class="brief ">Returns the camera control object for the map</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-530615237%2FFunctions%2F1617540583" anchor-label="getFrameRate" id="-530615237%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-frame-rate.html"><span>get</span><wbr></wbr><span>Frame</span><wbr></wbr><span><span>Rate</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-530615237%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="get-frame-rate.html"><span class="token function">getFrameRate</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief ">Gets maximum render frame rate in frames per second.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="49009032%2FFunctions%2F1617540583" anchor-label="getGestures" id="49009032%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-gestures.html"><span>get</span><wbr></wbr><span><span>Gestures</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="49009032%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="get-gestures.html"><span class="token function">getGestures</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.gestures/-gestures/index.html">Gestures</a></div><div class="brief ">Returns the gestures control object.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1667168380%2FFunctions%2F1617540583" anchor-label="getHereMap" id="1667168380%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-here-map.html"><span>get</span><wbr></wbr><span>Here</span><wbr></wbr><span><span>Map</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1667168380%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="get-here-map.html"><span class="token function">getHereMap</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-here-map/index.html">HereMap</a></div><div class="brief ">Gets the HereMap associated with this map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1828432895%2FFunctions%2F1617540583" anchor-label="getMapContext" id="1828432895%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-map-context.html"><span>get</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Context</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1828432895%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="get-map-context.html"><span class="token function">getMapContext</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-map-context/index.html">MapContext</a></div><div class="brief ">Gets the map context associated with this map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1207458818%2FFunctions%2F1617540583" anchor-label="getMapScene" id="1207458818%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-map-scene.html"><span>get</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Scene</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1207458818%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="get-map-scene.html"><span class="token function">getMapScene</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-map-scene/index.html">MapScene</a></div><div class="brief ">Gets the map scene associated with this map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-241237138%2FFunctions%2F1617540583" anchor-label="getPixelScale" id="-241237138%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-pixel-scale.html"><span>get</span><wbr></wbr><span>Pixel</span><wbr></wbr><span><span>Scale</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-241237138%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="get-pixel-scale.html"><span class="token function">getPixelScale</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief ">Gets the pixel scale factor used by this MapView.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2087597865%2FFunctions%2F1617540583" anchor-label="getShadowQuality" id="2087597865%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-shadow-quality.html"><span>get</span><wbr></wbr><span>Shadow</span><wbr></wbr><span><span>Quality</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2087597865%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="get-shadow-quality.html"><span class="token function">getShadowQuality</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-shadow-quality/index.html">ShadowQuality</a></div><div class="brief ">Gets the currently set shadow quality.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="642471979%2FFunctions%2F1617540583" anchor-label="getViewportSize" id="642471979%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-viewport-size.html"><span>get</span><wbr></wbr><span>Viewport</span><wbr></wbr><span><span>Size</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="642471979%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="get-viewport-size.html"><span class="token function">getViewportSize</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core/-size2-d/index.html">Size2D</a></div><div class="brief ">Returns the viewport size of this MapView in physical pixels.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1044073693%2FFunctions%2F1617540583" anchor-label="getWatermarkSize" id="-1044073693%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-watermark-size.html"><span>get</span><wbr></wbr><span>Watermark</span><wbr></wbr><span><span>Size</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1044073693%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="get-watermark-size.html"><span class="token function">getWatermarkSize</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core/-size2-d/index.html">Size2D</a></div><div class="brief ">Returns the watermark size in physical pixels.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1313654762%2FFunctions%2F1617540583" anchor-label="isValid" id="-1313654762%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-valid.html"><span>is</span><wbr></wbr><span><span>Valid</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1313654762%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="is-valid.html"><span class="token function">isValid</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief ">Returns whether this <code class="lang-kotlin">MapSurface</code> is valid.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="748291409%2FFunctions%2F1617540583" anchor-label="onPause" id="748291409%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-pause.html"><span>on</span><wbr></wbr><span><span>Pause</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="748291409%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="on-pause.html"><span class="token function">onPause</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief ">Call this method in the onPause() method of the lifecycle owner.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="808340134%2FFunctions%2F1617540583" anchor-label="onResume" id="808340134%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-resume.html"><span>on</span><wbr></wbr><span><span>Resume</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="808340134%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="on-resume.html"><span class="token function">onResume</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief ">Call this method in the onResume() method of the lifecycle owner.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-763952649%2FFunctions%2F1617540583" anchor-label="pick" id="-763952649%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="pick.html"><span><span>pick</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-763952649%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="pick.html"><span class="token function">pick</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html"><span class="token annotation builtin">Nullable</span></a> </span>filter<span class="token operator">: </span><a href="../-map-scene/-map-pick-filter/index.html">MapScene.MapPickFilter</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>viewArea<span class="token operator">: </span><a href="../../com.here.sdk.core/-rectangle2-d/index.html">Rectangle2D</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>callback<span class="token operator">: </span><a href="../-map-view-base/-map-pick-callback/index.html">MapViewBase.MapPickCallback</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Returns all map content located inside the specified pick area.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-26445526%2FFunctions%2F1617540583" anchor-label="redraw" id="-26445526%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="redraw.html"><span><span>redraw</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-26445526%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="redraw.html"><span class="token function">redraw</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">redrawFinished<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/lang/Runnable.html">Runnable</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Redraws the map and reports back on completion.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1015620773%2FFunctions%2F1617540583" anchor-label="removeLifecycleListener" id="1015620773%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-lifecycle-listener.html"><span>remove</span><wbr></wbr><span>Lifecycle</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1015620773%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="remove-lifecycle-listener.html"><span class="token function">removeLifecycleListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>lifecycleListener<span class="token operator">: </span><a href="../-map-view-lifecycle-listener/index.html">MapViewLifecycleListener</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Removes a <a href="../-map-view-lifecycle-listener/index.html">com.here.sdk.mapview.MapViewLifecycleListener</a> from this map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="152586572%2FFunctions%2F1617540583" anchor-label="setFrameRate" id="152586572%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-frame-rate.html"><span>set</span><wbr></wbr><span>Frame</span><wbr></wbr><span><span>Rate</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="152586572%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="set-frame-rate.html"><span class="token function">setFrameRate</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Sets maximum render frame rate in frames per second.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1490176797%2FFunctions%2F1617540583" anchor-label="setOnReadyListener" id="-1490176797%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-on-ready-listener.html"><span>set</span><wbr></wbr><span>On</span><wbr></wbr><span>Ready</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1490176797%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="set-on-ready-listener.html"><span class="token function">setOnReadyListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">readyListener<span class="token operator">: </span><a href="../-map-view/-on-ready-listener/index.html">MapView.OnReadyListener</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Sets the OnReadyListener, which will be notified once MapView initialization has been finished.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="412421704%2FFunctions%2F1617540583" anchor-label="setShadowQuality" id="412421704%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-shadow-quality.html"><span>set</span><wbr></wbr><span>Shadow</span><wbr></wbr><span><span>Quality</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="412421704%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="set-shadow-quality.html"><span class="token function">setShadowQuality</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">shadowQuality<span class="token operator">: </span><a href="../-shadow-quality/index.html">ShadowQuality</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Set desired shadow quality for all instances of MapSurface/MapView.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1767141461%2FFunctions%2F1617540583" anchor-label="setWatermarkLocation" id="1767141461%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-watermark-location.html"><span>set</span><wbr></wbr><span>Watermark</span><wbr></wbr><span><span>Location</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1767141461%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="set-watermark-location.html"><span class="token function">setWatermarkLocation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>anchor<span class="token operator">: </span><a href="../../com.here.sdk.core/-anchor2-d/index.html">Anchor2D</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>offset<span class="token operator">: </span><a href="../../com.here.sdk.core/-point2-d/index.html">Point2D</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Sets the position of the HERE logo watermark within the map view.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1970699628%2FFunctions%2F1617540583" anchor-label="takeScreenshot" id="1970699628%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="take-screenshot.html"><span>take</span><wbr></wbr><span><span>Screenshot</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1970699628%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="take-screenshot.html"><span class="token function">takeScreenshot</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">callback<span class="token operator">: </span><a href="../-map-view/-take-screenshot-callback/index.html">MapView.TakeScreenshotCallback</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Asynchronously retrieves screenshot of current map view</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2086970366%2FFunctions%2F1617540583" anchor-label="viewToGeoCoordinates" id="-2086970366%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="view-to-geo-coordinates.html"><span>view</span><wbr></wbr><span>To</span><wbr></wbr><span>Geo</span><wbr></wbr><span><span>Coordinates</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2086970366%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html"><span class="token annotation builtin">Nullable</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="view-to-geo-coordinates.html"><span class="token function">viewToGeoCoordinates</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>viewCoordinates<span class="token operator">: </span><a href="../../com.here.sdk.core/-point2-d/index.html">Point2D</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-coordinates/index.html">GeoCoordinates</a></div><div class="brief ">Converts view coordinates to geographical coordinates.</div></div></div>
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
