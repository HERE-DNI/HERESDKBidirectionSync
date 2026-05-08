---
title: "ManeuverAction"
slug: "sdk-for-flutter-explore"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>ManeuverAction</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.routing/ManeuverAction///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.routing</a><span class="delimiter">/</span><span class="current">ManeuverAction</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Maneuver</span><wbr></wbr><span><span>Action</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">ManeuverAction</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">ManeuverAction</a><span class="token operator">&gt; </span></div><p class="paragraph">Maneuver action type.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
    <div class="tabs-section-body">
      <div data-togglable="ENTRY">
        <h2 class="">Entries</h2>
        <div class="table"><a data-name="2041326425%2FClasslikes%2F1617540583" anchor-label="DEPART" id="2041326425%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">DEPART</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2041326425%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">DEPART</a></div></div><div class="brief "><p class="paragraph">Departure maneuver, such as &quot;Head towards&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-813889796%2FClasslikes%2F1617540583" anchor-label="ARRIVE" id="-813889796%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">ARRIVE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-813889796%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">ARRIVE</a></div></div><div class="brief "><p class="paragraph">Arrival maneuver, such as &quot;You have reached your destination/waypoint&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1671073662%2FClasslikes%2F1617540583" anchor-label="LEFT_U_TURN" id="-1671073662%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_U_TURN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1671073662%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_U_TURN</a></div></div><div class="brief "><p class="paragraph">Left-hand U-turn maneuver, such as &quot;Make a U-turn&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1950000285%2FClasslikes%2F1617540583" anchor-label="SHARP_LEFT_TURN" id="-1950000285%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">SHARP_LEFT_TURN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1950000285%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">SHARP_LEFT_TURN</a></div></div><div class="brief "><p class="paragraph">Sharp left turn maneuver, such as &quot;Turn sharply left&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-844259816%2FClasslikes%2F1617540583" anchor-label="LEFT_TURN" id="-844259816%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_TURN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-844259816%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_TURN</a></div></div><div class="brief "><p class="paragraph">Left turn maneuver, such as &quot;Turn left&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1037827166%2FClasslikes%2F1617540583" anchor-label="SLIGHT_LEFT_TURN" id="1037827166%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">SLIGHT_LEFT_TURN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1037827166%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">SLIGHT_LEFT_TURN</a></div></div><div class="brief "><p class="paragraph">Slight left turn maneuver, such as &quot;Turn slightly left&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="931779994%2FClasslikes%2F1617540583" anchor-label="CONTINUE_ON" id="931779994%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">CONTINUE_ON</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="931779994%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">CONTINUE_ON</a></div></div><div class="brief "><p class="paragraph">Continue maneuver, such as &quot;Continue straight ahead&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-451913409%2FClasslikes%2F1617540583" anchor-label="SLIGHT_RIGHT_TURN" id="-451913409%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">SLIGHT_RIGHT_TURN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-451913409%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">SLIGHT_RIGHT_TURN</a></div></div><div class="brief "><p class="paragraph">Slight right turn maneuver, such as &quot;Turn slightly right&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1332932293%2FClasslikes%2F1617540583" anchor-label="RIGHT_TURN" id="1332932293%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_TURN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1332932293%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_TURN</a></div></div><div class="brief "><p class="paragraph">Right turn maneuver, such as &quot;Turn right&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1414716122%2FClasslikes%2F1617540583" anchor-label="SHARP_RIGHT_TURN" id="1414716122%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">SHARP_RIGHT_TURN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1414716122%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">SHARP_RIGHT_TURN</a></div></div><div class="brief "><p class="paragraph">Sharp right turn maneuver, such as &quot;Turn sharply right&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1038530065%2FClasslikes%2F1617540583" anchor-label="RIGHT_U_TURN" id="-1038530065%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_U_TURN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1038530065%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_U_TURN</a></div></div><div class="brief "><p class="paragraph">Right u-turn maneuver, such as &quot;Make a U-turn&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="440367865%2FClasslikes%2F1617540583" anchor-label="LEFT_EXIT" id="440367865%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_EXIT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="440367865%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_EXIT</a></div></div><div class="brief "><p class="paragraph">Left exit maneuver, such as &quot;Take the exit&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1677407322%2FClasslikes%2F1617540583" anchor-label="RIGHT_EXIT" id="-1677407322%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_EXIT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1677407322%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_EXIT</a></div></div><div class="brief "><p class="paragraph">Right exit maneuver, such as &quot;Take the exit&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="398588653%2FClasslikes%2F1617540583" anchor-label="LEFT_RAMP" id="398588653%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_RAMP</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="398588653%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_RAMP</a></div></div><div class="brief "><p class="paragraph">Left ramp maneuver, such as &quot;Join the highway&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1719186534%2FClasslikes%2F1617540583" anchor-label="RIGHT_RAMP" id="-1719186534%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_RAMP</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1719186534%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_RAMP</a></div></div><div class="brief "><p class="paragraph">Right ramp maneuver, such as &quot;Join the highway&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="73017245%2FClasslikes%2F1617540583" anchor-label="LEFT_FORK" id="73017245%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_FORK</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="73017245%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_FORK</a></div></div><div class="brief "><p class="paragraph">Left fork maneuver, such as &quot;Keep left&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1598920591%2FClasslikes%2F1617540583" anchor-label="MIDDLE_FORK" id="1598920591%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">MIDDLE_FORK</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1598920591%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">MIDDLE_FORK</a></div></div><div class="brief "><p class="paragraph">Middle fork maneuver, such as &quot;Keep middle&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2044757942%2FClasslikes%2F1617540583" anchor-label="RIGHT_FORK" id="-2044757942%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_FORK</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2044757942%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_FORK</a></div></div><div class="brief "><p class="paragraph">Right fork maneuver, such as &quot;Keep right&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="159051654%2FClasslikes%2F1617540583" anchor-label="ENTER_HIGHWAY_FROM_LEFT" id="159051654%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">ENTER_HIGHWAY_FROM_LEFT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="159051654%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">ENTER_HIGHWAY_FROM_LEFT</a></div></div><div class="brief "><p class="paragraph">Merge onto a highway from the left side. Such a maneuver occurs only in countries that drive on the left side of the road (left-hand traffic).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1680124869%2FClasslikes%2F1617540583" anchor-label="ENTER_HIGHWAY_FROM_RIGHT" id="1680124869%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">ENTER_HIGHWAY_FROM_RIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1680124869%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">ENTER_HIGHWAY_FROM_RIGHT</a></div></div><div class="brief "><p class="paragraph">Merge onto a highway from the right side. Such a maneuver occurs only in countries that drive on the right side of the road (right-hand traffic).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="279233299%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_ENTER" id="279233299%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_ENTER</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="279233299%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_ENTER</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as &quot;Enter the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="863860800%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_ENTER" id="863860800%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_ENTER</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="863860800%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_ENTER</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Enter the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-789888962%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_PASS" id="-789888962%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_PASS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-789888962%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_PASS</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as &quot;Pass the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1463766671%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_PASS" id="-1463766671%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_PASS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1463766671%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_PASS</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Pass the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="915456494%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_EXIT1" id="915456494%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT1</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="915456494%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT1</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as  &quot;Take the first exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1449279953%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_EXIT2" id="-1449279953%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT2</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1449279953%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT2</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as &quot;Take the second exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="480950896%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_EXIT3" id="480950896%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT3</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="480950896%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT3</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as &quot;Take the third exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1883785551%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_EXIT4" id="-1883785551%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT4</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1883785551%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT4</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as &quot;Take the fourth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="46445298%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_EXIT5" id="46445298%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT5</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="46445298%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT5</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as &quot;Take the fifth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1976676147%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_EXIT6" id="1976676147%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT6</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1976676147%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT6</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as &quot;Take the sixth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-388060300%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_EXIT7" id="-388060300%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT7</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-388060300%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT7</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as &quot;Take the seventh exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1542170549%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_EXIT8" id="1542170549%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT8</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1542170549%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT8</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as &quot;Take the eighth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-822565898%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_EXIT9" id="-822565898%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT9</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-822565898%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT9</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as &quot;Take the ninth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="134698154%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_EXIT10" id="134698154%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT10</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="134698154%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT10</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as &quot;Take the tenth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2064929003%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_EXIT11" id="2064929003%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT11</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2064929003%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT11</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as &quot;Take the eleventh exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-299807444%2FClasslikes%2F1617540583" anchor-label="LEFT_ROUNDABOUT_EXIT12" id="-299807444%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT12</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-299807444%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">LEFT_ROUNDABOUT_EXIT12</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (left-hand traffic), such as &quot;Take the twelfth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1500083995%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_EXIT1" id="1500083995%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT1</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1500083995%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT1</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Take the first exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-864652452%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_EXIT2" id="-864652452%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT2</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-864652452%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT2</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Take the second exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1065578397%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_EXIT3" id="1065578397%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT3</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1065578397%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT3</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Take the third exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1299158050%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_EXIT4" id="-1299158050%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT4</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1299158050%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT4</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Take the fourth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="631072799%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_EXIT5" id="631072799%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT5</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="631072799%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT5</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Take the fifth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1733663648%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_EXIT6" id="-1733663648%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT6</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1733663648%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT6</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Take the sixth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="196567201%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_EXIT7" id="196567201%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT7</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="196567201%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT7</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Take the seventh exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2126798050%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_EXIT8" id="2126798050%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT8</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2126798050%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT8</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Take the eighth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-237938397%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_EXIT9" id="-237938397%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT9</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-237938397%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT9</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Take the ninth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1078281501%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_EXIT10" id="1078281501%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT10</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1078281501%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT10</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Take the tenth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1286454946%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_EXIT11" id="-1286454946%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT11</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1286454946%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT11</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Take the eleventh exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="643775903%2FClasslikes%2F1617540583" anchor-label="RIGHT_ROUNDABOUT_EXIT12" id="643775903%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT12</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="643775903%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">RIGHT_ROUNDABOUT_EXIT12</a></div></div><div class="brief "><p class="paragraph">Roundabout maneuver (right-hand traffic), such as &quot;Take the twelfth exit at the roundabout&quot;.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="852638847%2FProperties%2F1617540583" anchor-label="entries" id="852638847%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-entries"><span><span>entries</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="852638847%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-entries">entries</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">ManeuverAction</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1802660670%2FProperties%2F1617540583" anchor-label="value" id="1802660670%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-value"><span><span>value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1802660670%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-value">value</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="2021795709%2FFunctions%2F1617540583" anchor-label="valueOf" id="2021795709%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-value-of"><span>value</span><wbr></wbr><span><span>Of</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2021795709%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-value-of"><span class="token function">valueOf</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">ManeuverAction</a></div><div class="brief "><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1614160713%2FFunctions%2F1617540583" anchor-label="values" id="1614160713%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-values"><span><span>values</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1614160713%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-values"><span class="token function">values</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">ManeuverAction</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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
