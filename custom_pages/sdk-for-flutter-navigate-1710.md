---
title: "NavigatorInterface"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>NavigatorInterface</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.navigation/NavigatorInterface///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.navigation</a><span class="delimiter">/</span><span class="current">NavigatorInterface</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Navigator</span><wbr></wbr><span><span>Interface</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">NavigatorInterface</a> : <a href="sdk-for-flutter-explore-index">LocationListener</a></div><p class="paragraph">This interface provides the basic functionality needed to run a navigation session.</p><h4 class="">Inheritors</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="sdk-for-flutter-explore-index">Navigator</a></div></span></div><div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="sdk-for-flutter-explore-index">VisualNavigator</a></div></span></div><div></div></div></div></div></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="477560530%2FProperties%2F1617540583" anchor-label="borderCrossingWarningListener" id="477560530%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-border-crossing-warning-listener"><span>border</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="477560530%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-border-crossing-warning-listener">borderCrossingWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">BorderCrossingWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about border crossings on the current road. Border crossing notifications are given only if a route is present. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="381464694%2FProperties%2F1617540583" anchor-label="borderCrossingWarningOptions" id="381464694%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-border-crossing-warning-options"><span>border</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="381464694%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-border-crossing-warning-options">borderCrossingWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">BorderCrossingWarningOptions</a></div><div class="brief "><p class="paragraph">Border crossing warning options to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.BorderCrossingWarningListener</a>. These options allow the filtering of the border crossing warnings received and set the notification distances.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-261360476%2FProperties%2F1617540583" anchor-label="currentSituationLaneAssistanceViewListener" id="-261360476%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-current-situation-lane-assistance-view-listener"><span>current</span><wbr></wbr><span>Situation</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span>View</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-261360476%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-current-situation-lane-assistance-view-listener">currentSituationLaneAssistanceViewListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">CurrentSituationLaneAssistanceViewListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive current situation lane assistance view notifications. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2034246189%2FProperties%2F1617540583" anchor-label="dangerZoneWarningListener" id="-2034246189%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-danger-zone-warning-listener"><span>danger</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2034246189%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-danger-zone-warning-listener">dangerZoneWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">DangerZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notification on approaching danger zones. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-995433362%2FProperties%2F1617540583" anchor-label="destinationReachedListener" id="-995433362%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-destination-reached-listener"><span>destination</span><wbr></wbr><span>Reached</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-995433362%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-destination-reached-listener">destinationReachedListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">DestinationReachedListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive the notification about the arrival at the destination. Destination reached notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-608917792%2FProperties%2F1617540583" anchor-label="environmentalZoneWarningListener" id="-608917792%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-environmental-zone-warning-listener"><span>environmental</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-608917792%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-environmental-zone-warning-listener">environmentalZoneWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">EnvironmentalZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notification on approaching environmental zones. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1177685337%2FProperties%2F1617540583" anchor-label="eventTextListener" id="1177685337%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-event-text-listener"><span>event</span><wbr></wbr><span>Text</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1177685337%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-event-text-listener">eventTextListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">EventTextListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive text notifications when they are available. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user. <strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner, when <code class="lang-kotlin">TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code class="lang-kotlin">sdk.navigation.EventTextListener</code> must be enabled as well.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1951255281%2FProperties%2F1617540583" anchor-label="eventTextOptions" id="-1951255281%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-event-text-options"><span>event</span><wbr></wbr><span>Text</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1951255281%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-event-text-options">eventTextOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">EventTextOptions</a></div><div class="brief "><p class="paragraph">Options used for text notifications. Notifications are only available if a route is present.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1285600657%2FProperties%2F1617540583" anchor-label="isEnableTunnelExtrapolation" id="1285600657%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-enable-tunnel-extrapolation"><span>is</span><wbr></wbr><span>Enable</span><wbr></wbr><span>Tunnel</span><wbr></wbr><span><span>Extrapolation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1285600657%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-enable-tunnel-extrapolation">isEnableTunnelExtrapolation</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Defines whether to enable or disable tunnel extrapolation. By default the tunnel extrapolation is enabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-639158560%2FProperties%2F1617540583" anchor-label="isPassthroughWaypointsHandlingEnabled" id="-639158560%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-passthrough-waypoints-handling-enabled"><span>is</span><wbr></wbr><span>Passthrough</span><wbr></wbr><span>Waypoints</span><wbr></wbr><span>Handling</span><wbr></wbr><span><span>Enabled</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-639158560%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-passthrough-waypoints-handling-enabled">isPassthroughWaypointsHandlingEnabled</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Defines whether to enable or disable handling of passthrough waypoints. By default the handling of passthrough waypoints is disabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1238745397%2FProperties%2F1617540583" anchor-label="junctionViewLaneAssistanceListener" id="1238745397%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-junction-view-lane-assistance-listener"><span>junction</span><wbr></wbr><span>View</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1238745397%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-junction-view-lane-assistance-listener">junctionViewLaneAssistanceListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">JunctionViewLaneAssistanceListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive junction view lane assistance notifications. Junction view lane assistance notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1199019068%2FProperties%2F1617540583" anchor-label="locationManager" id="1199019068%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-location-manager"><span>location</span><wbr></wbr><span><span>Manager</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1199019068%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="sdk-for-flutter-explore-location-manager">locationManager</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LocationManager</a></div><div class="brief "><p class="paragraph">The location manager used by the navigator for map-matched location processing.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-240435389%2FProperties%2F1617540583" anchor-label="lowSpeedZoneWarningListener" id="-240435389%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-low-speed-zone-warning-listener"><span>low</span><wbr></wbr><span>Speed</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-240435389%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-low-speed-zone-warning-listener">lowSpeedZoneWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LowSpeedZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about low speed zones on the current road. Low speed zone notifications are given regardless if a route is set. This listener is currently available <i>only</i> for Japan. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1492445082%2FProperties%2F1617540583" anchor-label="maneuverNotificationOptions" id="1492445082%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-maneuver-notification-options"><span>maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1492445082%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-maneuver-notification-options">maneuverNotificationOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">ManeuverNotificationOptions</a></div><div class="brief "><p class="paragraph">Options used for maneuver notifications. Notifications are only available if a route is present.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="732904592%2FProperties%2F1617540583" anchor-label="maneuverViewLaneAssistanceListener" id="732904592%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-maneuver-view-lane-assistance-listener"><span>maneuver</span><wbr></wbr><span>View</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="732904592%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-maneuver-view-lane-assistance-listener">maneuverViewLaneAssistanceListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">ManeuverViewLaneAssistanceListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive maneuver view lane assistance notifications. Maneuver view lane assistance notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1789672226%2FProperties%2F1617540583" anchor-label="milestoneStatusListener" id="-1789672226%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-milestone-status-listener"><span>milestone</span><wbr></wbr><span>Status</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1789672226%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-milestone-status-listener">milestoneStatusListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MilestoneStatusListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the arrival at each <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Milestone</a> or missing it. It informs on all waypoints (passed or missed) that are of type <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.MilestoneType.STOPOVER</a> but excludes the starting waypoint. Waypoints of type <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.MilestoneType.PASSTHROUGH</a> are excluded, by default, but can be included via <a href="sdk-for-flutter-explore-is-passthrough-waypoints-handling-enabled">com.here.sdk.navigation.NavigatorInterface.isPassthroughWaypointsHandlingEnabled</a>. Milestone status notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="391250736%2FProperties%2F1617540583" anchor-label="navigableLocationListener" id="391250736%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-navigable-location-listener"><span>navigable</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="391250736%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-navigable-location-listener">navigableLocationListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">NavigableLocationListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the current location. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1853366989%2FProperties%2F1617540583" anchor-label="offRoadDestinationReachedListener" id="1853366989%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-off-road-destination-reached-listener"><span>off</span><wbr></wbr><span>Road</span><wbr></wbr><span>Destination</span><wbr></wbr><span>Reached</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1853366989%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-off-road-destination-reached-listener">offRoadDestinationReachedListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">OffRoadDestinationReachedListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive the notification about the arrival at the off-road destination. Off-road destination reached notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="574698788%2FProperties%2F1617540583" anchor-label="offRoadProgressListener" id="574698788%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-off-road-progress-listener"><span>off</span><wbr></wbr><span>Road</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="574698788%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-off-road-progress-listener">offRoadProgressListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">OffRoadProgressListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive the notification about the off-road progress. Off-road progress notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-719001060%2FProperties%2F1617540583" anchor-label="postActionListener" id="-719001060%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-post-action-listener"><span>post</span><wbr></wbr><span>Action</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-719001060%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-post-action-listener">postActionListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">PostActionListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive post action notifications, such as a charge action at a charging station. Post actions notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1481227595%2FProperties%2F1617540583" anchor-label="railwayCrossingWarningListener" id="-1481227595%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-railway-crossing-warning-listener"><span>railway</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1481227595%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-railway-crossing-warning-listener">railwayCrossingWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RailwayCrossingWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about railway crossings on the current road. Railway crossing notifications are given regardless if a route is set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1097654239%2FProperties%2F1617540583" anchor-label="realisticViewWarningListener" id="-1097654239%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-realistic-view-warning-listener"><span>realistic</span><wbr></wbr><span>View</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1097654239%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-realistic-view-warning-listener">realisticViewWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RealisticViewWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about junction views on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. This feature requires a map version greater or equal to 67 in order to function properly. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1023387975%2FProperties%2F1617540583" anchor-label="realisticViewWarningOptions" id="1023387975%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-realistic-view-warning-options"><span>realistic</span><wbr></wbr><span>View</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1023387975%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-realistic-view-warning-options">realisticViewWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RealisticViewWarningOptions</a></div><div class="brief "><p class="paragraph">Realistic view warning options. It allow to filter realistic views to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RealisticViewWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="467022875%2FProperties%2F1617540583" anchor-label="roadAttributesListener" id="467022875%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-road-attributes-listener"><span>road</span><wbr></wbr><span>Attributes</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="467022875%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-road-attributes-listener">roadAttributesListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RoadAttributesListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about attributes of the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1023698465%2FProperties%2F1617540583" anchor-label="roadSignWarningListener" id="1023698465%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-road-sign-warning-listener"><span>road</span><wbr></wbr><span>Sign</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1023698465%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-road-sign-warning-listener">roadSignWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RoadSignWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about road signs on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="676176711%2FProperties%2F1617540583" anchor-label="roadSignWarningOptions" id="676176711%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-road-sign-warning-options"><span>road</span><wbr></wbr><span>Sign</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="676176711%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-road-sign-warning-options">roadSignWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RoadSignWarningOptions</a></div><div class="brief "><p class="paragraph">Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RoadSignWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2089612678%2FProperties%2F1617540583" anchor-label="roadTextsListener" id="-2089612678%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-road-texts-listener"><span>road</span><wbr></wbr><span>Texts</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2089612678%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-road-texts-listener">roadTextsListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RoadTextsListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the textual attributes of the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="205206027%2FProperties%2F1617540583" anchor-label="route" id="205206027%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-route"><span><span>route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="205206027%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-route">route</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Route</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The route to navigate. Gets and sets the route that is being navigated. If not set, only the current location information will be provided through <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.NavigableLocationListener</a>. If set, both route progress (<a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RouteProgressListener</a>) and route deviation (<a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RouteDeviationListener</a>) will receive notifications on updates. A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1214143334%2FProperties%2F1617540583" anchor-label="routeDeviationListener" id="-1214143334%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-route-deviation-listener"><span>route</span><wbr></wbr><span>Deviation</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1214143334%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-route-deviation-listener">routeDeviationListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RouteDeviationListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about deviations from the route if any occurs. Route deviation notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="658184970%2FProperties%2F1617540583" anchor-label="routeProgressListener" id="658184970%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-route-progress-listener"><span>route</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="658184970%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-route-progress-listener">routeProgressListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RouteProgressListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about navigation route progress. Route progress notifications only occurs if the route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2104014907%2FProperties%2F1617540583" anchor-label="safetyCameraWarningListener" id="2104014907%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-safety-camera-warning-listener"><span>safety</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2104014907%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-safety-camera-warning-listener">safetyCameraWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SafetyCameraWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive safety camera warner notifications. If a listener  is present, notifications about safety speed cameras will be also sent via <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.SafetyCameraWarningListener</a>. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1265214957%2FProperties%2F1617540583" anchor-label="safetyCameraWarningOptions" id="1265214957%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-safety-camera-warning-options"><span>safety</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1265214957%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-safety-camera-warning-options">safetyCameraWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SafetyCameraWarningOptions</a></div><div class="brief "><p class="paragraph">Safety camera warning options to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.SafetyCameraWarningListener</a>. These options allow the enabling or disabling the text notification for the warner.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1631834716%2FProperties%2F1617540583" anchor-label="schoolZoneWarningListener" id="-1631834716%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-school-zone-warning-listener"><span>school</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1631834716%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-school-zone-warning-listener">schoolZoneWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SchoolZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about school zones on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. school zones on the current road. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1903337628%2FProperties%2F1617540583" anchor-label="schoolZoneWarningOptions" id="-1903337628%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-school-zone-warning-options"><span>school</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1903337628%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-school-zone-warning-options">schoolZoneWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SchoolZoneWarningOptions</a></div><div class="brief "><p class="paragraph">School zone warning options It allow to configure school zone notifications to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.SchoolZoneWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2079429918%2FProperties%2F1617540583" anchor-label="speedLimitListener" id="2079429918%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-speed-limit-listener"><span>speed</span><wbr></wbr><span>Limit</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2079429918%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-speed-limit-listener">speedLimitListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SpeedLimitListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the speed limit of the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="461909341%2FProperties%2F1617540583" anchor-label="speedWarningListener" id="461909341%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-speed-warning-listener"><span>speed</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="461909341%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-speed-warning-listener">speedWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SpeedWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1697250165%2FProperties%2F1617540583" anchor-label="speedWarningOptions" id="-1697250165%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-speed-warning-options"><span>speed</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1697250165%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-speed-warning-options">speedWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SpeedWarningOptions</a></div><div class="brief "><p class="paragraph">Options used for the speed warning feature.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1409510143%2FProperties%2F1617540583" anchor-label="tollStopWarningListener" id="-1409510143%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-toll-stop-warning-listener"><span>toll</span><wbr></wbr><span>Stop</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1409510143%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-toll-stop-warning-listener">tollStopWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TollStopWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive information on the upcoming toll stop. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1306376529%2FProperties%2F1617540583" anchor-label="trackingTransportProfile" id="-1306376529%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-tracking-transport-profile"><span>tracking</span><wbr></wbr><span>Transport</span><wbr></wbr><span><span>Profile</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1306376529%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-tracking-transport-profile"><strike>trackingTransportProfile</strike></a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TransportProfile</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Defines the transport profile for the <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Navigator</a>, when no route is present. Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a <a href="sdk-for-flutter-explore-index">com.here.sdk.core.TransportProfile</a> can be defined with a <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.VehicleProfile</a>. A vehicle profile can have several parameters such as <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.VehicleType</a> to set the source of information describing the vehicle. The default is a <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.VehicleType.CAR</a> profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1812406357%2FProperties%2F1617540583" anchor-label="trackingTransportSpecification" id="1812406357%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-tracking-transport-specification"><span>tracking</span><wbr></wbr><span>Transport</span><wbr></wbr><span><span>Specification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1812406357%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-tracking-transport-specification">trackingTransportSpecification</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TransportSpecification</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Defines the transport specification for the <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Navigator</a>, when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportSpecification</a> must have the <a href="sdk-for-flutter-explore-transport-mode">com.here.sdk.transport.TransportSpecification.transportMode</a> set. A transport specification can have several parameters defined such as <a href="sdk-for-flutter-explore-length-in-centimeters">com.here.sdk.transport.VehicleSpecification.lengthInCentimeters</a> defined in <a href="sdk-for-flutter-explore-vehicle-specification">com.here.sdk.transport.TransportSpecification.vehicleSpecification</a> to set the source of information describing the vehicle. By default the <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportSpecification</a> will have the transport mode set to <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportMode.CAR</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1987683295%2FProperties%2F1617540583" anchor-label="trafficMergeWarningListener" id="1987683295%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-traffic-merge-warning-listener"><span>traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1987683295%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-traffic-merge-warning-listener">trafficMergeWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficMergeWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about merging traffic to the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1954198985%2FProperties%2F1617540583" anchor-label="trafficMergeWarningOptions" id="1954198985%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-traffic-merge-warning-options"><span>traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1954198985%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-traffic-merge-warning-options">trafficMergeWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficMergeWarningOptions</a></div><div class="brief "><p class="paragraph">Merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TrafficMergeWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1115100455%2FProperties%2F1617540583" anchor-label="trafficOnRoute" id="-1115100455%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-traffic-on-route"><span>traffic</span><wbr></wbr><span>On</span><wbr></wbr><span><span>Route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1115100455%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-traffic-on-route">trafficOnRoute</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficOnRoute</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Traffic information for the current route. This impacts <code class="lang-kotlin">RouteProgress</code> updates as the duration of the <code class="lang-kotlin">SectionProgress</code> might change. However, the remaining distance and the route geometry will remain unchanged.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1027650372%2FProperties%2F1617540583" anchor-label="truckRestrictionsWarningListener" id="-1027650372%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-truck-restrictions-warning-listener"><span>truck</span><wbr></wbr><span>Restrictions</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1027650372%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-truck-restrictions-warning-listener">truckRestrictionsWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TruckRestrictionsWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about truck restrictions on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="748551500%2FProperties%2F1617540583" anchor-label="truckRestrictionsWarningOptions" id="748551500%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-truck-restrictions-warning-options"><span>truck</span><wbr></wbr><span>Restrictions</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="748551500%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-truck-restrictions-warning-options">truckRestrictionsWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TruckRestrictionsWarningOptions</a></div><div class="brief "><p class="paragraph">Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TruckRestrictionsWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="368923441%2FProperties%2F1617540583" anchor-label="warnerEngine" id="368923441%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-warner-engine"><span>warner</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="368923441%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="sdk-for-flutter-explore-warner-engine">warnerEngine</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WarnerEngine</a></div><div class="brief "><p class="paragraph">Warner engine used by the navigator. This engine can be used to configure navigation warnings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1162826530%2FFunctions%2F1617540583" anchor-label="calculateRemainingDistanceInMeters" id="-1162826530%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-calculate-remaining-distance-in-meters"><span>calculate</span><wbr></wbr><span>Remaining</span><wbr></wbr><span>Distance</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1162826530%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-calculate-remaining-distance-in-meters"><span class="token function">calculateRemainingDistanceInMeters</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">coordinates<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">This method calculates the distance between the current position and given coordinates. The coordinates must be on the polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="382761955%2FFunctions%2F1617540583" anchor-label="getManeuver" id="382761955%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-maneuver"><span>get</span><wbr></wbr><span><span>Maneuver</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="382761955%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-maneuver"><span class="token function">getManeuver</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">index<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Maneuver</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns maneuver at the given index.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1040273629%2FFunctions%2F1617540583" anchor-label="getManeuverNotificationTimingOptions" id="-1040273629%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-maneuver-notification-timing-options"><span>get</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Timing</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1040273629%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-maneuver-notification-timing-options"><span class="token function">getManeuverNotificationTimingOptions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TransportMode</a><span class="token punctuation">, </span></span><span class="parameter ">timingProfile<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TimingProfile</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">ManeuverNotificationTimingOptions</a></div><div class="brief "><p class="paragraph">Returns maneuver notification timing options with default values given the combination of transport mode and timing profile. The return value can be used as the base for configuring maneuver notification timings. Configure the relevant attributes of this object according to your preferences, and then set it by calling setManeuverNotificationTimingOptions function for the same combination of transport mode and timing profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1281340582%2FFunctions%2F1617540583" anchor-label="getWarningNotificationDistances" id="-1281340582%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-warning-notification-distances"><span>get</span><wbr></wbr><span>Warning</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Distances</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1281340582%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-warning-notification-distances"><span class="token function">getWarningNotificationDistances</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningType<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WarningType</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WarningNotificationDistances</a></div><div class="brief "><p class="paragraph">Returns the warning notification distances for the requested warning type. The return value can be used as the base for configuring warning notification distances. Configure the relevant attributes of this object according to your preferences, and then set it by calling <code class="lang-kotlin">setWarningNotificationDistances</code> function with the same warning type and the modified warning notification distances object.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="792081649%2FFunctions%2F1617540583" anchor-label="repeatLastManeuverNotification" id="792081649%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-repeat-last-maneuver-notification"><span>repeat</span><wbr></wbr><span>Last</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span><span>Notification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="792081649%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-repeat-last-maneuver-notification"><span class="token function">repeatLastManeuverNotification</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-503485507%2FFunctions%2F1617540583" anchor-label="setCustomOption" id="-503485507%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-custom-option"><span>set</span><wbr></wbr><span>Custom</span><wbr></wbr><span><span>Option</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-503485507%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-custom-option"><span class="token function">setCustomOption</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">key<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">This method sets custom options that controls navigator behavior. Unsupported options are silently ignored. Undocumented options can change their meaning without going through deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1057633993%2FFunctions%2F1617540583" anchor-label="setManeuverNotificationTimingOptions" id="-1057633993%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-maneuver-notification-timing-options"><span>set</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Timing</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1057633993%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-maneuver-notification-timing-options"><span class="token function">setManeuverNotificationTimingOptions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TransportMode</a><span class="token punctuation">, </span></span><span class="parameter ">timingProfile<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TimingProfile</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">ManeuverNotificationTimingOptions</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Set timing option values for the combination of transport mode and timing profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-748456627%2FFunctions%2F1617540583" anchor-label="setWarningNotificationDistances" id="-748456627%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-warning-notification-distances"><span>set</span><wbr></wbr><span>Warning</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Distances</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-748456627%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-warning-notification-distances"><span class="token function">setWarningNotificationDistances</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningType<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WarningType</a><span class="token punctuation">, </span></span><span class="parameter ">warningNotificationDistances<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WarningNotificationDistances</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Set the warning notification distances for the specified warning types. <strong>Note:</strong> The warning notification distances are set for most warners. This method can't be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use <code class="lang-kotlin">NavigatorInterface.school_zone_warning_options</code> instead. Attempting to set the warning notification distances for the school zone warner using the <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code class="lang-kotlin">false</code>. Always use <code class="lang-kotlin">SchoolZoneWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the school zone warner regardless of the <code class="lang-kotlin">TimingProfile</code>. If <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> could be used, this would allow for different distances to be set for each timing profile, which is undesirable. Attempting to set the warning notification distances for the traffic merge warner using the <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code class="lang-kotlin">false</code>. Always use <code class="lang-kotlin">TrafficMergeWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the traffic merge warner regardless of the <code class="lang-kotlin">TimingProfile</code>. Using the <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code class="lang-kotlin">false</code> to avoid seting different distances on each timing profile since the traffic merge warning is only applicable on highways.</p></div></div></div>
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
