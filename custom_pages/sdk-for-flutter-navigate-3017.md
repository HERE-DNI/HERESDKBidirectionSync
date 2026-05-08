---
title: "com.here.sdk.venue.data"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>com.here.sdk.venue.data</title>
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
<div class="main-content" data-page-type="package" id="content" pageIds="API Reference::com.here.sdk.venue.data////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><span class="current">com.here.sdk.venue.data</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Package-level</span></span> <span><span>declarations</span></span></h1>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="TYPE">Types</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="659864137%2FClasslikes%2F1617540583" anchor-label="Crosswalk" id="659864137%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Crosswalk</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="659864137%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Crosswalk</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Represents crosswalk's inside the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueLevel</a>. A crosswalk is an area of the road surface where pedestrians are expected to walk across the road. The area is represented as a polygon, which is often, but not necessarily, rectangular and oriented with the shorter dimension in the vehicle's direction of travel.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-965788709%2FClasslikes%2F1617540583" anchor-label="Property" id="-965788709%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Property</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-965788709%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Property</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Holds information of varying types, such as Boolean, Integer, String. Properties are used in <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueModel</a>, <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueLevel</a> and <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueGeometry</a> to describe this objects.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2000206655%2FClasslikes%2F1617540583" anchor-label="VenueDrawing" id="-2000206655%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Venue</span><wbr></wbr><span><span>Drawing</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2000206655%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">VenueDrawing</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Represents a drawing inside the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueModel</a>. The drawing can be a separate building in a complex of buildings, or show a different view of a venue. For example, in an airport, one drawing can be used as an overview of all buildings in this venue, while other drawings contains details for each terminal in this airport.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1181349167%2FClasslikes%2F1617540583" anchor-label="VenueGeometry" id="-1181349167%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Venue</span><wbr></wbr><span><span>Geometry</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1181349167%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">VenueGeometry</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Represents a geometry inside the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueLevel</a>. The geometry can be any object inside the level, like a room, a wall or a table. Also the geometry can represent virtual objects, like a team area in an open space.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-158013409%2FClasslikes%2F1617540583" anchor-label="VenueGeometryFilterType" id="-158013409%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Venue</span><wbr></wbr><span>Geometry</span><wbr></wbr><span>Filter</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-158013409%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">VenueGeometryFilterType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">VenueGeometryFilterType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Filter types for the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueGeometry</a> search.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1655497493%2FClasslikes%2F1617540583" anchor-label="VenueInfo" id="1655497493%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Venue</span><wbr></wbr><span><span>Info</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1655497493%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">VenueInfo</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Represents the venue info existing in a catalogs contains id and name.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1061502875%2FClasslikes%2F1617540583" anchor-label="VenueLevel" id="1061502875%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Venue</span><wbr></wbr><span><span>Level</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1061502875%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">VenueLevel</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Represents one level of a building or a complex of buildings inside the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueDrawing</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-295808106%2FClasslikes%2F1617540583" anchor-label="VenueModel" id="-295808106%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Venue</span><wbr></wbr><span><span>Model</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-295808106%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">VenueModel</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Represents a building or a complex of buildings, like airports or universities.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2085459828%2FClasslikes%2F1617540583" anchor-label="VenueTopology" id="2085459828%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Venue</span><wbr></wbr><span><span>Topology</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2085459828%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">VenueTopology</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Represents routing topologies inside the <a href="sdk-for-flutter-explore-index">com.here.sdk.venue.data.VenueLevel</a>. The topologies can be paths used for enabling routing services.</p></div></div></div>
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
