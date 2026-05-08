---
title: "Companion"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>Companion</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapCameraUpdateFactory.Companion///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapCameraUpdateFactory</a><span class="delimiter">/</span><span class="current">Companion</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Companion</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-27497207%2FFunctions%2F1617540583" anchor-label="compositeUpdate" id="-27497207%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-composite-update"><span>composite</span><wbr></wbr><span><span>Update</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-27497207%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-composite-update"><span class="token function">compositeUpdate</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapCameraUpdates<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates a composite camera update from a list of camera updates. The result update will be equivalent to executing all given updates sequentially in the order they were provided.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1980750055%2FFunctions%2F1617540583" anchor-label="lookAt" id="1980750055%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-look-at"><span>look</span><wbr></wbr><span><span>At</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1980750055%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">target<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoBox</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to look at the given geo-box, preserving current orientation and zooming at the center of viewport.</p></div><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">target<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinatesUpdate</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to position the map camera to look at the given target, preserving the current orientation at look-at target and map measure.</p></div><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">target<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoBox</a><span class="token punctuation">, </span></span><span class="parameter ">viewRectangle<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Rectangle2D</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to look at the given geo-box and fit it inside the given rectangle, preserving current orientation and zooming at the center of view rectangle.</p></div><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">target<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinatesUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">orientation<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to position the map camera to look at the given target with the given orientation preserving the current map measure (zoom level/distance/scale) Any target or orientation sub-element value that is not finite will be excluded from the update.</p></div><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">target<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinatesUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">measure<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasure</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to position the map camera to look at the given target with the given map measure preserving the current orientation at look-at target. Any target sub-element value that is not finite will be excluded from the update. If the map measure is not valid, the current map camera distance to the target point is preserved.</p></div><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">target<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoBox</a><span class="token punctuation">, </span></span><span class="parameter ">orientation<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">viewRectangle<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Rectangle2D</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Create an update to look at the given geo-box and fit it inside the given rectangle.</p></div><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">target<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinatesUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">orientation<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">measure<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasure</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to position the map camera to look at the given target with the given orientation and map measure. Any target or orientation sub-element value that is not finite will be excluded from the update. If the map measure is not valid, the current map camera distance to the target point is preserved.</p></div><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">points<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">viewRectangle<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Rectangle2D</a><span class="token punctuation">, </span></span><span class="parameter ">orientation<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">measureLimit<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasure</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Create an update to look at the given geo locations and fit them inside the given rectangle, in accordance with a map measure limit.</p></div><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">target<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinatesUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">orientation<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">points<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token operator">&gt;</span><span class="token punctuation">, </span></span><span class="parameter ">viewRectangle<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Rectangle2D</a><span class="token punctuation">, </span></span><span class="parameter ">minMeasure<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasure</a><span class="token punctuation">, </span></span><span class="parameter ">maxMeasure<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasure</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to position the camera to look at the given target with the given orientation and obeying map measure limits, so that the given geo locations are inside the given rectangle. Such position update can possibly not be found.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1995101296%2FFunctions%2F1617540583" anchor-label="lookToMatch" id="-1995101296%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-look-to-match"><span>look</span><wbr></wbr><span>To</span><wbr></wbr><span><span>Match</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1995101296%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-to-match"><span class="token function">lookToMatch</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">geoPoint<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">viewPoint<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to position the map camera to look at the map with the given geo point located at the given view point. Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-to-match"><span class="token function">lookToMatch</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">geoPoint<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">viewPoint<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a><span class="token punctuation">, </span></span><span class="parameter ">orientation<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">measure<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasure</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to position the map camera to look at the map with the given orientation and map measure and with the given geo point located at the given view point.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-209855181%2FFunctions%2F1617540583" anchor-label="orbitBy" id="-209855181%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-orbit-by"><span>orbit</span><wbr></wbr><span><span>By</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-209855181%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-orbit-by"><span class="token function">orbitBy</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">delta<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">origin<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to orbit map camera around a pixel origin by specified geodetic orientation delta. If the origin cannot be converted to geo coordinates, no update will be applied to the map camera.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="92600546%2FFunctions%2F1617540583" anchor-label="panBy" id="92600546%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-pan-by"><span>pan</span><wbr></wbr><span><span>By</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="92600546%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-pan-by"><span class="token function">panBy</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">xOffset<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">yOffset<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to pan map camera over the map by the specified number of pixels in the x and y direction starting from current principal point position.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-640000677%2FFunctions%2F1617540583" anchor-label="rotateBy" id="-640000677%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-rotate-by"><span>rotate</span><wbr></wbr><span><span>By</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-640000677%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-rotate-by"><span class="token function">rotateBy</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">delta<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to change map camera orientation by specified geodetic orientation delta. Orientation elements that are not valid will be excluded from the update. Resulting bearing values are wrapped around degrees range \[0, 360\]. Resulting tilt values are clamped inside degrees range \[0, 180\]. Resulting roll values are wrapped around degrees range \[-180, 180\].</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="439480559%2FFunctions%2F1617540583" anchor-label="setNormalizedPrincipalPoint" id="439480559%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-normalized-principal-point"><span>set</span><wbr></wbr><span>Normalized</span><wbr></wbr><span>Principal</span><wbr></wbr><span><span>Point</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="439480559%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-normalized-principal-point"><span class="token function">setNormalizedPrincipalPoint</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">principalPoint<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Anchor2D</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to change the map camera's principal point (where the view vector intersects the image plane - default is (0.5, 0.5)). Point values are in normalized screen coordinates.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="867232435%2FFunctions%2F1617540583" anchor-label="setPrincipalPoint" id="867232435%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-principal-point"><span>set</span><wbr></wbr><span>Principal</span><wbr></wbr><span><span>Point</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="867232435%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-principal-point"><span class="token function">setPrincipalPoint</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">principalPoint<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to change the map camera's principal point (where the view vector intersects the image plane - default is the center of the view). Point values are in screen coordinates and values that fall outside of the viewport, are clamped. (0,0) is top left of the viewport.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="302890243%2FFunctions%2F1617540583" anchor-label="setVerticalFieldOfView" id="302890243%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-vertical-field-of-view"><span>set</span><wbr></wbr><span>Vertical</span><wbr></wbr><span>Field</span><wbr></wbr><span>Of</span><wbr></wbr><span><span>View</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="302890243%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-vertical-field-of-view"><span class="token function">setVerticalFieldOfView</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">verticalFieldOfView<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to change the vertical field of view of the map camera.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1793078362%2FFunctions%2F1617540583" anchor-label="zoomBy" id="1793078362%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-zoom-by"><span>zoom</span><wbr></wbr><span><span>By</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1793078362%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-zoom-by"><span class="token function">zoomBy</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">factor<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">origin<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to zoom map camera by a given factor preserving a given focus point.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1938106093%2FFunctions%2F1617540583" anchor-label="zoomTo" id="-1938106093%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-zoom-to"><span>zoom</span><wbr></wbr><span><span>To</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1938106093%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="token annotation builtin">JvmStatic</span></a></div></div><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-zoom-to"><span class="token function">zoomTo</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">zoomLevel<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></div><div class="brief "><p class="paragraph">Creates an update to move map camera's viewpoint to a particular zoom level by adjusting its position.</p></div></div></div>
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
