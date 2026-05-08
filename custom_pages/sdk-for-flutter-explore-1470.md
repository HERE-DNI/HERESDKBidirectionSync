---
title: "SectionNoticeCode"
slug: "sdk-for-flutter-explore"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>SectionNoticeCode</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.routing/SectionNoticeCode///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.routing</a><span class="delimiter">/</span><span class="current">SectionNoticeCode</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Section</span><wbr></wbr><span>Notice</span><wbr></wbr><span><span>Code</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">SectionNoticeCode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">SectionNoticeCode</a><span class="token operator">&gt; </span></div><p class="paragraph">Notice codes which point the issues encountered during processing of a <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.Section</a>.</p><p class="paragraph"><strong>Note:</strong> The section notice codes are going to be extended for new error situations.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
    <div class="tabs-section-body">
      <div data-togglable="ENTRY">
        <h2 class="">Entries</h2>
        <div class="table"><a data-name="173090341%2FClasslikes%2F1617540583" anchor-label="VIOLATED_CRITICAL_RULE" id="173090341%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_CRITICAL_RULE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="173090341%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_CRITICAL_RULE</a></div></div><div class="brief "><p class="paragraph">Route has violoated a non-detailed critical rule. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-868528382%2FClasslikes%2F1617540583" anchor-label="VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY" id="-868528382%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-868528382%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY</a></div></div><div class="brief "><p class="paragraph">Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-363736573%2FClasslikes%2F1617540583" anchor-label="VIOLATED_AVOID_TOLL_ROAD" id="-363736573%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_TOLL_ROAD</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-363736573%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_TOLL_ROAD</a></div></div><div class="brief "><p class="paragraph">Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="425269849%2FClasslikes%2F1617540583" anchor-label="VIOLATED_AVOID_FERRY" id="425269849%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_FERRY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="425269849%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_FERRY</a></div></div><div class="brief "><p class="paragraph">Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="91958289%2FClasslikes%2F1617540583" anchor-label="VIOLATED_AVOID_TUNNEL" id="91958289%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_TUNNEL</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="91958289%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_TUNNEL</a></div></div><div class="brief "><p class="paragraph">Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-162399689%2FClasslikes%2F1617540583" anchor-label="VIOLATED_AVOID_DIRT_ROAD" id="-162399689%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_DIRT_ROAD</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-162399689%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_DIRT_ROAD</a></div></div><div class="brief "><p class="paragraph">Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="249013366%2FClasslikes%2F1617540583" anchor-label="VIOLATED_AVOID_RAIL_FERRY" id="249013366%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_RAIL_FERRY</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="249013366%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_RAIL_FERRY</a></div></div><div class="brief "><p class="paragraph">Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2047302995%2FClasslikes%2F1617540583" anchor-label="VIOLATED_AVOID_PARK" id="2047302995%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_PARK</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2047302995%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_PARK</a></div></div><div class="brief "><p class="paragraph">Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="21621618%2FClasslikes%2F1617540583" anchor-label="VIOLATED_BLOCKED_ROAD" id="21621618%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_BLOCKED_ROAD</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="21621618%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_BLOCKED_ROAD</a></div></div><div class="brief "><p class="paragraph">Route uses roads blocked by traffic events or route did not manage to avoid the requested <code class="lang-kotlin">avoidBoundingBoxAreas</code> or <code class="lang-kotlin">countries</code> or <code class="lang-kotlin">segments</code>. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2051935851%2FClasslikes%2F1617540583" anchor-label="VIOLATED_START_DIRECTION" id="2051935851%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_START_DIRECTION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2051935851%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_START_DIRECTION</a></div></div><div class="brief "><p class="paragraph">Start direction of the route is not as requested. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="905841945%2FClasslikes%2F1617540583" anchor-label="VIOLATED_CARPOOL" id="905841945%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_CARPOOL</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="905841945%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_CARPOOL</a></div></div><div class="brief "><p class="paragraph">Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2019698455%2FClasslikes%2F1617540583" anchor-label="VIOLATED_TURN_RESTRICTION" id="-2019698455%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_TURN_RESTRICTION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2019698455%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_TURN_RESTRICTION</a></div></div><div class="brief "><p class="paragraph">Route uses a time-restricted turn. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1642979070%2FClasslikes%2F1617540583" anchor-label="VIOLATED_VEHICLE_RESTRICTION" id="-1642979070%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_VEHICLE_RESTRICTION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1642979070%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_VEHICLE_RESTRICTION</a></div></div><div class="brief "><p class="paragraph">Route uses a road which is forbidden for the given vehicle profile. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-243819176%2FClasslikes%2F1617540583" anchor-label="VIOLATED_ZONE_RESTRICTION" id="-243819176%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_ZONE_RESTRICTION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-243819176%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_ZONE_RESTRICTION</a></div></div><div class="brief "><p class="paragraph">Route uses a road which is part of restricted <code class="lang-kotlin">zoneCategories</code> requested to be avoided by user. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1264274987%2FClasslikes%2F1617540583" anchor-label="VIOLATED_AVOID_U_TURNS" id="1264274987%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_U_TURNS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1264274987%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_U_TURNS</a></div></div><div class="brief "><p class="paragraph">Route did not manage to avoid u turns. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="822498136%2FClasslikes%2F1617540583" anchor-label="VIOLATED_EMERGENCY_GATE" id="822498136%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_EMERGENCY_GATE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="822498136%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_EMERGENCY_GATE</a></div></div><div class="brief "><p class="paragraph">Route goes through an emergency gate. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1630682349%2FClasslikes%2F1617540583" anchor-label="VIOLATED_AVOID_SEASONAL_CLOSURE" id="-1630682349%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_SEASONAL_CLOSURE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1630682349%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_SEASONAL_CLOSURE</a></div></div><div class="brief "><p class="paragraph">Route did not manage to avoid seasonal closure. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1055075416%2FClasslikes%2F1617540583" anchor-label="VIOLATED_AVOID_TRUCK_ROAD_TYPE" id="1055075416%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_TRUCK_ROAD_TYPE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1055075416%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_TRUCK_ROAD_TYPE</a></div></div><div class="brief "><p class="paragraph">Route did not manage to avoid restricted truck road types.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1341744177%2FClasslikes%2F1617540583" anchor-label="VIOLATED_AVOID_TOLL_TRANSPONDER" id="-1341744177%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_TOLL_TRANSPONDER</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1341744177%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_TOLL_TRANSPONDER</a></div></div><div class="brief "><p class="paragraph">Route did not manage to avoid toll booth that requires transponder. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1455156754%2FClasslikes%2F1617540583" anchor-label="VIOLATED_CHARGING_STATION_OPENING_HOURS" id="-1455156754%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_CHARGING_STATION_OPENING_HOURS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1455156754%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_CHARGING_STATION_OPENING_HOURS</a></div></div><div class="brief "><p class="paragraph">Charging at the charging station planned at the destination of this section falls outside of opening hours. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1485307572%2FClasslikes%2F1617540583" anchor-label="VIOLATED_AVOID_DIFFICULT_TURNS" id="1485307572%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_DIFFICULT_TURNS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1485307572%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_AVOID_DIFFICULT_TURNS</a></div></div><div class="brief "><p class="paragraph">Route did not manage to avoid difficult turns. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.CRITICAL</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1253061232%2FClasslikes%2F1617540583" anchor-label="SEASONAL_CLOSURE" id="-1253061232%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">SEASONAL_CLOSURE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1253061232%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">SEASONAL_CLOSURE</a></div></div><div class="brief "><p class="paragraph">Route goes through seasonal closure. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-964123060%2FClasslikes%2F1617540583" anchor-label="TOLL_TRANSPONDER" id="-964123060%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">TOLL_TRANSPONDER</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-964123060%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">TOLL_TRANSPONDER</a></div></div><div class="brief "><p class="paragraph">Route goes through toll booth that requires transponder. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1144704280%2FClasslikes%2F1617540583" anchor-label="TOLLS_DATA_UNAVAILABLE" id="-1144704280%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">TOLLS_DATA_UNAVAILABLE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1144704280%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">TOLLS_DATA_UNAVAILABLE</a></div></div><div class="brief "><p class="paragraph">Tolls data was requested but could not be calculated for this section. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1537427799%2FClasslikes%2F1617540583" anchor-label="TOLLS_DATA_TEMPORARILY_UNAVAILABLE" id="1537427799%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">TOLLS_DATA_TEMPORARILY_UNAVAILABLE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1537427799%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">TOLLS_DATA_TEMPORARILY_UNAVAILABLE</a></div></div><div class="brief "><p class="paragraph">Tolls data was requested but is temporarily unavailable. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1099461942%2FClasslikes%2F1617540583" anchor-label="CHARGING_STOP_NOT_NEEDED" id="1099461942%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">CHARGING_STOP_NOT_NEEDED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1099461942%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">CHARGING_STOP_NOT_NEEDED</a></div></div><div class="brief "><p class="paragraph">A charging stop was planned at the destination of this section, but it is no longer needed. It may be issued only when refreshing a route via <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.RouteHandle</a>. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1612577129%2FClasslikes%2F1617540583" anchor-label="NO_SCHEDULE" id="-1612577129%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">NO_SCHEDULE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1612577129%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">NO_SCHEDULE</a></div></div><div class="brief "><p class="paragraph">No schedule information is available for a transit section. As a result, departure/arrival times are approximated. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-536148103%2FClasslikes%2F1617540583" anchor-label="NO_INTERMEDIATE" id="-536148103%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">NO_INTERMEDIATE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-536148103%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">NO_INTERMEDIATE</a></div></div><div class="brief "><p class="paragraph">Information about intermediate stops is not available for a transit section. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="205316604%2FClasslikes%2F1617540583" anchor-label="UNWANTED_MODE" id="205316604%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">UNWANTED_MODE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="205316604%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">UNWANTED_MODE</a></div></div><div class="brief "><p class="paragraph">This transit section contains a transport mode that was explictly disabled. Mode filtering is not available in this area. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2083332874%2FClasslikes%2F1617540583" anchor-label="SCHEDULED_TIMES" id="-2083332874%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">SCHEDULED_TIMES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2083332874%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">SCHEDULED_TIMES</a></div></div><div class="brief "><p class="paragraph">This transit section returned times which are scheduled times, even though delay information is available. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1642002449%2FClasslikes%2F1617540583" anchor-label="SIMPLE_POLYLINE" id="-1642002449%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">SIMPLE_POLYLINE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1642002449%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">SIMPLE_POLYLINE</a></div></div><div class="brief "><p class="paragraph">An accurate polyline is not available for this section. An accurate polyline is not available for this section. The returned polyline has been generated from departure and arrival places. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2063793711%2FClasslikes%2F1617540583" anchor-label="POTENTIAL_CARPOOL" id="-2063793711%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">POTENTIAL_CARPOOL</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2063793711%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">POTENTIAL_CARPOOL</a></div></div><div class="brief "><p class="paragraph">Route utilizes a designated carpool lane, potentially subject to restrictions beyond the scheduled travel hours. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-889539791%2FClasslikes%2F1617540583" anchor-label="POTENTIAL_TURN_RESTRICTION" id="-889539791%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">POTENTIAL_TURN_RESTRICTION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-889539791%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">POTENTIAL_TURN_RESTRICTION</a></div></div><div class="brief "><p class="paragraph">Route includes a turn that is potentially restricted and inaccessible beyond the scheduled travel hours. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1334853190%2FClasslikes%2F1617540583" anchor-label="POTENTIAL_VEHICLE_RESTRICTION" id="-1334853190%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">POTENTIAL_VEHICLE_RESTRICTION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1334853190%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">POTENTIAL_VEHICLE_RESTRICTION</a></div></div><div class="brief "><p class="paragraph">Route utilizes roads that are potentially off-limits to the specified vehicle profile beyond the scheduled travel hours. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="886339488%2FClasslikes%2F1617540583" anchor-label="POTENTIAL_ZONE_RESTRICTION" id="886339488%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">POTENTIAL_ZONE_RESTRICTION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="886339488%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">POTENTIAL_ZONE_RESTRICTION</a></div></div><div class="brief "><p class="paragraph">Route incorporates roads within zones, which are potentially not accessible beyond the scheduled travel hours. Severity: <a href="sdk-for-flutter-explore-index">com.here.sdk.routing.NoticeSeverity.INFO</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-480439380%2FClasslikes%2F1617540583" anchor-label="VIOLATED_MIN_CHARGE_AT_FIRST_CS" id="-480439380%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_MIN_CHARGE_AT_FIRST_CS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-480439380%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_MIN_CHARGE_AT_FIRST_CS</a></div></div><div class="brief "><p class="paragraph">The route can not reach the first charging station with the minimum required charge, as the initial charge was to low.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-504913251%2FClasslikes%2F1617540583" anchor-label="VIOLATED_MIN_CHARGE_AT_CS" id="-504913251%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_MIN_CHARGE_AT_CS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-504913251%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_MIN_CHARGE_AT_CS</a></div></div><div class="brief "><p class="paragraph">The route can not reach all charging stations on the route with the minimum required charge, as the initial charge was to low.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1944696969%2FClasslikes%2F1617540583" anchor-label="VIOLATED_MIN_CHARGE_AT_DESTINATION" id="1944696969%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">VIOLATED_MIN_CHARGE_AT_DESTINATION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1944696969%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">VIOLATED_MIN_CHARGE_AT_DESTINATION</a></div></div><div class="brief "><p class="paragraph">The route can not reach the waypoint, as the there are not enough charging stops available or the initial charge was to low.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1102091526%2FClasslikes%2F1617540583" anchor-label="NO_THROUGH_RESTRICTION" id="-1102091526%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index">NO_THROUGH_RESTRICTION</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1102091526%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="sdk-for-flutter-explore-index">NO_THROUGH_RESTRICTION</a></div></div><div class="brief "><p class="paragraph">Route goes through a road that does not allow through traffic.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-2050543872%2FProperties%2F1617540583" anchor-label="entries" id="-2050543872%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-entries"><span><span>entries</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2050543872%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-entries">entries</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">SectionNoticeCode</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1884555775%2FProperties%2F1617540583" anchor-label="value" id="1884555775%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-value"><span><span>value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1884555775%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="sdk-for-flutter-explore-value">value</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="191434396%2FFunctions%2F1617540583" anchor-label="valueOf" id="191434396%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-value-of"><span>value</span><wbr></wbr><span><span>Of</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="191434396%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-value-of"><span class="token function">valueOf</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SectionNoticeCode</a></div><div class="brief "><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-142058328%2FFunctions%2F1617540583" anchor-label="values" id="-142058328%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-values"><span><span>values</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-142058328%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-values"><span class="token function">values</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">SectionNoticeCode</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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
