---
title: "com.here.sdk.navigation"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>com.here.sdk.navigation</title>
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
<div class="main-content" data-page-type="package" id="content" pageIds="API Reference::com.here.sdk.navigation////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><span class="current">com.here.sdk.navigation</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Package-level</span></span> <span><span>declarations</span></span></h1>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="TYPE">Types</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-2089978601%2FClasslikes%2F1617540583" anchor-label="AreaCameraBehavior" id="-2089978601%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Area</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Behavior</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2089978601%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">AreaCameraBehavior</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a>, <a href="sdk-for-flutter-explore-index">CameraBehavior</a></div><div class="brief "><p class="paragraph">Use this class to show an overview of geo points. By default, the orientation of the camera will be perpendicular to the Earth's surface (ie. looking towards the center of the Earth), while bearing will be towards north.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-217302258%2FClasslikes%2F1617540583" anchor-label="ArrivalNotificationOption" id="-217302258%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Arrival</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Option</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-217302258%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">ArrivalNotificationOption</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">ArrivalNotificationOption</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates arrival point type to announce in maneuver notification.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1871731028%2FClasslikes%2F1617540583" anchor-label="AspectRatio" id="1871731028%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Aspect</span><wbr></wbr><span><span>Ratio</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1871731028%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">AspectRatio</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">AspectRatio</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">The aspect ratio of the image.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1784949295%2FClasslikes%2F1617540583" anchor-label="AutomotiveCameraBehavior" id="1784949295%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Automotive</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Behavior</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1784949295%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">AutomotiveCameraBehavior</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a>, <a href="sdk-for-flutter-explore-index">CameraBehavior</a></div><div class="brief "><p class="paragraph">Provides a high-level camera controller for automotive navigation that manages both tracking and area camera behaviors. This class acts as a facade, delegating camera operations to either a <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TrackingCameraBehavior</a> for following the vehicle during navigation or an <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.AreaCameraBehavior</a> for showing overview areas such as points of interest or route previews.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-734011437%2FClasslikes%2F1617540583" anchor-label="BorderCrossingType" id="-734011437%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Border</span><wbr></wbr><span>Crossing</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-734011437%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">BorderCrossingType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">BorderCrossingType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Type of a border crossing given in a <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.BorderCrossingWarning</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1861080313%2FClasslikes%2F1617540583" anchor-label="BorderCrossingWarning" id="1861080313%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Border</span><wbr></wbr><span>Crossing</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1861080313%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">BorderCrossingWarning</a></div><div class="brief "><p class="paragraph">A border crossing. The main field describing the border crossing is <a href="sdk-for-flutter-explore-type">com.here.sdk.navigation.BorderCrossingWarning.type</a> specifying whether the border crossing is given for a country border or a state border. The <a href="sdk-for-flutter-explore-type">com.here.sdk.navigation.BorderCrossingWarning.type</a> must be known. The country and state codes are contained in <a href="sdk-for-flutter-explore-administrative-rules">com.here.sdk.navigation.BorderCrossingWarning.administrativeRules</a> along with other information such as speed limits, u-turn regulations or pre-trip planning information contained by the <a href="sdk-for-flutter-explore-index">com.here.sdk.mapdata.AdministrativeRules</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1623538341%2FClasslikes%2F1617540583" anchor-label="BorderCrossingWarningListener" id="1623538341%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Border</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1623538341%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">BorderCrossingWarningListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive border crossing warnings for country and state borders. <strong>Note:</strong> The border crossing warner is a point warner, which means that for a border crossing there will <i>always</i> be 2 warnings emitted, with the BorderCrossingWarning.distance_type set to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.DistanceType.AHEAD</a> and <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.DistanceType.PASSED</a> which is given when the location of the border crossing is reached. A <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.BorderCrossingWarning</a> will not be given until the previous warning of that type has been passed. For example, a route with <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.BorderCrossingWarning</a> 120 meters and <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.BorderCrossingWarning</a> 160 meters ahead, the first BorderCrossingWarning.distance_to_border_crossing_in_meters is 120 meters and the next BorderCrossingWarning.distance_to_border_crossing_in_meters is then 40 meters, since that is the distance between the first and second warnings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="610120107%2FClasslikes%2F1617540583" anchor-label="BorderCrossingWarningOptions" id="610120107%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Border</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="610120107%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">BorderCrossingWarningOptions</a></div><div class="brief "><p class="paragraph">Border crossing warning options.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="525567844%2FClasslikes%2F1617540583" anchor-label="CameraBehavior" id="525567844%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Camera</span><wbr></wbr><span><span>Behavior</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="525567844%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">CameraBehavior</a></div><div class="brief "><p class="paragraph">Interface used to change implement different camera behaviors.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-157884819%2FClasslikes%2F1617540583" anchor-label="CurrentSituationLaneAssistanceView" id="-157884819%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Current</span><wbr></wbr><span>Situation</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span><span>View</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-157884819%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">CurrentSituationLaneAssistanceView</a></div><div class="brief "><p class="paragraph">A class that provides current situation lane assistance view information for the street at the current location.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-967340007%2FClasslikes%2F1617540583" anchor-label="CurrentSituationLaneAssistanceViewListener" id="-967340007%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Current</span><wbr></wbr><span>Situation</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span>View</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-967340007%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">CurrentSituationLaneAssistanceViewListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications on <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.CurrentSituationLaneAssistanceView</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-710580731%2FClasslikes%2F1617540583" anchor-label="CurrentSituationLaneView" id="-710580731%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Current</span><wbr></wbr><span>Situation</span><wbr></wbr><span>Lane</span><wbr></wbr><span><span>View</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-710580731%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">CurrentSituationLaneView</a></div><div class="brief "><p class="paragraph">A class that provides current situation lane assistance view information for the street at the current position of a single lane.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="382706013%2FClasslikes%2F1617540583" anchor-label="CustomPanningData" id="382706013%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Custom</span><wbr></wbr><span>Panning</span><wbr></wbr><span><span>Data</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="382706013%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">CustomPanningData</a></div><div class="brief "><p class="paragraph">This class contains all the information regarding the next angular panning element, including a new estimated audio cue duration, and a new set of initial and sweep angular angle, allowing the customization of the spatial audio trajectories for any type of notification, such as speed or merge warners, maneuvers or even roundabouts notifications. The orientation in space for <a href="sdk-for-flutter-explore-initial-azimuth-in-degrees">com.here.sdk.navigation.CustomPanningData.initialAzimuthInDegrees</a> and <a href="sdk-for-flutter-explore-sweep-azimuth-in-degrees">com.here.sdk.navigation.CustomPanningData.sweepAzimuthInDegrees</a> can be represented by the following angular values:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-253539206%2FClasslikes%2F1617540583" anchor-label="DangerZoneWarning" id="-253539206%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Danger</span><wbr></wbr><span>Zone</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-253539206%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">DangerZoneWarning</a></div><div class="brief "><p class="paragraph">Represents danger zones. A danger zone refers to areas where there is an increased risk of traffic incidents. These zones are designated to alert drivers to potential hazards and encourage safer driving behaviors. Legally, certain devices can alert you to being in a danger zone, typically indicating the presence of a speed camera. In line with applicable law and industry standard, these alerts are usually provided along a road within a range of 4 km on a motorway, 2 km outside built-up areas, and 300 m in built-up areas. The HERE SDK warns when approaching the danger zone, as well as when leaving such a zone. A danger zone may or may not have one or more speed cameras in it. The exact location of such speed cameras is not provided. Note that danger zones are only available in selected countries, such as France.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1546673882%2FClasslikes%2F1617540583" anchor-label="DangerZoneWarningListener" id="-1546673882%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Danger</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1546673882%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">DangerZoneWarningListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications about the Danger zones.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-412966429%2FClasslikes%2F1617540583" anchor-label="DestinationReachedListener" id="-412966429%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Destination</span><wbr></wbr><span>Reached</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-412966429%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">DestinationReachedListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications from this class about the arrival at the destination.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-137823019%2FClasslikes%2F1617540583" anchor-label="DimensionRestriction" id="-137823019%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Dimension</span><wbr></wbr><span><span>Restriction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-137823019%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">DimensionRestriction</a></div><div class="brief "><p class="paragraph">Defines a dimension restriction.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="876978363%2FClasslikes%2F1617540583" anchor-label="DimensionRestrictionType" id="876978363%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Dimension</span><wbr></wbr><span>Restriction</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="876978363%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">DimensionRestrictionType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">DimensionRestrictionType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Defines the type of a dimension restriction.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1767606626%2FClasslikes%2F1617540583" anchor-label="DirectionInformationUsageOption" id="-1767606626%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Direction</span><wbr></wbr><span>Information</span><wbr></wbr><span>Usage</span><wbr></wbr><span><span>Option</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1767606626%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">DirectionInformationUsageOption</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">DirectionInformationUsageOption</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates the option of direction information included in the notification.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="862224556%2FClasslikes%2F1617540583" anchor-label="DistanceType" id="862224556%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Distance</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="862224556%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">DistanceType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">DistanceType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph"><strong>Note:</strong> The distance types are being given for warnings at distances which can be configured via options specific for each warner. These distances are defined based on the <code class="lang-kotlin">sdk.navigation.TimingProfile</code> calculated based on the speed limit present at the driver's current location. Indicates the distance type for a warning.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1489705548%2FClasslikes%2F1617540583" anchor-label="DividerMarker" id="-1489705548%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Divider</span><wbr></wbr><span><span>Marker</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1489705548%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">DividerMarker</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">DividerMarker</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates the divider between the lanes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="929222417%2FClasslikes%2F1617540583" anchor-label="DynamicCameraBehavior" id="929222417%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Dynamic</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Behavior</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="929222417%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">DynamicCameraBehavior</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a>, <a href="sdk-for-flutter-explore-index">CameraBehavior</a></div><div class="brief "><p class="paragraph">Use this class to follow the current location of the user: The camera will look at the target location that was fed into the navigator instance, gradually zooming in as the user approaches each maneuver and zooming out after the user passes them. Since location updates happen in discrete intervals, locations in-between will be interpolated to achieve a smooth camera movement.  If no route is set, constant values of camera distance and tilt are used.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-764220951%2FClasslikes%2F1617540583" anchor-label="EnvironmentalZoneWarning" id="-764220951%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Environmental</span><wbr></wbr><span>Zone</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-764220951%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">EnvironmentalZoneWarning</a></div><div class="brief "><p class="paragraph">Represents Environmental zones.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-937533547%2FClasslikes%2F1617540583" anchor-label="EnvironmentalZoneWarningListener" id="-937533547%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Environmental</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-937533547%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">EnvironmentalZoneWarningListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications about the environmental zones.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1096397056%2FClasslikes%2F1617540583" anchor-label="EventText" id="1096397056%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Event</span><wbr></wbr><span><span>Text</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1096397056%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">EventText</a></div><div class="brief "><p class="paragraph">Contains all the information regarding the next text announcement.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1970544556%2FClasslikes%2F1617540583" anchor-label="EventTextListener" id="1970544556%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Event</span><wbr></wbr><span>Text</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1970544556%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">EventTextListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications when text notifications are available from <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Navigator</a>. Multiple notifications can be given for the same maneuver at different distances.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="759861188%2FClasslikes%2F1617540583" anchor-label="EventTextOptions" id="759861188%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Event</span><wbr></wbr><span>Text</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="759861188%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">EventTextOptions</a></div><div class="brief "><p class="paragraph">Text notifications options.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-278527044%2FClasslikes%2F1617540583" anchor-label="FixedCameraBehavior" id="-278527044%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Fixed</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Behavior</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-278527044%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">FixedCameraBehavior</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a>, <a href="sdk-for-flutter-explore-index">CameraBehavior</a></div><div class="brief "><p class="paragraph">Use this class to follow the current location of the user: The camera will permanently look at the target location that was fed into the navigator instance. Since location updates happen in discrete intervals, locations in-between will be interpolated to achieve a smooth camera movement.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1608391152%2FClasslikes%2F1617540583" anchor-label="GeneralWarningRoadSignType" id="1608391152%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>General</span><wbr></wbr><span>Warning</span><wbr></wbr><span>Road</span><wbr></wbr><span>Sign</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1608391152%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">GeneralWarningRoadSignType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">GeneralWarningRoadSignType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Type of a general warning that a road sign represents.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="928790749%2FClasslikes%2F1617540583" anchor-label="GPXDocument" id="928790749%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>GPXDocument</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="928790749%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">GPXDocument</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Use the GPXDocument to load the GPX file. Only track data is used from the GPX file format (see trkType at https://www.topografix.com/GPX/1/1/#type_trkType). Any unknown elements in the file are ignored. Any known element with an invalid value returns an error. Elevation values are ignored.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1445397772%2FClasslikes%2F1617540583" anchor-label="GPXOptions" id="1445397772%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>GPXOptions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1445397772%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">GPXOptions</a></div><div class="brief "><p class="paragraph">Options used when reading the GPX file.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-647585473%2FClasslikes%2F1617540583" anchor-label="GPXTrack" id="-647585473%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>GPXTrack</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-647585473%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">GPXTrack</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Single track from the <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.GPXDocument</a>. Can be used as an input to the <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.LocationSimulator</a>. Can be created and modified via <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.GPXTrackWriter</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1936143988%2FClasslikes%2F1617540583" anchor-label="GPXTrackWriter" id="-1936143988%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>GPXTrack</span><wbr></wbr><span><span>Writer</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1936143988%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">GPXTrackWriter</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a>, <a href="sdk-for-flutter-explore-index">LocationListener</a></div><div class="brief "><p class="paragraph">Writes GPX track points to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.GPXTrack</a>. The instance of the class should be added as a listener to the <code class="lang-kotlin">LocationEngine</code> for GPX track recording. Appends the new location to the back segment of the track whenever the listener is called. The following data (if provided) can be recorded and inserted into the resulting <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.GPXTrack</a>: <code class="lang-kotlin">latitude</code>, <code class="lang-kotlin">longitude</code>, <code class="lang-kotlin">altitude</code>, <code class="lang-kotlin">time</code>, <code class="lang-kotlin">bearingInDegrees</code>, <code class="lang-kotlin">pitchInDegrees</code>, <code class="lang-kotlin">speedInMetersPerSecond</code>, <code class="lang-kotlin">horizontalAccuracyInMeters</code>, <code class="lang-kotlin">verticalAccuracyInMeters</code>, <code class="lang-kotlin">bearingAccuracyInDegrees</code>, <code class="lang-kotlin">speedAccuracyInMetersPerSecond</code> and <code class="lang-kotlin">locationTechnology</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1057374959%2FClasslikes%2F1617540583" anchor-label="InterpolatedLocationListener" id="1057374959%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Interpolated</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1057374959%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">InterpolatedLocationListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive interpolated locations. The interpolated locations are only provided between <a href="sdk-for-flutter-explore-start-rendering">com.here.sdk.navigation.VisualNavigator.startRendering</a> and <a href="sdk-for-flutter-explore-stop-rendering">com.here.sdk.navigation.VisualNavigator.stopRendering</a> calls and the application is not running in the background.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2104581374%2FClasslikes%2F1617540583" anchor-label="JunctionViewLaneAssistance" id="2104581374%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Junction</span><wbr></wbr><span>View</span><wbr></wbr><span>Lane</span><wbr></wbr><span><span>Assistance</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2104581374%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">JunctionViewLaneAssistance</a></div><div class="brief "><p class="paragraph">A class that provides lane assistance information for the next complex junction in order to keep following the route. It is recommended to indicate <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.JunctionViewLaneAssistance</a> and <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverViewLaneAssistance</a> separately or to indicate only <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverViewLaneAssistance</a> information - <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.JunctionViewLaneAssistance</a> will recommend all lanes that allow to pass the upcoming complex junction, regardless if they will lead to the next maneuver or not. If the location of a maneuver lies on an upcoming complex junction, the recommended lanes will be the same as the ones from <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverViewLaneAssistance</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2090266026%2FClasslikes%2F1617540583" anchor-label="JunctionViewLaneAssistanceListener" id="2090266026%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Junction</span><wbr></wbr><span>View</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2090266026%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">JunctionViewLaneAssistanceListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications on <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.JunctionViewLaneAssistance</a>. See <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.JunctionViewLaneAssistance</a> documentation for further details.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-736325585%2FClasslikes%2F1617540583" anchor-label="Lane" id="-736325585%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Lane</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-736325585%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Lane</a></div><div class="brief "><p class="paragraph">A class that provides information for a lane.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-930745173%2FClasslikes%2F1617540583" anchor-label="LaneAccess" id="-930745173%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Lane</span><wbr></wbr><span><span>Access</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-930745173%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">LaneAccess</a></div><div class="brief "><p class="paragraph">A class which identifies the vehicle type(s) allowed to access a lane.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-930870412%2FClasslikes%2F1617540583" anchor-label="LaneDirection" id="-930870412%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Lane</span><wbr></wbr><span><span>Direction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-930870412%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">LaneDirection</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">LaneDirection</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">This enum defines the lane direction.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="114939158%2FClasslikes%2F1617540583" anchor-label="LaneDirectionCategory" id="114939158%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Lane</span><wbr></wbr><span>Direction</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="114939158%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">LaneDirectionCategory</a></div><div class="brief "><p class="paragraph">Indicates the directions of a lane. Most lanes lead only to one direction, but there can be also lanes that split up into multiple directions. A road can consist of multiple lanes towards the same direction. Note: All members can be <code class="lang-kotlin">true</code> or <code class="lang-kotlin">false</code> at the same time. Lanes such as bicycle lanes mostly never contain a direction category and thus, all members are <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="915296945%2FClasslikes%2F1617540583" anchor-label="LaneMarkings" id="915296945%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Lane</span><wbr></wbr><span><span>Markings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="915296945%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">LaneMarkings</a></div><div class="brief "><p class="paragraph">A class that provides information for the lane markings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-481946053%2FClasslikes%2F1617540583" anchor-label="LaneRecommendationState" id="-481946053%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Lane</span><wbr></wbr><span>Recommendation</span><wbr></wbr><span><span>State</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-481946053%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">LaneRecommendationState</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">LaneRecommendationState</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates whether this lane leads to the next maneuvers or not. The next maneuver is the next upcoming maneuver which is not yet reached, but that was already announced as <i>new</i> maneuver in sdk.navigation.RouteProgress.maneuver_progress.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-880019691%2FClasslikes%2F1617540583" anchor-label="LaneType" id="-880019691%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Lane</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-880019691%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">LaneType</a></div><div class="brief "><p class="paragraph">A class that provides information on the available lane properties. The lane type values can be combined as follows:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-223707368%2FClasslikes%2F1617540583" anchor-label="LocationSimulator" id="-223707368%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Location</span><wbr></wbr><span><span>Simulator</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-223707368%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">LocationSimulator</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Use the <code class="lang-kotlin">LocationSimulator</code> to generate locations along a route or a GPX document. It notifies the registered object about the current location at a fixed interval. In order to customize the interval, see <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.LocationSimulatorOptions</a>. The locations are closely matched to the shape and proceeded from the start to the destination as found in the provided route or the GPX document. When providing a route, the <code class="lang-kotlin">LocationSimulator</code> uses a base speed taken from each span found in the provided route object. This base speed can be multiplied upfront with a custom <code class="lang-kotlin">speedFactor</code> for simulation purposes. Effectively, this means that traffic-related information is not considered to adjust the speed of the simulation. For the <code class="lang-kotlin">GPXTrack</code>, a speed is either based on timestamps in the original file or provided by the user. The following data is read from a <code class="lang-kotlin">GPXTrack</code> and inserted into the provided <code class="lang-kotlin">Location</code> object: <code class="lang-kotlin">latitude</code>, <code class="lang-kotlin">longitude</code>, <code class="lang-kotlin">altitude</code>, <code class="lang-kotlin">time</code>, <code class="lang-kotlin">bearingInDegrees</code>, <code class="lang-kotlin">speedInMetersPerSecond</code>, <code class="lang-kotlin">horizontalAccuracyInMeters</code>, <code class="lang-kotlin">verticalAccuracyInMeters</code> and <code class="lang-kotlin">locationTechnology</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1362245292%2FClasslikes%2F1617540583" anchor-label="LocationSimulatorOptions" id="1362245292%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Location</span><wbr></wbr><span>Simulator</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1362245292%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">LocationSimulatorOptions</a></div><div class="brief "><p class="paragraph">Options to specify how the location simulator will behave.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="468099626%2FClasslikes%2F1617540583" anchor-label="LowSpeedZoneWarning" id="468099626%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Low</span><wbr></wbr><span>Speed</span><wbr></wbr><span>Zone</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="468099626%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">LowSpeedZoneWarning</a></div><div class="brief "><p class="paragraph">A class that provides low speed zone. The main field describing the low speed zone is <code class="lang-kotlin">LowSpeedZoneWarning.speed_limit_in_meters_per_second</code> specifying the speed limit of the low speed zone. Use <code class="lang-kotlin">LowSpeedZoneWarningListener</code> to get notifications about upcoming low speed zones.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1011202346%2FClasslikes%2F1617540583" anchor-label="LowSpeedZoneWarningListener" id="-1011202346%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Low</span><wbr></wbr><span>Speed</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1011202346%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">LowSpeedZoneWarningListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive low speed zone warnings. <strong>Note:</strong> This is currently available <i>only</i> for Japan. The low speed zone warner is a zone warner, which means that for a low speed zone there will <i>always</i> be 3 warnings emitted, with the <code class="lang-kotlin">LowSpeedZoneWarning.distance_type</code> set to <code class="lang-kotlin">DistanceType.AHEAD</code>, <code class="lang-kotlin">DistanceType.REACHED</code> and lastly <code class="lang-kotlin">DistanceType.PASSED</code> when the end of the low speed zone is passed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="149496841%2FClasslikes%2F1617540583" anchor-label="ManeuverNotificationDetails" id="149496841%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Details</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="149496841%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">ManeuverNotificationDetails</a></div><div class="brief "><p class="paragraph">This class provides the information regarding the next maneuver to be triggered</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="721678125%2FClasslikes%2F1617540583" anchor-label="ManeuverNotificationOptions" id="721678125%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="721678125%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">ManeuverNotificationOptions</a></div><div class="brief "><p class="paragraph">A class containing all options to be used when generating maneuver notifications.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1702694889%2FClasslikes%2F1617540583" anchor-label="ManeuverNotificationTimingOptions" id="-1702694889%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Timing</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1702694889%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">ManeuverNotificationTimingOptions</a></div><div class="brief "><p class="paragraph">A class defining timing and distance thresholds for maneuver notifications.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="319703197%2FClasslikes%2F1617540583" anchor-label="ManeuverNotificationType" id="319703197%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="319703197%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">ManeuverNotificationType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">ManeuverNotificationType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates the type of the maneuver notification.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="538307381%2FClasslikes%2F1617540583" anchor-label="ManeuverProgress" id="538307381%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Maneuver</span><wbr></wbr><span><span>Progress</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="538307381%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">ManeuverProgress</a></div><div class="brief "><p class="paragraph">Indicates a user's progress to a <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.Maneuver</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1134730407%2FClasslikes%2F1617540583" anchor-label="ManeuverViewLaneAssistance" id="-1134730407%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Maneuver</span><wbr></wbr><span>View</span><wbr></wbr><span>Lane</span><wbr></wbr><span><span>Assistance</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1134730407%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">ManeuverViewLaneAssistance</a></div><div class="brief "><p class="paragraph">A class that provides lane assistance information for the next maneuver(s). During turn-by-turn navigation lane assistance can help a driver to choose the recommended lanes in order to complete the upcoming maneuvers. The notifications are synchronized with the <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.EventTextListener</a>. <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.EventTextListener</a> has 4 notification types for each maneuver: Range, Reminder, Distance and Action. Only the maneuver notification of type Distance will also notify a ManeuverViewLaneAssistance object (e.g. &quot;After 400 meters, turn right onto Invalidenstraße&quot;). The notification will not be sent when other types of maneuver notification are given. The notification will not be sent when no lane data is available. During tracking mode, no notifications are delivered. This ManeuverViewLaneAssistance information is valid until the next maneuver is reached.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1584425221%2FClasslikes%2F1617540583" anchor-label="ManeuverViewLaneAssistanceListener" id="1584425221%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Maneuver</span><wbr></wbr><span>View</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1584425221%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">ManeuverViewLaneAssistanceListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications on <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverViewLaneAssistance</a>. See <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.ManeuverViewLaneAssistance</a> documentation for further details.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1490783678%2FClasslikes%2F1617540583" anchor-label="MapMatchedLocation" id="1490783678%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Map</span><wbr></wbr><span>Matched</span><wbr></wbr><span><span>Location</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1490783678%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">MapMatchedLocation</a></div><div class="brief "><p class="paragraph">Describes a map-matched location in the world at a given time.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-65428841%2FClasslikes%2F1617540583" anchor-label="Milestone" id="-65428841%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Milestone</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-65428841%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Milestone</a></div><div class="brief "><p class="paragraph">Represents information about the waypoints along the route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1400055227%2FClasslikes%2F1617540583" anchor-label="MilestoneStatus" id="-1400055227%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Milestone</span><wbr></wbr><span><span>Status</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1400055227%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">MilestoneStatus</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MilestoneStatus</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">This enum represents the status of the <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Milestone</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-371182607%2FClasslikes%2F1617540583" anchor-label="MilestoneStatusListener" id="-371182607%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Milestone</span><wbr></wbr><span>Status</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-371182607%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">MilestoneStatusListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications from this class about the arrival at each <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Milestone</a> or missing it.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1335257731%2FClasslikes%2F1617540583" anchor-label="MilestoneType" id="-1335257731%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Milestone</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1335257731%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">MilestoneType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MilestoneType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">This enum represents the type of the <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Milestone</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-822607508%2FClasslikes%2F1617540583" anchor-label="NaturalGuidanceType" id="-822607508%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Natural</span><wbr></wbr><span>Guidance</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-822607508%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">NaturalGuidanceType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">NaturalGuidanceType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates the type of the natural guidance element.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="411770583%2FClasslikes%2F1617540583" anchor-label="NavigableLocation" id="411770583%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Navigable</span><wbr></wbr><span><span>Location</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="411770583%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">NavigableLocation</a></div><div class="brief "><p class="paragraph">Contains all the relevant information on the current location.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="878823043%2FClasslikes%2F1617540583" anchor-label="NavigableLocationListener" id="878823043%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Navigable</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="878823043%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">NavigableLocationListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications about the current location from <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Navigator</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-596995184%2FClasslikes%2F1617540583" anchor-label="Navigator" id="-596995184%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Navigator</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-596995184%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">Navigator</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a>, <a href="sdk-for-flutter-explore-index">NavigatorInterface</a></div><div class="brief "><p class="paragraph">This class provides the basic navigation functionality. It provides notifications about current map-matched location updates (see <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.NavigableLocation</a>). And, if a route has been set, about the route progress (see <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RouteProgress</a>), route deviations (see <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RouteDeviation</a>) and maneuver notifications (see <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.EventTextListener</a>).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-602282823%2FClasslikes%2F1617540583" anchor-label="NavigatorInterface" id="-602282823%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Navigator</span><wbr></wbr><span><span>Interface</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-602282823%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">NavigatorInterface</a> : <a href="sdk-for-flutter-explore-index">LocationListener</a></div><div class="brief "><p class="paragraph">This interface provides the basic functionality needed to run a navigation session.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2007698340%2FClasslikes%2F1617540583" anchor-label="NotificationFormatOption" id="2007698340%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Notification</span><wbr></wbr><span>Format</span><wbr></wbr><span><span>Option</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2007698340%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">NotificationFormatOption</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">NotificationFormatOption</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates the formatting option of phoneme included in the notification.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1391159520%2FClasslikes%2F1617540583" anchor-label="OffRoadDestinationReachedListener" id="-1391159520%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Off</span><wbr></wbr><span>Road</span><wbr></wbr><span>Destination</span><wbr></wbr><span>Reached</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1391159520%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">OffRoadDestinationReachedListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications from this class about the arrival at the off-road destination.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-902172533%2FClasslikes%2F1617540583" anchor-label="OffRoadProgress" id="-902172533%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Off</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Progress</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-902172533%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">OffRoadProgress</a></div><div class="brief "><p class="paragraph">Represents the information needed to help the users to reach their off-road destination.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1993188407%2FClasslikes%2F1617540583" anchor-label="OffRoadProgressListener" id="1993188407%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Off</span><wbr></wbr><span>Road</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1993188407%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">OffRoadProgressListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications about the current off-road location from <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Navigator</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="737425553%2FClasslikes%2F1617540583" anchor-label="PostActionListener" id="737425553%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Post</span><wbr></wbr><span>Action</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="737425553%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">PostActionListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive post action notifications.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1529022206%2FClasslikes%2F1617540583" anchor-label="RailwayCrossingWarning" id="1529022206%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Railway</span><wbr></wbr><span>Crossing</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1529022206%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RailwayCrossingWarning</a></div><div class="brief "><p class="paragraph">A class that provides railway crossing. The main field describing the railway crossing is <code class="lang-kotlin">RailwayCrossingWarning.type</code> specifying whether the railway crossing is protected by a barrier or not. Use <code class="lang-kotlin">RailwayCrossingWarningListener</code> to get notifications about upcoming railway crossings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1963026518%2FClasslikes%2F1617540583" anchor-label="RailwayCrossingWarningListener" id="-1963026518%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Railway</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1963026518%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">RailwayCrossingWarningListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive railway crossing warnings. <strong>Note:</strong> The railway crossing warner can be either a zone warner or a point warner, depending on whether the railroad crossing warning is given for a railroad crossing zone or just a point. This means that for a railway crossing there will can be either 2 or 3 warnings emitted. In case the railroad crossing is a zone warner then 3 warnings will be emitted with the <code class="lang-kotlin">RailwayCrossingWarning.distance_type</code> set to <code class="lang-kotlin">DistanceType.AHEAD</code>, <code class="lang-kotlin">DistanceType.REACHED</code> and lastly <code class="lang-kotlin">DistanceType.PASSED</code> when the end of the railway crossing is passed. In case the railroad crossing is a point warner then 2 warnings will be emitted with the <code class="lang-kotlin">RailwayCrossingWarning.distance_type</code> set to <code class="lang-kotlin">DistanceType.AHEAD</code> and <code class="lang-kotlin">DistanceType.PASSED</code> when the end of the railway crossing is passed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1731513896%2FClasslikes%2F1617540583" anchor-label="RealisticViewRasterImage" id="1731513896%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Realistic</span><wbr></wbr><span>View</span><wbr></wbr><span>Raster</span><wbr></wbr><span><span>Image</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1731513896%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RealisticViewRasterImage</a></div><div class="brief "><p class="paragraph">A realistic view. The fields describing the realistic view are <a href="sdk-for-flutter-explore-realistic-view-png-image-content">com.here.sdk.navigation.RealisticViewRasterImage.realisticViewPngImageContent</a> contains a PNG image of the realistic view and is represented as binary data. <span data-unresolved-link="com.here.sdk.navigation/RealisticViewRasterImage/realisticViewType/#/PointingToDeclaration/">com.here.sdk.navigation.RealisticViewRasterImage.realisticViewType</span> indicates the type of the realistic view. A valid realistic view contains a non-empty <a href="sdk-for-flutter-explore-realistic-view-png-image-content">com.here.sdk.navigation.RealisticViewRasterImage.realisticViewPngImageContent</a>. Use <code class="lang-kotlin">RealisticViewWarningListener</code> to get notifications with the realistic views of the upcoming realistic view.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1400564590%2FClasslikes%2F1617540583" anchor-label="RealisticViewVectorImage" id="1400564590%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Realistic</span><wbr></wbr><span>View</span><wbr></wbr><span>Vector</span><wbr></wbr><span><span>Image</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1400564590%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RealisticViewVectorImage</a></div><div class="brief "><p class="paragraph">A realistic view of a junction. The fields describing the realistic view are <a href="sdk-for-flutter-explore-junction-view-svg-image-content">com.here.sdk.navigation.RealisticViewVectorImage.junctionViewSvgImageContent</a> contains a SVG image of the junction view represented as a string. <a href="sdk-for-flutter-explore-signpost-svg-image-content">com.here.sdk.navigation.RealisticViewVectorImage.signpostSvgImageContent</a> contains an SVG image of the signpost corresponding to the junction, also represented as a string. A valid realistic view contains a non-empty <a href="sdk-for-flutter-explore-junction-view-svg-image-content">com.here.sdk.navigation.RealisticViewVectorImage.junctionViewSvgImageContent</a> and a non-empty <a href="sdk-for-flutter-explore-signpost-svg-image-content">com.here.sdk.navigation.RealisticViewVectorImage.signpostSvgImageContent</a>. Use <code class="lang-kotlin">RealisticViewWarningListener</code> to get notifications with the realistic views of the upcoming junctions.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-282919766%2FClasslikes%2F1617540583" anchor-label="RealisticViewWarning" id="-282919766%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Realistic</span><wbr></wbr><span>View</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-282919766%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RealisticViewWarning</a></div><div class="brief "><p class="paragraph">A realistic view notification. This notification is given for complex junctions and it includes a visual representation of that junction, in order to help the user to better navigate it. When <a href="sdk-for-flutter-explore-distance-type">com.here.sdk.navigation.RealisticViewWarning.distanceType</a> is <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.DistanceType.AHEAD</a>, the <a href="sdk-for-flutter-explore-realistic-view-vector-image">com.here.sdk.navigation.RealisticViewWarning.realisticViewVectorImage</a> object will be provided with the junction view and the signpost representations. For <a href="sdk-for-flutter-explore-distance-type">com.here.sdk.navigation.RealisticViewWarning.distanceType</a> with value <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.DistanceType.PASSED</a>, the <a href="sdk-for-flutter-explore-realistic-view-vector-image">com.here.sdk.navigation.RealisticViewWarning.realisticViewVectorImage</a> object will be null. Use <code class="lang-kotlin">RealisticViewWarningListener</code> to get notifications about the realistic views of the upcoming junctions.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-868998826%2FClasslikes%2F1617540583" anchor-label="RealisticViewWarningListener" id="-868998826%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Realistic</span><wbr></wbr><span>View</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-868998826%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">RealisticViewWarningListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive realistic view warnings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="252621018%2FClasslikes%2F1617540583" anchor-label="RealisticViewWarningOptions" id="252621018%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Realistic</span><wbr></wbr><span>View</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="252621018%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RealisticViewWarningOptions</a></div><div class="brief "><p class="paragraph">Realistic view warning options. Set the options for filtering the realistic view notifications and setting the realistic view notification distances based on the road type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="992857956%2FClasslikes%2F1617540583" anchor-label="RoadAttributes" id="992857956%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Road</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="992857956%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RoadAttributes</a></div><div class="brief "><p class="paragraph">Road attributes, including usage and physical characteristics. Note that a road can have more than one attribute at the same time.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1258658320%2FClasslikes%2F1617540583" anchor-label="RoadAttributesListener" id="1258658320%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Road</span><wbr></wbr><span>Attributes</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1258658320%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">RoadAttributesListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive attributes of the current road.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2012253877%2FClasslikes%2F1617540583" anchor-label="RoadClassification" id="2012253877%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Road</span><wbr></wbr><span><span>Classification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2012253877%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">RoadClassification</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">RoadClassification</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Classification of the surrounding road environment. Note: This enum is in beta; its underlying layout is not stable and may change without any deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-148307650%2FClasslikes%2F1617540583" anchor-label="RoadSign" id="-148307650%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Road</span><wbr></wbr><span><span>Sign</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-148307650%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RoadSign</a></div><div class="brief "><p class="paragraph">Describes a road sign.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-843489056%2FClasslikes%2F1617540583" anchor-label="RoadSignCategory" id="-843489056%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Road</span><wbr></wbr><span>Sign</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-843489056%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">RoadSignCategory</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">RoadSignCategory</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Road sign category defining a general purpose of the sign.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1043642204%2FClasslikes%2F1617540583" anchor-label="RoadSignType" id="-1043642204%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Road</span><wbr></wbr><span>Sign</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1043642204%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">RoadSignType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">RoadSignType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">A road sign type classifying road signs that can appear along a road. Some signs are standardized and look the same in all countries, e.g. <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RoadSignType.STOP_SIGN</a>. In general, the visual appearance of the road signs can differ across countries. Some road signs can be combined with other signs, like <code class="lang-kotlin">WeatherType</code> signs. The road sign will be always shown topmost.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1791101790%2FClasslikes%2F1617540583" anchor-label="RoadSignVehicleType" id="1791101790%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Road</span><wbr></wbr><span>Sign</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1791101790%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">RoadSignVehicleType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">RoadSignVehicleType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Vehicle type for which a road sign is applicable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1054314872%2FClasslikes%2F1617540583" anchor-label="RoadSignWarning" id="-1054314872%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Road</span><wbr></wbr><span>Sign</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1054314872%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RoadSignWarning</a></div><div class="brief "><p class="paragraph">A road sign. The main field describing the sign is <a href="sdk-for-flutter-explore-type">com.here.sdk.navigation.RoadSignWarning.type</a>. Some road types are standardized, others can be country specific. A valid road sign contains known <a href="sdk-for-flutter-explore-type">com.here.sdk.navigation.RoadSignWarning.type</a> or <a href="sdk-for-flutter-explore-category">com.here.sdk.navigation.RoadSignWarning.category</a>. Use <code class="lang-kotlin">RoadSignWarningListener</code> to get notifications with current road signs.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1852779212%2FClasslikes%2F1617540583" anchor-label="RoadSignWarningListener" id="-1852779212%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Road</span><wbr></wbr><span>Sign</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1852779212%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">RoadSignWarningListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive road sign warnings. <strong>Note:</strong> The road sign warner is a point warner, which means that for a road sign there will <i>always</i> be 2 warnings emitted, with the RoadSignWarning.distance_type set to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.DistanceType.AHEAD</a> and <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.DistanceType.PASSED</a> which is given when the location of the road sign is reached. A <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RoadSignWarning</a> will not be given until the previous warning of that type has been passed. For example, a route with <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RoadSignWarning</a> 120 meters and <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RoadSignWarning</a> 160 meters ahead, the first RoadSignWarning.distance_to_road_sign_in_meters is 120 meters and the next RoadSignWarning.distance_to_road_sign_in_meters is then 40 meters, since that is the distance between the first and second warnings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1467812156%2FClasslikes%2F1617540583" anchor-label="RoadSignWarningOptions" id="1467812156%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Road</span><wbr></wbr><span>Sign</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1467812156%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RoadSignWarningOptions</a></div><div class="brief "><p class="paragraph">A class that provides road sign warning options. Set the options for filtering of road sign notifications.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1296753459%2FClasslikes%2F1617540583" anchor-label="RoadTextsListener" id="-1296753459%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Road</span><wbr></wbr><span>Texts</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1296753459%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">RoadTextsListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive textual attributes of the current road.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2060791523%2FClasslikes%2F1617540583" anchor-label="RouteDeviation" id="2060791523%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Route</span><wbr></wbr><span><span>Deviation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2060791523%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RouteDeviation</a></div><div class="brief "><p class="paragraph">Contains all the relevant information on a deviation from the route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-422507889%2FClasslikes%2F1617540583" anchor-label="RouteDeviationListener" id="-422507889%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Route</span><wbr></wbr><span>Deviation</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-422507889%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">RouteDeviationListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications about route deviations from <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Navigator</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="618780459%2FClasslikes%2F1617540583" anchor-label="RouteMatchedLocation" id="618780459%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Route</span><wbr></wbr><span>Matched</span><wbr></wbr><span><span>Location</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="618780459%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RouteMatchedLocation</a></div><div class="brief "><p class="paragraph">Represents a location matched to a specific position on a navigation route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1686144975%2FClasslikes%2F1617540583" anchor-label="RouteProgress" id="-1686144975%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Route</span><wbr></wbr><span><span>Progress</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1686144975%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RouteProgress</a></div><div class="brief "><p class="paragraph">Contains all the relevant information on the user's progress along a route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-495374175%2FClasslikes%2F1617540583" anchor-label="RouteProgressColors" id="-495374175%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Route</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Colors</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-495374175%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">RouteProgressColors</a></div><div class="brief "><p class="paragraph">This struct contains colors for the route progress visualization.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1845241309%2FClasslikes%2F1617540583" anchor-label="RouteProgressListener" id="1845241309%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Route</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1845241309%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">RouteProgressListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications about the route progress from <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Navigator</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2043476554%2FClasslikes%2F1617540583" anchor-label="SafetyCameraType" id="2043476554%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Safety</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2043476554%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">SafetyCameraType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">SafetyCameraType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates the type of the safety camera.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-834104542%2FClasslikes%2F1617540583" anchor-label="SafetyCameraWarning" id="-834104542%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Safety</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-834104542%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SafetyCameraWarning</a></div><div class="brief "><p class="paragraph">A class that provides safety camera warning information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1333247950%2FClasslikes%2F1617540583" anchor-label="SafetyCameraWarningListener" id="1333247950%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Safety</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1333247950%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">SafetyCameraWarningListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications on safety cameras. A <code class="lang-kotlin">SafetyCameraWarning</code> will not be given until the previous warning of that type has been passed. For example, a route with <code class="lang-kotlin">SafetyCameraWarning</code> 120 meters and <code class="lang-kotlin">SafetyCameraWarning</code> 160 meters ahead, the first <code class="lang-kotlin">SafetyCameraWarning.distance_to_camera_in_meters</code> is 120 meters and the next <code class="lang-kotlin">SafetyCameraWarning.distance_to_camera_in_meters</code> is then 40 meters, since that is the distance between the first and second warnings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1847681890%2FClasslikes%2F1617540583" anchor-label="SafetyCameraWarningOptions" id="1847681890%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Safety</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1847681890%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SafetyCameraWarningOptions</a></div><div class="brief "><p class="paragraph">Safety camera warning options. Set the options in order to enable them.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="229702987%2FClasslikes%2F1617540583" anchor-label="SchoolZoneWarning" id="229702987%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>School</span><wbr></wbr><span>Zone</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="229702987%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SchoolZoneWarning</a></div><div class="brief "><p class="paragraph">A school zone warning which notifies about a school zone presence on road with a speed limit different than the default speed limit applicable for cars. Use <code class="lang-kotlin">SchoolZoneWarningListener</code> to get notifications about school zones.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1144262409%2FClasslikes%2F1617540583" anchor-label="SchoolZoneWarningListener" id="-1144262409%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>School</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1144262409%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">SchoolZoneWarningListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive school zone warnings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1767762201%2FClasslikes%2F1617540583" anchor-label="SchoolZoneWarningOptions" id="1767762201%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>School</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1767762201%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SchoolZoneWarningOptions</a></div><div class="brief "><p class="paragraph">School zone warning options. Set the options for configuring of school zone notifications.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="530567573%2FClasslikes%2F1617540583" anchor-label="SectionProgress" id="530567573%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Section</span><wbr></wbr><span><span>Progress</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="530567573%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SectionProgress</a></div><div class="brief "><p class="paragraph">Indicates a user's progress along a <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.Section</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-604858325%2FClasslikes%2F1617540583" anchor-label="SpatialAudioCuePanning" id="-604858325%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Spatial</span><wbr></wbr><span>Audio</span><wbr></wbr><span>Cue</span><wbr></wbr><span><span>Panning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-604858325%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SpatialAudioCuePanning</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">Use the <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.SpatialAudioCuePanning</a> to notify each of the azimuths which compose a spatial audio trajectory along the audio cue.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1336070840%2FClasslikes%2F1617540583" anchor-label="SpatialNotificationDetails" id="-1336070840%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Spatial</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Details</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1336070840%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SpatialNotificationDetails</a></div><div class="brief "><p class="paragraph">This class provides all the information for a spatial text notification, including the maneuver data and extra data which is required to set the direction of spatialization of the audio cue.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-376942926%2FClasslikes%2F1617540583" anchor-label="SpatialTrajectoryData" id="-376942926%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Spatial</span><wbr></wbr><span>Trajectory</span><wbr></wbr><span><span>Data</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-376942926%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SpatialTrajectoryData</a></div><div class="brief "><p class="paragraph">This struct provides all the information regarding an angular panning element, including the panning angle and whether or not it is the last element on the spatial audio trajectory.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="90882456%2FClasslikes%2F1617540583" anchor-label="SpeedBasedCameraBehavior" id="90882456%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Speed</span><wbr></wbr><span>Based</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Behavior</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="90882456%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SpeedBasedCameraBehavior</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a>, <a href="sdk-for-flutter-explore-index">CameraBehavior</a></div><div class="brief "><p class="paragraph">Use this class to follow the current location of the user, zooming in and out and changing camera tilt according to the current speed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-803189785%2FClasslikes%2F1617540583" anchor-label="SpeedLimit" id="-803189785%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Speed</span><wbr></wbr><span><span>Limit</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-803189785%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SpeedLimit</a></div><div class="brief "><p class="paragraph">Represents the speed limit of the current road. Speed limits that are described as conditional can be time-dependent. For time-dependent speed limits, the HERE SDK internally reads the current device time and notifies only on speed limits that are currently active.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-759110765%2FClasslikes%2F1617540583" anchor-label="SpeedLimitListener" id="-759110765%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Speed</span><wbr></wbr><span>Limit</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-759110765%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">SpeedLimitListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive the speed limit of the current road.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1452636692%2FClasslikes%2F1617540583" anchor-label="SpeedLimitOffset" id="1452636692%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Speed</span><wbr></wbr><span>Limit</span><wbr></wbr><span><span>Offset</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1452636692%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SpeedLimitOffset</a></div><div class="brief "><p class="paragraph">A class that represents two separate speed limit offsets for higher and lower speed limits. A driver will be notified when the current driving speed is above the speed limit + offset. Only one of the two offsets is used depending on the current speed limit.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1247772782%2FClasslikes%2F1617540583" anchor-label="SpeedWarningListener" id="-1247772782%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Speed</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1247772782%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">SpeedWarningListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1145070818%2FClasslikes%2F1617540583" anchor-label="SpeedWarningOptions" id="-1145070818%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Speed</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1145070818%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SpeedWarningOptions</a></div><div class="brief "><p class="paragraph">A class that contains all options to be used for the speed limit warnings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1427646636%2FClasslikes%2F1617540583" anchor-label="SpeedWarningStatus" id="-1427646636%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Speed</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Status</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1427646636%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">SpeedWarningStatus</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">SpeedWarningStatus</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">This enum represents the status of the speed warning feature.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-890226999%2FClasslikes%2F1617540583" anchor-label="TextNotificationType" id="-890226999%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Text</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-890226999%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">TextNotificationType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">TextNotificationType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Different types of text notifications.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1517410840%2FClasslikes%2F1617540583" anchor-label="TimingProfile" id="-1517410840%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Timing</span><wbr></wbr><span><span>Profile</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1517410840%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">TimingProfile</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">TimingProfile</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Identifies the timing profile used for emitting notifications and warnings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1690702036%2FClasslikes%2F1617540583" anchor-label="TollBooth" id="-1690702036%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Toll</span><wbr></wbr><span><span>Booth</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1690702036%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">TollBooth</a></div><div class="brief "><p class="paragraph">A class that provides information of a toll stop. <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1510106848%2FClasslikes%2F1617540583" anchor-label="TollBoothLane" id="-1510106848%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Toll</span><wbr></wbr><span>Booth</span><wbr></wbr><span><span>Lane</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1510106848%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">TollBoothLane</a></div><div class="brief "><p class="paragraph">A class that provides information for a toll booth.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2031217311%2FClasslikes%2F1617540583" anchor-label="TollCollectionMethod" id="-2031217311%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Toll</span><wbr></wbr><span>Collection</span><wbr></wbr><span><span>Method</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2031217311%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">TollCollectionMethod</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">TollCollectionMethod</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Available payment methods.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="91549278%2FClasslikes%2F1617540583" anchor-label="TollStop" id="91549278%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Toll</span><wbr></wbr><span><span>Stop</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="91549278%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">TollStop</a></div><div class="brief "><p class="paragraph">A class that provides information for a toll stop with multiple toll booths.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="8979476%2FClasslikes%2F1617540583" anchor-label="TollStopWarningListener" id="8979476%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Toll</span><wbr></wbr><span>Stop</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="8979476%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">TollStopWarningListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive information on the upcoming toll booth structure.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1921803949%2FClasslikes%2F1617540583" anchor-label="TrackingCameraBehavior" id="1921803949%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Tracking</span><wbr></wbr><span>Camera</span><wbr></wbr><span><span>Behavior</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1921803949%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">TrackingCameraBehavior</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a>, <a href="sdk-for-flutter-explore-index">CameraBehavior</a></div><div class="brief "><p class="paragraph">Use this class to follow a moving target. The camera smoothly tracks the target’s position while adjusting heading, tilt, and zoom as needed. When tracking starts or resumes, the camera first animates a re-centering transition to align with the target.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1204641178%2FClasslikes%2F1617540583" anchor-label="TrafficMergeRoadType" id="-1204641178%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1204641178%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">TrafficMergeRoadType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">TrafficMergeRoadType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">The type of road which is merging onto the current road.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="862833065%2FClasslikes%2F1617540583" anchor-label="TrafficMergeSide" id="862833065%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span><span>Side</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="862833065%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">TrafficMergeSide</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">TrafficMergeSide</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">The side from where the merging traffic is joining with the current highway.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1841390278%2FClasslikes%2F1617540583" anchor-label="TrafficMergeWarning" id="1841390278%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1841390278%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">TrafficMergeWarning</a></div><div class="brief "><p class="paragraph">A class that provides warning for merging traffic. The main field describing the merging traffic is <code class="lang-kotlin">TrafficMergeWarning.road_type</code> specifying the type of road containing traffic which is merging with the current road. Use <code class="lang-kotlin">TrafficMergeWarningListener</code> to get notifications about upcoming merging traffic.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1216916338%2FClasslikes%2F1617540583" anchor-label="TrafficMergeWarningListener" id="1216916338%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1216916338%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">TrafficMergeWarningListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive traffic merge warnings. <strong>Note:</strong> The traffic merge warner is a point warner, which means that for a traffic merge there will <i>always</i> be 2 warnings emitted, with the <code class="lang-kotlin">TrafficMergeWarning.distance_type</code> set to <code class="lang-kotlin">DistanceType.AHEAD</code> and <code class="lang-kotlin">DistanceType.PASSED</code> which is given when the location of the traffic merge is reached. A <code class="lang-kotlin">TrafficMergeWarning</code> will not be given until the previous warning of that type has been passed. For example, a route with <code class="lang-kotlin">TrafficMergeWarning</code> 120 meters and <code class="lang-kotlin">TrafficMergeWarning</code> 160 meters ahead, the first <code class="lang-kotlin">TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is 120 meters and the next <code class="lang-kotlin">TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is then 40 meters, since that is the distance between the first and second warnings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1758301378%2FClasslikes%2F1617540583" anchor-label="TrafficMergeWarningOptions" id="-1758301378%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1758301378%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">TrafficMergeWarningOptions</a></div><div class="brief "><p class="paragraph">A class that provides traffic merge warning options. Set the options for filtering the traffic merge notifications.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1453739906%2FClasslikes%2F1617540583" anchor-label="TrafficOnRouteColors" id="-1453739906%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Traffic</span><wbr></wbr><span>On</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Colors</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1453739906%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">TrafficOnRouteColors</a></div><div class="brief "><p class="paragraph">This type contains colors used for the traffic with jam factor greater or equal to 4.0 on route ahead of the current location visualization.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1356266127%2FClasslikes%2F1617540583" anchor-label="TruckRestrictionsWarningListener" id="-1356266127%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Truck</span><wbr></wbr><span>Restrictions</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1356266127%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">TruckRestrictionsWarningListener</a></div><div class="brief "><p class="paragraph">This interface should be implemented in order to receive truck restriction warnings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1345281375%2FClasslikes%2F1617540583" anchor-label="TruckRestrictionsWarningOptions" id="1345281375%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Truck</span><wbr></wbr><span>Restrictions</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1345281375%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">TruckRestrictionsWarningOptions</a></div><div class="brief "><p class="paragraph">Truck restrictions warning options.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-679275144%2FClasslikes%2F1617540583" anchor-label="TruckRestrictionWarning" id="-679275144%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Truck</span><wbr></wbr><span>Restriction</span><wbr></wbr><span><span>Warning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-679275144%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">TruckRestrictionWarning</a></div><div class="brief "><p class="paragraph">Represents truck restrictions. For example, there can be a bridge ahead not high enough to pass a big truck or there can be a road ahead where the truck’s weight exceeds the permissible limit.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1824919152%2FClasslikes%2F1617540583" anchor-label="VisualNavigator" id="1824919152%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Visual</span><wbr></wbr><span><span>Navigator</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1824919152%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">VisualNavigator</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a>, <a href="sdk-for-flutter-explore-index">NavigatorInterface</a></div><div class="brief "><p class="paragraph">This class provides all functionality of <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.NavigatorInterface</a>. In addition, it provides advanced rendering capabilities for a smooth navigation experience. This includes interpolation of location updates along a route during turn-by-turn navigation and during tracking mode. By default, suitable map view settings are automatically applied. For example, a predefined current location marker is rendered. Similar to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Navigator</a>, this class continuously reacts to new locations provided from a location source and acts as a <a href="sdk-for-flutter-explore-index">com.here.sdk.core.LocationListener</a>. Note that the VisualNavigator takes control of the MapView's (maximum) frame rate when rendering, i.e., between <a href="sdk-for-flutter-explore-start-rendering">com.here.sdk.navigation.VisualNavigator.startRendering</a> and <a href="sdk-for-flutter-explore-stop-rendering">com.here.sdk.navigation.VisualNavigator.stopRendering</a> calls. It overwrites the MapView's frame rate when some camera behavior is set using the <a href="sdk-for-flutter-explore-guidance-frame-rate">com.here.sdk.navigation.VisualNavigator.guidanceFrameRate</a>. When no camera behavior is preset, the original MapView's frame rate (the value prior to the <a href="sdk-for-flutter-explore-start-rendering">com.here.sdk.navigation.VisualNavigator.startRendering</a> call) will be used. While the VisualNavigator is rendering, direct changes in the MapView's frame rate can lead to unexpected behavior and therefore should be avoided.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="312466336%2FClasslikes%2F1617540583" anchor-label="VisualNavigatorColors" id="312466336%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Visual</span><wbr></wbr><span>Navigator</span><wbr></wbr><span><span>Colors</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="312466336%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">VisualNavigatorColors</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><div class="brief "><p class="paragraph">This class contains colors used by <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.VisualNavigator</a> to render the route and the maneuver arrow visualization.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="749981219%2FClasslikes%2F1617540583" anchor-label="WallClock" id="749981219%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Wall</span><wbr></wbr><span><span>Clock</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="749981219%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">WallClock</a></div><div class="brief "><p class="paragraph">Clock used to properly retrieve time-dependent data from the map.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2002550204%2FClasslikes%2F1617540583" anchor-label="WarningNotificationDistances" id="-2002550204%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Warning</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Distances</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2002550204%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">WarningNotificationDistances</a></div><div class="brief "><p class="paragraph">Distances for emitting warnings according to the timing profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-198280111%2FClasslikes%2F1617540583" anchor-label="WarningType" id="-198280111%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Warning</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-198280111%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">WarningType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">WarningType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Identifies the warning type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="915403513%2FClasslikes%2F1617540583" anchor-label="WeatherType" id="915403513%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Weather</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="915403513%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">WeatherType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">WeatherType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Weather type attached to <code class="lang-kotlin">RoadSignWarning</code> or <code class="lang-kotlin">VehicleRestriction.Condition</code> which limits the conditions for which the sign is applicable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1791683667%2FClasslikes%2F1617540583" anchor-label="WeightRestriction" id="1791683667%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Weight</span><wbr></wbr><span><span>Restriction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1791683667%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">WeightRestriction</a></div><div class="brief "><p class="paragraph">Defines a weight restriction.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1839702329%2FClasslikes%2F1617540583" anchor-label="WeightRestrictionType" id="1839702329%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Weight</span><wbr></wbr><span>Restriction</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1839702329%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">WeightRestrictionType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">WeightRestrictionType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Defines the type of a weight restriction.</p></div></div></div>
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
