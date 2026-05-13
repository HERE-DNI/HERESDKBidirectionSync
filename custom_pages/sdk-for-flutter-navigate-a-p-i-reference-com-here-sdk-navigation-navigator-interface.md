---
title: "NavigatorInterface"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-navigation-navigator-interface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.navigation/NavigatorInterface///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.navigation</a><span class="delimiter">/</span><span class="current">NavigatorInterface</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Navigator</span><wbr></wbr><span><span>Interface</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="index.html">NavigatorInterface</a> : <a href="../../com.here.sdk.core/-location-listener/index.html">LocationListener</a></div><p class="paragraph">This interface provides the basic functionality needed to run a navigation session.</p><h4 class="">Inheritors</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="../-navigator/index.html">Navigator</a></div></span></div><div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="../-visual-navigator/index.html">VisualNavigator</a></div></span></div><div></div></div></div></div></div></div>
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
                  <div><a href="border-crossing-warning-listener.html"><span>border</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="477560530%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="border-crossing-warning-listener.html">borderCrossingWarningListener</a><span class="token operator">: </span><a href="../-border-crossing-warning-listener/index.html">BorderCrossingWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about border crossings on the current road. Border crossing notifications are given only if a route is present. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="381464694%2FProperties%2F1617540583" anchor-label="borderCrossingWarningOptions" id="381464694%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="border-crossing-warning-options.html"><span>border</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="381464694%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="border-crossing-warning-options.html">borderCrossingWarningOptions</a><span class="token operator">: </span><a href="../-border-crossing-warning-options/index.html">BorderCrossingWarningOptions</a></div><div class="brief "><p class="paragraph">Border crossing warning options to be passed to <a href="../-border-crossing-warning-listener/index.html">com.here.sdk.navigation.BorderCrossingWarningListener</a>. These options allow the filtering of the border crossing warnings received and set the notification distances.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-261360476%2FProperties%2F1617540583" anchor-label="currentSituationLaneAssistanceViewListener" id="-261360476%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="current-situation-lane-assistance-view-listener.html"><span>current</span><wbr></wbr><span>Situation</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span>View</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-261360476%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="current-situation-lane-assistance-view-listener.html">currentSituationLaneAssistanceViewListener</a><span class="token operator">: </span><a href="../-current-situation-lane-assistance-view-listener/index.html">CurrentSituationLaneAssistanceViewListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive current situation lane assistance view notifications. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2034246189%2FProperties%2F1617540583" anchor-label="dangerZoneWarningListener" id="-2034246189%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="danger-zone-warning-listener.html"><span>danger</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2034246189%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="danger-zone-warning-listener.html">dangerZoneWarningListener</a><span class="token operator">: </span><a href="../-danger-zone-warning-listener/index.html">DangerZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notification on approaching danger zones. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-995433362%2FProperties%2F1617540583" anchor-label="destinationReachedListener" id="-995433362%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="destination-reached-listener.html"><span>destination</span><wbr></wbr><span>Reached</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-995433362%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="destination-reached-listener.html">destinationReachedListener</a><span class="token operator">: </span><a href="../-destination-reached-listener/index.html">DestinationReachedListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive the notification about the arrival at the destination. Destination reached notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-608917792%2FProperties%2F1617540583" anchor-label="environmentalZoneWarningListener" id="-608917792%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="environmental-zone-warning-listener.html"><span>environmental</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-608917792%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="environmental-zone-warning-listener.html">environmentalZoneWarningListener</a><span class="token operator">: </span><a href="../-environmental-zone-warning-listener/index.html">EnvironmentalZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notification on approaching environmental zones. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1177685337%2FProperties%2F1617540583" anchor-label="eventTextListener" id="1177685337%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="event-text-listener.html"><span>event</span><wbr></wbr><span>Text</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1177685337%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="event-text-listener.html">eventTextListener</a><span class="token operator">: </span><a href="../-event-text-listener/index.html">EventTextListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive text notifications when they are available. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user. <strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner, when <code class="lang-kotlin">TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code class="lang-kotlin">sdk.navigation.EventTextListener</code> must be enabled as well.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1951255281%2FProperties%2F1617540583" anchor-label="eventTextOptions" id="-1951255281%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="event-text-options.html"><span>event</span><wbr></wbr><span>Text</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1951255281%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="event-text-options.html">eventTextOptions</a><span class="token operator">: </span><a href="../-event-text-options/index.html">EventTextOptions</a></div><div class="brief "><p class="paragraph">Options used for text notifications. Notifications are only available if a route is present.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1285600657%2FProperties%2F1617540583" anchor-label="isEnableTunnelExtrapolation" id="1285600657%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-enable-tunnel-extrapolation.html"><span>is</span><wbr></wbr><span>Enable</span><wbr></wbr><span>Tunnel</span><wbr></wbr><span><span>Extrapolation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1285600657%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="is-enable-tunnel-extrapolation.html">isEnableTunnelExtrapolation</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Defines whether to enable or disable tunnel extrapolation. By default the tunnel extrapolation is enabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-639158560%2FProperties%2F1617540583" anchor-label="isPassthroughWaypointsHandlingEnabled" id="-639158560%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-passthrough-waypoints-handling-enabled.html"><span>is</span><wbr></wbr><span>Passthrough</span><wbr></wbr><span>Waypoints</span><wbr></wbr><span>Handling</span><wbr></wbr><span><span>Enabled</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-639158560%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="is-passthrough-waypoints-handling-enabled.html">isPassthroughWaypointsHandlingEnabled</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Defines whether to enable or disable handling of passthrough waypoints. By default the handling of passthrough waypoints is disabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1238745397%2FProperties%2F1617540583" anchor-label="junctionViewLaneAssistanceListener" id="1238745397%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="junction-view-lane-assistance-listener.html"><span>junction</span><wbr></wbr><span>View</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1238745397%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="junction-view-lane-assistance-listener.html">junctionViewLaneAssistanceListener</a><span class="token operator">: </span><a href="../-junction-view-lane-assistance-listener/index.html">JunctionViewLaneAssistanceListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive junction view lane assistance notifications. Junction view lane assistance notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1199019068%2FProperties%2F1617540583" anchor-label="locationManager" id="1199019068%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="location-manager.html"><span>location</span><wbr></wbr><span><span>Manager</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1199019068%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="location-manager.html">locationManager</a><span class="token operator">: </span><a href="../../com.here.sdk.mapmatcher/-location-manager/index.html">LocationManager</a></div><div class="brief "><p class="paragraph">The location manager used by the navigator for map-matched location processing.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-240435389%2FProperties%2F1617540583" anchor-label="lowSpeedZoneWarningListener" id="-240435389%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="low-speed-zone-warning-listener.html"><span>low</span><wbr></wbr><span>Speed</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-240435389%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="low-speed-zone-warning-listener.html">lowSpeedZoneWarningListener</a><span class="token operator">: </span><a href="../-low-speed-zone-warning-listener/index.html">LowSpeedZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about low speed zones on the current road. Low speed zone notifications are given regardless if a route is set. This listener is currently available <i>only</i> for Japan. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1492445082%2FProperties%2F1617540583" anchor-label="maneuverNotificationOptions" id="1492445082%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="maneuver-notification-options.html"><span>maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1492445082%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="maneuver-notification-options.html">maneuverNotificationOptions</a><span class="token operator">: </span><a href="../-maneuver-notification-options/index.html">ManeuverNotificationOptions</a></div><div class="brief "><p class="paragraph">Options used for maneuver notifications. Notifications are only available if a route is present.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="732904592%2FProperties%2F1617540583" anchor-label="maneuverViewLaneAssistanceListener" id="732904592%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="maneuver-view-lane-assistance-listener.html"><span>maneuver</span><wbr></wbr><span>View</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="732904592%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="maneuver-view-lane-assistance-listener.html">maneuverViewLaneAssistanceListener</a><span class="token operator">: </span><a href="../-maneuver-view-lane-assistance-listener/index.html">ManeuverViewLaneAssistanceListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive maneuver view lane assistance notifications. Maneuver view lane assistance notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1789672226%2FProperties%2F1617540583" anchor-label="milestoneStatusListener" id="-1789672226%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="milestone-status-listener.html"><span>milestone</span><wbr></wbr><span>Status</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1789672226%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="milestone-status-listener.html">milestoneStatusListener</a><span class="token operator">: </span><a href="../-milestone-status-listener/index.html">MilestoneStatusListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the arrival at each <a href="../-milestone/index.html">com.here.sdk.navigation.Milestone</a> or missing it. It informs on all waypoints (passed or missed) that are of type <a href="../-milestone-type/-s-t-o-p-o-v-e-r/index.html">com.here.sdk.navigation.MilestoneType.STOPOVER</a> but excludes the starting waypoint. Waypoints of type <a href="../-milestone-type/-p-a-s-s-t-h-r-o-u-g-h/index.html">com.here.sdk.navigation.MilestoneType.PASSTHROUGH</a> are excluded, by default, but can be included via <a href="is-passthrough-waypoints-handling-enabled.html">com.here.sdk.navigation.NavigatorInterface.isPassthroughWaypointsHandlingEnabled</a>. Milestone status notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="391250736%2FProperties%2F1617540583" anchor-label="navigableLocationListener" id="391250736%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="navigable-location-listener.html"><span>navigable</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="391250736%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="navigable-location-listener.html">navigableLocationListener</a><span class="token operator">: </span><a href="../-navigable-location-listener/index.html">NavigableLocationListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the current location. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1853366989%2FProperties%2F1617540583" anchor-label="offRoadDestinationReachedListener" id="1853366989%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="off-road-destination-reached-listener.html"><span>off</span><wbr></wbr><span>Road</span><wbr></wbr><span>Destination</span><wbr></wbr><span>Reached</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1853366989%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="off-road-destination-reached-listener.html">offRoadDestinationReachedListener</a><span class="token operator">: </span><a href="../-off-road-destination-reached-listener/index.html">OffRoadDestinationReachedListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive the notification about the arrival at the off-road destination. Off-road destination reached notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="574698788%2FProperties%2F1617540583" anchor-label="offRoadProgressListener" id="574698788%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="off-road-progress-listener.html"><span>off</span><wbr></wbr><span>Road</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="574698788%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="off-road-progress-listener.html">offRoadProgressListener</a><span class="token operator">: </span><a href="../-off-road-progress-listener/index.html">OffRoadProgressListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive the notification about the off-road progress. Off-road progress notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-719001060%2FProperties%2F1617540583" anchor-label="postActionListener" id="-719001060%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="post-action-listener.html"><span>post</span><wbr></wbr><span>Action</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-719001060%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="post-action-listener.html">postActionListener</a><span class="token operator">: </span><a href="../-post-action-listener/index.html">PostActionListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive post action notifications, such as a charge action at a charging station. Post actions notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1481227595%2FProperties%2F1617540583" anchor-label="railwayCrossingWarningListener" id="-1481227595%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="railway-crossing-warning-listener.html"><span>railway</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1481227595%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="railway-crossing-warning-listener.html">railwayCrossingWarningListener</a><span class="token operator">: </span><a href="../-railway-crossing-warning-listener/index.html">RailwayCrossingWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about railway crossings on the current road. Railway crossing notifications are given regardless if a route is set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1097654239%2FProperties%2F1617540583" anchor-label="realisticViewWarningListener" id="-1097654239%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="realistic-view-warning-listener.html"><span>realistic</span><wbr></wbr><span>View</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1097654239%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="realistic-view-warning-listener.html">realisticViewWarningListener</a><span class="token operator">: </span><a href="../-realistic-view-warning-listener/index.html">RealisticViewWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about junction views on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. This feature requires a map version greater or equal to 67 in order to function properly. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1023387975%2FProperties%2F1617540583" anchor-label="realisticViewWarningOptions" id="1023387975%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="realistic-view-warning-options.html"><span>realistic</span><wbr></wbr><span>View</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1023387975%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="realistic-view-warning-options.html">realisticViewWarningOptions</a><span class="token operator">: </span><a href="../-realistic-view-warning-options/index.html">RealisticViewWarningOptions</a></div><div class="brief "><p class="paragraph">Realistic view warning options. It allow to filter realistic views to be passed to <a href="../-realistic-view-warning-listener/index.html">com.here.sdk.navigation.RealisticViewWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="467022875%2FProperties%2F1617540583" anchor-label="roadAttributesListener" id="467022875%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="road-attributes-listener.html"><span>road</span><wbr></wbr><span>Attributes</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="467022875%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="road-attributes-listener.html">roadAttributesListener</a><span class="token operator">: </span><a href="../-road-attributes-listener/index.html">RoadAttributesListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about attributes of the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1023698465%2FProperties%2F1617540583" anchor-label="roadSignWarningListener" id="1023698465%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="road-sign-warning-listener.html"><span>road</span><wbr></wbr><span>Sign</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1023698465%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="road-sign-warning-listener.html">roadSignWarningListener</a><span class="token operator">: </span><a href="../-road-sign-warning-listener/index.html">RoadSignWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about road signs on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="676176711%2FProperties%2F1617540583" anchor-label="roadSignWarningOptions" id="676176711%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="road-sign-warning-options.html"><span>road</span><wbr></wbr><span>Sign</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="676176711%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="road-sign-warning-options.html">roadSignWarningOptions</a><span class="token operator">: </span><a href="../-road-sign-warning-options/index.html">RoadSignWarningOptions</a></div><div class="brief "><p class="paragraph">Road sign warning options that allow to filter road sings to be passed to <a href="../-road-sign-warning-listener/index.html">com.here.sdk.navigation.RoadSignWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2089612678%2FProperties%2F1617540583" anchor-label="roadTextsListener" id="-2089612678%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="road-texts-listener.html"><span>road</span><wbr></wbr><span>Texts</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2089612678%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="road-texts-listener.html">roadTextsListener</a><span class="token operator">: </span><a href="../-road-texts-listener/index.html">RoadTextsListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the textual attributes of the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="205206027%2FProperties%2F1617540583" anchor-label="route" id="205206027%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="route.html"><span><span>route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="205206027%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="route.html">route</a><span class="token operator">: </span><a href="../../com.here.sdk.routing/-route/index.html">Route</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The route to navigate. Gets and sets the route that is being navigated. If not set, only the current location information will be provided through <a href="../-navigable-location-listener/index.html">com.here.sdk.navigation.NavigableLocationListener</a>. If set, both route progress (<a href="../-route-progress-listener/index.html">com.here.sdk.navigation.RouteProgressListener</a>) and route deviation (<a href="../-route-deviation-listener/index.html">com.here.sdk.navigation.RouteDeviationListener</a>) will receive notifications on updates. A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1214143334%2FProperties%2F1617540583" anchor-label="routeDeviationListener" id="-1214143334%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="route-deviation-listener.html"><span>route</span><wbr></wbr><span>Deviation</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1214143334%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="route-deviation-listener.html">routeDeviationListener</a><span class="token operator">: </span><a href="../-route-deviation-listener/index.html">RouteDeviationListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about deviations from the route if any occurs. Route deviation notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="658184970%2FProperties%2F1617540583" anchor-label="routeProgressListener" id="658184970%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="route-progress-listener.html"><span>route</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="658184970%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="route-progress-listener.html">routeProgressListener</a><span class="token operator">: </span><a href="../-route-progress-listener/index.html">RouteProgressListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about navigation route progress. Route progress notifications only occurs if the route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2104014907%2FProperties%2F1617540583" anchor-label="safetyCameraWarningListener" id="2104014907%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="safety-camera-warning-listener.html"><span>safety</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2104014907%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="safety-camera-warning-listener.html">safetyCameraWarningListener</a><span class="token operator">: </span><a href="../-safety-camera-warning-listener/index.html">SafetyCameraWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive safety camera warner notifications. If a listener  is present, notifications about safety speed cameras will be also sent via <a href="../-safety-camera-warning-listener/index.html">com.here.sdk.navigation.SafetyCameraWarningListener</a>. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1265214957%2FProperties%2F1617540583" anchor-label="safetyCameraWarningOptions" id="1265214957%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="safety-camera-warning-options.html"><span>safety</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1265214957%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="safety-camera-warning-options.html">safetyCameraWarningOptions</a><span class="token operator">: </span><a href="../-safety-camera-warning-options/index.html">SafetyCameraWarningOptions</a></div><div class="brief "><p class="paragraph">Safety camera warning options to be passed to <a href="../-safety-camera-warning-listener/index.html">com.here.sdk.navigation.SafetyCameraWarningListener</a>. These options allow the enabling or disabling the text notification for the warner.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1631834716%2FProperties%2F1617540583" anchor-label="schoolZoneWarningListener" id="-1631834716%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="school-zone-warning-listener.html"><span>school</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1631834716%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="school-zone-warning-listener.html">schoolZoneWarningListener</a><span class="token operator">: </span><a href="../-school-zone-warning-listener/index.html">SchoolZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about school zones on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. school zones on the current road. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1903337628%2FProperties%2F1617540583" anchor-label="schoolZoneWarningOptions" id="-1903337628%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="school-zone-warning-options.html"><span>school</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1903337628%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="school-zone-warning-options.html">schoolZoneWarningOptions</a><span class="token operator">: </span><a href="../-school-zone-warning-options/index.html">SchoolZoneWarningOptions</a></div><div class="brief "><p class="paragraph">School zone warning options It allow to configure school zone notifications to be passed to <a href="../-school-zone-warning-listener/index.html">com.here.sdk.navigation.SchoolZoneWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2079429918%2FProperties%2F1617540583" anchor-label="speedLimitListener" id="2079429918%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="speed-limit-listener.html"><span>speed</span><wbr></wbr><span>Limit</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2079429918%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="speed-limit-listener.html">speedLimitListener</a><span class="token operator">: </span><a href="../-speed-limit-listener/index.html">SpeedLimitListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the speed limit of the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="461909341%2FProperties%2F1617540583" anchor-label="speedWarningListener" id="461909341%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="speed-warning-listener.html"><span>speed</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="461909341%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="speed-warning-listener.html">speedWarningListener</a><span class="token operator">: </span><a href="../-speed-warning-listener/index.html">SpeedWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1697250165%2FProperties%2F1617540583" anchor-label="speedWarningOptions" id="-1697250165%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="speed-warning-options.html"><span>speed</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1697250165%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="speed-warning-options.html">speedWarningOptions</a><span class="token operator">: </span><a href="../-speed-warning-options/index.html">SpeedWarningOptions</a></div><div class="brief "><p class="paragraph">Options used for the speed warning feature.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1409510143%2FProperties%2F1617540583" anchor-label="tollStopWarningListener" id="-1409510143%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="toll-stop-warning-listener.html"><span>toll</span><wbr></wbr><span>Stop</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1409510143%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="toll-stop-warning-listener.html">tollStopWarningListener</a><span class="token operator">: </span><a href="../-toll-stop-warning-listener/index.html">TollStopWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive information on the upcoming toll stop. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1306376529%2FProperties%2F1617540583" anchor-label="trackingTransportProfile" id="-1306376529%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="tracking-transport-profile.html"><span>tracking</span><wbr></wbr><span>Transport</span><wbr></wbr><span><span>Profile</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1306376529%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="tracking-transport-profile.html"><strike>trackingTransportProfile</strike></a><span class="token operator">: </span><a href="../../com.here.sdk.core/-transport-profile/index.html">TransportProfile</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Defines the transport profile for the <a href="../-navigator/index.html">com.here.sdk.navigation.Navigator</a>, when no route is present. Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a <a href="../../com.here.sdk.core/-transport-profile/index.html">com.here.sdk.core.TransportProfile</a> can be defined with a <a href="../../com.here.sdk.transport/-vehicle-profile/index.html">com.here.sdk.transport.VehicleProfile</a>. A vehicle profile can have several parameters such as <a href="../../com.here.sdk.transport/-vehicle-type/index.html">com.here.sdk.transport.VehicleType</a> to set the source of information describing the vehicle. The default is a <a href="../../com.here.sdk.transport/-vehicle-type/-c-a-r/index.html">com.here.sdk.transport.VehicleType.CAR</a> profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1812406357%2FProperties%2F1617540583" anchor-label="trackingTransportSpecification" id="1812406357%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="tracking-transport-specification.html"><span>tracking</span><wbr></wbr><span>Transport</span><wbr></wbr><span><span>Specification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1812406357%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="tracking-transport-specification.html">trackingTransportSpecification</a><span class="token operator">: </span><a href="../../com.here.sdk.transport/-transport-specification/index.html">TransportSpecification</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Defines the transport specification for the <a href="../-navigator/index.html">com.here.sdk.navigation.Navigator</a>, when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An <a href="../../com.here.sdk.transport/-transport-specification/index.html">com.here.sdk.transport.TransportSpecification</a> must have the <a href="../../com.here.sdk.transport/-transport-specification/transport-mode.html">com.here.sdk.transport.TransportSpecification.transportMode</a> set. A transport specification can have several parameters defined such as <a href="../../com.here.sdk.transport/-vehicle-specification/length-in-centimeters.html">com.here.sdk.transport.VehicleSpecification.lengthInCentimeters</a> defined in <a href="../../com.here.sdk.transport/-transport-specification/vehicle-specification.html">com.here.sdk.transport.TransportSpecification.vehicleSpecification</a> to set the source of information describing the vehicle. By default the <a href="../../com.here.sdk.transport/-transport-specification/index.html">com.here.sdk.transport.TransportSpecification</a> will have the transport mode set to <a href="../../com.here.sdk.transport/-transport-mode/-c-a-r/index.html">com.here.sdk.transport.TransportMode.CAR</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1987683295%2FProperties%2F1617540583" anchor-label="trafficMergeWarningListener" id="1987683295%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="traffic-merge-warning-listener.html"><span>traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1987683295%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="traffic-merge-warning-listener.html">trafficMergeWarningListener</a><span class="token operator">: </span><a href="../-traffic-merge-warning-listener/index.html">TrafficMergeWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about merging traffic to the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1954198985%2FProperties%2F1617540583" anchor-label="trafficMergeWarningOptions" id="1954198985%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="traffic-merge-warning-options.html"><span>traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1954198985%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="traffic-merge-warning-options.html">trafficMergeWarningOptions</a><span class="token operator">: </span><a href="../-traffic-merge-warning-options/index.html">TrafficMergeWarningOptions</a></div><div class="brief "><p class="paragraph">Merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="../-traffic-merge-warning-listener/index.html">com.here.sdk.navigation.TrafficMergeWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1115100455%2FProperties%2F1617540583" anchor-label="trafficOnRoute" id="-1115100455%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="traffic-on-route.html"><span>traffic</span><wbr></wbr><span>On</span><wbr></wbr><span><span>Route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1115100455%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="traffic-on-route.html">trafficOnRoute</a><span class="token operator">: </span><a href="../../com.here.sdk.routing/-traffic-on-route/index.html">TrafficOnRoute</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Traffic information for the current route. This impacts <code class="lang-kotlin">RouteProgress</code> updates as the duration of the <code class="lang-kotlin">SectionProgress</code> might change. However, the remaining distance and the route geometry will remain unchanged.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1027650372%2FProperties%2F1617540583" anchor-label="truckRestrictionsWarningListener" id="-1027650372%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="truck-restrictions-warning-listener.html"><span>truck</span><wbr></wbr><span>Restrictions</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1027650372%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="truck-restrictions-warning-listener.html">truckRestrictionsWarningListener</a><span class="token operator">: </span><a href="../-truck-restrictions-warning-listener/index.html">TruckRestrictionsWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about truck restrictions on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="748551500%2FProperties%2F1617540583" anchor-label="truckRestrictionsWarningOptions" id="748551500%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="truck-restrictions-warning-options.html"><span>truck</span><wbr></wbr><span>Restrictions</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="748551500%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">var </span><a href="truck-restrictions-warning-options.html">truckRestrictionsWarningOptions</a><span class="token operator">: </span><a href="../-truck-restrictions-warning-options/index.html">TruckRestrictionsWarningOptions</a></div><div class="brief "><p class="paragraph">Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="../-truck-restrictions-warning-listener/index.html">com.here.sdk.navigation.TruckRestrictionsWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="368923441%2FProperties%2F1617540583" anchor-label="warnerEngine" id="368923441%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="warner-engine.html"><span>warner</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="368923441%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="warner-engine.html">warnerEngine</a><span class="token operator">: </span><a href="../../com.here.sdk.warner/-warner-engine/index.html">WarnerEngine</a></div><div class="brief "><p class="paragraph">Warner engine used by the navigator. This engine can be used to configure navigation warnings.</p></div></div></div>
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
                  <div><a href="calculate-remaining-distance-in-meters.html"><span>calculate</span><wbr></wbr><span>Remaining</span><wbr></wbr><span>Distance</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1162826530%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="calculate-remaining-distance-in-meters.html"><span class="token function">calculateRemainingDistanceInMeters</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">coordinates<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-coordinates/index.html">GeoCoordinates</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">This method calculates the distance between the current position and given coordinates. The coordinates must be on the polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="382761955%2FFunctions%2F1617540583" anchor-label="getManeuver" id="382761955%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-maneuver.html"><span>get</span><wbr></wbr><span><span>Maneuver</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="382761955%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="get-maneuver.html"><span class="token function">getManeuver</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">index<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.routing/-maneuver/index.html">Maneuver</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns maneuver at the given index.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1040273629%2FFunctions%2F1617540583" anchor-label="getManeuverNotificationTimingOptions" id="-1040273629%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-maneuver-notification-timing-options.html"><span>get</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Timing</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1040273629%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="get-maneuver-notification-timing-options.html"><span class="token function">getManeuverNotificationTimingOptions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportMode<span class="token operator">: </span><a href="../../com.here.sdk.transport/-transport-mode/index.html">TransportMode</a><span class="token punctuation">, </span></span><span class="parameter ">timingProfile<span class="token operator">: </span><a href="../-timing-profile/index.html">TimingProfile</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-maneuver-notification-timing-options/index.html">ManeuverNotificationTimingOptions</a></div><div class="brief "><p class="paragraph">Returns maneuver notification timing options with default values given the combination of transport mode and timing profile. The return value can be used as the base for configuring maneuver notification timings. Configure the relevant attributes of this object according to your preferences, and then set it by calling setManeuverNotificationTimingOptions function for the same combination of transport mode and timing profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1281340582%2FFunctions%2F1617540583" anchor-label="getWarningNotificationDistances" id="-1281340582%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-warning-notification-distances.html"><span>get</span><wbr></wbr><span>Warning</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Distances</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1281340582%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="get-warning-notification-distances.html"><span class="token function">getWarningNotificationDistances</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningType<span class="token operator">: </span><a href="../-warning-type/index.html">WarningType</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-warning-notification-distances/index.html">WarningNotificationDistances</a></div><div class="brief "><p class="paragraph">Returns the warning notification distances for the requested warning type. The return value can be used as the base for configuring warning notification distances. Configure the relevant attributes of this object according to your preferences, and then set it by calling <code class="lang-kotlin">setWarningNotificationDistances</code> function with the same warning type and the modified warning notification distances object.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="792081649%2FFunctions%2F1617540583" anchor-label="repeatLastManeuverNotification" id="792081649%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="repeat-last-maneuver-notification.html"><span>repeat</span><wbr></wbr><span>Last</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span><span>Notification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="792081649%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="repeat-last-maneuver-notification.html"><span class="token function">repeatLastManeuverNotification</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-503485507%2FFunctions%2F1617540583" anchor-label="setCustomOption" id="-503485507%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-custom-option.html"><span>set</span><wbr></wbr><span>Custom</span><wbr></wbr><span><span>Option</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-503485507%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="set-custom-option.html"><span class="token function">setCustomOption</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">key<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">This method sets custom options that controls navigator behavior. Unsupported options are silently ignored. Undocumented options can change their meaning without going through deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1057633993%2FFunctions%2F1617540583" anchor-label="setManeuverNotificationTimingOptions" id="-1057633993%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-maneuver-notification-timing-options.html"><span>set</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Timing</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1057633993%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="set-maneuver-notification-timing-options.html"><span class="token function">setManeuverNotificationTimingOptions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportMode<span class="token operator">: </span><a href="../../com.here.sdk.transport/-transport-mode/index.html">TransportMode</a><span class="token punctuation">, </span></span><span class="parameter ">timingProfile<span class="token operator">: </span><a href="../-timing-profile/index.html">TimingProfile</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-maneuver-notification-timing-options/index.html">ManeuverNotificationTimingOptions</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Set timing option values for the combination of transport mode and timing profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-748456627%2FFunctions%2F1617540583" anchor-label="setWarningNotificationDistances" id="-748456627%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-warning-notification-distances.html"><span>set</span><wbr></wbr><span>Warning</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Distances</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-748456627%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="set-warning-notification-distances.html"><span class="token function">setWarningNotificationDistances</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningType<span class="token operator">: </span><a href="../-warning-type/index.html">WarningType</a><span class="token punctuation">, </span></span><span class="parameter ">warningNotificationDistances<span class="token operator">: </span><a href="../-warning-notification-distances/index.html">WarningNotificationDistances</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Set the warning notification distances for the specified warning types. <strong>Note:</strong> The warning notification distances are set for most warners. This method can't be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use <code class="lang-kotlin">NavigatorInterface.school_zone_warning_options</code> instead. Attempting to set the warning notification distances for the school zone warner using the <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code class="lang-kotlin">false</code>. Always use <code class="lang-kotlin">SchoolZoneWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the school zone warner regardless of the <code class="lang-kotlin">TimingProfile</code>. If <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> could be used, this would allow for different distances to be set for each timing profile, which is undesirable. Attempting to set the warning notification distances for the traffic merge warner using the <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code class="lang-kotlin">false</code>. Always use <code class="lang-kotlin">TrafficMergeWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the traffic merge warner regardless of the <code class="lang-kotlin">TimingProfile</code>. Using the <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code class="lang-kotlin">false</code> to avoid seting different distances on each timing profile since the traffic merge warning is only applicable on highways.</p></div></div></div>
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
