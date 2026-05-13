---
title: "com.here.sdk.mapdata"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapdata"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>com.here.sdk.mapdata</title>
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
<div class="main-content" data-page-type="package" id="content" pageIds="API Reference::com.here.sdk.mapdata////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../index.html">API Reference</a><span class="delimiter">/</span><span class="current">com.here.sdk.mapdata</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Package-level</span></span> <span><span>declarations</span></span></h1>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="TYPE">Types</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="357965544%2FClasslikes%2F1617540583" anchor-label="AdminContextId" id="357965544%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-admin-context-id/index.html"><span>Admin</span><wbr></wbr><span>Context</span><wbr></wbr><span><span>Id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="357965544%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-admin-context-id/index.html">AdminContextId</a></div><div class="brief "><p class="paragraph">Represents a set of administrative rules for a country or a state.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-472320352%2FClasslikes%2F1617540583" anchor-label="AdministrativeCommercialVehicleRules" id="-472320352%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-administrative-commercial-vehicle-rules/index.html"><span>Administrative</span><wbr></wbr><span>Commercial</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span><span>Rules</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-472320352%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-administrative-commercial-vehicle-rules/index.html">AdministrativeCommercialVehicleRules</a></div><div class="brief "><p class="paragraph">Commercial vehicle regulations for an administrative region (country or state). Contains access restrictions, speed limits, and drive/rest rules applicable to commercial vehicles on road segments within the region.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1402759222%2FClasslikes%2F1617540583" anchor-label="AdministrativeRules" id="1402759222%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-administrative-rules/index.html"><span>Administrative</span><wbr></wbr><span><span>Rules</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1402759222%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-administrative-rules/index.html">AdministrativeRules</a></div><div class="brief "><p class="paragraph">Represents a set of administrative rules for a country or a state.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1485896797%2FClasslikes%2F1617540583" anchor-label="AdministrativeRulesLoader" id="-1485896797%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-administrative-rules-loader/index.html"><span>Administrative</span><wbr></wbr><span>Rules</span><wbr></wbr><span><span>Loader</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1485896797%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-administrative-rules-loader/index.html">AdministrativeRulesLoader</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Provides the interface for the access to the administrative rules available for a country or a state in the local OCM map. Please be aware that the methods within this classload map data synchronously. In the event of absent data in the disk cache, the data will be retrieved from the remote server. To mitigate the potential freezing of the calling thread, it is advisable to proactively prefetch map data around the working area.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1953680752%2FClasslikes%2F1617540583" anchor-label="AllowedTransportModes" id="-1953680752%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-allowed-transport-modes/index.html"><span>Allowed</span><wbr></wbr><span>Transport</span><wbr></wbr><span><span>Modes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1953680752%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-allowed-transport-modes/index.html">AllowedTransportModes</a></div><div class="brief "><p class="paragraph">Specifies which transport modes are allowed in a particular direction.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-384171827%2FClasslikes%2F1617540583" anchor-label="BloodAlcoholContentLimit" id="-384171827%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-blood-alcohol-content-limit/index.html"><span>Blood</span><wbr></wbr><span>Alcohol</span><wbr></wbr><span>Content</span><wbr></wbr><span><span>Limit</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-384171827%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-blood-alcohol-content-limit/index.html">BloodAlcoholContentLimit</a></div><div class="brief "><p class="paragraph">Represents the rules regarding alcohol in blood content limit in a country or state for all types of drivers.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="441925731%2FClasslikes%2F1617540583" anchor-label="CommercialVehicleRoadType" id="441925731%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-commercial-vehicle-road-type/index.html"><span>Commercial</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="441925731%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-commercial-vehicle-road-type/index.html">CommercialVehicleRoadType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-commercial-vehicle-road-type/index.html">CommercialVehicleRoadType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Concise description of road type used in commercial vehicle regulations.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-253168180%2FClasslikes%2F1617540583" anchor-label="Connectivity" id="-253168180%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-connectivity/index.html"><span><span>Connectivity</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-253168180%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-connectivity/index.html">Connectivity</a></div><div class="brief "><p class="paragraph">A class that provides information about link id and accessibility.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1175003974%2FClasslikes%2F1617540583" anchor-label="DirectedOCMSegmentId" id="1175003974%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-directed-o-c-m-segment-id/index.html"><span>Directed</span><wbr></wbr><span>OCMSegment</span><wbr></wbr><span><span>Id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1175003974%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-directed-o-c-m-segment-id/index.html">DirectedOCMSegmentId</a></div><div class="brief "><p class="paragraph">OCM Segment ID with travel direction of segment.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-792088741%2FClasslikes%2F1617540583" anchor-label="DownloadingFileOptions" id="-792088741%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-downloading-file-options/index.html"><span>Downloading</span><wbr></wbr><span>File</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-792088741%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-downloading-file-options/index.html">DownloadingFileOptions</a></div><div class="brief "><p class="paragraph">A class which identifies the configuration when downloading a file reference.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1155960503%2FClasslikes%2F1617540583" anchor-label="DriveRestRegulation" id="1155960503%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-drive-rest-regulation/index.html"><span>Drive</span><wbr></wbr><span>Rest</span><wbr></wbr><span><span>Regulation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1155960503%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-drive-rest-regulation/index.html">DriveRestRegulation</a></div><div class="brief "><p class="paragraph">Drive-rest regulation defining mandatory rest requirements for commercial vehicle drivers.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1080074881%2FClasslikes%2F1617540583" anchor-label="DrivingSide" id="1080074881%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-driving-side/index.html"><span>Driving</span><wbr></wbr><span><span>Side</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1080074881%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-driving-side/index.html">DrivingSide</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-driving-side/index.html">DrivingSide</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">The side of the road on which the driving is done.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1482255184%2FClasslikes%2F1617540583" anchor-label="FileReference" id="-1482255184%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-file-reference/index.html"><span>File</span><wbr></wbr><span><span>Reference</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1482255184%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-file-reference/index.html">FileReference</a></div><div class="brief "><p class="paragraph">A class that provides information for a file reference.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="160289558%2FClasslikes%2F1617540583" anchor-label="FileReferenceType" id="160289558%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-file-reference-type/index.html"><span>File</span><wbr></wbr><span>Reference</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="160289558%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-file-reference-type/index.html">FileReferenceType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-file-reference-type/index.html">FileReferenceType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Type of reference file.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1084847645%2FClasslikes%2F1617540583" anchor-label="HazardousMaterialType" id="-1084847645%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-hazardous-material-type/index.html"><span>Hazardous</span><wbr></wbr><span>Material</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1084847645%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-hazardous-material-type/index.html">HazardousMaterialType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-hazardous-material-type/index.html">HazardousMaterialType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Hazardous material type as defined in the enum applicable for those that carry these</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2106258503%2FClasslikes%2F1617540583" anchor-label="HeadlightsRequirement" id="-2106258503%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-headlights-requirement/index.html"><span>Headlights</span><wbr></wbr><span><span>Requirement</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2106258503%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-headlights-requirement/index.html">HeadlightsRequirement</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-headlights-requirement/index.html">HeadlightsRequirement</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">The situations in which headlights are required to be turned on.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-269789457%2FClasslikes%2F1617540583" anchor-label="LaneAttribute" id="-269789457%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-lane-attribute/index.html"><span>Lane</span><wbr></wbr><span><span>Attribute</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-269789457%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-lane-attribute/index.html">LaneAttribute</a></div><div class="brief "><p class="paragraph">A class that describes attributes assigned to a specific section of a lane. It includes lane markings, allowed travel directions, tolling info, access restrictions, and optional lane type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-850847591%2FClasslikes%2F1617540583" anchor-label="LocalRoadCharacteristic" id="-850847591%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-local-road-characteristic/index.html"><span>Local</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Characteristic</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-850847591%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-local-road-characteristic/index.html">LocalRoadCharacteristic</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-local-road-characteristic/index.html">LocalRoadCharacteristic</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies the local road characteristics: frontage, parking lot road, poi access.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="392591207%2FClasslikes%2F1617540583" anchor-label="MapDataLoaderErrorCode" id="392591207%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-data-loader-error-code/index.html"><span>Map</span><wbr></wbr><span>Data</span><wbr></wbr><span>Loader</span><wbr></wbr><span>Error</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="392591207%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-map-data-loader-error-code/index.html">MapDataLoaderErrorCode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-map-data-loader-error-code/index.html">MapDataLoaderErrorCode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies possible errors from map data accessing.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="129248365%2FClasslikes%2F1617540583" anchor-label="MapDataLoaderException" id="129248365%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-data-loader-exception/index.html"><span>Map</span><wbr></wbr><span>Data</span><wbr></wbr><span>Loader</span><wbr></wbr><span><span>Exception</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="129248365%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-map-data-loader-exception/index.html">MapDataLoaderException</a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span class="token keyword">val </span>error<span class="token operator">: </span><a href="-map-data-loader-error-code/index.html">MapDataLoaderErrorCode</a></span></span><span class="token punctuation">)</span> : <a href="https://developer.android.com/reference/kotlin/java/lang/Exception.html">Exception</a></div><div class="brief "><p class="paragraph">Error occurred during obtaining data form the map. <a href="-map-data-loader-error-code/index.html">com.here.sdk.mapdata.MapDataLoaderErrorCode</a> represents possible errors.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="5909166%2FClasslikes%2F1617540583" anchor-label="OCMSegmentId" id="5909166%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-c-m-segment-id/index.html"><span>OCMSegment</span><wbr></wbr><span><span>Id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="5909166%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-o-c-m-segment-id/index.html">OCMSegmentId</a></div><div class="brief "><p class="paragraph">OCM Segment ID of particular matched <a href="../com.here.sdk.routing/-segment-reference/index.html">com.here.sdk.routing.SegmentReference</a> from OCM map, represented in form: Tile + Local ID's .</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="616552678%2FClasslikes%2F1617540583" anchor-label="ParkingSideRegulation" id="616552678%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-parking-side-regulation/index.html"><span>Parking</span><wbr></wbr><span>Side</span><wbr></wbr><span><span>Regulation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="616552678%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-parking-side-regulation/index.html">ParkingSideRegulation</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-parking-side-regulation/index.html">ParkingSideRegulation</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">The regulations for parking on the side of the road.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1585753173%2FClasslikes%2F1617540583" anchor-label="PhysicalAttributes" id="1585753173%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-physical-attributes/index.html"><span>Physical</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1585753173%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-physical-attributes/index.html">PhysicalAttributes</a></div><div class="brief "><p class="paragraph">Physical attributes of the segment.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1121083101%2FClasslikes%2F1617540583" anchor-label="PhysicalStructure" id="-1121083101%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-physical-structure/index.html"><span>Physical</span><wbr></wbr><span><span>Structure</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1121083101%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-physical-structure/index.html">PhysicalStructure</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-physical-structure/index.html">PhysicalStructure</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Physical structure of a road feature that causes an access restriction, such as a bridge or tunnel that may limit vehicle dimensions or weight.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1114042938%2FClasslikes%2F1617540583" anchor-label="PreTripPlanning" id="1114042938%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-pre-trip-planning/index.html"><span>Pre</span><wbr></wbr><span>Trip</span><wbr></wbr><span><span>Planning</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1114042938%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-pre-trip-planning/index.html">PreTripPlanning</a></div><div class="brief "><p class="paragraph">Represents the legal requirements to be considered before a trip for all vehicles types.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-318544000%2FClasslikes%2F1617540583" anchor-label="RailwayCrossing" id="-318544000%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-railway-crossing/index.html"><span>Railway</span><wbr></wbr><span><span>Crossing</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-318544000%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-railway-crossing/index.html">RailwayCrossing</a></div><div class="brief "><p class="paragraph">Identifies the presence and the location of railway corssings. Included in <a href="-segment-data/index.html">com.here.sdk.mapdata.SegmentData</a> only if <a href="-segment-data-loader-options/load-railway-crossings.html">com.here.sdk.mapdata.SegmentDataLoaderOptions.loadRailwayCrossings</a> is set to <code class="lang-kotlin">true</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-609960474%2FClasslikes%2F1617540583" anchor-label="RailwayCrossingType" id="-609960474%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-railway-crossing-type/index.html"><span>Railway</span><wbr></wbr><span>Crossing</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-609960474%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-railway-crossing-type/index.html">RailwayCrossingType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-railway-crossing-type/index.html">RailwayCrossingType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Type of railway crossing.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1042427706%2FClasslikes%2F1617540583" anchor-label="RoadDivider" id="-1042427706%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-road-divider/index.html"><span>Road</span><wbr></wbr><span><span>Divider</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1042427706%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-road-divider/index.html">RoadDivider</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-road-divider/index.html">RoadDivider</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">A physical structure or painted road marking intended to legally prohibit left turns in right-side driving countries, right turns in left-side driving countries, and U-turns at divided intersections or in the middle of divided segments.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="392050993%2FClasslikes%2F1617540583" anchor-label="RoadProfileCondition" id="392050993%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-road-profile-condition/index.html"><span>Road</span><wbr></wbr><span>Profile</span><wbr></wbr><span><span>Condition</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="392050993%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-road-profile-condition/index.html">RoadProfileCondition</a></div><div class="brief "><p class="paragraph">Road profile conditions that must be met for a regulation to apply.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1615316431%2FClasslikes%2F1617540583" anchor-label="RoadUsages" id="-1615316431%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-road-usages/index.html"><span>Road</span><wbr></wbr><span><span>Usages</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1615316431%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-road-usages/index.html">RoadUsages</a></div><div class="brief "><p class="paragraph">Road Usages of the segment.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-743102633%2FClasslikes%2F1617540583" anchor-label="SegmentConnectivities" id="-743102633%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-segment-connectivities/index.html"><span>Segment</span><wbr></wbr><span><span>Connectivities</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-743102633%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-segment-connectivities/index.html">SegmentConnectivities</a></div><div class="brief "><p class="paragraph">A class that provides information about segment one direction source and target connectivities.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1941366690%2FClasslikes%2F1617540583" anchor-label="SegmentData" id="1941366690%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-segment-data/index.html"><span>Segment</span><wbr></wbr><span><span>Data</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1941366690%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-segment-data/index.html">SegmentData</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Contains the requested information for a segment</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1418674703%2FClasslikes%2F1617540583" anchor-label="SegmentDataLoader" id="1418674703%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-segment-data-loader/index.html"><span>Segment</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Loader</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1418674703%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-segment-data-loader/index.html">SegmentDataLoader</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Provides the interface for the access to the segments data available in the local OCM map. Please be aware that the methods within this class load map data synchronously. In the event of absent data in the disk cache, the data will be retrieved from the remote server. To mitigate the potential freezing of the calling thread, it is advisable to proactively prefetch map data around the working area.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1525579819%2FClasslikes%2F1617540583" anchor-label="SegmentDataLoaderOptions" id="-1525579819%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-segment-data-loader-options/index.html"><span>Segment</span><wbr></wbr><span>Data</span><wbr></wbr><span>Loader</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1525579819%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-segment-data-loader-options/index.html">SegmentDataLoaderOptions</a></div><div class="brief "><p class="paragraph">Specifies which data should be loaded by the <a href="-segment-data-loader/load-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadData</a> or <a href="-segment-data-loader/load-directed-segment-data.html">com.here.sdk.mapdata.SegmentDataLoader.loadDirectedSegmentData</a> function.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1959173079%2FClasslikes%2F1617540583" anchor-label="SegmentReferenceConverter" id="1959173079%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-segment-reference-converter/index.html"><span>Segment</span><wbr></wbr><span>Reference</span><wbr></wbr><span><span>Converter</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1959173079%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-segment-reference-converter/index.html">SegmentReferenceConverter</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">A SegmentReferenceConverter provides possibility to convert mapmatched instances of <a href="../com.here.sdk.routing/-segment-reference/index.html">com.here.sdk.routing.SegmentReference</a> to corresponding instances of <a href="-directed-o-c-m-segment-id/index.html">com.here.sdk.mapdata.DirectedOCMSegmentId</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1773467384%2FClasslikes%2F1617540583" anchor-label="SegmentSpanData" id="1773467384%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-segment-span-data/index.html"><span>Segment</span><wbr></wbr><span>Span</span><wbr></wbr><span><span>Data</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1773467384%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-segment-span-data/index.html">SegmentSpanData</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Contains attributes that are not necessarily constant on a full segment. A Span is a portion of a Segment where the requested attributes are constant.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1489646298%2FClasslikes%2F1617540583" anchor-label="SegmentSpecialSpeedSituation" id="-1489646298%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-segment-special-speed-situation/index.html"><span>Segment</span><wbr></wbr><span>Special</span><wbr></wbr><span>Speed</span><wbr></wbr><span><span>Situation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1489646298%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-segment-special-speed-situation/index.html">SegmentSpecialSpeedSituation</a></div><div class="brief "><p class="paragraph">A special speed situation indicates a speed that exists under special circumstances. It can be used to further refine the estimation of traversal times, route calculation and calculation of route guidance timing.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="977442456%2FClasslikes%2F1617540583" anchor-label="SegmentSpeedLimit" id="977442456%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-segment-speed-limit/index.html"><span>Segment</span><wbr></wbr><span>Speed</span><wbr></wbr><span><span>Limit</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="977442456%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-segment-speed-limit/index.html">SegmentSpeedLimit</a></div><div class="brief "><p class="paragraph">Describes the posted speed limit on the segment span.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1362081733%2FClasslikes%2F1617540583" anchor-label="SpecialSpeedType" id="-1362081733%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-special-speed-type/index.html"><span>Special</span><wbr></wbr><span>Speed</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1362081733%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-special-speed-type/index.html">SpecialSpeedType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-special-speed-type/index.html">SpecialSpeedType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Represents the speed situation type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1039183365%2FClasslikes%2F1617540583" anchor-label="TollCost" id="-1039183365%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-toll-cost/index.html"><span>Toll</span><wbr></wbr><span><span>Cost</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1039183365%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-toll-cost/index.html">TollCost</a></div><div class="brief "><p class="paragraph">Contains informations about the toll costs for a specific vehicle profile.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-980253046%2FClasslikes%2F1617540583" anchor-label="TollPoint" id="-980253046%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-toll-point/index.html"><span>Toll</span><wbr></wbr><span><span>Point</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-980253046%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-toll-point/index.html">TollPoint</a></div><div class="brief "><p class="paragraph">A class to represent the toll point attributes of a segment.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-526243961%2FClasslikes%2F1617540583" anchor-label="TollStructure" id="-526243961%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-toll-structure/index.html"><span>Toll</span><wbr></wbr><span><span>Structure</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-526243961%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-toll-structure/index.html">TollStructure</a></div><div class="brief "><p class="paragraph">A class that defines tolling configuration for a lane. It describes which types of toll structures apply and the acceptable payment methods. This information can be used to guide drivers through toll roads based on their preferences or vehicle capabilities.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-315660370%2FClasslikes%2F1617540583" anchor-label="TollStructureManeuver" id="-315660370%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-toll-structure-maneuver/index.html"><span>Toll</span><wbr></wbr><span>Structure</span><wbr></wbr><span><span>Maneuver</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-315660370%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-toll-structure-maneuver/index.html">TollStructureManeuver</a></div><div class="brief "><p class="paragraph">A class that provides information for a toll structure at a toll point.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1648763501%2FClasslikes%2F1617540583" anchor-label="TollStructureType" id="1648763501%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-toll-structure-type/index.html"><span>Toll</span><wbr></wbr><span>Structure</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1648763501%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-toll-structure-type/index.html">TollStructureType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-toll-structure-type/index.html">TollStructureType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">This enum defines the type of toll structure used on a road segment or lane. Each value represents a different tolling mechanism used in road infrastructure. This enum helps in providing detailed tolling information for routing and navigation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="143573017%2FClasslikes%2F1617540583" anchor-label="TollSystem" id="143573017%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-toll-system/index.html"><span>Toll</span><wbr></wbr><span><span>System</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="143573017%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-toll-system/index.html">TollSystem</a></div><div class="brief "><p class="paragraph">Contains informations about a toll system.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1493484646%2FClasslikes%2F1617540583" anchor-label="TrafficSignal" id="-1493484646%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-signal/index.html"><span>Traffic</span><wbr></wbr><span><span>Signal</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1493484646%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-traffic-signal/index.html">TrafficSignal</a></div><div class="brief "><p class="paragraph">Identifies the presence and the location of traffic lights at an intersection</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2110175131%2FClasslikes%2F1617540583" anchor-label="TrafficSignalLocation" id="-2110175131%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-signal-location/index.html"><span>Traffic</span><wbr></wbr><span>Signal</span><wbr></wbr><span><span>Location</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2110175131%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-traffic-signal-location/index.html">TrafficSignalLocation</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-traffic-signal-location/index.html">TrafficSignalLocation</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Indicates the location of a traffic signal.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-263940064%2FClasslikes%2F1617540583" anchor-label="TurnOnRedRegulation" id="-263940064%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-turn-on-red-regulation/index.html"><span>Turn</span><wbr></wbr><span>On</span><wbr></wbr><span>Red</span><wbr></wbr><span><span>Regulation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-263940064%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-turn-on-red-regulation/index.html">TurnOnRedRegulation</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-turn-on-red-regulation/index.html">TurnOnRedRegulation</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">The regulations for turning on the red color of the traffic light.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-783925712%2FClasslikes%2F1617540583" anchor-label="VehicleProfileRestriction" id="-783925712%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-vehicle-profile-restriction/index.html"><span>Vehicle</span><wbr></wbr><span>Profile</span><wbr></wbr><span><span>Restriction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-783925712%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-vehicle-profile-restriction/index.html">VehicleProfileRestriction</a></div><div class="brief "><p class="paragraph">Physical and cargo profile of a vehicle that triggers a regulation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="390689508%2FClasslikes%2F1617540583" anchor-label="VehicleRestrictionCondition" id="390689508%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-vehicle-restriction-condition/index.html"><span>Vehicle</span><wbr></wbr><span>Restriction</span><wbr></wbr><span><span>Condition</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="390689508%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-vehicle-restriction-condition/index.html">VehicleRestrictionCondition</a></div><div class="brief "><p class="paragraph">Combined set of conditions that must all be satisfied for a regulation to apply.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="787854269%2FClasslikes%2F1617540583" anchor-label="VehicleSpecificAccess" id="787854269%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-vehicle-specific-access/index.html"><span>Vehicle</span><wbr></wbr><span>Specific</span><wbr></wbr><span><span>Access</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="787854269%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-vehicle-specific-access/index.html">VehicleSpecificAccess</a></div><div class="brief "><p class="paragraph">Access regulation for a specific vehicle type on a road segment.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1463125139%2FClasslikes%2F1617540583" anchor-label="VehicleSpecificSpeedLimit" id="-1463125139%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-vehicle-specific-speed-limit/index.html"><span>Vehicle</span><wbr></wbr><span>Specific</span><wbr></wbr><span>Speed</span><wbr></wbr><span><span>Limit</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1463125139%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-vehicle-specific-speed-limit/index.html">VehicleSpecificSpeedLimit</a></div><div class="brief "><p class="paragraph">Speed limit regulation specific to a vehicle type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="221917198%2FClasslikes%2F1617540583" anchor-label="VehicleTypeCondition" id="221917198%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-vehicle-type-condition/index.html"><span>Vehicle</span><wbr></wbr><span>Type</span><wbr></wbr><span><span>Condition</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="221917198%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-vehicle-type-condition/index.html">VehicleTypeCondition</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-vehicle-type-condition/index.html">VehicleTypeCondition</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Type of commercial vehicle to which a regulation applies.</p></div></div></div>
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
