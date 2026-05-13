---
title: "LocationEngineBase"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-location-location-engine-base"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>LocationEngineBase</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.location/LocationEngineBase///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.location</a><span class="delimiter">/</span><span class="current">LocationEngineBase</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Location</span><wbr></wbr><span>Engine</span><wbr></wbr><span><span>Base</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="index.html">LocationEngineBase</a></div><p class="paragraph">Public interface that describes the behaviour of <code class="lang-kotlin">LocationEngine</code>. Implementation is platform-specific.</p><h4 class="">Inheritors</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="../-location-engine/index.html">LocationEngine</a></div></span></div><div></div></div></div></div></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="730356184%2FProperties%2F1617540583" anchor-label="isStarted" id="730356184%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-started.html"><span>is</span><wbr></wbr><span><span>Started</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="730356184%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="is-started.html">isStarted</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Checks if the engine is in started state.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1841074445%2FProperties%2F1617540583" anchor-label="lastKnownLocation" id="1841074445%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="last-known-location.html"><span>last</span><wbr></wbr><span>Known</span><wbr></wbr><span><span>Location</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1841074445%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">val </span><a href="last-known-location.html">lastKnownLocation</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-location/index.html">Location</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The last known location obtained by the <code class="lang-kotlin">LocationEngine</code>. It is persisted throughout the app's lifecycle. This property can be obtained without starting the <code class="lang-kotlin">LocationEngine</code>. However, the initial value might be <code class="lang-kotlin">null</code> if no location has ever been obtained by the <code class="lang-kotlin">LocationEngine</code>. The time attribute of the <code class="lang-kotlin">Location</code> object indicates when the last location was obtained. Note: In order to receive continuous location updates, add a <code class="lang-kotlin">LocationListener</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1617560438%2FFunctions%2F1617540583" anchor-label="addLocationIssueListener" id="-1617560438%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-location-issue-listener.html"><span>add</span><wbr></wbr><span>Location</span><wbr></wbr><span>Issue</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1617560438%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="add-location-issue-listener.html"><span class="token function">addLocationIssueListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-location-issue-listener/index.html">LocationIssueListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a <a href="../-location-issue-listener/index.html">com.here.sdk.location.LocationIssueListener</a> to the engine to get notified when a location issue has occurred. Supports more than one listener, instance is added only once.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="945201426%2FFunctions%2F1617540583" anchor-label="addLocationListener" id="945201426%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-location-listener.html"><span>add</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="945201426%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="add-location-listener.html"><span class="token function">addLocationListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../../com.here.sdk.core/-location-listener/index.html">LocationListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a <code class="lang-kotlin">LocationListener</code> to the engine to get notified when there is a new location update available. Supports more than one listener, instance is added only once.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1991948220%2FFunctions%2F1617540583" anchor-label="addLocationStatusListener" id="-1991948220%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-location-status-listener.html"><span>add</span><wbr></wbr><span>Location</span><wbr></wbr><span>Status</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1991948220%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="add-location-status-listener.html"><span class="token function">addLocationStatusListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-location-status-listener/index.html">LocationStatusListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a <code class="lang-kotlin">LocationStatusListener</code> to the engine to get notified when there is an important status change. Supports more than one listener, instance is added only once.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1759338064%2FFunctions%2F1617540583" anchor-label="confirmHEREPrivacyNoticeException" id="1759338064%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="confirm-h-e-r-e-privacy-notice-exception.html"><span>confirm</span><wbr></wbr><span>HEREPrivacy</span><wbr></wbr><span>Notice</span><wbr></wbr><span><span>Exception</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1759338064%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="confirm-h-e-r-e-privacy-notice-exception.html"><span class="token function">confirmHEREPrivacyNoticeException</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-confirmation-status/index.html">ConfirmationStatus</a></div><div class="brief "><p class="paragraph">By calling this method, the application developer confirms that they have received an exceptional permission from HERE in written form to <strong>not</strong> include a reference to the HERE Privacy Notice. As a result, the <code class="lang-kotlin">LocationEngine</code> will not collect characteristic information about the nearby mobile and Wi-Fi network signals. However, the engine will still be fully functional and it will deliver location updates when the exception can be confirmed. Note that this call should not involve user interaction and it should be executed silently by the application before starting the <code class="lang-kotlin">LocationEngine</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-547617245%2FFunctions%2F1617540583" anchor-label="confirmHEREPrivacyNoticeInclusion" id="-547617245%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="confirm-h-e-r-e-privacy-notice-inclusion.html"><span>confirm</span><wbr></wbr><span>HEREPrivacy</span><wbr></wbr><span>Notice</span><wbr></wbr><span><span>Inclusion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-547617245%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="confirm-h-e-r-e-privacy-notice-inclusion.html"><span class="token function">confirmHEREPrivacyNoticeInclusion</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-confirmation-status/index.html">ConfirmationStatus</a></div><div class="brief "><p class="paragraph">It is the responsibility of the application developer to ensure that the application user is informed about the collection of characteristic information regarding nearby mobile and Wi-Fi network signals. Additionally, a link to the related <a href="https://legal.here.com/en-gb/here-network-positioning-via-sdk">HERE Privacy Notice</a> must be made available to the user.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1116998746%2FFunctions%2F1617540583" anchor-label="disableVehicleSensors" id="1116998746%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="disable-vehicle-sensors.html"><span>disable</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span><span>Sensors</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1116998746%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="disable-vehicle-sensors.html"><span class="token function">disableVehicleSensors</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Disables access to vehicle's sensor information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-927749840%2FFunctions%2F1617540583" anchor-label="enableVehicleSensors" id="-927749840%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="enable-vehicle-sensors.html"><span>enable</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span><span>Sensors</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-927749840%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="enable-vehicle-sensors.html"><span class="token function">enableVehicleSensors</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">manager<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/androidx/car/app/hardware/CarHardwareManager.html">CarHardwareManager</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">This feature enables the utilization of the vehicle's GNSS and movement sensor information. It is recommended to always enable this feature by default when the application supports Android Auto. This allows the phone's positioning sensor information to be augmented with the vehicle's sensor data, resulting in the best possible positioning estimates. However, given the varying quality of car sensor implementations, it is also advisable to provide application users with the option to disable the usage of vehicle sensor information - this would be helpful in case the vehicle reports information that is clearly misleading or contradictory. Furthermore, users should be able to re-enable this feature if the vehicle's capability improves.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1460397411%2FFunctions%2F1617540583" anchor-label="removeLocationIssueListener" id="1460397411%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-location-issue-listener.html"><span>remove</span><wbr></wbr><span>Location</span><wbr></wbr><span>Issue</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1460397411%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="remove-location-issue-listener.html"><span class="token function">removeLocationIssueListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-location-issue-listener/index.html">LocationIssueListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a <a href="../-location-issue-listener/index.html">com.here.sdk.location.LocationIssueListener</a> from the engine.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1539307093%2FFunctions%2F1617540583" anchor-label="removeLocationListener" id="-1539307093%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-location-listener.html"><span>remove</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1539307093%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="remove-location-listener.html"><span class="token function">removeLocationListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../../com.here.sdk.core/-location-listener/index.html">LocationListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a <code class="lang-kotlin">LocationListener</code> from the engine.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="988045021%2FFunctions%2F1617540583" anchor-label="removeLocationStatusListener" id="988045021%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-location-status-listener.html"><span>remove</span><wbr></wbr><span>Location</span><wbr></wbr><span>Status</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="988045021%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="remove-location-status-listener.html"><span class="token function">removeLocationStatusListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-location-status-listener/index.html">LocationStatusListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a <code class="lang-kotlin">LocationStatusListener</code> from the engine.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-807072423%2FFunctions%2F1617540583" anchor-label="setLastKnownLocationPersistent" id="-807072423%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-last-known-location-persistent.html"><span>set</span><wbr></wbr><span>Last</span><wbr></wbr><span>Known</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Persistent</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-807072423%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="set-last-known-location-persistent.html"><span class="token function">setLastKnownLocationPersistent</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">persistent<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-location-engine-status/index.html">LocationEngineStatus</a></div><div class="brief "><p class="paragraph">Enables or disables saving of last known location so that it persists between application sessions. Defaults to enabled.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1073651839%2FFunctions%2F1617540583" anchor-label="start" id="1073651839%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="start.html"><span><span>start</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1073651839%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="start.html"><span class="token function">start</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">locationAccuracy<span class="token operator">: </span><a href="../-location-accuracy/index.html">LocationAccuracy</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-location-engine-status/index.html">LocationEngineStatus</a></div><div class="brief "><p class="paragraph">Starts the location engine with desired <a href="../-location-accuracy/index.html">com.here.sdk.location.LocationAccuracy</a>. Returns <a href="../-location-engine-status/-a-l-r-e-a-d-y_-s-t-a-r-t-e-d/index.html">com.here.sdk.location.LocationEngineStatus.ALREADY_STARTED</a>, if <a href="start.html">com.here.sdk.location.LocationEngineBase.start</a> is called again without <a href="stop.html">com.here.sdk.location.LocationEngineBase.stop</a> in between. Make sure to call either <a href="confirm-h-e-r-e-privacy-notice-inclusion.html">com.here.sdk.location.LocationEngineBase.confirmHEREPrivacyNoticeInclusion</a> or <a href="confirm-h-e-r-e-privacy-notice-exception.html">com.here.sdk.location.LocationEngineBase.confirmHEREPrivacyNoticeException</a> beforehand.</p></div><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="start.html"><span class="token function">start</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">locationOptions<span class="token operator">: </span><a href="../-location-options/index.html">LocationOptions</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-location-engine-status/index.html">LocationEngineStatus</a></div><div class="brief "><p class="paragraph">Starts the location engine with desired <a href="../-location-options/index.html">com.here.sdk.location.LocationOptions</a>. Returns <a href="../-location-engine-status/-a-l-r-e-a-d-y_-s-t-a-r-t-e-d/index.html">com.here.sdk.location.LocationEngineStatus.ALREADY_STARTED</a>, if <a href="start.html">com.here.sdk.location.LocationEngineBase.start</a> is called again without <a href="stop.html">com.here.sdk.location.LocationEngineBase.stop</a> in between. Make sure to call either <a href="confirm-h-e-r-e-privacy-notice-inclusion.html">com.here.sdk.location.LocationEngineBase.confirmHEREPrivacyNoticeInclusion</a> or <a href="confirm-h-e-r-e-privacy-notice-exception.html">com.here.sdk.location.LocationEngineBase.confirmHEREPrivacyNoticeException</a> beforehand.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1048838007%2FFunctions%2F1617540583" anchor-label="stop" id="-1048838007%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="stop.html"><span><span>stop</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1048838007%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="stop.html"><span class="token function">stop</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Stops the location engine.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1467604242%2FFunctions%2F1617540583" anchor-label="updateLocationAccuracy" id="1467604242%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="update-location-accuracy.html"><span>update</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Accuracy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1467604242%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="update-location-accuracy.html"><span class="token function">updateLocationAccuracy</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">locationAccuracy<span class="token operator">: </span><a href="../-location-accuracy/index.html">LocationAccuracy</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-location-engine-status/index.html">LocationEngineStatus</a></div><div class="brief "><p class="paragraph">Reconfigures the location engine with desired <a href="../-location-accuracy/index.html">com.here.sdk.location.LocationAccuracy</a>. This method is a faster way to change location accuracy for already started location engine, than calling <a href="stop.html">com.here.sdk.location.LocationEngineBase.stop</a> and <a href="start.html">com.here.sdk.location.LocationEngineBase.start</a> in sequence. Returns <a href="../-location-engine-status/-n-o-t_-r-e-a-d-y/index.html">com.here.sdk.location.LocationEngineStatus.NOT_READY</a>, if called for unstarted location engine.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1889592670%2FFunctions%2F1617540583" anchor-label="updateLocationOptions" id="1889592670%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="update-location-options.html"><span>update</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1889592670%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="update-location-options.html"><span class="token function">updateLocationOptions</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">locationOptions<span class="token operator">: </span><a href="../-location-options/index.html">LocationOptions</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-location-engine-status/index.html">LocationEngineStatus</a></div><div class="brief "><p class="paragraph">Reconfigures the location engine with desired <a href="../-location-options/index.html">com.here.sdk.location.LocationOptions</a>. This method is a faster way to change location options for already started location engine, than calling <a href="stop.html">com.here.sdk.location.LocationEngineBase.stop</a> and <a href="start.html">com.here.sdk.location.LocationEngineBase.start</a> in sequence. Returns <a href="../-location-engine-status/-n-o-t_-r-e-a-d-y/index.html">com.here.sdk.location.LocationEngineStatus.NOT_READY</a>, if called for unstarted location engine.</p></div></div></div>
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
