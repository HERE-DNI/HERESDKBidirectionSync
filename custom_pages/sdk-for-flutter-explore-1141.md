---
title: "MapViewBase"
slug: "sdk-for-flutter-explore"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapViewBase</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapViewBase///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MapViewBase</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span>View</span><wbr></wbr><span><span>Base</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">MapViewBase</a></div><p class="paragraph">Represents the available public API from  <code class="lang-kotlin">MapView</code>.</p><h4 class="">Inheritors</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="sdk-for-flutter-explore-index">MapSurface</a></div></span></div><div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="sdk-for-flutter-explore-index">MapView</a></div></span></div><div></div></div></div></div></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="187770782%2FClasslikes%2F1617540583" anchor-label="MapPickCallback" id="187770782%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Map</span><wbr></wbr><span>Pick</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="187770782%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">MapPickCallback</a></div><div class="brief "><p class="paragraph">Callback for a pick request. In case of an error the result is not set.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-534831832%2FProperties%2F1617540583" anchor-label="camera" id="-534831832%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-camera"><span><span>camera</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-534831832%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="sdk-for-flutter-explore-camera">camera</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCamera</a></div><div class="brief "><p class="paragraph">The camera to control the view for the map.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2001882496%2FProperties%2F1617540583" anchor-label="frameRate" id="2001882496%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-frame-rate"><span>frame</span><wbr></wbr><span><span>Rate</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2001882496%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-frame-rate">frameRate</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">Maximum render frame rate in frames per second.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-146392157%2FProperties%2F1617540583" anchor-label="gestures" id="-146392157%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-gestures"><span><span>gestures</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-146392157%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="sdk-for-flutter-explore-gestures">gestures</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Gestures</a></div><div class="brief "><p class="paragraph">The gestures control object for setting up the capture of gestures.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1387176191%2FProperties%2F1617540583" anchor-label="hereMap" id="-1387176191%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-here-map"><span>here</span><wbr></wbr><span><span>Map</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1387176191%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="sdk-for-flutter-explore-here-map">hereMap</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">HereMap</a></div><div class="brief "><p class="paragraph">Here Map associated with this map view.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2143469595%2FProperties%2F1617540583" anchor-label="isValid" id="2143469595%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-valid"><span>is</span><wbr></wbr><span><span>Valid</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2143469595%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="sdk-for-flutter-explore-is-valid">isValid</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Indicates whether this instance is valid. It will be made invalid when the corresponding <code class="lang-kotlin">SDKNativeEngine</code> is destroyed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1268516006%2FProperties%2F1617540583" anchor-label="mapContext" id="-1268516006%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-map-context"><span>map</span><wbr></wbr><span><span>Context</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1268516006%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="sdk-for-flutter-explore-map-context">mapContext</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapContext</a></div><div class="brief "><p class="paragraph">Map context associated with this map view.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1012057629%2FProperties%2F1617540583" anchor-label="mapScene" id="1012057629%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-map-scene"><span>map</span><wbr></wbr><span><span>Scene</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1012057629%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="sdk-for-flutter-explore-map-scene">mapScene</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScene</a></div><div class="brief "><p class="paragraph">Map scene associated with this map view.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="956781257%2FProperties%2F1617540583" anchor-label="pixelScale" id="956781257%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-pixel-scale"><span>pixel</span><wbr></wbr><span><span>Scale</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="956781257%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="sdk-for-flutter-explore-pixel-scale">pixelScale</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">The pixel scale factor used by this <code class="lang-kotlin">MapView</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="886914246%2FProperties%2F1617540583" anchor-label="viewportSize" id="886914246%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-viewport-size"><span>viewport</span><wbr></wbr><span><span>Size</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="886914246%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="sdk-for-flutter-explore-viewport-size">viewportSize</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Size2D</a></div><div class="brief "><p class="paragraph">The size of this map view in physical pixels. If internally the map view's render surface is not attached yet (see: <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapViewLifecycleListener</a>), or after the map view has been destroyed then a <code class="lang-kotlin">Size2D</code> with zero width and height is returned.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2056298008%2FProperties%2F1617540583" anchor-label="watermarkSize" id="-2056298008%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-watermark-size"><span>watermark</span><wbr></wbr><span><span>Size</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2056298008%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="sdk-for-flutter-explore-watermark-size">watermarkSize</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Size2D</a></div><div class="brief "><p class="paragraph">Provides the size of the watermark in physical pixels.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1398677981%2FFunctions%2F1617540583" anchor-label="addLifecycleListener" id="-1398677981%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-lifecycle-listener"><span>add</span><wbr></wbr><span>Lifecycle</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1398677981%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-lifecycle-listener"><span class="token function">addLifecycleListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">lifecycleListener<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapViewLifecycleListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapViewLifecycleListener</a> to this map view. Adding the same object multiple times has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1003560143%2FFunctions%2F1617540583" anchor-label="geoToViewCoordinates" id="1003560143%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-geo-to-view-coordinates"><span>geo</span><wbr></wbr><span>To</span><wbr></wbr><span>View</span><wbr></wbr><span><span>Coordinates</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1003560143%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-geo-to-view-coordinates"><span class="token function">geoToViewCoordinates</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">geoCoordinates<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Converts geographical coordinates to view coordinates (in pixels).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="432243273%2FFunctions%2F1617540583" anchor-label="pick" id="432243273%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-pick"><span><span>pick</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="432243273%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-pick"><span class="token function">pick</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">filter<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapScene.MapPickFilter</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">viewArea<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Rectangle2D</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapViewBase.MapPickCallback</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Returns all map content located inside the specified pick area. Content to be picked is specified by a pick content filter. The pick area is defined by a rectangle in map view coordinates in pixels, relative to the map view's origin at (0, 0) which indicates the top-left corner of the map view.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-916534592%2FFunctions%2F1617540583" anchor-label="removeLifecycleListener" id="-916534592%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-lifecycle-listener"><span>remove</span><wbr></wbr><span>Lifecycle</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-916534592%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-lifecycle-listener"><span class="token function">removeLifecycleListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">lifecycleListener<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapViewLifecycleListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapViewLifecycleListener</a> from this map view. Trying to remove an object that was not added or was removed before has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1469869840%2FFunctions%2F1617540583" anchor-label="setWatermarkLocation" id="-1469869840%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-watermark-location"><span>set</span><wbr></wbr><span>Watermark</span><wbr></wbr><span><span>Location</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1469869840%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-watermark-location"><span class="token function">setWatermarkLocation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">anchor<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Anchor2D</a><span class="token punctuation">, </span></span><span class="parameter ">offset<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets the position of the HERE logo watermark within the map view.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1094076345%2FFunctions%2F1617540583" anchor-label="viewToGeoCoordinates" id="-1094076345%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-view-to-geo-coordinates"><span>view</span><wbr></wbr><span>To</span><wbr></wbr><span>Geo</span><wbr></wbr><span><span>Coordinates</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1094076345%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-view-to-geo-coordinates"><span class="token function">viewToGeoCoordinates</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">viewCoordinates<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Converts view coordinates (in pixels) to geographical coordinates.</p></div></div></div>
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
