---
title: "Navigator"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-navigation-navigator"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>Navigator</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.navigation/Navigator///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.navigation</a><span class="delimiter">/</span><span class="current">Navigator</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Navigator</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">Navigator</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a>, <a href="../-navigator-interface/index.html">NavigatorInterface</a></div><p class="paragraph">This class provides the basic navigation functionality. It provides notifications about current map-matched location updates (see <a href="../-navigable-location/index.html">com.here.sdk.navigation.NavigableLocation</a>). And, if a route has been set, about the route progress (see <a href="../-route-progress/index.html">com.here.sdk.navigation.RouteProgress</a>), route deviations (see <a href="../-route-deviation/index.html">com.here.sdk.navigation.RouteDeviation</a>) and maneuver notifications (see <a href="../-event-text-listener/index.html">com.here.sdk.navigation.EventTextListener</a>).</p><p class="paragraph">All transport modes are supported for turn-by-turn navigation, except for public transit. Public transit routes may lead to unsafe and unexpected results.</p><p class="paragraph">Navigation support for bus routes can be sometimes a bit limited and bus lane assistance and turn-by-turn bus instructions may not be as appropriate as expected.</p><p class="paragraph">The <a href="../../com.here.sdk.transport/-transport-mode/index.html">com.here.sdk.transport.TransportMode</a> is determined from the provided <a href="../../com.here.sdk.routing/-route/index.html">com.here.sdk.routing.Route</a> instance, but the actual <a href="../../com.here.sdk.routing/-section-transport-mode/index.html">com.here.sdk.routing.SectionTransportMode</a> can vary along a route, for example, when a ferry must be taken. When no route is set, the <a href="../-navigable-location/index.html">com.here.sdk.navigation.NavigableLocation</a> assumes a drive scenario.</p><p class="paragraph">This class continuously reacts to new locations provided from a location source and acts as a <a href="../../com.here.sdk.core/-location-listener/index.html">com.here.sdk.core.LocationListener</a>. The accuracy of the positioning increases with the update frequency. At least one update per second should be provided. More information can be found at <code class="lang-kotlin">LocationAccuracy.NAVIGATION</code>.</p><p class="paragraph"><strong>Note:</strong> Even without provided locations, for example, while driving through a tunnel, this class can interpolate missing location events and still send <a href="../-navigable-location/index.html">com.here.sdk.navigation.NavigableLocation</a>, <a href="../-route-progress/index.html">com.here.sdk.navigation.RouteProgress</a> and maneuver notifications.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-1991326037%2FConstructors%2F1617540583" anchor-label="Navigator" id="-1991326037%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-navigator.html"><span><span>Navigator</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1991326037%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">sdkEngine<span class="token operator">: </span><a href="../../com.here.sdk.core.engine/-s-d-k-native-engine/index.html">SDKNativeEngine</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="370539538%2FClasslikes%2F1617540583" anchor-label="Companion" id="370539538%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="370539538%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="2019777385%2FProperties%2F1617540583" anchor-label="borderCrossingWarningListener" id="2019777385%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="border-crossing-warning-listener.html"><span>border</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2019777385%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="border-crossing-warning-listener.html">borderCrossingWarningListener</a><span class="token operator">: </span><a href="../-border-crossing-warning-listener/index.html">BorderCrossingWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about border crossings on the current road. Border crossing notifications are given only if a route is present. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1508449025%2FProperties%2F1617540583" anchor-label="borderCrossingWarningOptions" id="-1508449025%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="border-crossing-warning-options.html"><span>border</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1508449025%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="border-crossing-warning-options.html">borderCrossingWarningOptions</a><span class="token operator">: </span><a href="../-border-crossing-warning-options/index.html">BorderCrossingWarningOptions</a></div><div class="brief "><p class="paragraph">Border crossing warning options to be passed to <a href="../-border-crossing-warning-listener/index.html">com.here.sdk.navigation.BorderCrossingWarningListener</a>. These options allow the filtering of the border crossing warnings received and set the notification distances.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1111950701%2FProperties%2F1617540583" anchor-label="currentSituationLaneAssistanceViewListener" id="1111950701%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="current-situation-lane-assistance-view-listener.html"><span>current</span><wbr></wbr><span>Situation</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span>View</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1111950701%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="current-situation-lane-assistance-view-listener.html">currentSituationLaneAssistanceViewListener</a><span class="token operator">: </span><a href="../-current-situation-lane-assistance-view-listener/index.html">CurrentSituationLaneAssistanceViewListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive current situation lane assistance view notifications. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-7856662%2FProperties%2F1617540583" anchor-label="dangerZoneWarningListener" id="-7856662%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="danger-zone-warning-listener.html"><span>danger</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-7856662%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="danger-zone-warning-listener.html">dangerZoneWarningListener</a><span class="token operator">: </span><a href="../-danger-zone-warning-listener/index.html">DangerZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notification on approaching danger zones. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1693099831%2FProperties%2F1617540583" anchor-label="destinationReachedListener" id="1693099831%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="destination-reached-listener.html"><span>destination</span><wbr></wbr><span>Reached</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1693099831%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="destination-reached-listener.html">destinationReachedListener</a><span class="token operator">: </span><a href="../-destination-reached-listener/index.html">DestinationReachedListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive the notification about the arrival at the destination. Destination reached notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="308244201%2FProperties%2F1617540583" anchor-label="environmentalZoneWarningListener" id="308244201%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="environmental-zone-warning-listener.html"><span>environmental</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="308244201%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="environmental-zone-warning-listener.html">environmentalZoneWarningListener</a><span class="token operator">: </span><a href="../-environmental-zone-warning-listener/index.html">EnvironmentalZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notification on approaching environmental zones. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1527469168%2FProperties%2F1617540583" anchor-label="eventTextListener" id="1527469168%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="event-text-listener.html"><span>event</span><wbr></wbr><span>Text</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1527469168%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="event-text-listener.html">eventTextListener</a><span class="token operator">: </span><a href="../-event-text-listener/index.html">EventTextListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive text notifications when they are available. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user. <strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner, when <code class="lang-kotlin">TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code class="lang-kotlin">sdk.navigation.EventTextListener</code> must be enabled as well.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1939353368%2FProperties%2F1617540583" anchor-label="eventTextOptions" id="1939353368%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="event-text-options.html"><span>event</span><wbr></wbr><span>Text</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1939353368%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="event-text-options.html">eventTextOptions</a><span class="token operator">: </span><a href="../-event-text-options/index.html">EventTextOptions</a></div><div class="brief "><p class="paragraph">Options used for text notifications. Notifications are only available if a route is present.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1269216280%2FProperties%2F1617540583" anchor-label="isEnableTunnelExtrapolation" id="-1269216280%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-enable-tunnel-extrapolation.html"><span>is</span><wbr></wbr><span>Enable</span><wbr></wbr><span>Tunnel</span><wbr></wbr><span><span>Extrapolation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1269216280%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="is-enable-tunnel-extrapolation.html">isEnableTunnelExtrapolation</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Defines whether to enable or disable tunnel extrapolation. By default the tunnel extrapolation is enabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1777005449%2FProperties%2F1617540583" anchor-label="isPassthroughWaypointsHandlingEnabled" id="-1777005449%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-passthrough-waypoints-handling-enabled.html"><span>is</span><wbr></wbr><span>Passthrough</span><wbr></wbr><span>Waypoints</span><wbr></wbr><span>Handling</span><wbr></wbr><span><span>Enabled</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1777005449%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="is-passthrough-waypoints-handling-enabled.html">isPassthroughWaypointsHandlingEnabled</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Defines whether to enable or disable handling of passthrough waypoints. By default the handling of passthrough waypoints is disabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2131842306%2FProperties%2F1617540583" anchor-label="junctionViewLaneAssistanceListener" id="-2131842306%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="junction-view-lane-assistance-listener.html"><span>junction</span><wbr></wbr><span>View</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2131842306%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="junction-view-lane-assistance-listener.html">junctionViewLaneAssistanceListener</a><span class="token operator">: </span><a href="../-junction-view-lane-assistance-listener/index.html">JunctionViewLaneAssistanceListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive junction view lane assistance notifications. Junction view lane assistance notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-615140077%2FProperties%2F1617540583" anchor-label="locationManager" id="-615140077%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="location-manager.html"><span>location</span><wbr></wbr><span><span>Manager</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-615140077%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">val </span><a href="location-manager.html">locationManager</a><span class="token operator">: </span><a href="../../com.here.sdk.mapmatcher/-location-manager/index.html">LocationManager</a></div><div class="brief "><p class="paragraph">The location manager used by the navigator for map-matched location processing.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1499714970%2FProperties%2F1617540583" anchor-label="lowSpeedZoneWarningListener" id="1499714970%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="low-speed-zone-warning-listener.html"><span>low</span><wbr></wbr><span>Speed</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1499714970%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="low-speed-zone-warning-listener.html">lowSpeedZoneWarningListener</a><span class="token operator">: </span><a href="../-low-speed-zone-warning-listener/index.html">LowSpeedZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about low speed zones on the current road. Low speed zone notifications are given regardless if a route is set. This listener is currently available <i>only</i> for Japan. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1062371855%2FProperties%2F1617540583" anchor-label="maneuverNotificationOptions" id="-1062371855%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="maneuver-notification-options.html"><span>maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1062371855%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="maneuver-notification-options.html">maneuverNotificationOptions</a><span class="token operator">: </span><a href="../-maneuver-notification-options/index.html">ManeuverNotificationOptions</a></div><div class="brief "><p class="paragraph">Options used for maneuver notifications. Notifications are only available if a route is present.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1657284185%2FProperties%2F1617540583" anchor-label="maneuverViewLaneAssistanceListener" id="1657284185%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="maneuver-view-lane-assistance-listener.html"><span>maneuver</span><wbr></wbr><span>View</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1657284185%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="maneuver-view-lane-assistance-listener.html">maneuverViewLaneAssistanceListener</a><span class="token operator">: </span><a href="../-maneuver-view-lane-assistance-listener/index.html">ManeuverViewLaneAssistanceListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive maneuver view lane assistance notifications. Maneuver view lane assistance notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2123046581%2FProperties%2F1617540583" anchor-label="milestoneStatusListener" id="2123046581%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="milestone-status-listener.html"><span>milestone</span><wbr></wbr><span>Status</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2123046581%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="milestone-status-listener.html">milestoneStatusListener</a><span class="token operator">: </span><a href="../-milestone-status-listener/index.html">MilestoneStatusListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the arrival at each <a href="../-milestone/index.html">com.here.sdk.navigation.Milestone</a> or missing it. It informs on all waypoints (passed or missed) that are of type <a href="../-milestone-type/-s-t-o-p-o-v-e-r/index.html">com.here.sdk.navigation.MilestoneType.STOPOVER</a> but excludes the starting waypoint. Waypoints of type <a href="../-milestone-type/-p-a-s-s-t-h-r-o-u-g-h/index.html">com.here.sdk.navigation.MilestoneType.PASSTHROUGH</a> are excluded, by default, but can be included via <a href="../-navigator-interface/is-passthrough-waypoints-handling-enabled.html">com.here.sdk.navigation.NavigatorInterface.isPassthroughWaypointsHandlingEnabled</a>. Milestone status notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1877327033%2FProperties%2F1617540583" anchor-label="navigableLocationListener" id="-1877327033%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="navigable-location-listener.html"><span>navigable</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1877327033%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="navigable-location-listener.html">navigableLocationListener</a><span class="token operator">: </span><a href="../-navigable-location-listener/index.html">NavigableLocationListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the current location. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="220617700%2FProperties%2F1617540583" anchor-label="offRoadDestinationReachedListener" id="220617700%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="off-road-destination-reached-listener.html"><span>off</span><wbr></wbr><span>Road</span><wbr></wbr><span>Destination</span><wbr></wbr><span>Reached</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="220617700%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="off-road-destination-reached-listener.html">offRoadDestinationReachedListener</a><span class="token operator">: </span><a href="../-off-road-destination-reached-listener/index.html">OffRoadDestinationReachedListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive the notification about the arrival at the off-road destination. Off-road destination reached notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="192450299%2FProperties%2F1617540583" anchor-label="offRoadProgressListener" id="192450299%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="off-road-progress-listener.html"><span>off</span><wbr></wbr><span>Road</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="192450299%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="off-road-progress-listener.html">offRoadProgressListener</a><span class="token operator">: </span><a href="../-off-road-progress-listener/index.html">OffRoadProgressListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive the notification about the off-road progress. Off-road progress notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1534363109%2FProperties%2F1617540583" anchor-label="postActionListener" id="1534363109%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="post-action-listener.html"><span>post</span><wbr></wbr><span>Action</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1534363109%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="post-action-listener.html">postActionListener</a><span class="token operator">: </span><a href="../-post-action-listener/index.html">PostActionListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive post action notifications, such as a charge action at a charging station. Post actions notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-917145346%2FProperties%2F1617540583" anchor-label="railwayCrossingWarningListener" id="-917145346%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="railway-crossing-warning-listener.html"><span>railway</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-917145346%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="railway-crossing-warning-listener.html">railwayCrossingWarningListener</a><span class="token operator">: </span><a href="../-railway-crossing-warning-listener/index.html">RailwayCrossingWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about railway crossings on the current road. Railway crossing notifications are given regardless if a route is set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1307399338%2FProperties%2F1617540583" anchor-label="realisticViewWarningListener" id="1307399338%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="realistic-view-warning-listener.html"><span>realistic</span><wbr></wbr><span>View</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1307399338%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="realistic-view-warning-listener.html">realisticViewWarningListener</a><span class="token operator">: </span><a href="../-realistic-view-warning-listener/index.html">RealisticViewWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about junction views on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. This feature requires a map version greater or equal to 67 in order to function properly. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1531428962%2FProperties%2F1617540583" anchor-label="realisticViewWarningOptions" id="-1531428962%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="realistic-view-warning-options.html"><span>realistic</span><wbr></wbr><span>View</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1531428962%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="realistic-view-warning-options.html">realisticViewWarningOptions</a><span class="token operator">: </span><a href="../-realistic-view-warning-options/index.html">RealisticViewWarningOptions</a></div><div class="brief "><p class="paragraph">Realistic view warning options. It allow to filter realistic views to be passed to <a href="../-realistic-view-warning-listener/index.html">com.here.sdk.navigation.RealisticViewWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1978712932%2FProperties%2F1617540583" anchor-label="roadAttributesListener" id="1978712932%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="road-attributes-listener.html"><span>road</span><wbr></wbr><span>Attributes</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1978712932%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="road-attributes-listener.html">roadAttributesListener</a><span class="token operator">: </span><a href="../-road-attributes-listener/index.html">RoadAttributesListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about attributes of the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="641449976%2FProperties%2F1617540583" anchor-label="roadSignWarningListener" id="641449976%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="road-sign-warning-listener.html"><span>road</span><wbr></wbr><span>Sign</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="641449976%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="road-sign-warning-listener.html">roadSignWarningListener</a><span class="token operator">: </span><a href="../-road-sign-warning-listener/index.html">RoadSignWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about road signs on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2107100528%2FProperties%2F1617540583" anchor-label="roadSignWarningOptions" id="-2107100528%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="road-sign-warning-options.html"><span>road</span><wbr></wbr><span>Sign</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2107100528%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="road-sign-warning-options.html">roadSignWarningOptions</a><span class="token operator">: </span><a href="../-road-sign-warning-options/index.html">RoadSignWarningOptions</a></div><div class="brief "><p class="paragraph">Road sign warning options that allow to filter road sings to be passed to <a href="../-road-sign-warning-listener/index.html">com.here.sdk.navigation.RoadSignWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1739828847%2FProperties%2F1617540583" anchor-label="roadTextsListener" id="-1739828847%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="road-texts-listener.html"><span>road</span><wbr></wbr><span>Texts</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1739828847%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="road-texts-listener.html">roadTextsListener</a><span class="token operator">: </span><a href="../-road-texts-listener/index.html">RoadTextsListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the textual attributes of the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2049778594%2FProperties%2F1617540583" anchor-label="route" id="2049778594%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="route.html"><span><span>route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2049778594%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="route.html">route</a><span class="token operator">: </span><a href="../../com.here.sdk.routing/-route/index.html">Route</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The route to navigate. Gets and sets the route that is being navigated. If not set, only the current location information will be provided through <a href="../-navigable-location-listener/index.html">com.here.sdk.navigation.NavigableLocationListener</a>. If set, both route progress (<a href="../-route-progress-listener/index.html">com.here.sdk.navigation.RouteProgressListener</a>) and route deviation (<a href="../-route-deviation-listener/index.html">com.here.sdk.navigation.RouteDeviationListener</a>) will receive notifications on updates. A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="297546723%2FProperties%2F1617540583" anchor-label="routeDeviationListener" id="297546723%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="route-deviation-listener.html"><span>route</span><wbr></wbr><span>Deviation</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="297546723%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="route-deviation-listener.html">routeDeviationListener</a><span class="token operator">: </span><a href="../-route-deviation-listener/index.html">RouteDeviationListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about deviations from the route if any occurs. Route deviation notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="291307169%2FProperties%2F1617540583" anchor-label="routeProgressListener" id="291307169%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="route-progress-listener.html"><span>route</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="291307169%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="route-progress-listener.html">routeProgressListener</a><span class="token operator">: </span><a href="../-route-progress-listener/index.html">RouteProgressListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about navigation route progress. Route progress notifications only occurs if the route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-450802030%2FProperties%2F1617540583" anchor-label="safetyCameraWarningListener" id="-450802030%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="safety-camera-warning-listener.html"><span>safety</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-450802030%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="safety-camera-warning-listener.html">safetyCameraWarningListener</a><span class="token operator">: </span><a href="../-safety-camera-warning-listener/index.html">SafetyCameraWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive safety camera warner notifications. If a listener  is present, notifications about safety speed cameras will be also sent via <a href="../-safety-camera-warning-listener/index.html">com.here.sdk.navigation.SafetyCameraWarningListener</a>. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-341219146%2FProperties%2F1617540583" anchor-label="safetyCameraWarningOptions" id="-341219146%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="safety-camera-warning-options.html"><span>safety</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-341219146%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="safety-camera-warning-options.html">safetyCameraWarningOptions</a><span class="token operator">: </span><a href="../-safety-camera-warning-options/index.html">SafetyCameraWarningOptions</a></div><div class="brief "><p class="paragraph">Safety camera warning options to be passed to <a href="../-safety-camera-warning-listener/index.html">com.here.sdk.navigation.SafetyCameraWarningListener</a>. These options allow the enabling or disabling the text notification for the warner.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="394554811%2FProperties%2F1617540583" anchor-label="schoolZoneWarningListener" id="394554811%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="school-zone-warning-listener.html"><span>school</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="394554811%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="school-zone-warning-listener.html">schoolZoneWarningListener</a><span class="token operator">: </span><a href="../-school-zone-warning-listener/index.html">SchoolZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about school zones on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. school zones on the current road. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-868138899%2FProperties%2F1617540583" anchor-label="schoolZoneWarningOptions" id="-868138899%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="school-zone-warning-options.html"><span>school</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-868138899%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="school-zone-warning-options.html">schoolZoneWarningOptions</a><span class="token operator">: </span><a href="../-school-zone-warning-options/index.html">SchoolZoneWarningOptions</a></div><div class="brief "><p class="paragraph">School zone warning options It allow to configure school zone notifications to be passed to <a href="../-school-zone-warning-listener/index.html">com.here.sdk.navigation.SchoolZoneWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="37826791%2FProperties%2F1617540583" anchor-label="speedLimitListener" id="37826791%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="speed-limit-listener.html"><span>speed</span><wbr></wbr><span>Limit</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="37826791%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="speed-limit-listener.html">speedLimitListener</a><span class="token operator">: </span><a href="../-speed-limit-listener/index.html">SpeedLimitListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the speed limit of the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1281358566%2FProperties%2F1617540583" anchor-label="speedWarningListener" id="1281358566%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="speed-warning-listener.html"><span>speed</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1281358566%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="speed-warning-listener.html">speedWarningListener</a><span class="token operator">: </span><a href="../-speed-warning-listener/index.html">SpeedWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-562437662%2FProperties%2F1617540583" anchor-label="speedWarningOptions" id="-562437662%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="speed-warning-options.html"><span>speed</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-562437662%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="speed-warning-options.html">speedWarningOptions</a><span class="token operator">: </span><a href="../-speed-warning-options/index.html">SpeedWarningOptions</a></div><div class="brief "><p class="paragraph">Options used for the speed warning feature.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1791758632%2FProperties%2F1617540583" anchor-label="tollStopWarningListener" id="-1791758632%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="toll-stop-warning-listener.html"><span>toll</span><wbr></wbr><span>Stop</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1791758632%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="toll-stop-warning-listener.html">tollStopWarningListener</a><span class="token operator">: </span><a href="../-toll-stop-warning-listener/index.html">TollStopWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive information on the upcoming toll stop. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-271177800%2FProperties%2F1617540583" anchor-label="trackingTransportProfile" id="-271177800%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="tracking-transport-profile.html"><span>tracking</span><wbr></wbr><span>Transport</span><wbr></wbr><span><span>Profile</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-271177800%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="tracking-transport-profile.html"><strike>trackingTransportProfile</strike></a><span class="token operator">: </span><a href="../../com.here.sdk.core/-transport-profile/index.html">TransportProfile</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Defines the transport profile for the <a href="index.html">com.here.sdk.navigation.Navigator</a>, when no route is present. Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a <a href="../../com.here.sdk.core/-transport-profile/index.html">com.here.sdk.core.TransportProfile</a> can be defined with a <a href="../../com.here.sdk.transport/-vehicle-profile/index.html">com.here.sdk.transport.VehicleProfile</a>. A vehicle profile can have several parameters such as <a href="../../com.here.sdk.transport/-vehicle-type/index.html">com.here.sdk.transport.VehicleType</a> to set the source of information describing the vehicle. The default is a <a href="../../com.here.sdk.transport/-vehicle-type/-c-a-r/index.html">com.here.sdk.transport.VehicleType.CAR</a> profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1918478690%2FProperties%2F1617540583" anchor-label="trackingTransportSpecification" id="-1918478690%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="tracking-transport-specification.html"><span>tracking</span><wbr></wbr><span>Transport</span><wbr></wbr><span><span>Specification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1918478690%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="tracking-transport-specification.html">trackingTransportSpecification</a><span class="token operator">: </span><a href="../../com.here.sdk.transport/-transport-specification/index.html">TransportSpecification</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Defines the transport specification for the <a href="index.html">com.here.sdk.navigation.Navigator</a>, when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An <a href="../../com.here.sdk.transport/-transport-specification/index.html">com.here.sdk.transport.TransportSpecification</a> must have the <a href="../../com.here.sdk.transport/-transport-specification/transport-mode.html">com.here.sdk.transport.TransportSpecification.transportMode</a> set. A transport specification can have several parameters defined such as <a href="../../com.here.sdk.transport/-vehicle-specification/length-in-centimeters.html">com.here.sdk.transport.VehicleSpecification.lengthInCentimeters</a> defined in <a href="../../com.here.sdk.transport/-transport-specification/vehicle-specification.html">com.here.sdk.transport.TransportSpecification.vehicleSpecification</a> to set the source of information describing the vehicle. By default the <a href="../../com.here.sdk.transport/-transport-specification/index.html">com.here.sdk.transport.TransportSpecification</a> will have the transport mode set to <a href="../../com.here.sdk.transport/-transport-mode/-c-a-r/index.html">com.here.sdk.transport.TransportMode.CAR</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-567133642%2FProperties%2F1617540583" anchor-label="trafficMergeWarningListener" id="-567133642%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="traffic-merge-warning-listener.html"><span>traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-567133642%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="traffic-merge-warning-listener.html">trafficMergeWarningListener</a><span class="token operator">: </span><a href="../-traffic-merge-warning-listener/index.html">TrafficMergeWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about merging traffic to the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="347764882%2FProperties%2F1617540583" anchor-label="trafficMergeWarningOptions" id="347764882%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="traffic-merge-warning-options.html"><span>traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="347764882%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="traffic-merge-warning-options.html">trafficMergeWarningOptions</a><span class="token operator">: </span><a href="../-traffic-merge-warning-options/index.html">TrafficMergeWarningOptions</a></div><div class="brief "><p class="paragraph">Merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="../-traffic-merge-warning-listener/index.html">com.here.sdk.navigation.TrafficMergeWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1450716382%2FProperties%2F1617540583" anchor-label="trafficOnRoute" id="-1450716382%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="traffic-on-route.html"><span>traffic</span><wbr></wbr><span>On</span><wbr></wbr><span><span>Route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1450716382%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="traffic-on-route.html">trafficOnRoute</a><span class="token operator">: </span><a href="../../com.here.sdk.routing/-traffic-on-route/index.html">TrafficOnRoute</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Traffic information for the current route. This impacts <code class="lang-kotlin">RouteProgress</code> updates as the duration of the <code class="lang-kotlin">SectionProgress</code> might change. However, the remaining distance and the route geometry will remain unchanged.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-110488379%2FProperties%2F1617540583" anchor-label="truckRestrictionsWarningListener" id="-110488379%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="truck-restrictions-warning-listener.html"><span>truck</span><wbr></wbr><span>Restrictions</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-110488379%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="truck-restrictions-warning-listener.html">truckRestrictionsWarningListener</a><span class="token operator">: </span><a href="../-truck-restrictions-warning-listener/index.html">TruckRestrictionsWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about truck restrictions on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1055232035%2FProperties%2F1617540583" anchor-label="truckRestrictionsWarningOptions" id="1055232035%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="truck-restrictions-warning-options.html"><span>truck</span><wbr></wbr><span>Restrictions</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1055232035%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="truck-restrictions-warning-options.html">truckRestrictionsWarningOptions</a><span class="token operator">: </span><a href="../-truck-restrictions-warning-options/index.html">TruckRestrictionsWarningOptions</a></div><div class="brief "><p class="paragraph">Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="../-truck-restrictions-warning-listener/index.html">com.here.sdk.navigation.TruckRestrictionsWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2013546054%2FProperties%2F1617540583" anchor-label="warnerEngine" id="-2013546054%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="warner-engine.html"><span>warner</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2013546054%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">val </span><a href="warner-engine.html">warnerEngine</a><span class="token operator">: </span><a href="../../com.here.sdk.warner/-warner-engine/index.html">WarnerEngine</a></div><div class="brief "><p class="paragraph">Warner engine used by the navigator. This engine can be used to configure navigation warnings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1169673561%2FFunctions%2F1617540583" anchor-label="calculateRemainingDistanceInMeters" id="-1169673561%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="calculate-remaining-distance-in-meters.html"><span>calculate</span><wbr></wbr><span>Remaining</span><wbr></wbr><span>Distance</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1169673561%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="calculate-remaining-distance-in-meters.html"><span class="token function">calculateRemainingDistanceInMeters</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">coordinates<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-coordinates/index.html">GeoCoordinates</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">This method calculates the distance between the current position and given coordinates. The coordinates must be on the polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="15884154%2FFunctions%2F1617540583" anchor-label="getManeuver" id="15884154%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-maneuver.html"><span>get</span><wbr></wbr><span><span>Maneuver</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="15884154%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="get-maneuver.html"><span class="token function">getManeuver</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">index<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.routing/-maneuver/index.html">Maneuver</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns maneuver at the given index.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-396661908%2FFunctions%2F1617540583" anchor-label="getManeuverNotificationTimingOptions" id="-396661908%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-maneuver-notification-timing-options.html"><span>get</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Timing</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-396661908%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="get-maneuver-notification-timing-options.html"><span class="token function">getManeuverNotificationTimingOptions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportMode<span class="token operator">: </span><a href="../../com.here.sdk.transport/-transport-mode/index.html">TransportMode</a><span class="token punctuation">, </span></span><span class="parameter ">timingProfile<span class="token operator">: </span><a href="../-timing-profile/index.html">TimingProfile</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-maneuver-notification-timing-options/index.html">ManeuverNotificationTimingOptions</a></div><div class="brief "><p class="paragraph">Returns maneuver notification timing options with default values given the combination of transport mode and timing profile. The return value can be used as the base for configuring maneuver notification timings. Configure the relevant attributes of this object according to your preferences, and then set it by calling setManeuverNotificationTimingOptions function for the same combination of transport mode and timing profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1288187613%2FFunctions%2F1617540583" anchor-label="getWarningNotificationDistances" id="-1288187613%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-warning-notification-distances.html"><span>get</span><wbr></wbr><span>Warning</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Distances</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1288187613%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="get-warning-notification-distances.html"><span class="token function">getWarningNotificationDistances</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningType<span class="token operator">: </span><a href="../-warning-type/index.html">WarningType</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-warning-notification-distances/index.html">WarningNotificationDistances</a></div><div class="brief "><p class="paragraph">Returns the warning notification distances for the requested warning type. The return value can be used as the base for configuring warning notification distances. Configure the relevant attributes of this object according to your preferences, and then set it by calling <code class="lang-kotlin">setWarningNotificationDistances</code> function with the same warning type and the modified warning notification distances object.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-244359291%2FFunctions%2F1617540583" anchor-label="onLocationUpdated" id="-244359291%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-location-updated.html"><span>on</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Updated</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-244359291%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="on-location-updated.html"><span class="token function">onLocationUpdated</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">location<span class="token operator">: </span><a href="../../com.here.sdk.core/-location/index.html">Location</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Called each time a new location is available. In a navigation context while using the <code class="lang-kotlin">Navigator</code> or <code class="lang-kotlin">VisualNavigator</code>, it's required to set the <code class="lang-kotlin">Location.time</code> parameter for each <code class="lang-kotlin">Location</code> object so that the HERE SDK can map-match the locations properly. If the <code class="lang-kotlin">Location.time</code> parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the <code class="lang-kotlin">bearing</code> and <code class="lang-kotlin">speed</code> parameters for each <code class="lang-kotlin">Location</code> object. Invoked on the main thread.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1356163898%2FFunctions%2F1617540583" anchor-label="repeatLastManeuverNotification" id="1356163898%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="repeat-last-maneuver-notification.html"><span>repeat</span><wbr></wbr><span>Last</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span><span>Notification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1356163898%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="repeat-last-maneuver-notification.html"><span class="token function">repeatLastManeuverNotification</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="869825670%2FFunctions%2F1617540583" anchor-label="setCustomOption" id="869825670%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-custom-option.html"><span>set</span><wbr></wbr><span>Custom</span><wbr></wbr><span><span>Option</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="869825670%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="set-custom-option.html"><span class="token function">setCustomOption</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">key<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">This method sets custom options that controls navigator behavior. Unsupported options are silently ignored. Undocumented options can change their meaning without going through deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1116137536%2FFunctions%2F1617540583" anchor-label="setManeuverNotificationTimingOptions" id="1116137536%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-maneuver-notification-timing-options.html"><span>set</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Timing</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1116137536%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="set-maneuver-notification-timing-options.html"><span class="token function">setManeuverNotificationTimingOptions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportMode<span class="token operator">: </span><a href="../../com.here.sdk.transport/-transport-mode/index.html">TransportMode</a><span class="token punctuation">, </span></span><span class="parameter ">timingProfile<span class="token operator">: </span><a href="../-timing-profile/index.html">TimingProfile</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-maneuver-notification-timing-options/index.html">ManeuverNotificationTimingOptions</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Set timing option values for the combination of transport mode and timing profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1400145116%2FFunctions%2F1617540583" anchor-label="setWarningNotificationDistances" id="-1400145116%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-warning-notification-distances.html"><span>set</span><wbr></wbr><span>Warning</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Distances</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1400145116%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="set-warning-notification-distances.html"><span class="token function">setWarningNotificationDistances</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningType<span class="token operator">: </span><a href="../-warning-type/index.html">WarningType</a><span class="token punctuation">, </span></span><span class="parameter ">warningNotificationDistances<span class="token operator">: </span><a href="../-warning-notification-distances/index.html">WarningNotificationDistances</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Set the warning notification distances for the specified warning types. <strong>Note:</strong> The warning notification distances are set for most warners. This method can't be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use <code class="lang-kotlin">NavigatorInterface.school_zone_warning_options</code> instead. Attempting to set the warning notification distances for the school zone warner using the <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code class="lang-kotlin">false</code>. Always use <code class="lang-kotlin">SchoolZoneWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the school zone warner regardless of the <code class="lang-kotlin">TimingProfile</code>. If <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> could be used, this would allow for different distances to be set for each timing profile, which is undesirable. Attempting to set the warning notification distances for the traffic merge warner using the <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code class="lang-kotlin">false</code>. Always use <code class="lang-kotlin">TrafficMergeWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the traffic merge warner regardless of the <code class="lang-kotlin">TimingProfile</code>. Using the <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code class="lang-kotlin">false</code> to avoid seting different distances on each timing profile since the traffic merge warning is only applicable on highways.</p></div></div></div>
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
