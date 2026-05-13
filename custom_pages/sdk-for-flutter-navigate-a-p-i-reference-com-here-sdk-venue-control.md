---
title: "com.here.sdk.venue.control"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-venue-control"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>com.here.sdk.venue.control</title>
    <link href="../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../";</script>
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
<script type="text/javascript" src="../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../styles/style.css" rel="Stylesheet">
<link href="../../styles/main.css" rel="Stylesheet">
<link href="../../styles/prism.css" rel="Stylesheet">
<link href="../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
</head>
<body>
    <div class="root">
    <nav class="navigation theme-dark" id="navigation-wrapper">
            <a class="library-name--link" href="../../index.html">
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
<div class="main-content" data-page-type="package" id="content" pageIds="API Reference::com.here.sdk.venue.control////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../index.html">API Reference</a><span class="delimiter">/</span><span class="current">com.here.sdk.venue.control</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Package-level</span></span> <span><span>declarations</span></span></h1>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="TYPE">Types</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1904912600%2FClasslikes%2F1617540583" anchor-label="Venue" id="1904912600%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-venue/index.html"><span><span>Venue</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1904912600%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-venue/index.html">Venue</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Controls the <a href="../com.here.sdk.venue.data/-venue-model/index.html">com.here.sdk.venue.data.VenueModel</a> inside the <a href="-venue-map/index.html">com.here.sdk.venue.control.VenueMap</a> object. The venue controls the selection of the <a href="../com.here.sdk.venue.data/-venue-drawing/index.html">com.here.sdk.venue.data.VenueDrawing</a> and the <a href="../com.here.sdk.venue.data/-venue-level/index.html">com.here.sdk.venue.data.VenueLevel</a> of the <a href="../com.here.sdk.venue.data/-venue-model/index.html">com.here.sdk.venue.data.VenueModel</a>. It provides the possibility to customize styles for the <a href="../com.here.sdk.venue.data/-venue-geometry/index.html">com.here.sdk.venue.data.VenueGeometry</a>. Objects of this class can only be created using methods <a href="-venue-map/add-venue-async.html">com.here.sdk.venue.control.VenueMap.addVenueAsync</a> and <a href="-venue-map/select-venue-async.html">com.here.sdk.venue.control.VenueMap.selectVenueAsync</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="730123286%2FClasslikes%2F1617540583" anchor-label="VenueDrawingSelectionListener" id="730123286%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-venue-drawing-selection-listener/index.html"><span>Venue</span><wbr></wbr><span>Drawing</span><wbr></wbr><span>Selection</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="730123286%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-venue-drawing-selection-listener/index.html">VenueDrawingSelectionListener</a></div><div class="brief "><p class="paragraph">The interface for  for the <a href="../com.here.sdk.venue.data/-venue-drawing/index.html">com.here.sdk.venue.data.VenueDrawing</a> selection event. Use the <a href="-venue-map/index.html">com.here.sdk.venue.control.VenueMap</a> to add and remove the <a href="-venue-drawing-selection-listener/index.html">com.here.sdk.venue.control.VenueDrawingSelectionListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1213443349%2FClasslikes%2F1617540583" anchor-label="VenueErrorCode" id="1213443349%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-venue-error-code/index.html"><span>Venue</span><wbr></wbr><span>Error</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1213443349%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-venue-error-code/index.html">VenueErrorCode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-venue-error-code/index.html">VenueErrorCode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies possible errors that may occur during loading of indoor maps</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="950100507%2FClasslikes%2F1617540583" anchor-label="VenueException" id="950100507%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-venue-exception/index.html"><span>Venue</span><wbr></wbr><span><span>Exception</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="950100507%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-venue-exception/index.html">VenueException</a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span class="token keyword">val </span>error<span class="token operator">: </span><a href="-venue-error-code/index.html">VenueErrorCode</a></span></span><span class="token punctuation">)</span> : <a href="https://developer.android.com/reference/kotlin/java/lang/Exception.html">Exception</a></div><div class="brief "><p class="paragraph">Specifies possible errors that may occur during loading of indoor maps</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-65612606%2FClasslikes%2F1617540583" anchor-label="VenueInfoDataList" id="-65612606%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-venue-info-data-list/index.html"><span>Venue</span><wbr></wbr><span>Info</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>List</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-65612606%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">typealias </span><a href="-venue-info-data-list/index.html">VenueInfoDataList</a><span class="token operator"> = </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../com.here.sdk.venue.data/-venue-info/index.html">VenueInfo</a><span class="token operator">&gt;</span></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1787346056%2FClasslikes%2F1617540583" anchor-label="VenueInfoListListener" id="-1787346056%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-venue-info-list-listener/index.html"><span>Venue</span><wbr></wbr><span>Info</span><wbr></wbr><span>List</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1787346056%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-venue-info-list-listener/index.html">VenueInfoListListener</a></div><div class="brief "><p class="paragraph">The interface for  for the list of <a href="../com.here.sdk.venue.data/-venue-info/index.html">com.here.sdk.venue.data.VenueInfo</a> load event. Use <a href="-venue-map/index.html">com.here.sdk.venue.control.VenueMap</a> to add and remove the <a href="-venue-info-list-listener/index.html">com.here.sdk.venue.control.VenueInfoListListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1488275900%2FClasslikes%2F1617540583" anchor-label="VenueLevelSelectionListener" id="1488275900%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-venue-level-selection-listener/index.html"><span>Venue</span><wbr></wbr><span>Level</span><wbr></wbr><span>Selection</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1488275900%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-venue-level-selection-listener/index.html">VenueLevelSelectionListener</a></div><div class="brief "><p class="paragraph">The interface for  for the <a href="../com.here.sdk.venue.data/-venue-level/index.html">com.here.sdk.venue.data.VenueLevel</a> selection event. Use the <a href="-venue-map/index.html">com.here.sdk.venue.control.VenueMap</a> to add and remove the <a href="-venue-level-selection-listener/index.html">com.here.sdk.venue.control.VenueLevelSelectionListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2107638260%2FClasslikes%2F1617540583" anchor-label="VenueLifecycleListener" id="-2107638260%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-venue-lifecycle-listener/index.html"><span>Venue</span><wbr></wbr><span>Lifecycle</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2107638260%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-venue-lifecycle-listener/index.html">VenueLifecycleListener</a></div><div class="brief "><p class="paragraph">The interface for  for the <a href="-venue/index.html">com.here.sdk.venue.control.Venue</a> lifecycle events. Use the <a href="-venue-map/index.html">com.here.sdk.venue.control.VenueMap</a> to add and remove the <a href="-venue-lifecycle-listener/index.html">com.here.sdk.venue.control.VenueLifecycleListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="52809027%2FClasslikes%2F1617540583" anchor-label="VenueLoadErrorCallback" id="52809027%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-venue-load-error-callback/index.html"><span>Venue</span><wbr></wbr><span>Load</span><wbr></wbr><span>Error</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="52809027%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-venue-load-error-callback/index.html">VenueLoadErrorCallback</a></div><div class="brief "><p class="paragraph">A method which is called on the main thread when <a href="-venue-map/select-venue-async.html">com.here.sdk.venue.control.VenueMap.selectVenueAsync</a> has been completed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1770495086%2FClasslikes%2F1617540583" anchor-label="VenueMap" id="1770495086%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-venue-map/index.html"><span>Venue</span><wbr></wbr><span><span>Map</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1770495086%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-venue-map/index.html">VenueMap</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Connects a map with venues. When the <a href="-venue-map/index.html">com.here.sdk.venue.control.VenueMap</a> is started, venues can be seen on the map as interactive models. The user can switch drawings and levels, change a visual style of geometries and related labels inside the venue etc. After constructing the <a href="-venue-map/index.html">com.here.sdk.venue.control.VenueMap</a>, for relevant events should be added to the object. <a href="-venue-map/index.html">com.here.sdk.venue.control.VenueMap</a> is an add-on to the base map functionality with its own content loading and cache. For this reason, in certain situations there may be a small delay before the venue is visible.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1459492554%2FClasslikes%2F1617540583" anchor-label="VenueMapLifecycleListener" id="-1459492554%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-venue-map-lifecycle-listener/index.html"><span>Venue</span><wbr></wbr><span>Map</span><wbr></wbr><span>Lifecycle</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1459492554%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-venue-map-lifecycle-listener/index.html">VenueMapLifecycleListener</a></div><div class="brief "><p class="paragraph">The interface for  for the <a href="-venue/index.html">com.here.sdk.venue.control.Venue</a> lifecycle events. Use the <a href="-venue-map/index.html">com.here.sdk.venue.control.VenueMap</a> to add and remove the <a href="-venue-map-lifecycle-listener/index.html">com.here.sdk.venue.control.VenueMapLifecycleListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1077133354%2FClasslikes%2F1617540583" anchor-label="VenueSelectionListener" id="1077133354%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-venue-selection-listener/index.html"><span>Venue</span><wbr></wbr><span>Selection</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1077133354%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-venue-selection-listener/index.html">VenueSelectionListener</a></div><div class="brief "><p class="paragraph">The interface for  for the <a href="-venue/index.html">com.here.sdk.venue.control.Venue</a> selection event. Use the <a href="-venue-map/index.html">com.here.sdk.venue.control.VenueMap</a> to add and remove the <a href="-venue-selection-listener/index.html">com.here.sdk.venue.control.VenueSelectionListener</a>.</p></div></div></div>
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
