---
title: "com.here.sdk.location"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-location"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>com.here.sdk.location</title>
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
            <a class="library-name--link" href="../../index.html">
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
<div class="main-content" data-page-type="package" id="content" pageIds="API Reference::com.here.sdk.location////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../index.html">API Reference</a><span class="delimiter">/</span><span class="current">com.here.sdk.location</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Package-level</span></span> <span><span>declarations</span></span></h1>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="TYPE">Types</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="171205389%2FClasslikes%2F1617540583" anchor-label="CellularPositioningOptions" id="171205389%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-cellular-positioning-options/index.html"><span>Cellular</span><wbr></wbr><span>Positioning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="171205389%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-cellular-positioning-options/index.html">CellularPositioningOptions</a></div><div class="brief "><p class="paragraph">Cellular positioning options.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1712025045%2FClasslikes%2F1617540583" anchor-label="ConfirmationStatus" id="1712025045%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-confirmation-status/index.html"><span>Confirmation</span><wbr></wbr><span><span>Status</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1712025045%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-confirmation-status/index.html">ConfirmationStatus</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-confirmation-status/index.html">ConfirmationStatus</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Confirmation action specific status codes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="355551022%2FClasslikes%2F1617540583" anchor-label="LocationAccuracy" id="355551022%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-location-accuracy/index.html"><span>Location</span><wbr></wbr><span><span>Accuracy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="355551022%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-location-accuracy/index.html">LocationAccuracy</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-location-accuracy/index.html">LocationAccuracy</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates the desired location accuracy, however the actual accuracy is not guaranteed. When requesting high-accuracy locations, the initial update delivered by the LocationEngine may not have the requested accuracy. Requesting higher accuracy location updates usually means higher power consumption, therefore you should use the lowest accuracy suitable for your use case to preserve the device battery.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1535387771%2FClasslikes%2F1617540583" anchor-label="LocationEngine" id="-1535387771%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-location-engine/index.html"><span>Location</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1535387771%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">class </span><a href="-location-engine/index.html">LocationEngine</a> : <a href="-location-engine-base/index.html">LocationEngineBase</a>, <span data-unresolved-link="com.here.sdk.location/AppConfigListener///PointingToDeclaration/">AppConfigListener</span></div><div class="brief ">This class handles location updates received according to the desired  or <a href="-location-options/index.html">com.here.sdk.location.LocationOptions</a>.</div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1919423412%2FClasslikes%2F1617540583" anchor-label="LocationEngineBase" id="1919423412%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-location-engine-base/index.html"><span>Location</span><wbr></wbr><span>Engine</span><wbr></wbr><span><span>Base</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1919423412%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-location-engine-base/index.html">LocationEngineBase</a></div><div class="brief "><p class="paragraph">Public interface that describes the behaviour of <code class="lang-kotlin">LocationEngine</code>. Implementation is platform-specific.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-175954765%2FClasslikes%2F1617540583" anchor-label="LocationEngineStatus" id="-175954765%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-location-engine-status/index.html"><span>Location</span><wbr></wbr><span>Engine</span><wbr></wbr><span><span>Status</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-175954765%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-location-engine-status/index.html">LocationEngineStatus</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-location-engine-status/index.html">LocationEngineStatus</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates the status of the LocationEngine.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-645932699%2FClasslikes%2F1617540583" anchor-label="LocationFeature" id="-645932699%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-location-feature/index.html"><span>Location</span><wbr></wbr><span><span>Feature</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-645932699%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-location-feature/index.html">LocationFeature</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-location-feature/index.html">LocationFeature</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Location features supported by HERE positioning.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-118669298%2FClasslikes%2F1617540583" anchor-label="LocationIssueListener" id="-118669298%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-location-issue-listener/index.html"><span>Location</span><wbr></wbr><span>Issue</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-118669298%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-location-issue-listener/index.html">LocationIssueListener</a></div><div class="brief "><p class="paragraph">interface receiving notifications when the set of currently active location issues changes.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1208412360%2FClasslikes%2F1617540583" anchor-label="LocationIssueType" id="1208412360%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-location-issue-type/index.html"><span>Location</span><wbr></wbr><span>Issue</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1208412360%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-location-issue-type/index.html">LocationIssueType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-location-issue-type/index.html">LocationIssueType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Represents specific issues affecting location retrieval quality, availability, or functionality.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1598864061%2FClasslikes%2F1617540583" anchor-label="LocationOptions" id="1598864061%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-location-options/index.html"><span>Location</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1598864061%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-location-options/index.html">LocationOptions</a></div><div class="brief "><p class="paragraph">Location options that combine notification, sensor, cellular positioning, GNSS positioning and WiFi positioning options.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1123184255%2FClasslikes%2F1617540583" anchor-label="LocationStatusListener" id="-1123184255%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-location-status-listener/index.html"><span>Location</span><wbr></wbr><span>Status</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1123184255%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="-location-status-listener/index.html">LocationStatusListener</a></div><div class="brief "><p class="paragraph">Interface for listening the LocationEngine status updates.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1277527693%2FClasslikes%2F1617540583" anchor-label="NotificationOptions" id="-1277527693%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-notification-options/index.html"><span>Notification</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1277527693%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-notification-options/index.html">NotificationOptions</a></div><div class="brief "><p class="paragraph">Positioning notification options.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1762992794%2FClasslikes%2F1617540583" anchor-label="SatellitePositioningOptions" id="-1762992794%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-satellite-positioning-options/index.html"><span>Satellite</span><wbr></wbr><span>Positioning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1762992794%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-satellite-positioning-options/index.html">SatellitePositioningOptions</a></div><div class="brief "><p class="paragraph">GNSS positioning options.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-15434750%2FClasslikes%2F1617540583" anchor-label="SensorOptions" id="-15434750%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-sensor-options/index.html"><span>Sensor</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-15434750%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-sensor-options/index.html">SensorOptions</a></div><div class="brief "><p class="paragraph">Options for controlling sensor usage in positioning.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1539494398%2FClasslikes%2F1617540583" anchor-label="WifiPositioningOptions" id="-1539494398%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-wifi-positioning-options/index.html"><span>Wifi</span><wbr></wbr><span>Positioning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1539494398%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-wifi-positioning-options/index.html">WifiPositioningOptions</a></div><div class="brief "><p class="paragraph">Wi-Fi positioning options.</p></div></div></div>
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
