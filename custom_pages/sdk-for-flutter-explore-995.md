---
title: "Companion"
slug: "sdk-for-flutter-explore"
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapFeatureModes.Companion///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">MapFeatureModes</a><span class="delimiter">/</span><span class="current">Companion</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Companion</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="1648134755%2FProperties%2F1617540583" anchor-label="AMBIENT_OCCLUSION_ALL" id="1648134755%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-a-m-b-i-e-n-t-o-c-c-l-u-s-i-o-n-a-l-l"><span>AMBIENT_</span><wbr></wbr><span>OCCLUSION_</span><wbr></wbr><span>ALL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1648134755%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-a-m-b-i-e-n-t-o-c-c-l-u-s-i-o-n-a-l-l">AMBIENT_OCCLUSION_ALL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Ambient occlusion effect is shown for extruded buildings and landmarks.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1670109654%2FProperties%2F1617540583" anchor-label="BUILDING_FOOTPRINTS_ALL" id="-1670109654%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-i-l-d-i-n-g-f-o-o-t-p-r-i-n-t-s-a-l-l"><span>BUILDING_</span><wbr></wbr><span>FOOTPRINTS_</span><wbr></wbr><span>ALL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1670109654%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-i-l-d-i-n-g-f-o-o-t-p-r-i-n-t-s-a-l-l">BUILDING_FOOTPRINTS_ALL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">All building footprints are shown.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1083366910%2FProperties%2F1617540583" anchor-label="CONGESTION_ZONES_ALL" id="1083366910%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-c-o-n-g-e-s-t-i-o-n-z-o-n-e-s-a-l-l"><span>CONGESTION_</span><wbr></wbr><span>ZONES_</span><wbr></wbr><span>ALL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1083366910%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-c-o-n-g-e-s-t-i-o-n-z-o-n-e-s-a-l-l">CONGESTION_ZONES_ALL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">All congestion zones are shown.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2123973898%2FProperties%2F1617540583" anchor-label="DEFAULT" id="2123973898%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-d-e-f-a-u-l-t"><span><span>DEFAULT</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2123973898%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-d-e-f-a-u-l-t">DEFAULT</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Enables the default mode of a map feature. Can be used with any map feature.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1282625347%2FProperties%2F1617540583" anchor-label="ENVIRONMENTAL_ZONES_ALL" id="1282625347%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-e-n-v-i-r-o-n-m-e-n-t-a-l-z-o-n-e-s-a-l-l"><span>ENVIRONMENTAL_</span><wbr></wbr><span>ZONES_</span><wbr></wbr><span>ALL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1282625347%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-e-n-v-i-r-o-n-m-e-n-t-a-l-z-o-n-e-s-a-l-l">ENVIRONMENTAL_ZONES_ALL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">All environmental zones are shown.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2078391886%2FProperties%2F1617540583" anchor-label="EXTRUDED_BUILDINGS_ALL" id="2078391886%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-e-x-t-r-u-d-e-d-b-u-i-l-d-i-n-g-s-a-l-l"><span>EXTRUDED_</span><wbr></wbr><span>BUILDINGS_</span><wbr></wbr><span>ALL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2078391886%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-e-x-t-r-u-d-e-d-b-u-i-l-d-i-n-g-s-a-l-l">EXTRUDED_BUILDINGS_ALL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">All extruded buildings are shown.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1575499653%2FProperties%2F1617540583" anchor-label="LOW_SPEED_ZONES_ALL" id="1575499653%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-l-o-w-s-p-e-e-d-z-o-n-e-s-a-l-l"><span>LOW_</span><wbr></wbr><span>SPEED_</span><wbr></wbr><span>ZONES_</span><wbr></wbr><span>ALL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1575499653%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-l-o-w-s-p-e-e-d-z-o-n-e-s-a-l-l">LOW_SPEED_ZONES_ALL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">All low speed zones are shown.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="589381548%2FProperties%2F1617540583" anchor-label="ROAD_EXIT_LABELS_ALL" id="589381548%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-r-o-a-d-e-x-i-t-l-a-b-e-l-s-a-l-l"><span>ROAD_</span><wbr></wbr><span>EXIT_</span><wbr></wbr><span>LABELS_</span><wbr></wbr><span>ALL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="589381548%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-r-o-a-d-e-x-i-t-l-a-b-e-l-s-a-l-l">ROAD_EXIT_LABELS_ALL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Road exit labels are shown with numbers and names, if available.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="597847532%2FProperties%2F1617540583" anchor-label="ROAD_EXIT_LABELS_NUMBERS_ONLY" id="597847532%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-r-o-a-d-e-x-i-t-l-a-b-e-l-s-n-u-m-b-e-r-s-o-n-l-y"><span>ROAD_</span><wbr></wbr><span>EXIT_</span><wbr></wbr><span>LABELS_</span><wbr></wbr><span>NUMBERS_</span><wbr></wbr><span>ONLY</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="597847532%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-r-o-a-d-e-x-i-t-l-a-b-e-l-s-n-u-m-b-e-r-s-o-n-l-y">ROAD_EXIT_LABELS_NUMBERS_ONLY</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Road exit labels are shown with numbers, if available.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="566592566%2FProperties%2F1617540583" anchor-label="SHADOWS_ALL" id="566592566%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-h-a-d-o-w-s-a-l-l"><span>SHADOWS_</span><wbr></wbr><span>ALL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="566592566%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-h-a-d-o-w-s-a-l-l">SHADOWS_ALL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Shadows are shown for extruded buildings and landmarks.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1568255699%2FProperties%2F1617540583" anchor-label="TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW" id="-1568255699%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-f-l-o-w-j-a-p-a-n-w-i-t-h-o-u-t-f-r-e-e-f-l-o-w"><span>TRAFFIC_</span><wbr></wbr><span>FLOW_</span><wbr></wbr><span>JAPAN_</span><wbr></wbr><span>WITHOUT_</span><wbr></wbr><span>FREE_</span><wbr></wbr><span>FLOW</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1568255699%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-f-l-o-w-j-a-p-a-n-w-i-t-h-o-u-t-f-r-e-e-f-l-o-w">TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Only available when Japan map is used.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1229611060%2FProperties%2F1617540583" anchor-label="TRAFFIC_FLOW_WITH_FREE_FLOW" id="1229611060%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-f-l-o-w-w-i-t-h-f-r-e-e-f-l-o-w"><span>TRAFFIC_</span><wbr></wbr><span>FLOW_</span><wbr></wbr><span>WITH_</span><wbr></wbr><span>FREE_</span><wbr></wbr><span>FLOW</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1229611060%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-f-l-o-w-w-i-t-h-f-r-e-e-f-l-o-w">TRAFFIC_FLOW_WITH_FREE_FLOW</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Traffic flow shows green lines when there is no traffic congestion.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1996051468%2FProperties%2F1617540583" anchor-label="TRAFFIC_FLOW_WITHOUT_FREE_FLOW" id="-1996051468%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-f-l-o-w-w-i-t-h-o-u-t-f-r-e-e-f-l-o-w"><span>TRAFFIC_</span><wbr></wbr><span>FLOW_</span><wbr></wbr><span>WITHOUT_</span><wbr></wbr><span>FREE_</span><wbr></wbr><span>FLOW</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1996051468%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-f-l-o-w-w-i-t-h-o-u-t-f-r-e-e-f-l-o-w">TRAFFIC_FLOW_WITHOUT_FREE_FLOW</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Traffic flow does not show green lines when there is no traffic congestion.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1215896694%2FProperties%2F1617540583" anchor-label="TRAFFIC_INCIDENTS_ALL" id="-1215896694%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-i-n-c-i-d-e-n-t-s-a-l-l"><span>TRAFFIC_</span><wbr></wbr><span>INCIDENTS_</span><wbr></wbr><span>ALL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1215896694%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-i-n-c-i-d-e-n-t-s-a-l-l">TRAFFIC_INCIDENTS_ALL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">All available traffic incidents are shown.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1482344910%2FProperties%2F1617540583" anchor-label="TRAFFIC_LIGHTS_ALL" id="1482344910%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-l-i-g-h-t-s-a-l-l"><span>TRAFFIC_</span><wbr></wbr><span>LIGHTS_</span><wbr></wbr><span>ALL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1482344910%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-t-r-a-f-f-i-c-l-i-g-h-t-s-a-l-l">TRAFFIC_LIGHTS_ALL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">All available traffic lights are shown.</p></div></div></div>
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
