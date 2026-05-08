---
title: "VisualNavigator"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>VisualNavigator</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.navigation/VisualNavigator///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.navigation</a><span class="delimiter">/</span><span class="current">VisualNavigator</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Visual</span><wbr></wbr><span><span>Navigator</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">VisualNavigator</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a>, <a href="sdk-for-flutter-explore-index">NavigatorInterface</a></div><p class="paragraph">This class provides all functionality of <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.NavigatorInterface</a>. In addition, it provides advanced rendering capabilities for a smooth navigation experience. This includes interpolation of location updates along a route during turn-by-turn navigation and during tracking mode. By default, suitable map view settings are automatically applied. For example, a predefined current location marker is rendered. Similar to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Navigator</a>, this class continuously reacts to new locations provided from a location source and acts as a <a href="sdk-for-flutter-explore-index">com.here.sdk.core.LocationListener</a>. Note that the VisualNavigator takes control of the MapView's (maximum) frame rate when rendering, i.e., between <a href="sdk-for-flutter-explore-start-rendering">com.here.sdk.navigation.VisualNavigator.startRendering</a> and <a href="sdk-for-flutter-explore-stop-rendering">com.here.sdk.navigation.VisualNavigator.stopRendering</a> calls. It overwrites the MapView's frame rate when some camera behavior is set using the <a href="sdk-for-flutter-explore-guidance-frame-rate">com.here.sdk.navigation.VisualNavigator.guidanceFrameRate</a>. When no camera behavior is preset, the original MapView's frame rate (the value prior to the <a href="sdk-for-flutter-explore-start-rendering">com.here.sdk.navigation.VisualNavigator.startRendering</a> call) will be used. While the VisualNavigator is rendering, direct changes in the MapView's frame rate can lead to unexpected behavior and therefore should be avoided.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="426472549%2FConstructors%2F1617540583" anchor-label="VisualNavigator" id="426472549%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-visual-navigator"><span>Visual</span><wbr></wbr><span><span>Navigator</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="426472549%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">sdkEngine<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SDKNativeEngine</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">navigator<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">NavigatorInterface</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class using provided instance of <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.NavigatorInterface</a> as source of data.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">sdkEngine<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SDKNativeEngine</a><span class="token punctuation">, </span></span><span class="parameter ">navigator<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">NavigatorInterface</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class using provided instance of <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.NavigatorInterface</a> as source of data.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1979539186%2FClasslikes%2F1617540583" anchor-label="Companion" id="1979539186%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1979539186%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="1922862665%2FProperties%2F1617540583" anchor-label="borderCrossingWarningListener" id="1922862665%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-border-crossing-warning-listener"><span>border</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1922862665%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-border-crossing-warning-listener">borderCrossingWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">BorderCrossingWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about border crossings on the current road. Border crossing notifications are given only if a route is present. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-126101985%2FProperties%2F1617540583" anchor-label="borderCrossingWarningOptions" id="-126101985%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-border-crossing-warning-options"><span>border</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-126101985%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-border-crossing-warning-options">borderCrossingWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">BorderCrossingWarningOptions</a></div><div class="brief "><p class="paragraph">Border crossing warning options to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.BorderCrossingWarningListener</a>. These options allow the filtering of the border crossing warnings received and set the notification distances.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1161716184%2FProperties%2F1617540583" anchor-label="cameraBehavior" id="1161716184%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-camera-behavior"><span>camera</span><wbr></wbr><span><span>Behavior</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1161716184%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-camera-behavior">cameraBehavior</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">CameraBehavior</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Camera behavior which defines how the <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.VisualNavigator</a> handles the camera. Setting <code class="lang-kotlin">null</code> disables any camera behavior with the result that the camera does not follow the current location and keeps the last active camera state, i.e., current zoom and tilt. Furthermore, when <code class="lang-kotlin">null</code> is set map gestures can be used again to freely pan and zoom the map. In opposition, when a camera behavior is defined, then the map cannot be panned and zoomed by the user. The default value is an instance of <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.FixedCameraBehavior</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1209463071%2FProperties%2F1617540583" anchor-label="colors" id="1209463071%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-colors"><span><span>colors</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1209463071%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-colors">colors</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VisualNavigatorColors</a></div><div class="brief "><p class="paragraph">Object containing colors used to render route progress and maneuver arrow visualization. Setting a new instance overwrites the default color settings as specified in <code class="lang-kotlin">VisualNavigatorColors</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1612676749%2FProperties%2F1617540583" anchor-label="currentSituationLaneAssistanceViewListener" id="1612676749%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-current-situation-lane-assistance-view-listener"><span>current</span><wbr></wbr><span>Situation</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span>View</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1612676749%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-current-situation-lane-assistance-view-listener">currentSituationLaneAssistanceViewListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">CurrentSituationLaneAssistanceViewListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive current situation lane assistance view notifications. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-162369822%2FProperties%2F1617540583" anchor-label="customLocationIndicator" id="-162369822%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-custom-location-indicator"><span>custom</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Indicator</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-162369822%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-custom-location-indicator">customLocationIndicator</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LocationIndicator</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Custom location indicator <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.LocationIndicator</a> which <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.VisualNavigator</a> uses instead of the default. If set, the user is responsible for adding and removing the object to/from the mapview. It is important to stop sending location updates to the provided <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.LocationIndicator</a>, since <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.VisualNavigator</a> will control its position when rendering is active, i.e., between startRendering() and stopRendering() calls. By default this property is <code class="lang-kotlin">null</code>, which means the default indicator is used, and <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.VisualNavigator</a> automatically adds and removes it to/from the mapview upon startRendering() and stopRendering() calls.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1292746954%2FProperties%2F1617540583" anchor-label="dangerZoneWarningListener" id="1292746954%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-danger-zone-warning-listener"><span>danger</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1292746954%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-danger-zone-warning-listener">dangerZoneWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">DangerZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notification on approaching danger zones. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="821185394%2FProperties%2F1617540583" anchor-label="debugGpxFilePath" id="821185394%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-debug-gpx-file-path"><span>debug</span><wbr></wbr><span>Gpx</span><wbr></wbr><span>File</span><wbr></wbr><span><span>Path</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="821185394%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-debug-gpx-file-path">debugGpxFilePath</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Show the contents of a GPX file on the map. <strong>Note:</strong> This API should be used for debugging purposes only.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-937861033%2FProperties%2F1617540583" anchor-label="destinationReachedListener" id="-937861033%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-destination-reached-listener"><span>destination</span><wbr></wbr><span>Reached</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-937861033%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-destination-reached-listener">destinationReachedListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">DestinationReachedListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive the notification about the arrival at the destination. Destination reached notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-660156407%2FProperties%2F1617540583" anchor-label="environmentalZoneWarningListener" id="-660156407%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-environmental-zone-warning-listener"><span>environmental</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-660156407%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-environmental-zone-warning-listener">environmentalZoneWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">EnvironmentalZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notification on approaching environmental zones. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-766388400%2FProperties%2F1617540583" anchor-label="eventTextListener" id="-766388400%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-event-text-listener"><span>event</span><wbr></wbr><span>Text</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-766388400%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-event-text-listener">eventTextListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">EventTextListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive text notifications when they are available. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user. <strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner, when <code class="lang-kotlin">TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code class="lang-kotlin">sdk.navigation.EventTextListener</code> must be enabled as well.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-905588680%2FProperties%2F1617540583" anchor-label="eventTextOptions" id="-905588680%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-event-text-options"><span>event</span><wbr></wbr><span>Text</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-905588680%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-event-text-options">eventTextOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">EventTextOptions</a></div><div class="brief "><p class="paragraph">Options used for text notifications. Notifications are only available if a route is present.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-207177258%2FProperties%2F1617540583" anchor-label="guidanceFrameRate" id="-207177258%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-guidance-frame-rate"><span>guidance</span><wbr></wbr><span>Frame</span><wbr></wbr><span><span>Rate</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-207177258%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-guidance-frame-rate">guidanceFrameRate</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">Frame rate used during guidance. Frame rate used during guidance. Default is 30fps.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="321152867%2FProperties%2F1617540583" anchor-label="interpolatedLocationListener" id="321152867%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-interpolated-location-listener"><span>interpolated</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="321152867%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-interpolated-location-listener">interpolatedLocationListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">InterpolatedLocationListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive interpolated locations. For example, to pan a second instance of a <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapViewBase</a> or move additional markers smoothly. The map-matched locations are used if available, otherwise the non-map-matched ones are used instead. Defaults to <code class="lang-kotlin">null</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1755779558%2FProperties%2F1617540583" anchor-label="isDebugModeEnabled" id="-1755779558%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-debug-mode-enabled"><span>is</span><wbr></wbr><span>Debug</span><wbr></wbr><span>Mode</span><wbr></wbr><span><span>Enabled</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1755779558%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-debug-mode-enabled">isDebugModeEnabled</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">When enabled, it shows useful information for debugging purposes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="54019426%2FProperties%2F1617540583" anchor-label="isDynamicFrameRateEnabled" id="54019426%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-dynamic-frame-rate-enabled"><span>is</span><wbr></wbr><span>Dynamic</span><wbr></wbr><span>Frame</span><wbr></wbr><span>Rate</span><wbr></wbr><span><span>Enabled</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="54019426%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-dynamic-frame-rate-enabled">isDynamicFrameRateEnabled</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Flag used to enable or disable the dynamic frame rate. Controls whether the number of map updates is dynamically calculated based on the current zoom level. If the zoom level is low, i.e., the camera target distance is high, updates to LocationIndicator, MapCamera and MapPolylines representing the route progress will happen less frequent. It is on by default.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1224624440%2FProperties%2F1617540583" anchor-label="isEnableTunnelExtrapolation" id="-1224624440%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-enable-tunnel-extrapolation"><span>is</span><wbr></wbr><span>Enable</span><wbr></wbr><span>Tunnel</span><wbr></wbr><span><span>Extrapolation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1224624440%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-enable-tunnel-extrapolation">isEnableTunnelExtrapolation</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Defines whether to enable or disable tunnel extrapolation. By default the tunnel extrapolation is enabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-950872996%2FProperties%2F1617540583" anchor-label="isExtrapolationEnabled" id="-950872996%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-extrapolation-enabled"><span>is</span><wbr></wbr><span>Extrapolation</span><wbr></wbr><span><span>Enabled</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-950872996%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-extrapolation-enabled">isExtrapolationEnabled</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Defines whether the position extrapolation logic is enabled or not. The predicted location follows the geometry of the route (or road) ahead. By default it is enabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1336456199%2FProperties%2F1617540583" anchor-label="isLocationAccuracyVisualized" id="1336456199%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-location-accuracy-visualized"><span>is</span><wbr></wbr><span>Location</span><wbr></wbr><span>Accuracy</span><wbr></wbr><span><span>Visualized</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1336456199%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-location-accuracy-visualized">isLocationAccuracyVisualized</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Controls if the halo accuracy visualization of the default <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.LocationIndicator</a> is rendered or not. Does not affect halo accuracy indicator of the <a href="sdk-for-flutter-explore-custom-location-indicator">com.here.sdk.navigation.VisualNavigator.customLocationIndicator</a>. If <a href="sdk-for-flutter-explore-custom-location-indicator">com.here.sdk.navigation.VisualNavigator.customLocationIndicator</a> is set, then its halo accuracy indicator can be controlled using <a href="sdk-for-flutter-explore-is-accuracy-visualized">com.here.sdk.mapview.LocationIndicator.isAccuracyVisualized</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="944149414%2FProperties%2F1617540583" anchor-label="isManeuverArrowsVisible" id="944149414%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-maneuver-arrows-visible"><span>is</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span>Arrows</span><wbr></wbr><span><span>Visible</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="944149414%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-maneuver-arrows-visible">isManeuverArrowsVisible</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Maneuver arrows visibility which defines whether to perform maneuver arrow rendering during visual navigation. By default, it is enabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="950553666%2FProperties%2F1617540583" anchor-label="isOffRoadDestinationVisible" id="950553666%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-off-road-destination-visible"><span>is</span><wbr></wbr><span>Off</span><wbr></wbr><span>Road</span><wbr></wbr><span>Destination</span><wbr></wbr><span><span>Visible</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="950553666%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-off-road-destination-visible">isOffRoadDestinationVisible</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Off road destination visibility which defines whether to show a dashed line between the map-matched and the original destination which is off-road. By default it is enabled. <strong>Note:</strong> The dashed line will be drawn only if the original destination is off-road.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1625120599%2FProperties%2F1617540583" anchor-label="isPassthroughWaypointsHandlingEnabled" id="1625120599%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-passthrough-waypoints-handling-enabled"><span>is</span><wbr></wbr><span>Passthrough</span><wbr></wbr><span>Waypoints</span><wbr></wbr><span>Handling</span><wbr></wbr><span><span>Enabled</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1625120599%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-passthrough-waypoints-handling-enabled">isPassthroughWaypointsHandlingEnabled</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Defines whether to enable or disable handling of passthrough waypoints. By default the handling of passthrough waypoints is disabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1088608233%2FProperties%2F1617540583" anchor-label="isRendering" id="1088608233%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-rendering"><span>is</span><wbr></wbr><span><span>Rendering</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1088608233%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-is-rendering">isRendering</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Returns a value indicating whether visual navigation rendering is enabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-543454455%2FProperties%2F1617540583" anchor-label="isRouteProgressVisible" id="-543454455%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-route-progress-visible"><span>is</span><wbr></wbr><span>Route</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Visible</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-543454455%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-route-progress-visible">isRouteProgressVisible</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph"><code class="lang-kotlin">RouteProgress</code> visibility which defines whether to perform route progress coloring (&quot;eat-up&quot;) during visual navigation. By default, it is enabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-256673348%2FProperties%2F1617540583" anchor-label="isRouteVisible" id="-256673348%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-route-visible"><span>is</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Visible</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-256673348%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-route-visible">isRouteVisible</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph"><code class="lang-kotlin">Route</code> visibility which defines whether to perform route rendering during visual navigation. When enabled, the set <code class="lang-kotlin">Route</code> will be rendered as a <code class="lang-kotlin">MapPolyline</code> together with <code class="lang-kotlin">MapArrow</code> items that indicate the next turns. By default, it is enabled. When disabled, <code class="lang-kotlin">MapArrow</code> items are still rendered. To hide arrows, use <code class="lang-kotlin">VisualNavigatorColors</code> with transparent color.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-339685424%2FProperties%2F1617540583" anchor-label="isTrafficOnRouteVisible" id="-339685424%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-is-traffic-on-route-visible"><span>is</span><wbr></wbr><span>Traffic</span><wbr></wbr><span>On</span><wbr></wbr><span>Route</span><wbr></wbr><span><span>Visible</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-339685424%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-is-traffic-on-route-visible">isTrafficOnRouteVisible</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">A boolean which defines whether to perform rendering of traffic conditions on the route when <code class="lang-kotlin">Route</code> visualization is enabled during visual navigation. When enabled the route's <code class="lang-kotlin">MapPolyline</code> will be enhanced with visualization of the traffic conditions. Colors used for this visualization are defined in <a href="sdk-for-flutter-explore-traffic-on-route-colors">com.here.sdk.navigation.VisualNavigatorColors.trafficOnRouteColors</a>. The presented traffic information is either set by the user via <a href="sdk-for-flutter-explore-traffic-on-route">com.here.sdk.navigation.NavigatorInterface.trafficOnRoute</a> or is generated from historical traffic data stored in the map. <strong>Note:</strong> <code class="lang-kotlin">VisualNavigator</code> does not perform automatic traffic data updates. The updated traffic information is available through the sdk.routing.RoutingEngine.calculate_traffic_on_route interface. The returned <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.TrafficOnRoute</a> could then be used to update sdk.navigation.NavigatorInterface.traffic_on_route to refresh the traffic on route visualization. Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-756923362%2FProperties%2F1617540583" anchor-label="junctionViewLaneAssistanceListener" id="-756923362%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-junction-view-lane-assistance-listener"><span>junction</span><wbr></wbr><span>View</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-756923362%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-junction-view-lane-assistance-listener">junctionViewLaneAssistanceListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">JunctionViewLaneAssistanceListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive junction view lane assistance notifications. Junction view lane assistance notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-568365069%2FProperties%2F1617540583" anchor-label="locationManager" id="-568365069%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-location-manager"><span>location</span><wbr></wbr><span><span>Manager</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-568365069%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">val </span><a href="sdk-for-flutter-explore-location-manager">locationManager</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LocationManager</a></div><div class="brief "><p class="paragraph">The location manager used by the navigator for map-matched location processing.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1544306810%2FProperties%2F1617540583" anchor-label="lowSpeedZoneWarningListener" id="1544306810%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-low-speed-zone-warning-listener"><span>low</span><wbr></wbr><span>Speed</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1544306810%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-low-speed-zone-warning-listener">lowSpeedZoneWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LowSpeedZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about low speed zones on the current road. Low speed zone notifications are given regardless if a route is set. This listener is currently available <i>only</i> for Japan. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="656195274%2FProperties%2F1617540583" anchor-label="maneuverArrowWidthFactor" id="656195274%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-maneuver-arrow-width-factor"><span>maneuver</span><wbr></wbr><span>Arrow</span><wbr></wbr><span>Width</span><wbr></wbr><span><span>Factor</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="656195274%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-maneuver-arrow-width-factor">maneuverArrowWidthFactor</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief "><p class="paragraph">A factor of <a href="sdk-for-flutter-explore-measure-dependent-width">com.here.sdk.navigation.VisualNavigator.measureDependentWidth</a> defining the width of the maneuver arrow. The factor should be positive. A value less than or equal to 0 is ignored. By default it is set to one.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1017780015%2FProperties%2F1617540583" anchor-label="maneuverNotificationOptions" id="-1017780015%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-maneuver-notification-options"><span>maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1017780015%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-maneuver-notification-options">maneuverNotificationOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">ManeuverNotificationOptions</a></div><div class="brief "><p class="paragraph">Options used for maneuver notifications. Notifications are only available if a route is present.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1262764167%2FProperties%2F1617540583" anchor-label="maneuverViewLaneAssistanceListener" id="-1262764167%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-maneuver-view-lane-assistance-listener"><span>maneuver</span><wbr></wbr><span>View</span><wbr></wbr><span>Lane</span><wbr></wbr><span>Assistance</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1262764167%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-maneuver-view-lane-assistance-listener">maneuverViewLaneAssistanceListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">ManeuverViewLaneAssistanceListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive maneuver view lane assistance notifications. Maneuver view lane assistance notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-836687546%2FProperties%2F1617540583" anchor-label="measureDependentWidth" id="-836687546%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-measure-dependent-width"><span>measure</span><wbr></wbr><span>Dependent</span><wbr></wbr><span><span>Width</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-836687546%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-measure-dependent-width">measureDependentWidth</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">MapMeasure</a><span class="token punctuation">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The <code class="lang-kotlin">measureDependentWidth</code> that defines the route and maneuver arrows width. It is a dictionary that has keys that are <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasure</a>s and values that are width in pixels at this <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasure</a>s. This route and maneuver arrows width is multiplied by a pixel_scale <a href="sdk-for-flutter-explore-pixel-scale">com.here.sdk.mapview.MapViewBase.pixelScale</a> before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with <a href="sdk-for-flutter-explore-maneuver-arrow-width-factor">com.here.sdk.navigation.VisualNavigator.maneuverArrowWidthFactor</a>; which by default equals one. The function defined by a dictionary is linearly interpolated between each successive pair of data points. For keys below the lowest <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasure</a>, its corresponding value width is used. For keys above the highest <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasure</a>, its corresponding value width is used. Only <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasure</a> of sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL type are supported. <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasure</a> of other unsupported types will be ignored. <code class="lang-kotlin">measureDependentWidth</code> with a single entry is equivalent to use of the constant width value of this single entry for all <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapMeasure</a>s. Empty <code class="lang-kotlin">measureDependentWidth</code> is ignored and existing dictionary of width is maintained. The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored. If route and maneuver arrows were not configured with this property, then <code class="lang-kotlin">measureDependentWidth</code> contains predefined values chosen to be optimal for different route classes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="484178325%2FProperties%2F1617540583" anchor-label="milestoneStatusListener" id="484178325%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-milestone-status-listener"><span>milestone</span><wbr></wbr><span>Status</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="484178325%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-milestone-status-listener">milestoneStatusListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MilestoneStatusListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the arrival at each <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Milestone</a> or missing it. It informs on all waypoints (passed or missed) that are of type <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.MilestoneType.STOPOVER</a> but excludes the starting waypoint. Waypoints of type <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.MilestoneType.PASSTHROUGH</a> are excluded, by default, but can be included via <a href="sdk-for-flutter-explore-is-passthrough-waypoints-handling-enabled">com.here.sdk.navigation.NavigatorInterface.isPassthroughWaypointsHandlingEnabled</a>. Milestone status notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-576723417%2FProperties%2F1617540583" anchor-label="navigableLocationListener" id="-576723417%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-navigable-location-listener"><span>navigable</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-576723417%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-navigable-location-listener">navigableLocationListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">NavigableLocationListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the current location. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="264969924%2FProperties%2F1617540583" anchor-label="offRoadDestinationReachedListener" id="264969924%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-off-road-destination-reached-listener"><span>off</span><wbr></wbr><span>Road</span><wbr></wbr><span>Destination</span><wbr></wbr><span>Reached</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="264969924%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-off-road-destination-reached-listener">offRoadDestinationReachedListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">OffRoadDestinationReachedListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive the notification about the arrival at the off-road destination. Off-road destination reached notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1446417957%2FProperties%2F1617540583" anchor-label="offRoadProgressListener" id="-1446417957%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-off-road-progress-listener"><span>off</span><wbr></wbr><span>Road</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1446417957%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-off-road-progress-listener">offRoadProgressListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">OffRoadProgressListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive the notification about the off-road progress. Off-road progress notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-855744763%2FProperties%2F1617540583" anchor-label="postActionListener" id="-855744763%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-post-action-listener"><span>post</span><wbr></wbr><span>Action</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-855744763%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-post-action-listener">postActionListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">PostActionListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive post action notifications, such as a charge action at a charging station. Post actions notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="373465630%2FProperties%2F1617540583" anchor-label="railwayCrossingWarningListener" id="373465630%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-railway-crossing-warning-listener"><span>railway</span><wbr></wbr><span>Crossing</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="373465630%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-railway-crossing-warning-listener">railwayCrossingWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RailwayCrossingWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about railway crossings on the current road. Railway crossing notifications are given regardless if a route is set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1605220918%2FProperties%2F1617540583" anchor-label="realisticViewWarningListener" id="-1605220918%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-realistic-view-warning-listener"><span>realistic</span><wbr></wbr><span>View</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1605220918%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-realistic-view-warning-listener">realisticViewWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RealisticViewWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about junction views on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. This feature requires a map version greater or equal to 67 in order to function properly. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1486837122%2FProperties%2F1617540583" anchor-label="realisticViewWarningOptions" id="-1486837122%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-realistic-view-warning-options"><span>realistic</span><wbr></wbr><span>View</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1486837122%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-realistic-view-warning-options">realisticViewWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RealisticViewWarningOptions</a></div><div class="brief "><p class="paragraph">Realistic view warning options. It allow to filter realistic views to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RealisticViewWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-290911100%2FProperties%2F1617540583" anchor-label="roadAttributesListener" id="-290911100%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-road-attributes-listener"><span>road</span><wbr></wbr><span>Attributes</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-290911100%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-road-attributes-listener">roadAttributesListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RoadAttributesListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about attributes of the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-997418280%2FProperties%2F1617540583" anchor-label="roadSignWarningListener" id="-997418280%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-road-sign-warning-listener"><span>road</span><wbr></wbr><span>Sign</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-997418280%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-road-sign-warning-listener">roadSignWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RoadSignWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about road signs on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-81757264%2FProperties%2F1617540583" anchor-label="roadSignWarningOptions" id="-81757264%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-road-sign-warning-options"><span>road</span><wbr></wbr><span>Sign</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-81757264%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-road-sign-warning-options">roadSignWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RoadSignWarningOptions</a></div><div class="brief "><p class="paragraph">Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RoadSignWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="261280881%2FProperties%2F1617540583" anchor-label="roadTextsListener" id="261280881%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-road-texts-listener"><span>road</span><wbr></wbr><span>Texts</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="261280881%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-road-texts-listener">roadTextsListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RoadTextsListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the textual attributes of the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="469300866%2FProperties%2F1617540583" anchor-label="route" id="469300866%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-route"><span><span>route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="469300866%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-route">route</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Route</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The route to navigate. Gets and sets the route that is being navigated. If not set, only the current location information will be provided through <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.NavigableLocationListener</a>. If set, both route progress (<a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RouteProgressListener</a>) and route deviation (<a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.RouteDeviationListener</a>) will receive notifications on updates. A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1972077309%2FProperties%2F1617540583" anchor-label="routeDeviationListener" id="-1972077309%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-route-deviation-listener"><span>route</span><wbr></wbr><span>Deviation</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1972077309%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-route-deviation-listener">routeDeviationListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RouteDeviationListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about deviations from the route if any occurs. Route deviation notifications only occurs if a route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1260654194%2FProperties%2F1617540583" anchor-label="routeDrawOrder" id="-1260654194%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-route-draw-order"><span>route</span><wbr></wbr><span>Draw</span><wbr></wbr><span><span>Order</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1260654194%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-route-draw-order">routeDrawOrder</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The draw order of the polylines representing the route. The draw order of the polylines representing the route. For more details see <a href="sdk-for-flutter-explore-draw-order">com.here.sdk.mapview.MapPolyline.drawOrder</a>. The default is 0.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="178730740%2FProperties%2F1617540583" anchor-label="routeDrawOrderType" id="178730740%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-route-draw-order-type"><span>route</span><wbr></wbr><span>Draw</span><wbr></wbr><span>Order</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="178730740%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-route-draw-order-type">routeDrawOrderType</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">DrawOrderType</a></div><div class="brief "><p class="paragraph">The draw order type of the polylines representing the route. The draw order type of the polylines representing the route. For more details see <a href="sdk-for-flutter-explore-draw-order-type">com.here.sdk.mapview.MapPolyline.drawOrderType</a>. The default is <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1444474495%2FProperties%2F1617540583" anchor-label="routeProgressListener" id="-1444474495%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-route-progress-listener"><span>route</span><wbr></wbr><span>Progress</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1444474495%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-route-progress-listener">routeProgressListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">RouteProgressListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about navigation route progress. Route progress notifications only occurs if the route has been set. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-406210190%2FProperties%2F1617540583" anchor-label="safetyCameraWarningListener" id="-406210190%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-safety-camera-warning-listener"><span>safety</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-406210190%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-safety-camera-warning-listener">safetyCameraWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SafetyCameraWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive safety camera warner notifications. If a listener  is present, notifications about safety speed cameras will be also sent via <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.SafetyCameraWarningListener</a>. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1322787286%2FProperties%2F1617540583" anchor-label="safetyCameraWarningOptions" id="1322787286%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-safety-camera-warning-options"><span>safety</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1322787286%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-safety-camera-warning-options">safetyCameraWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SafetyCameraWarningOptions</a></div><div class="brief "><p class="paragraph">Safety camera warning options to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.SafetyCameraWarningListener</a>. These options allow the enabling or disabling the text notification for the warner.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1695158427%2FProperties%2F1617540583" anchor-label="schoolZoneWarningListener" id="1695158427%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-school-zone-warning-listener"><span>school</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1695158427%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-school-zone-warning-listener">schoolZoneWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SchoolZoneWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about school zones on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. school zones on the current road. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-133447283%2FProperties%2F1617540583" anchor-label="schoolZoneWarningOptions" id="-133447283%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-school-zone-warning-options"><span>school</span><wbr></wbr><span>Zone</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-133447283%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-school-zone-warning-options">schoolZoneWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SchoolZoneWarningOptions</a></div><div class="brief "><p class="paragraph">School zone warning options It allow to configure school zone notifications to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.SchoolZoneWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1942686215%2FProperties%2F1617540583" anchor-label="speedLimitListener" id="1942686215%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-speed-limit-listener"><span>speed</span><wbr></wbr><span>Limit</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1942686215%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-speed-limit-listener">speedLimitListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SpeedLimitListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about the speed limit of the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2099770362%2FProperties%2F1617540583" anchor-label="speedWarningListener" id="-2099770362%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-speed-warning-listener"><span>speed</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2099770362%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-speed-warning-listener">speedWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SpeedWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1641337662%2FProperties%2F1617540583" anchor-label="speedWarningOptions" id="-1641337662%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-speed-warning-options"><span>speed</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1641337662%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-speed-warning-options">speedWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SpeedWarningOptions</a></div><div class="brief "><p class="paragraph">Options used for the speed warning feature.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="864340408%2FProperties%2F1617540583" anchor-label="tollStopWarningListener" id="864340408%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-toll-stop-warning-listener"><span>toll</span><wbr></wbr><span>Stop</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="864340408%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-toll-stop-warning-listener">tollStopWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TollStopWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive information on the upcoming toll stop. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="463513816%2FProperties%2F1617540583" anchor-label="trackingTransportProfile" id="463513816%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-tracking-transport-profile"><span>tracking</span><wbr></wbr><span>Transport</span><wbr></wbr><span><span>Profile</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="463513816%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-tracking-transport-profile"><strike>trackingTransportProfile</strike></a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TransportProfile</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Defines the transport profile for the <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Navigator</a>, when no route is present. Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a <a href="sdk-for-flutter-explore-index">com.here.sdk.core.TransportProfile</a> can be defined with a <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.VehicleProfile</a>. A vehicle profile can have several parameters such as <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.VehicleType</a> to set the source of information describing the vehicle. The default is a <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.VehicleType.CAR</a> profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-627867714%2FProperties%2F1617540583" anchor-label="trackingTransportSpecification" id="-627867714%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-tracking-transport-specification"><span>tracking</span><wbr></wbr><span>Transport</span><wbr></wbr><span><span>Specification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-627867714%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-tracking-transport-specification">trackingTransportSpecification</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TransportSpecification</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Defines the transport specification for the <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.Navigator</a>, when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportSpecification</a> must have the <a href="sdk-for-flutter-explore-transport-mode">com.here.sdk.transport.TransportSpecification.transportMode</a> set. A transport specification can have several parameters defined such as <a href="sdk-for-flutter-explore-length-in-centimeters">com.here.sdk.transport.VehicleSpecification.lengthInCentimeters</a> defined in <a href="sdk-for-flutter-explore-vehicle-specification">com.here.sdk.transport.TransportSpecification.vehicleSpecification</a> to set the source of information describing the vehicle. By default the <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportSpecification</a> will have the transport mode set to <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportMode.CAR</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-522541802%2FProperties%2F1617540583" anchor-label="trafficMergeWarningListener" id="-522541802%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-traffic-merge-warning-listener"><span>traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-522541802%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-traffic-merge-warning-listener">trafficMergeWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficMergeWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about merging traffic to the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2011771314%2FProperties%2F1617540583" anchor-label="trafficMergeWarningOptions" id="2011771314%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-traffic-merge-warning-options"><span>traffic</span><wbr></wbr><span>Merge</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2011771314%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-traffic-merge-warning-options">trafficMergeWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficMergeWarningOptions</a></div><div class="brief "><p class="paragraph">Merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TrafficMergeWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-617923518%2FProperties%2F1617540583" anchor-label="trafficOnRoute" id="-617923518%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-traffic-on-route"><span>traffic</span><wbr></wbr><span>On</span><wbr></wbr><span><span>Route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-617923518%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-traffic-on-route">trafficOnRoute</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TrafficOnRoute</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Traffic information for the current route. This impacts <code class="lang-kotlin">RouteProgress</code> updates as the duration of the <code class="lang-kotlin">SectionProgress</code> might change. However, the remaining distance and the route geometry will remain unchanged.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1078888987%2FProperties%2F1617540583" anchor-label="truckRestrictionsWarningListener" id="-1078888987%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-truck-restrictions-warning-listener"><span>truck</span><wbr></wbr><span>Restrictions</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1078888987%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-truck-restrictions-warning-listener">truckRestrictionsWarningListener</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TruckRestrictionsWarningListener</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Object to receive notifications about truck restrictions on the current road. Setting <code class="lang-kotlin">null</code> value to the listener will unset the listener. It returns <code class="lang-kotlin">null</code> when no listener is set by an user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1885500669%2FProperties%2F1617540583" anchor-label="truckRestrictionsWarningOptions" id="-1885500669%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-truck-restrictions-warning-options"><span>truck</span><wbr></wbr><span>Restrictions</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1885500669%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">var </span><a href="sdk-for-flutter-explore-truck-restrictions-warning-options">truckRestrictionsWarningOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TruckRestrictionsWarningOptions</a></div><div class="brief "><p class="paragraph">Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-flutter-explore-index">com.here.sdk.navigation.TruckRestrictionsWarningListener</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-140055846%2FProperties%2F1617540583" anchor-label="warnerEngine" id="-140055846%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-warner-engine"><span>warner</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-140055846%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">val </span><a href="sdk-for-flutter-explore-warner-engine">warnerEngine</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WarnerEngine</a></div><div class="brief "><p class="paragraph">Warner engine used by the navigator. This engine can be used to configure navigation warnings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="714034119%2FFunctions%2F1617540583" anchor-label="calculateRemainingDistanceInMeters" id="714034119%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-calculate-remaining-distance-in-meters"><span>calculate</span><wbr></wbr><span>Remaining</span><wbr></wbr><span>Distance</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="714034119%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-calculate-remaining-distance-in-meters"><span class="token function">calculateRemainingDistanceInMeters</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">coordinates<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">This method calculates the distance between the current position and given coordinates. The coordinates must be on the polyline.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1719897510%2FFunctions%2F1617540583" anchor-label="getManeuver" id="-1719897510%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-maneuver"><span>get</span><wbr></wbr><span><span>Maneuver</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1719897510%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-maneuver"><span class="token function">getManeuver</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">index<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Maneuver</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Returns maneuver at the given index.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1362711692%2FFunctions%2F1617540583" anchor-label="getManeuverNotificationTimingOptions" id="1362711692%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-maneuver-notification-timing-options"><span>get</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Timing</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1362711692%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-maneuver-notification-timing-options"><span class="token function">getManeuverNotificationTimingOptions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TransportMode</a><span class="token punctuation">, </span></span><span class="parameter ">timingProfile<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TimingProfile</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">ManeuverNotificationTimingOptions</a></div><div class="brief "><p class="paragraph">Returns maneuver notification timing options with default values given the combination of transport mode and timing profile. The return value can be used as the base for configuring maneuver notification timings. Configure the relevant attributes of this object according to your preferences, and then set it by calling setManeuverNotificationTimingOptions function for the same combination of transport mode and timing profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="595520067%2FFunctions%2F1617540583" anchor-label="getWarningNotificationDistances" id="595520067%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-get-warning-notification-distances"><span>get</span><wbr></wbr><span>Warning</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Distances</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="595520067%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-get-warning-notification-distances"><span class="token function">getWarningNotificationDistances</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningType<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WarningType</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WarningNotificationDistances</a></div><div class="brief "><p class="paragraph">Returns the warning notification distances for the requested warning type. The return value can be used as the base for configuring warning notification distances. Configure the relevant attributes of this object according to your preferences, and then set it by calling <code class="lang-kotlin">setWarningNotificationDistances</code> function with the same warning type and the modified warning notification distances object.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1901720987%2FFunctions%2F1617540583" anchor-label="onLocationUpdated" id="-1901720987%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-on-location-updated"><span>on</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Updated</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1901720987%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-on-location-updated"><span class="token function">onLocationUpdated</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">location<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Location</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Called each time a new location is available. In a navigation context while using the <code class="lang-kotlin">Navigator</code> or <code class="lang-kotlin">VisualNavigator</code>, it's required to set the <code class="lang-kotlin">Location.time</code> parameter for each <code class="lang-kotlin">Location</code> object so that the HERE SDK can map-match the locations properly. If the <code class="lang-kotlin">Location.time</code> parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the <code class="lang-kotlin">bearing</code> and <code class="lang-kotlin">speed</code> parameters for each <code class="lang-kotlin">Location</code> object. Invoked on the main thread.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1648192422%2FFunctions%2F1617540583" anchor-label="repeatLastManeuverNotification" id="-1648192422%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-repeat-last-maneuver-notification"><span>repeat</span><wbr></wbr><span>Last</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span><span>Notification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1648192422%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-repeat-last-maneuver-notification"><span class="token function">repeatLastManeuverNotification</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1370551718%2FFunctions%2F1617540583" anchor-label="setCustomOption" id="1370551718%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-custom-option"><span>set</span><wbr></wbr><span>Custom</span><wbr></wbr><span><span>Option</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1370551718%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-custom-option"><span class="token function">setCustomOption</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">key<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span></span><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">This method sets custom options that controls navigator behavior. Unsupported options are silently ignored. Undocumented options can change their meaning without going through deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-80139936%2FFunctions%2F1617540583" anchor-label="setManeuverNotificationTimingOptions" id="-80139936%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-maneuver-notification-timing-options"><span>set</span><wbr></wbr><span>Maneuver</span><wbr></wbr><span>Notification</span><wbr></wbr><span>Timing</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-80139936%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-maneuver-notification-timing-options"><span class="token function">setManeuverNotificationTimingOptions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">transportMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TransportMode</a><span class="token punctuation">, </span></span><span class="parameter ">timingProfile<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TimingProfile</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">ManeuverNotificationTimingOptions</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Set timing option values for the combination of transport mode and timing profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1299305988%2FFunctions%2F1617540583" anchor-label="setWarningNotificationDistances" id="1299305988%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-warning-notification-distances"><span>set</span><wbr></wbr><span>Warning</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Distances</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1299305988%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-warning-notification-distances"><span class="token function">setWarningNotificationDistances</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningType<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WarningType</a><span class="token punctuation">, </span></span><span class="parameter ">warningNotificationDistances<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WarningNotificationDistances</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Set the warning notification distances for the specified warning types. <strong>Note:</strong> The warning notification distances are set for most warners. This method can't be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use <code class="lang-kotlin">NavigatorInterface.school_zone_warning_options</code> instead. Attempting to set the warning notification distances for the school zone warner using the <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code class="lang-kotlin">false</code>. Always use <code class="lang-kotlin">SchoolZoneWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the school zone warner regardless of the <code class="lang-kotlin">TimingProfile</code>. If <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> could be used, this would allow for different distances to be set for each timing profile, which is undesirable. Attempting to set the warning notification distances for the traffic merge warner using the <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code class="lang-kotlin">false</code>. Always use <code class="lang-kotlin">TrafficMergeWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the traffic merge warner regardless of the <code class="lang-kotlin">TimingProfile</code>. Using the <code class="lang-kotlin">NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code class="lang-kotlin">false</code> to avoid seting different distances on each timing profile since the traffic merge warning is only applicable on highways.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1746099173%2FFunctions%2F1617540583" anchor-label="startRendering" id="1746099173%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-start-rendering"><span>start</span><wbr></wbr><span><span>Rendering</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1746099173%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-start-rendering"><span class="token function">startRendering</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapView<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapViewBase</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Starts visual navigation rendering. A preconfigured current location marker is shown as soon as a location is received. The marker is chosen according to the transport mode specified in the route. If no route is present, the marker is chosen based on the <a href="sdk-for-flutter-explore-tracking-transport-specification">com.here.sdk.navigation.NavigatorInterface.trackingTransportSpecification</a> property. Calling startRendering() changes the <a href="sdk-for-flutter-explore-principal-point">com.here.sdk.mapview.MapCamera.principalPoint</a> property so that the current position indicator is equal to the value from <a href="sdk-for-flutter-explore-normalized-principal-point">com.here.sdk.navigation.CameraBehavior.normalizedPrincipalPoint</a>, in which by default places the principal point slightly at the bottom of the mapview. It is restored to its original value when stopRendering() is called. <strong>Note:</strong> When rendering is started again for a new map view instance, rendering is automatically stopped on the previous map view instance. Also note that the <a href="sdk-for-flutter-explore-frame-rate">com.here.sdk.mapview.MapViewBase.frameRate</a> can be lowered to reduce CPU usage, to adjust for tradeoffs between rendering smoothness versus battery consumption.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2030844225%2FFunctions%2F1617540583" anchor-label="stopRendering" id="2030844225%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-stop-rendering"><span>stop</span><wbr></wbr><span><span>Rendering</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2030844225%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-stop-rendering"><span class="token function">stopRendering</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Stops visual navigation rendering. This removes the current location marker. Other settings, like map orientation or camera distance, which may have been altered during rendering are no longer updated.</p></div></div></div>
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
