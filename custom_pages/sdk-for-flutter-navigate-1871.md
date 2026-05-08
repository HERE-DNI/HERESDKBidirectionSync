---
title: "TrackingCameraBehavior"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>TrackingCameraBehavior</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.navigation/TrackingCameraBehavior///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.navigation</a><span class="delimiter">/</span><span class="current">TrackingCameraBehavior</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Tracking</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Behavior</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">TrackingCameraBehavior</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a>, <a href="sdk-for-flutter-explore-index">CameraBehavior</a></div><p class="paragraph">Use this class to follow a moving target. The camera smoothly tracks the target’s position while adjusting heading, tilt, and zoom as needed. When tracking starts or resumes, the camera first animates a re-centering transition to align with the target.</p><p class="paragraph">Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are subject to change without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-673135580%2FConstructors%2F1617540583" anchor-label="TrackingCameraBehavior" id="-673135580%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-tracking-camera-behavior"><span>Tracking</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Behavior</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-673135580%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-1808511249%2FClasslikes%2F1617540583" anchor-label="Companion" id="-1808511249%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1808511249%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1654314275%2FClasslikes%2F1617540583" anchor-label="FunctionalRoadClassZoomPolicyOptions" id="1654314275%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Functional</span><wbr></wbr><span>Road</span><wbr></wbr><span>Class</span><wbr></wbr><span>Zoom</span><wbr></wbr><span>Policy</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1654314275%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">FunctionalRoadClassZoomPolicyOptions</a></div><div class="brief "><p class="paragraph">Configuration for mapping functional road classes to zoom levels. For correct default initialization, use <a href="sdk-for-flutter-explore-default-functional-road-class-zoom-policy-options">com.here.sdk.navigation.TrackingCameraBehavior.defaultFunctionalRoadClassZoomPolicyOptions</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-683690879%2FClasslikes%2F1617540583" anchor-label="ManeuverModeConfiguration" id="-683690879%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Maneuver</span><wbr></wbr><span>Mode</span><wbr></wbr><span><span>Configuration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-683690879%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">ManeuverModeConfiguration</a></div><div class="brief "><p class="paragraph">Configuration that defines how <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TrackingCameraBehavior</a> reacts to nearby maneuvers.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1742468398%2FClasslikes%2F1617540583" anchor-label="ManeuverRule" id="-1742468398%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Maneuver</span><wbr></wbr><span><span>Rule</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1742468398%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">ManeuverRule</a></div><div class="brief "><p class="paragraph">Defines a single rule that determines how <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TrackingCameraBehavior</a> reacts to nearby maneuvers when the current position matches this rule.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-24058446%2FClasslikes%2F1617540583" anchor-label="ManeuverRuleOptions" id="-24058446%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Maneuver</span><wbr></wbr><span>Rule</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-24058446%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">ManeuverRuleOptions</a></div><div class="brief "><p class="paragraph">Defines a set of configurations specific to a <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TrackingCameraBehavior.ManeuverRule</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1524980298%2FClasslikes%2F1617540583" anchor-label="ManeuverZoomRange" id="1524980298%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Maneuver</span><wbr></wbr><span>Zoom</span><wbr></wbr><span><span>Range</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1524980298%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">ManeuverZoomRange</a></div><div class="brief "><p class="paragraph">Defines the bounds within which the zoom level is constrained when approaching a maneuver. Used as part of <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TrackingCameraBehavior.ManeuverRuleOptions</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1861571346%2FClasslikes%2F1617540583" anchor-label="SpeedBasedZoomPolicyOptions" id="-1861571346%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Speed</span><wbr></wbr><span>Based</span><wbr></wbr><span>Zoom</span><wbr></wbr><span>Policy</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1861571346%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SpeedBasedZoomPolicyOptions</a></div><div class="brief "><p class="paragraph">Configuration for computing zoom levels from speed thresholds defined per road classification. For correct default initialization, use <a href="sdk-for-flutter-explore-default-speed-based-zoom-policy-options">com.here.sdk.navigation.TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1717183171%2FClasslikes%2F1617540583" anchor-label="SpeedThreshold" id="1717183171%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Speed</span><wbr></wbr><span><span>Threshold</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1717183171%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SpeedThreshold</a></div><div class="brief "><p class="paragraph">Defines a zoom level triggered when the vehicle reaches a specific speed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1762338334%2FClasslikes%2F1617540583" anchor-label="ZoomPolicy" id="-1762338334%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Zoom</span><wbr></wbr><span><span>Policy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1762338334%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">ZoomPolicy</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Defines zoom behavior in different policy settings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="249380798%2FProperties%2F1617540583" anchor-label="bearingInDegrees" id="249380798%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-bearing-in-degrees"><span>bearing</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Degrees</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="249380798%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-bearing-in-degrees">bearingInDegrees</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The camera bearing in degrees. Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range is \[0, 360]\. If set, it will prevent the map from rotating to the direction of travel. For example, a value of zero results in &quot;north up&quot; mode. Defaults to <code class="lang-kotlin">null</code>, which means the camera derives the bearing from the <a href="sdk-for-flutter-explore-index">com.here.sdk.core.Location</a>, so that it points to the direction of travel. If this property is <code class="lang-kotlin">null</code> and the device does not provide bearing, the last known value is used or zero otherwise.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-935189549%2FProperties%2F1617540583" anchor-label="isManeuverDetectionEnabled" id="-935189549%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-maneuver-detection-enabled"><span>is</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span>Detection</span><wbr></wbr><span><span>Enabled</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-935189549%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-maneuver-detection-enabled">isManeuverDetectionEnabled</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Whether maneuver detection is enabled. When <code class="lang-kotlin">true</code>, the camera detects adjacent maneuvers and reacts according to the <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration</a> set via <a href="sdk-for-flutter-explore-set-maneuver-mode-configuration">com.here.sdk.navigation.TrackingCameraBehavior.setManeuverModeConfiguration</a>. A valid <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration</a> must be set for the camera to react. Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-207188578%2FProperties%2F1617540583" anchor-label="maxRotationSpeedInDegreesPerSecond" id="-207188578%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-max-rotation-speed-in-degrees-per-second"><span>max</span><wbr></wbr><span>Rotation</span><wbr></wbr><span>Speed</span><wbr></wbr><span>In</span><wbr></wbr><span>Degrees</span><wbr></wbr><span>Per</span><wbr></wbr><span><span>Second</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-207188578%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-max-rotation-speed-in-degrees-per-second">maxRotationSpeedInDegreesPerSecond</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">The maximum rotation speed. Maximum bearing rotation speed in degrees per second, limiting how fast the camera turns. Defaults to 20 degrees per second.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1969821625%2FProperties%2F1617540583" anchor-label="normalizedPrincipalPoint" id="1969821625%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-normalized-principal-point"><span>normalized</span><wbr></wbr><span>Principal</span><wbr></wbr><span><span>Point</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1969821625%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-normalized-principal-point">normalizedPrincipalPoint</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Anchor2D</a></div><div class="brief "><p class="paragraph">The normalized principal point. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="580406482%2FProperties%2F1617540583" anchor-label="principalPointAnimationDuration" id="580406482%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-principal-point-animation-duration"><span>principal</span><wbr></wbr><span>Point</span><wbr></wbr><span>Animation</span><wbr></wbr><span><span>Duration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="580406482%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-principal-point-animation-duration">principalPointAnimationDuration</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Duration</a></div><div class="brief "><p class="paragraph">The duration of principal point animation in milliseconds. If the principal point is changed, the change will be animated over this duration. Defaults to 500 milliseconds, or half a second.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1461766184%2FProperties%2F1617540583" anchor-label="recenterAnimationDuration" id="-1461766184%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-recenter-animation-duration"><span>recenter</span><wbr></wbr><span>Animation</span><wbr></wbr><span><span>Duration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1461766184%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-recenter-animation-duration">recenterAnimationDuration</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Duration</a></div><div class="brief "><p class="paragraph">The duration of recenter animation in milliseconds. Time to recenter the camera reaching current car position. Defaults to 500 milliseconds, or half a second.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-574338109%2FProperties%2F1617540583" anchor-label="tiltInDegrees" id="-574338109%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-tilt-in-degrees"><span>tilt</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Degrees</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-574338109%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-tilt-in-degrees">tiltInDegrees</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">The value of camera tilt in degrees. Camera tilt angle relative to the ground plane, in degrees. Defaults to 50.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-941073634%2FProperties%2F1617540583" anchor-label="viewRectangle" id="-941073634%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-view-rectangle"><span>view</span><wbr></wbr><span><span>Rectangle</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-941073634%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-view-rectangle">viewRectangle</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Rectangle2D</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The view rectangle for camera updates. Defines a sub-space of the screen that the behavior should consider for camera updates. Defaults to <code class="lang-kotlin">null</code>. If not set, it uses the viewport bounds of the underlying map view.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="372856813%2FProperties%2F1617540583" anchor-label="zoomPolicy" id="372856813%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-zoom-policy"><span>zoom</span><wbr></wbr><span><span>Policy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="372856813%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-zoom-policy">zoomPolicy</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrackingCameraBehavior.ZoomPolicy</a></div><div class="brief "><p class="paragraph">The strategy of computing the zoom level. Defines the strategy used to compute the zoom level based on scene heuristics. Defaults to a fixed zoom policy at zoom level 16.5.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1139910711%2FProperties%2F1617540583" anchor-label="zoomSpeedInLevelsPerSecond" id="-1139910711%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-zoom-speed-in-levels-per-second"><span>zoom</span><wbr></wbr><span>Speed</span><wbr></wbr><span>In</span><wbr></wbr><span>Levels</span><wbr></wbr><span>Per</span><wbr></wbr><span><span>Second</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1139910711%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-zoom-speed-in-levels-per-second">zoomSpeedInLevelsPerSecond</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">The zoom level transition speed. Speed factor controlling how quickly the camera transitions between zoom levels Defaults to 0.5 zoom levels per second.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1886421916%2FFunctions%2F1617540583" anchor-label="flagFixedDurationForNextAnimation" id="-1886421916%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-flag-fixed-duration-for-next-animation"><span>flag</span><wbr></wbr><span>Fixed</span><wbr></wbr><span>Duration</span><wbr></wbr><span>For</span><wbr></wbr><span>Next</span><wbr></wbr><span><span>Animation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1886421916%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-flag-fixed-duration-for-next-animation"><span class="token function">flagFixedDurationForNextAnimation</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Enables fixed-duration animation mode for the next property change. When called, the next setter call (e.g., tilt_in_degrees or bearing_in_degrees) will animate using a fast fixed-duration animation instead of the default speed-based animation. The flag is automatically reset after the next setter is called.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-35743250%2FFunctions%2F1617540583" anchor-label="getManeuverModeConfiguration" id="-35743250%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-maneuver-mode-configuration"><span>get</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span>Mode</span><wbr></wbr><span><span>Configuration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-35743250%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-maneuver-mode-configuration"><span class="token function">getManeuverModeConfiguration</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrackingCameraBehavior.ManeuverModeConfiguration</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Gets the current maneuver mode configuration, or <code class="lang-kotlin">null</code> if not set.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-465110056%2FFunctions%2F1617540583" anchor-label="setManeuverModeConfiguration" id="-465110056%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-maneuver-mode-configuration"><span>set</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span>Mode</span><wbr></wbr><span><span>Configuration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-465110056%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-maneuver-mode-configuration"><span class="token function">setManeuverModeConfiguration</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">maneuverModeConfiguration<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrackingCameraBehavior.ManeuverModeConfiguration</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets the configuration for camera behavior near maneuvers. Defines how the camera reacts to nearby maneuvers when <a href="sdk-for-flutter-explore-is-maneuver-detection-enabled">com.here.sdk.navigation.TrackingCameraBehavior.isManeuverDetectionEnabled</a> is <code class="lang-kotlin">true</code>. When set to <code class="lang-kotlin">null</code>, the camera does not react to maneuvers. The configuration must contain at least one rule to be valid. Defaults to <code class="lang-kotlin">null</code>.</p></div></div></div>
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
