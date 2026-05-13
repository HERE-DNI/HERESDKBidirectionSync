---
title: "LocationEngine"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-location-location-engine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>LocationEngine</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.location/LocationEngine///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.location</a><span class="delimiter">/</span><span class="current">LocationEngine</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Location</span><wbr></wbr><span><span>Engine</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">class </span><a href="index.html">LocationEngine</a> : <a href="../-location-engine-base/index.html">LocationEngineBase</a>, <span data-unresolved-link="com.here.sdk.location/AppConfigListener///PointingToDeclaration/">AppConfigListener</span></div><p class="paragraph">This class handles location updates received according to the desired  or <a href="../-location-options/index.html">com.here.sdk.location.LocationOptions</a>. Each instance of this class will be using internally the same client providing the actual location updates. For that reason, only one <a href="index.html">com.here.sdk.location.LocationEngine</a> can be started at a time. Multiple listeners can be attached, either to receive location updates, see <a href="../../com.here.sdk.core/-location-listener/index.html">com.here.sdk.core.LocationListener</a>, status updates, see <a href="../-location-status-listener/index.html">com.here.sdk.location.LocationStatusListener</a> or location issue has occurred, see <a href="../-location-issue-listener/index.html">com.here.sdk.location.LocationIssueListener</a>. When a different  or <a href="../-location-options/index.html">com.here.sdk.location.LocationOptions</a> is desired, the LocationEngine needs to be stopped and started again.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-4305399%2FConstructors%2F1617540583" anchor-label="LocationEngine" id="-4305399%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-location-engine.html"><span>Location</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-4305399%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief ">Constructor of the LocationEngine</div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>engine<span class="token operator">: </span><a href="../../com.here.sdk.core.engine/-s-d-k-native-engine/index.html">SDKNativeEngine</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Constructor of the LocationEngine</div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1676777509%2FFunctions%2F1617540583" anchor-label="addLocationIssueListener" id="-1676777509%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-location-issue-listener.html"><span>add</span><wbr></wbr><span>Location</span><wbr></wbr><span>Issue</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1676777509%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="add-location-issue-listener.html"><span class="token function">addLocationIssueListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>listener<span class="token operator">: </span><a href="../-location-issue-listener/index.html">LocationIssueListener</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Adds a <a href="../-location-issue-listener/index.html">LocationIssueListener</a> to the engine to get notified when a location issue has occurred</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="955498019%2FFunctions%2F1617540583" anchor-label="addLocationListener" id="955498019%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-location-listener.html"><span>add</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="955498019%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="add-location-listener.html"><span class="token function">addLocationListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>listener<span class="token operator">: </span><a href="../../com.here.sdk.core/-location-listener/index.html">LocationListener</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Adds a <a href="../../com.here.sdk.core/-location-listener/index.html">LocationListener</a> to the engine to get notified when there is a new <a href="../../com.here.sdk.core/-location/index.html">com.here.sdk.core.Location</a>.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1229988693%2FFunctions%2F1617540583" anchor-label="addLocationStatusListener" id="1229988693%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-location-status-listener.html"><span>add</span><wbr></wbr><span>Location</span><wbr></wbr><span>Status</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1229988693%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="add-location-status-listener.html"><span class="token function">addLocationStatusListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>listener<span class="token operator">: </span><a href="../-location-status-listener/index.html">LocationStatusListener</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Adds a <a href="../-location-status-listener/index.html">LocationStatusListener</a> to the engine to get notified when there is an important status change.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1731522017%2FFunctions%2F1617540583" anchor-label="confirmHEREPrivacyNoticeException" id="1731522017%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="confirm-h-e-r-e-privacy-notice-exception.html"><span>confirm</span><wbr></wbr><span>HEREPrivacy</span><wbr></wbr><span>Notice</span><wbr></wbr><span><span>Exception</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1731522017%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="confirm-h-e-r-e-privacy-notice-exception.html"><span class="token function">confirmHEREPrivacyNoticeException</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-confirmation-status/index.html">ConfirmationStatus</a></div><div class="brief ">By calling this method, the application developer confirms that they have received an exceptional permission from HERE in written form to **not** include a reference to the HERE Privacy Notice.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-575433292%2FFunctions%2F1617540583" anchor-label="confirmHEREPrivacyNoticeInclusion" id="-575433292%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="confirm-h-e-r-e-privacy-notice-inclusion.html"><span>confirm</span><wbr></wbr><span>HEREPrivacy</span><wbr></wbr><span>Notice</span><wbr></wbr><span><span>Inclusion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-575433292%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="confirm-h-e-r-e-privacy-notice-inclusion.html"><span class="token function">confirmHEREPrivacyNoticeInclusion</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-confirmation-status/index.html">ConfirmationStatus</a></div><div class="brief ">It is the responsibility of the application developer to ensure that the application user is informed about the collection of characteristic information regarding nearby mobile and Wi-Fi network signals.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1365136021%2FFunctions%2F1617540583" anchor-label="disableVehicleSensors" id="-1365136021%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="disable-vehicle-sensors.html"><span>disable</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span><span>Sensors</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1365136021%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="disable-vehicle-sensors.html"><span class="token function">disableVehicleSensors</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief ">Disables access to vehicle's sensor information.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-696359041%2FFunctions%2F1617540583" anchor-label="enableVehicleSensors" id="-696359041%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="enable-vehicle-sensors.html"><span>enable</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span><span>Sensors</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-696359041%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="enable-vehicle-sensors.html"><span class="token function">enableVehicleSensors</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>manager<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/androidx/car/app/hardware/CarHardwareManager.html">CarHardwareManager</a></span></span><span class="token punctuation">)</span></div><div class="brief ">This feature enables the utilization of the vehicle's GNSS and movement sensor information.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2080470062%2FFunctions%2F1617540583" anchor-label="getLastKnownLocation" id="2080470062%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-last-known-location.html"><span>get</span><wbr></wbr><span>Last</span><wbr></wbr><span>Known</span><wbr></wbr><span><span>Location</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2080470062%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html"><span class="token annotation builtin">Nullable</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="get-last-known-location.html"><span class="token function">getLastKnownLocation</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core/-location/index.html">Location</a></div><div class="brief ">Gets the last known location obtained by the engine.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-457552791%2FFunctions%2F1617540583" anchor-label="isStarted" id="-457552791%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-started.html"><span>is</span><wbr></wbr><span><span>Started</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-457552791%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="is-started.html"><span class="token function">isStarted</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief ">Checks if the engine is in started state.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1738773390%2FFunctions%2F1617540583" anchor-label="removeLocationIssueListener" id="-1738773390%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-location-issue-listener.html"><span>remove</span><wbr></wbr><span>Location</span><wbr></wbr><span>Issue</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1738773390%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="remove-location-issue-listener.html"><span class="token function">removeLocationIssueListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>listener<span class="token operator">: </span><a href="../-location-issue-listener/index.html">LocationIssueListener</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Removes a <a href="../-location-issue-listener/index.html">LocationIssueListener</a> from the engine</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="263816954%2FFunctions%2F1617540583" anchor-label="removeLocationListener" id="263816954%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-location-listener.html"><span>remove</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="263816954%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="remove-location-listener.html"><span class="token function">removeLocationListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>listener<span class="token operator">: </span><a href="../../com.here.sdk.core/-location-listener/index.html">LocationListener</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Removes a <a href="../../com.here.sdk.core/-location-listener/index.html">LocationListener</a> from the engine</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1781489196%2FFunctions%2F1617540583" anchor-label="removeLocationStatusListener" id="1781489196%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-location-status-listener.html"><span>remove</span><wbr></wbr><span>Location</span><wbr></wbr><span>Status</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1781489196%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="remove-location-status-listener.html"><span class="token function">removeLocationStatusListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>listener<span class="token operator">: </span><a href="../-location-status-listener/index.html">LocationStatusListener</a></span></span><span class="token punctuation">)</span></div><div class="brief ">Removes a <a href="../-location-status-listener/index.html">LocationStatusListener</a> from the engine</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="707429271%2FFunctions%2F1617540583" anchor-label="setLastKnownLocationPersistent" id="707429271%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-last-known-location-persistent.html"><span>set</span><wbr></wbr><span>Last</span><wbr></wbr><span>Known</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Persistent</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="707429271%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="set-last-known-location-persistent.html"><span class="token function">setLastKnownLocationPersistent</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">persistent<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-location-engine-status/index.html">LocationEngineStatus</a></div><div class="brief ">Enables or disables saving of last known location so it persists between application sessions.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1855003807%2FFunctions%2F1617540583" anchor-label="start" id="1855003807%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="start.html"><span><span>start</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1855003807%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="start.html"><span class="token function">start</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>locationAccuracy<span class="token operator">: </span><a href="../-location-accuracy/index.html">LocationAccuracy</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-location-engine-status/index.html">LocationEngineStatus</a></div><div class="brief ">Starts the location engine with desired <a href="../-location-accuracy/index.html">com.here.sdk.location.LocationAccuracy</a>.</div><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="start.html"><span class="token function">start</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>locationOptions<span class="token operator">: </span><a href="../-location-options/index.html">LocationOptions</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-location-engine-status/index.html">LocationEngineStatus</a></div><div class="brief ">Starts the location engine with desired <a href="../-location-options/index.html">com.here.sdk.location.LocationOptions</a>.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="149878616%2FFunctions%2F1617540583" anchor-label="stop" id="149878616%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="stop.html"><span><span>stop</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="149878616%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="stop.html"><span class="token function">stop</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief ">Stops the location engine.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1145445089%2FFunctions%2F1617540583" anchor-label="updateLocationAccuracy" id="1145445089%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="update-location-accuracy.html"><span>update</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Accuracy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1145445089%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="update-location-accuracy.html"><span class="token function">updateLocationAccuracy</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>locationAccuracy<span class="token operator">: </span><a href="../-location-accuracy/index.html">LocationAccuracy</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-location-engine-status/index.html">LocationEngineStatus</a></div><div class="brief ">Reconfigures the location engine with desired LocationAccuracy.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-474985747%2FFunctions%2F1617540583" anchor-label="updateLocationOptions" id="-474985747%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="update-location-options.html"><span>update</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-474985747%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a></div></div><span class="token keyword">open </span><span class="token keyword">fun </span><a href="update-location-options.html"><span class="token function">updateLocationOptions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>locationOptions<span class="token operator">: </span><a href="../-location-options/index.html">LocationOptions</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-location-engine-status/index.html">LocationEngineStatus</a></div><div class="brief ">Reconfigures the location engine with desired LocationOptions.</div></div></div>
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
