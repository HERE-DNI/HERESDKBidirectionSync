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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.search/PlaceCategory.Companion///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.search</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">PlaceCategory</a><span class="delimiter">/</span><span class="current">Companion</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Companion</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="1414813241%2FProperties%2F1617540583" anchor-label="ACCOMMODATION" id="1414813241%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-a-c-c-o-m-m-o-d-a-t-i-o-n"><span><span>ACCOMMODATION</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1414813241%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-a-c-c-o-m-m-o-d-a-t-i-o-n">ACCOMMODATION</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Top level category for places offering lodging accommodations, dwellings or similar living quarters to travellers, such as hotels, motels, resorts, cruise ships and campgrounds.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-132772822%2FProperties%2F1617540583" anchor-label="ACCOMMODATION_HOTEL_MOTEL" id="-132772822%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-a-c-c-o-m-m-o-d-a-t-i-o-n-h-o-t-e-l-m-o-t-e-l"><span>ACCOMMODATION_</span><wbr></wbr><span>HOTEL_</span><wbr></wbr><span>MOTEL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-132772822%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-a-c-c-o-m-m-o-d-a-t-i-o-n-h-o-t-e-l-m-o-t-e-l">ACCOMMODATION_HOTEL_MOTEL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A business that provides lodging or temporary living quarters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1551489372%2FProperties%2F1617540583" anchor-label="ACCOMMODATION_LODGING" id="1551489372%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-a-c-c-o-m-m-o-d-a-t-i-o-n-l-o-d-g-i-n-g"><span>ACCOMMODATION_</span><wbr></wbr><span>LODGING</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1551489372%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-a-c-c-o-m-m-o-d-a-t-i-o-n-l-o-d-g-i-n-g">ACCOMMODATION_LODGING</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A business that provides lodging to the public generally without room service.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="392662253%2FProperties%2F1617540583" anchor-label="AREAS_AND_BUILDINGS" id="392662253%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-a-r-e-a-s-a-n-d-b-u-i-l-d-i-n-g-s"><span>AREAS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>BUILDINGS</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="392662253%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-a-r-e-a-s-a-n-d-b-u-i-l-d-i-n-g-s">AREAS_AND_BUILDINGS</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Top level category for places that are owned, operated or managed by municipalities, such as cities, towns, villages, boroughs and shires.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2006522815%2FProperties%2F1617540583" anchor-label="AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX" id="2006522815%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-a-r-e-a-s-a-n-d-b-u-i-l-d-i-n-g-s-o-u-t-d-o-o-r-c-o-m-p-l-e-x"><span>AREAS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>BUILDINGS_</span><wbr></wbr><span>OUTDOOR_</span><wbr></wbr><span>COMPLEX</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2006522815%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-a-r-e-a-s-a-n-d-b-u-i-l-d-i-n-g-s-o-u-t-d-o-o-r-c-o-m-p-l-e-x">AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Outdoor areas or complexes with designations for specific businesses or interests.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-750056308%2FProperties%2F1617540583" anchor-label="AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE" id="-750056308%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-a-r-e-a-s-a-n-d-b-u-i-l-d-i-n-g-s-r-e-s-i-d-e-n-t-a-l-o-f-f-i-c-e"><span>AREAS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>BUILDINGS_</span><wbr></wbr><span>RESIDENTAL_</span><wbr></wbr><span>OFFICE</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-750056308%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-a-r-e-a-s-a-n-d-b-u-i-l-d-i-n-g-s-r-e-s-i-d-e-n-t-a-l-o-f-f-i-c-e">AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Areas and buildings designated for residential or office use.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-957018013%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_COMMERCIAL_SERVICES" id="-957018013%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-c-o-m-m-e-r-c-i-a-l-s-e-r-v-i-c-e-s"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>COMMERCIAL_</span><wbr></wbr><span>SERVICES</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-957018013%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-c-o-m-m-e-r-c-i-a-l-s-e-r-v-i-c-e-s">BUSINESS_AND_COMMERCIAL_SERVICES</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Businesses that provide a service or product for use by other businesses.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="376904783%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_CONSUMER_SERVICES" id="376904783%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-c-o-n-s-u-m-e-r-s-e-r-v-i-c-e-s"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>CONSUMER_</span><wbr></wbr><span>SERVICES</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="376904783%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-c-o-n-s-u-m-e-r-s-e-r-v-i-c-e-s">BUSINESS_AND_CONSUMER_SERVICES</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">An organization that provides consumer services for a variety of products for used by the public.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-785875002%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES" id="-785875002%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-785875002%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s">BUSINESS_AND_SERVICES</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Top level category for places that provide professional services to other businesses, such as printing, photocopying, graphic design, marketing, advertising and other general business services.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1668710933%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_ATM" id="-1668710933%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-a-t-m"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>ATM</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1668710933%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-a-t-m">BUSINESS_AND_SERVICES_ATM</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A computer terminal that allows bank customers to deposit, withdraw, or transfer funds without the assistance of a bank teller.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1708721697%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_BANKING" id="-1708721697%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-b-a-n-k-i-n-g"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>BANKING</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1708721697%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-b-a-n-k-i-n-g">BUSINESS_AND_SERVICES_BANKING</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Businesses that specialize in the maintenance, lending, exchange, or issuance of money.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1270528132%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_CAR_DEALER_SALES" id="1270528132%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-c-a-r-d-e-a-l-e-r-s-a-l-e-s"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>CAR_</span><wbr></wbr><span>DEALER_</span><wbr></wbr><span>SALES</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1270528132%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-c-a-r-d-e-a-l-e-r-s-a-l-e-s">BUSINESS_AND_SERVICES_CAR_DEALER_SALES</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Businesses that sell new automobiles and motorcycles.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="843663910%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_CAR_RENTAL" id="843663910%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-c-a-r-r-e-n-t-a-l"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>CAR_</span><wbr></wbr><span>RENTAL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="843663910%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-c-a-r-r-e-n-t-a-l">BUSINESS_AND_SERVICES_CAR_RENTAL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Businesses that rent or lease automobiles.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1571145600%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES" id="-1571145600%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-c-a-r-r-e-p-a-i-r-s-e-r-v-i-c-e-s"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>CAR_</span><wbr></wbr><span>REPAIR_</span><wbr></wbr><span>SERVICES</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1571145600%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-c-a-r-r-e-p-a-i-r-s-e-r-v-i-c-e-s">BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Businesses that provide automotive repair services.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1900065398%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA" id="-1900065398%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-c-o-m-m-u-n-i-c-a-t-i-o-n-m-e-d-i-a"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>COMMUNICATION_</span><wbr></wbr><span>MEDIA</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1900065398%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-c-o-m-m-u-n-i-c-a-t-i-o-n-m-e-d-i-a">BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Businesses that provide communication services.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1608545937%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_EV_CHARGING_STATION" id="1608545937%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-e-v-c-h-a-r-g-i-n-g-s-t-a-t-i-o-n"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>EV_</span><wbr></wbr><span>CHARGING_</span><wbr></wbr><span>STATION</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1608545937%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-e-v-c-h-a-r-g-i-n-g-s-t-a-t-i-o-n">BUSINESS_AND_SERVICES_EV_CHARGING_STATION</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Businesses that provide recharging services for electric vehicles.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1630702556%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_FUELING_STATION" id="-1630702556%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-f-u-e-l-i-n-g-s-t-a-t-i-o-n"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>FUELING_</span><wbr></wbr><span>STATION</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1630702556%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-f-u-e-l-i-n-g-s-t-a-t-i-o-n">BUSINESS_AND_SERVICES_FUELING_STATION</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Businesses that sell fuel for vehicles, such as petrol, electricity etc.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="562171191%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_INDUSTRY" id="562171191%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-i-n-d-u-s-t-r-y"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>INDUSTRY</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="562171191%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-i-n-d-u-s-t-r-y">BUSINESS_AND_SERVICES_INDUSTRY</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Businesses that employ people in and around the city in which it is located.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1065713629%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_MONEY_CASH" id="-1065713629%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-m-o-n-e-y-c-a-s-h"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>MONEY_</span><wbr></wbr><span>CASH</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1065713629%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-m-o-n-e-y-c-a-s-h">BUSINESS_AND_SERVICES_MONEY_CASH</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Businesses that provide money related services.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1765946199%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION" id="1765946199%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-p-e-t-r-o-l-g-a-s-o-l-i-n-e-s-t-a-t-i-o-n"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>PETROL_</span><wbr></wbr><span>GASOLINE_</span><wbr></wbr><span>STATION</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1765946199%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-p-e-t-r-o-l-g-a-s-o-l-i-n-e-s-t-a-t-i-o-n">BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Businesses that sell fuel, oil, and other motoring supplies.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-227084964%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY" id="-227084964%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-p-o-l-i-c-e-f-i-r-e-e-m-e-r-g-e-n-c-y"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>POLICE_</span><wbr></wbr><span>FIRE_</span><wbr></wbr><span>EMERGENCY</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-227084964%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-p-o-l-i-c-e-f-i-r-e-e-m-e-r-g-e-n-c-y">BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Municipal emergency services.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1905202250%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_POST_OFFICE" id="1905202250%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-p-o-s-t-o-f-f-i-c-e"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>POST_</span><wbr></wbr><span>OFFICE</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1905202250%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-p-o-s-t-o-f-f-i-c-e">BUSINESS_AND_SERVICES_POST_OFFICE</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">An office or station that receives, sorts, dispatches and delivers mail to a specific area or region.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1489383590%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_TOURIST_INFORMATION" id="1489383590%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-t-o-u-r-i-s-t-i-n-f-o-r-m-a-t-i-o-n"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>TOURIST_</span><wbr></wbr><span><span>INFORMATION</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1489383590%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-t-o-u-r-i-s-t-i-n-f-o-r-m-a-t-i-o-n">BUSINESS_AND_SERVICES_TOURIST_INFORMATION</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Businesses that provide a variety of information for visiting tourists, such as event schedules, lodging/accommodations, restaurants, attractions and more.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="548494427%2FProperties%2F1617540583" anchor-label="BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER" id="548494427%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-t-r-u-c-k-s-e-m-i-d-e-a-l-e-r"><span>BUSINESS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>SERVICES_</span><wbr></wbr><span>TRUCK_</span><wbr></wbr><span>SEMI_</span><wbr></wbr><span>DEALER</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="548494427%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-t-r-u-c-k-s-e-m-i-d-e-a-l-e-r">BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Business that sell or service trucks and tractor trailers.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1131148962%2FProperties%2F1617540583" anchor-label="EAT_AND_DRINK" id="1131148962%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-e-a-t-a-n-d-d-r-i-n-k"><span>EAT_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>DRINK</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1131148962%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-e-a-t-a-n-d-d-r-i-n-k">EAT_AND_DRINK</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Top level category for places where food or beverages are prepared or served.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-346189668%2FProperties%2F1617540583" anchor-label="EAT_AND_DRINK_COFFEE_TEA" id="-346189668%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-e-a-t-a-n-d-d-r-i-n-k-c-o-f-f-e-e-t-e-a"><span>EAT_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>DRINK_</span><wbr></wbr><span>COFFEE_</span><wbr></wbr><span>TEA</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-346189668%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-e-a-t-a-n-d-d-r-i-n-k-c-o-f-f-e-e-t-e-a">EAT_AND_DRINK_COFFEE_TEA</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">An establishment that sells drinks, such as coffee and tea, as well as refreshments.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1257988700%2FProperties%2F1617540583" anchor-label="EAT_AND_DRINK_RESTAURANT" id="1257988700%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-e-a-t-a-n-d-d-r-i-n-k-r-e-s-t-a-u-r-a-n-t"><span>EAT_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>DRINK_</span><wbr></wbr><span>RESTAURANT</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1257988700%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-e-a-t-a-n-d-d-r-i-n-k-r-e-s-t-a-u-r-a-n-t">EAT_AND_DRINK_RESTAURANT</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">An establishment that prepares and serves refreshments and prepared meals.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="992047278%2FProperties%2F1617540583" anchor-label="FACILITIES" id="992047278%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s"><span><span>FACILITIES</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="992047278%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s">FACILITIES</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Top level category for places associated with specialized facilities, such as sports venues, government buildings, health care centers and other types of facilities.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-977112699%2FProperties%2F1617540583" anchor-label="FACILITIES_EDUCATION" id="-977112699%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-e-d-u-c-a-t-i-o-n"><span>FACILITIES_</span><wbr></wbr><span>EDUCATION</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-977112699%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-e-d-u-c-a-t-i-o-n">FACILITIES_EDUCATION</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Facilities that are used for educational purposes including training, coaching, universities and more.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="927728667%2FProperties%2F1617540583" anchor-label="FACILITIES_EVENT_SPACES" id="927728667%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-e-v-e-n-t-s-p-a-c-e-s"><span>FACILITIES_</span><wbr></wbr><span>EVENT_</span><wbr></wbr><span>SPACES</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="927728667%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-e-v-e-n-t-s-p-a-c-e-s">FACILITIES_EVENT_SPACES</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">An area or facility used for the hosting of fairs and conventions.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1726147914%2FProperties%2F1617540583" anchor-label="FACILITIES_GOVERNMENT_COMMUNITTY" id="1726147914%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-g-o-v-e-r-n-m-e-n-t-c-o-m-m-u-n-i-t-t-y"><span>FACILITIES_</span><wbr></wbr><span>GOVERNMENT_</span><wbr></wbr><span>COMMUNITTY</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1726147914%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-g-o-v-e-r-n-m-e-n-t-c-o-m-m-u-n-i-t-t-y">FACILITIES_GOVERNMENT_COMMUNITTY</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A Place where government services are provided.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-391353925%2FProperties%2F1617540583" anchor-label="FACILITIES_HOSPITAL_HEALTHCARE" id="-391353925%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-h-o-s-p-i-t-a-l-h-e-a-l-t-h-c-a-r-e"><span>FACILITIES_</span><wbr></wbr><span>HOSPITAL_</span><wbr></wbr><span>HEALTHCARE</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-391353925%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-h-o-s-p-i-t-a-l-h-e-a-l-t-h-c-a-r-e">FACILITIES_HOSPITAL_HEALTHCARE</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Facilities that include dental offices, hospitals, nursing homes and other health care-related services.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1535617070%2FProperties%2F1617540583" anchor-label="FACILITIES_LIBRARY" id="-1535617070%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-l-i-b-r-a-r-y"><span>FACILITIES_</span><wbr></wbr><span>LIBRARY</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1535617070%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-l-i-b-r-a-r-y">FACILITIES_LIBRARY</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Facilities that offer books, periodicals, audio, video and other material for public use.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-277303523%2FProperties%2F1617540583" anchor-label="FACILITIES_OTHER" id="-277303523%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-o-t-h-e-r"><span>FACILITIES_</span><wbr></wbr><span>OTHER</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-277303523%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-o-t-h-e-r">FACILITIES_OTHER</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Facilities with miscellaneous uses such as Clubhouses, Offices, and Registration Offices.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2020954251%2FProperties%2F1617540583" anchor-label="FACILITIES_PARKING" id="-2020954251%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-p-a-r-k-i-n-g"><span>FACILITIES_</span><wbr></wbr><span>PARKING</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2020954251%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-p-a-r-k-i-n-g">FACILITIES_PARKING</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Area or building used for parking cars.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="423593081%2FProperties%2F1617540583" anchor-label="FACILITIES_SCHOOL" id="423593081%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-s-c-h-o-o-l"><span>FACILITIES_</span><wbr></wbr><span>SCHOOL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="423593081%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-s-c-h-o-o-l">FACILITIES_SCHOOL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Educational facilities that include primary schools, secondary schools and more.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1903513822%2FProperties%2F1617540583" anchor-label="FACILITIES_VENUE_SPORTS" id="1903513822%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-v-e-n-u-e-s-p-o-r-t-s"><span>FACILITIES_</span><wbr></wbr><span>VENUE_</span><wbr></wbr><span>SPORTS</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1903513822%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-f-a-c-i-l-i-t-i-e-s-v-e-n-u-e-s-p-o-r-t-s">FACILITIES_VENUE_SPORTS</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A facility used for individual and team sports including recreational sports.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1477136440%2FProperties%2F1617540583" anchor-label="GOING_OUT_CINEMA" id="-1477136440%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-g-o-i-n-g-o-u-t-c-i-n-e-m-a"><span>GOING_</span><wbr></wbr><span>OUT_</span><wbr></wbr><span>CINEMA</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1477136440%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-g-o-i-n-g-o-u-t-c-i-n-e-m-a">GOING_OUT_CINEMA</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">An establishment that shows movies through screen projection.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="59387897%2FProperties%2F1617540583" anchor-label="GOING_OUT_ENTERTAINMENT" id="59387897%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-g-o-i-n-g-o-u-t-e-n-t-e-r-t-a-i-n-m-e-n-t"><span>GOING_</span><wbr></wbr><span>OUT_</span><wbr></wbr><span><span>ENTERTAINMENT</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="59387897%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-g-o-i-n-g-o-u-t-e-n-t-e-r-t-a-i-n-m-e-n-t">GOING_OUT_ENTERTAINMENT</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Top level category for places commonly associated with entertainment, such as bars, cinemas, theatres, casinos and night clubs.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-632255094%2FProperties%2F1617540583" anchor-label="GOING_OUT_GAMBLING_LOTTERY_BETTING" id="-632255094%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-g-o-i-n-g-o-u-t-g-a-m-b-l-i-n-g-l-o-t-t-e-r-y-b-e-t-t-i-n-g"><span>GOING_</span><wbr></wbr><span>OUT_</span><wbr></wbr><span>GAMBLING_</span><wbr></wbr><span>LOTTERY_</span><wbr></wbr><span>BETTING</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-632255094%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-g-o-i-n-g-o-u-t-g-a-m-b-l-i-n-g-l-o-t-t-e-r-y-b-e-t-t-i-n-g">GOING_OUT_GAMBLING_LOTTERY_BETTING</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">An establishment that provides gambling entertainment.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1482340333%2FProperties%2F1617540583" anchor-label="GOING_OUT_NIGHTLIFE" id="1482340333%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-g-o-i-n-g-o-u-t-n-i-g-h-t-l-i-f-e"><span>GOING_</span><wbr></wbr><span>OUT_</span><wbr></wbr><span>NIGHTLIFE</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1482340333%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-g-o-i-n-g-o-u-t-n-i-g-h-t-l-i-f-e">GOING_OUT_NIGHTLIFE</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">An establishment that provides evening entertainment and usually serves alcoholic beverages.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1792307371%2FProperties%2F1617540583" anchor-label="GOING_OUT_THEATRE_MUSIC_CULTURE" id="-1792307371%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-g-o-i-n-g-o-u-t-t-h-e-a-t-r-e-m-u-s-i-c-c-u-l-t-u-r-e"><span>GOING_</span><wbr></wbr><span>OUT_</span><wbr></wbr><span>THEATRE_</span><wbr></wbr><span>MUSIC_</span><wbr></wbr><span>CULTURE</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1792307371%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-g-o-i-n-g-o-u-t-t-h-e-a-t-r-e-m-u-s-i-c-c-u-l-t-u-r-e">GOING_OUT_THEATRE_MUSIC_CULTURE</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">An establishment where various types of performing arts are presented.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="927638225%2FProperties%2F1617540583" anchor-label="LEISURE_AND_OUTDOOR" id="927638225%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-l-e-i-s-u-r-e-a-n-d-o-u-t-d-o-o-r"><span>LEISURE_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>OUTDOOR</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="927638225%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-l-e-i-s-u-r-e-a-n-d-o-u-t-d-o-o-r">LEISURE_AND_OUTDOOR</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Top level category for places that are designated for sports, recreation, parking, beaches and other leisure and outdoor activities.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="583628469%2FProperties%2F1617540583" anchor-label="LEISURE_OTHER" id="583628469%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-l-e-i-s-u-r-e-o-t-h-e-r"><span>LEISURE_</span><wbr></wbr><span>OTHER</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="583628469%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-l-e-i-s-u-r-e-o-t-h-e-r">LEISURE_OTHER</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A park that contains rides and/or other entertainment which may be based on a central theme.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-707930080%2FProperties%2F1617540583" anchor-label="LEISURE_OUTDOOR_RECREATION" id="-707930080%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-l-e-i-s-u-r-e-o-u-t-d-o-o-r-r-e-c-r-e-a-t-i-o-n"><span>LEISURE_</span><wbr></wbr><span>OUTDOOR_</span><wbr></wbr><span>RECREATION</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-707930080%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-l-e-i-s-u-r-e-o-u-t-d-o-o-r-r-e-c-r-e-a-t-i-o-n">LEISURE_OUTDOOR_RECREATION</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Public land preserved and maintained for recreational use.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1308883119%2FProperties%2F1617540583" anchor-label="NATURAL_AND_GEOGRAPHICAL" id="1308883119%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-n-a-t-u-r-a-l-a-n-d-g-e-o-g-r-a-p-h-i-c-a-l"><span>NATURAL_</span><wbr></wbr><span>AND_</span><wbr></wbr><span><span>GEOGRAPHICAL</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1308883119%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-n-a-t-u-r-a-l-a-n-d-g-e-o-g-r-a-p-h-i-c-a-l">NATURAL_AND_GEOGRAPHICAL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Top level category for natural or man-made areas of regional importance, such as bodies of water, mountains, forested areas and other geographic areas.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="769125698%2FProperties%2F1617540583" anchor-label="NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER" id="769125698%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-n-a-t-u-r-a-l-a-n-d-g-e-o-g-r-a-p-h-i-c-a-l-b-o-d-y-o-f-w-a-t-e-r"><span>NATURAL_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>GEOGRAPHICAL_</span><wbr></wbr><span>BODY_</span><wbr></wbr><span>OF_</span><wbr></wbr><span>WATER</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="769125698%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-n-a-t-u-r-a-l-a-n-d-g-e-o-g-r-a-p-h-i-c-a-l-b-o-d-y-o-f-w-a-t-e-r">NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A natural and geographical feature of the earth's surface that is covered with water, such as a lake, river, stream or ocean.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1518029806%2FProperties%2F1617540583" anchor-label="NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION" id="1518029806%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-n-a-t-u-r-a-l-a-n-d-g-e-o-g-r-a-p-h-i-c-a-l-f-o-r-e-s-t-h-e-a-l-t-h-o-t-h-e-r-v-e-g-e-t-a-t-i-o-n"><span>NATURAL_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>GEOGRAPHICAL_</span><wbr></wbr><span>FOREST_</span><wbr></wbr><span>HEALTH_</span><wbr></wbr><span>OTHER_</span><wbr></wbr><span>VEGETATION</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1518029806%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-n-a-t-u-r-a-l-a-n-d-g-e-o-g-r-a-p-h-i-c-a-l-f-o-r-e-s-t-h-e-a-l-t-h-o-t-h-e-r-v-e-g-e-t-a-t-i-o-n">NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A dense growth of trees, open uncultivated land or other large masses of vegetation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1184290433%2FProperties%2F1617540583" anchor-label="NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL" id="1184290433%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-n-a-t-u-r-a-l-a-n-d-g-e-o-g-r-a-p-h-i-c-a-l-m-o-u-n-t-a-i-n-o-r-h-i-l-l"><span>NATURAL_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>GEOGRAPHICAL_</span><wbr></wbr><span>MOUNTAIN_</span><wbr></wbr><span>OR_</span><wbr></wbr><span>HILL</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1184290433%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-n-a-t-u-r-a-l-a-n-d-g-e-o-g-r-a-p-h-i-c-a-l-m-o-u-n-t-a-i-n-o-r-h-i-l-l">NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A natural and geographical feature that is higher than the surrounding land.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1429959262%2FProperties%2F1617540583" anchor-label="NATURAL_AND_GEOGRAPHICAL_OTHER" id="1429959262%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-n-a-t-u-r-a-l-a-n-d-g-e-o-g-r-a-p-h-i-c-a-l-o-t-h-e-r"><span>NATURAL_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>GEOGRAPHICAL_</span><wbr></wbr><span>OTHER</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1429959262%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-n-a-t-u-r-a-l-a-n-d-g-e-o-g-r-a-p-h-i-c-a-l-o-t-h-e-r">NATURAL_AND_GEOGRAPHICAL_OTHER</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A feature not classified as a Body of Water, Mountain or Hill, Undersea Feature, or Forest, Heath or Other Vegetation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1969508926%2FProperties%2F1617540583" anchor-label="NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE" id="1969508926%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-n-a-t-u-r-a-l-a-n-d-g-e-o-g-r-a-p-h-i-c-a-l-u-n-d-e-r-s-e-a-f-e-a-t-u-r-e"><span>NATURAL_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>GEOGRAPHICAL_</span><wbr></wbr><span>UNDERSEA_</span><wbr></wbr><span>FEATURE</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1969508926%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-n-a-t-u-r-a-l-a-n-d-g-e-o-g-r-a-p-h-i-c-a-l-u-n-d-e-r-s-e-a-f-e-a-t-u-r-e">NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A natural or artificial feature that is below sea level.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-982856665%2FProperties%2F1617540583" anchor-label="SHOPPING" id="-982856665%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g"><span><span>SHOPPING</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-982856665%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g">SHOPPING</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Top level category for places where consumer goods are commonly sold, such as clothing stores, grocery stores, hardware stores and other types of shopping centers.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-405628978%2FProperties%2F1617540583" anchor-label="SHOPPING_BOOKSTORE" id="-405628978%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-b-o-o-k-s-t-o-r-e"><span>SHOPPING_</span><wbr></wbr><span>BOOKSTORE</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-405628978%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-b-o-o-k-s-t-o-r-e">SHOPPING_BOOKSTORE</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A business that sells books, magazines and other reading material.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1769965214%2FProperties%2F1617540583" anchor-label="SHOPPING_CLOTHING_AND_ACCESORIES" id="-1769965214%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-c-l-o-t-h-i-n-g-a-n-d-a-c-c-e-s-o-r-i-e-s"><span>SHOPPING_</span><wbr></wbr><span>CLOTHING_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>ACCESORIES</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1769965214%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-c-l-o-t-h-i-n-g-a-n-d-a-c-c-e-s-o-r-i-e-s">SHOPPING_CLOTHING_AND_ACCESORIES</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A business that sells apparel items, garments or fashion accessories for men, women, and children.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-989895737%2FProperties%2F1617540583" anchor-label="SHOPPING_CONSUMER_GOODS" id="-989895737%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-c-o-n-s-u-m-e-r-g-o-o-d-s"><span>SHOPPING_</span><wbr></wbr><span>CONSUMER_</span><wbr></wbr><span>GOODS</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-989895737%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-c-o-n-s-u-m-e-r-g-o-o-d-s">SHOPPING_CONSUMER_GOODS</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A business that sells a variety of products targeted to consumers.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2009174285%2FProperties%2F1617540583" anchor-label="SHOPPING_CONVENIENCE_STORE" id="2009174285%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-c-o-n-v-e-n-i-e-n-c-e-s-t-o-r-e"><span>SHOPPING_</span><wbr></wbr><span>CONVENIENCE_</span><wbr></wbr><span>STORE</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2009174285%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-c-o-n-v-e-n-i-e-n-c-e-s-t-o-r-e">SHOPPING_CONVENIENCE_STORE</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">An establishment that sells groceries, candy, toiletries, soft drinks, tobacco products, newspapers and other products.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="373765120%2FProperties%2F1617540583" anchor-label="SHOPPING_DEPARTMENT_STORE" id="373765120%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-d-e-p-a-r-t-m-e-n-t-s-t-o-r-e"><span>SHOPPING_</span><wbr></wbr><span>DEPARTMENT_</span><wbr></wbr><span>STORE</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="373765120%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-d-e-p-a-r-t-m-e-n-t-s-t-o-r-e">SHOPPING_DEPARTMENT_STORE</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A business that sells a wide variety of merchandise that is organized by product or service departments.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="182165603%2FProperties%2F1617540583" anchor-label="SHOPPING_DRUGSTORE_PHARMACY" id="182165603%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-d-r-u-g-s-t-o-r-e-p-h-a-r-m-a-c-y"><span>SHOPPING_</span><wbr></wbr><span>DRUGSTORE_</span><wbr></wbr><span>PHARMACY</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="182165603%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-d-r-u-g-s-t-o-r-e-p-h-a-r-m-a-c-y">SHOPPING_DRUGSTORE_PHARMACY</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A business that sells medications, toiletry items and other retail cosmetics.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1093552271%2FProperties%2F1617540583" anchor-label="SHOPPING_ELECTRONICS" id="1093552271%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-e-l-e-c-t-r-o-n-i-c-s"><span>SHOPPING_</span><wbr></wbr><span><span>ELECTRONICS</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1093552271%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-e-l-e-c-t-r-o-n-i-c-s">SHOPPING_ELECTRONICS</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A business that sells consumer electronics and electronic entertainment equipment.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2008693147%2FProperties%2F1617540583" anchor-label="SHOPPING_FOOD_AND_DRINK" id="-2008693147%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-f-o-o-d-a-n-d-d-r-i-n-k"><span>SHOPPING_</span><wbr></wbr><span>FOOD_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>DRINK</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2008693147%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-f-o-o-d-a-n-d-d-r-i-n-k">SHOPPING_FOOD_AND_DRINK</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A business that sells specialty products of a particular type of food or beverage.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1168333861%2FProperties%2F1617540583" anchor-label="SHOPPING_HAIR_AND_BEAUTY" id="1168333861%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-h-a-i-r-a-n-d-b-e-a-u-t-y"><span>SHOPPING_</span><wbr></wbr><span>HAIR_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>BEAUTY</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1168333861%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-h-a-i-r-a-n-d-b-e-a-u-t-y">SHOPPING_HAIR_AND_BEAUTY</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A business that provides hair styling and personal appearance services. Places in this category may also sell hair products and other related cosmetic items.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1011525669%2FProperties%2F1617540583" anchor-label="SHOPPING_HARDWARE_HOUSE_GARDEN" id="-1011525669%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-h-a-r-d-w-a-r-e-h-o-u-s-e-g-a-r-d-e-n"><span>SHOPPING_</span><wbr></wbr><span>HARDWARE_</span><wbr></wbr><span>HOUSE_</span><wbr></wbr><span>GARDEN</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1011525669%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-h-a-r-d-w-a-r-e-h-o-u-s-e-g-a-r-d-e-n">SHOPPING_HARDWARE_HOUSE_GARDEN</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A business that sells crafts, gardening, remodeling, or decorating items for the home.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2021998385%2FProperties%2F1617540583" anchor-label="SHOPPING_MALL_COMPLEX" id="-2021998385%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-m-a-l-l-c-o-m-p-l-e-x"><span>SHOPPING_</span><wbr></wbr><span>MALL_</span><wbr></wbr><span>COMPLEX</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2021998385%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-h-o-p-p-i-n-g-m-a-l-l-c-o-m-p-l-e-x">SHOPPING_MALL_COMPLEX</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A complex of businesses that are co-located and share common services.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-809401761%2FProperties%2F1617540583" anchor-label="SIGHTS_AND_MUSEUMS" id="-809401761%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-i-g-h-t-s-a-n-d-m-u-s-e-u-m-s"><span>SIGHTS_</span><wbr></wbr><span>AND_</span><wbr></wbr><span>MUSEUMS</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-809401761%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-i-g-h-t-s-a-n-d-m-u-s-e-u-m-s">SIGHTS_AND_MUSEUMS</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Top level category for places of special interest, such as common tourist attractions, museums and places of worship.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1774628906%2FProperties%2F1617540583" anchor-label="SIGHTS_LANDMARK_ATTRACTION" id="1774628906%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-i-g-h-t-s-l-a-n-d-m-a-r-k-a-t-t-r-a-c-t-i-o-n"><span>SIGHTS_</span><wbr></wbr><span>LANDMARK_</span><wbr></wbr><span>ATTRACTION</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1774628906%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-i-g-h-t-s-l-a-n-d-m-a-r-k-a-t-t-r-a-c-t-i-o-n">SIGHTS_LANDMARK_ATTRACTION</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A designated area of special interest to tourists.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-130533744%2FProperties%2F1617540583" anchor-label="SIGHTS_MUSEUM" id="-130533744%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-i-g-h-t-s-m-u-s-e-u-m"><span>SIGHTS_</span><wbr></wbr><span>MUSEUM</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-130533744%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-i-g-h-t-s-m-u-s-e-u-m">SIGHTS_MUSEUM</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">An establishment dedicated to the preservation and exhibition of artistic, historical, or scientific artifacts.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1299195819%2FProperties%2F1617540583" anchor-label="SIGHTS_RELIGIOUS_PLACE" id="-1299195819%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-i-g-h-t-s-r-e-l-i-g-i-o-u-s-p-l-a-c-e"><span>SIGHTS_</span><wbr></wbr><span>RELIGIOUS_</span><wbr></wbr><span>PLACE</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1299195819%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-s-i-g-h-t-s-r-e-l-i-g-i-o-u-s-p-l-a-c-e">SIGHTS_RELIGIOUS_PLACE</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">An establishment special religious significance or where religious services are held.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="563273282%2FProperties%2F1617540583" anchor-label="TRANSPORT" id="563273282%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-t-r-a-n-s-p-o-r-t"><span><span>TRANSPORT</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="563273282%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-t-r-a-n-s-p-o-r-t">TRANSPORT</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Top level category for places commonly associated with pedestrian and cargo transport facilities, including airports, rail yards and seaports.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1694821206%2FProperties%2F1617540583" anchor-label="TRANSPORT_AIRPORT" id="1694821206%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-t-r-a-n-s-p-o-r-t-a-i-r-p-o-r-t"><span>TRANSPORT_</span><wbr></wbr><span>AIRPORT</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1694821206%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-t-r-a-n-s-p-o-r-t-a-i-r-p-o-r-t">TRANSPORT_AIRPORT</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A designated area that serves various aspects of aviation related sports, including gliders, recreational aircraft and model airplanes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-709292411%2FProperties%2F1617540583" anchor-label="TRANSPORT_CARGO" id="-709292411%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-t-r-a-n-s-p-o-r-t-c-a-r-g-o"><span>TRANSPORT_</span><wbr></wbr><span>CARGO</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-709292411%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-t-r-a-n-s-p-o-r-t-c-a-r-g-o">TRANSPORT_CARGO</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A facility that handles some aspect of the transportation of cargo freight.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-897294576%2FProperties%2F1617540583" anchor-label="TRANSPORT_PUBLIC" id="-897294576%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-t-r-a-n-s-p-o-r-t-p-u-b-l-i-c"><span>TRANSPORT_</span><wbr></wbr><span>PUBLIC</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-897294576%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-t-r-a-n-s-p-o-r-t-p-u-b-l-i-c">TRANSPORT_PUBLIC</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A facility for travelers who are travelling between stops on public transport.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1740374647%2FProperties%2F1617540583" anchor-label="TRANSPORT_REST_AREA" id="-1740374647%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-t-r-a-n-s-p-o-r-t-r-e-s-t-a-r-e-a"><span>TRANSPORT_</span><wbr></wbr><span>REST_</span><wbr></wbr><span>AREA</span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1740374647%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-t-r-a-n-s-p-o-r-t-r-e-s-t-a-r-e-a">TRANSPORT_REST_AREA</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">An establishment along a motorway (controlled access road) that provides restrooms and parking.</p></div></div></div>
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
