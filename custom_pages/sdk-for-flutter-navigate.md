---
title: "API Reference"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>API Reference</title>
    <link href="images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "";</script>
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
<script type="text/javascript" src="scripts/sourceset_dependencies.js" async="async"></script>
<link href="styles/style.css" rel="Stylesheet">
<link href="styles/main.css" rel="Stylesheet">
<link href="styles/prism.css" rel="Stylesheet">
<link href="styles/logo-styles.css" rel="Stylesheet">
<link href="styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="scripts/prism.js" async="async"></script>
<script type="text/javascript" src="ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
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
<div class="main-content" id="content" pageIds="API Reference::////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"></div>
  <div class="cover ">
    <h1 class="cover"><span><span>API</span></span> <span><span>Reference</span></span></h1>
    <div class="platform-hinted UnderCoverText" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><p class="paragraph">Browse the latest API Reference for the HERE SDK for Android - Kotlin (Navigate), Version 4.26.0.0.278965 Release.</p><p class="paragraph">For the terms and conditions covering this documentation, see the <a href="https://legal.here.com/en-gb/terms/documentation-license">HERE Documentation License</a>.</p><h2 class="">More Documentation Resources</h2><p class="paragraph">Be sure to check out our <i>User Guide</i> including a <i>Get Started</i> tutorial that shows how to integrate the HERE SDK into your own apps with a few simple steps.</p><h2 class="">Get in Touch</h2><p class="paragraph">We love feedback. Please <a href="https://www.here.com/contact">contact us</a> for any questions, suggestions or improvements. Thank you for using the HERE SDK.</p></div></div>
  </div>
  <h2 class="">Packages</h2>
  <div class="table"><a data-name="-406919457%2FPackages%2F1617540583" anchor-label="com.here" id="-406919457%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-406919457%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="455030529%2FPackages%2F1617540583" anchor-label="com.here.sdk.animation" id="455030529%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.animation</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="455030529%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="1714731846%2FPackages%2F1617540583" anchor-label="com.here.sdk.core" id="1714731846%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.core</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1714731846%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-1330294290%2FPackages%2F1617540583" anchor-label="com.here.sdk.core.engine" id="-1330294290%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1330294290%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-380226089%2FPackages%2F1617540583" anchor-label="com.here.sdk.core.errors" id="-380226089%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.core.errors</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-380226089%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="1152923376%2FPackages%2F1617540583" anchor-label="com.here.sdk.core.threading" id="1152923376%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.core.threading</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1152923376%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="1413072988%2FPackages%2F1617540583" anchor-label="com.here.sdk.electronichorizon" id="1413072988%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.electronichorizon</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1413072988%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="1305371369%2FPackages%2F1617540583" anchor-label="com.here.sdk.engine" id="1305371369%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.engine</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1305371369%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-1645862120%2FPackages%2F1617540583" anchor-label="com.here.sdk.ev" id="-1645862120%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.ev</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1645862120%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="991641009%2FPackages%2F1617540583" anchor-label="com.here.sdk.gestures" id="991641009%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.gestures</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="991641009%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="469094748%2FPackages%2F1617540583" anchor-label="com.here.sdk.location" id="469094748%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.location</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="469094748%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-611414333%2FPackages%2F1617540583" anchor-label="com.here.sdk.mapdata" id="-611414333%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.mapdata</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-611414333%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-2116690900%2FPackages%2F1617540583" anchor-label="com.here.sdk.maploader" id="-2116690900%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.maploader</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2116690900%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-442192188%2FPackages%2F1617540583" anchor-label="com.here.sdk.maploader.remote.connection" id="-442192188%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.maploader.remote.connection</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-442192188%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="263057789%2FPackages%2F1617540583" anchor-label="com.here.sdk.mapmatcher" id="263057789%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.mapmatcher</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="263057789%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="48875006%2FPackages%2F1617540583" anchor-label="com.here.sdk.mapview" id="48875006%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="48875006%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="27285369%2FPackages%2F1617540583" anchor-label="com.here.sdk.mapview.datasource" id="27285369%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.datasource</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="27285369%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="1456784827%2FPackages%2F1617540583" anchor-label="com.here.sdk.navigation" id="1456784827%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.navigation</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1456784827%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="1347273867%2FPackages%2F1617540583" anchor-label="com.here.sdk.prefetcher" id="1347273867%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.prefetcher</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1347273867%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="876525699%2FPackages%2F1617540583" anchor-label="com.here.sdk.routing" id="876525699%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.routing</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="876525699%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-956450097%2FPackages%2F1617540583" anchor-label="com.here.sdk.search" id="-956450097%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.search</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-956450097%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="127193850%2FPackages%2F1617540583" anchor-label="com.here.sdk.traffic" id="127193850%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.traffic</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="127193850%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="486139964%2FPackages%2F1617540583" anchor-label="com.here.sdk.trafficawarenavigation" id="486139964%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.trafficawarenavigation</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="486139964%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-291650741%2FPackages%2F1617540583" anchor-label="com.here.sdk.trafficbroadcast" id="-291650741%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.trafficbroadcast</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-291650741%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-485810586%2FPackages%2F1617540583" anchor-label="com.here.sdk.transport" id="-485810586%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.transport</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-485810586%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-481989716%2FPackages%2F1617540583" anchor-label="com.here.sdk.venue" id="-481989716%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.venue</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-481989716%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="1276017243%2FPackages%2F1617540583" anchor-label="com.here.sdk.venue.control" id="1276017243%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.venue.control</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1276017243%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-868401360%2FPackages%2F1617540583" anchor-label="com.here.sdk.venue.data" id="-868401360%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-868401360%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-1160080252%2FPackages%2F1617540583" anchor-label="com.here.sdk.venue.routing" id="-1160080252%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.venue.routing</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1160080252%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-573481549%2FPackages%2F1617540583" anchor-label="com.here.sdk.venue.service" id="-573481549%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.venue.service</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-573481549%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-1108109137%2FPackages%2F1617540583" anchor-label="com.here.sdk.venue.style" id="-1108109137%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.venue.style</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1108109137%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="421536538%2FPackages%2F1617540583" anchor-label="com.here.sdk.warner" id="421536538%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.sdk.warner</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="421536538%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    </div>
<a data-name="-1957250752%2FPackages%2F1617540583" anchor-label="com.here.time" id="-1957250752%2FPackages%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
    <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
      <div>
        <div class="main-subrow ">
          <div class=""><span class="inline-flex">
              <div><a href="sdk-for-flutter-explore-index">com.here.time</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1957250752%2FPackages%2F1617540583"></span>
                <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
              </span></span></div>
          <div class="pull-right">
            <div class="platform-tags no-gutters">
              <div class="platform-tag jvm-like">androidJvm</div>
            </div>
          </div>
        </div>
        <div></div>
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
