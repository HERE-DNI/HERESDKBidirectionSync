---
title: "Span"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-span"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>Span</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.routing/Span///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.routing</a><span class="delimiter">/</span><span class="current">Span</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Span</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">Span</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">A span is a part of the <a href="../-section/index.html">com.here.sdk.routing.Section</a> which is traversable or navigable. Each span usually has some geometry associated with it.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="396271771%2FClasslikes%2F1617540583" anchor-label="Companion" id="396271771%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="396271771%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="253818081%2FProperties%2F1617540583" anchor-label="baseDuration" id="253818081%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="base-duration.html"><span>base</span><wbr></wbr><span><span>Duration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="253818081%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="base-duration.html">baseDuration</a><span class="token operator">: </span><a href="../../com.here.time/-duration/index.html">Duration</a></div><div class="brief "><p class="paragraph">The time duration necessary to traverse the span, using the speed provided in <a href="dynamic-speed-info.html">com.here.sdk.routing.Span.dynamicSpeedInfo</a> without taking into consideration the delays caused by the traffic.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-601179671%2FProperties%2F1617540583" anchor-label="carAttributes" id="-601179671%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="car-attributes.html"><span>car</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-601179671%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="car-attributes.html">carAttributes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-access-attributes/index.html">AccessAttributes</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of car access attributes on the span.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-754496606%2FProperties%2F1617540583" anchor-label="consumptionInKilowattHours" id="-754496606%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="consumption-in-kilowatt-hours.html"><span>consumption</span><wbr></wbr><span>In</span><wbr></wbr><span>Kilowatt</span><wbr></wbr><span><span>Hours</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-754496606%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="consumption-in-kilowatt-hours.html">consumptionInKilowattHours</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The power consumption in kilowatt per hour necessary to traverse the span.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1543424943%2FProperties%2F1617540583" anchor-label="countryCode" id="-1543424943%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="country-code.html"><span>country</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1543424943%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="country-code.html">countryCode</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The country code of the span. The value is <code class="lang-kotlin">null</code> when no data is available.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1069643214%2FProperties%2F1617540583" anchor-label="duration" id="-1069643214%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="duration.html"><span><span>duration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1069643214%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="duration.html">duration</a><span class="token operator">: </span><a href="../../com.here.time/-duration/index.html">Duration</a></div><div class="brief "><p class="paragraph">The time duration necessary to traverse the span, using the speed provided in <a href="dynamic-speed-info.html">com.here.sdk.routing.Span.dynamicSpeedInfo</a>. This duration takes also into consideration the delays caused by the traffic.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-714063632%2FProperties%2F1617540583" anchor-label="dynamicSpeedInfo" id="-714063632%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="dynamic-speed-info.html"><span>dynamic</span><wbr></wbr><span>Speed</span><wbr></wbr><span><span>Info</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-714063632%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="dynamic-speed-info.html">dynamicSpeedInfo</a><span class="token operator">: </span><a href="../-dynamic-speed-info/index.html">DynamicSpeedInfo</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The dynamic speed information on the span.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1888426817%2FProperties%2F1617540583" anchor-label="functionalRoadClass" id="-1888426817%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="functional-road-class.html"><span>functional</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Class</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1888426817%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="functional-road-class.html">functionalRoadClass</a><span class="token operator">: </span><a href="../-functional-road-class/index.html">FunctionalRoadClass</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The functional road class of the span.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="766911764%2FProperties%2F1617540583" anchor-label="geometry" id="766911764%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="geometry.html"><span><span>geometry</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="766911764%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="geometry.html">geometry</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-polyline/index.html">GeoPolyline</a></div><div class="brief "><p class="paragraph">The <a href="../../com.here.sdk.core/-geo-polyline/index.html">com.here.sdk.core.GeoPolyline</a> object representing the polyline of this span.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="944805777%2FProperties%2F1617540583" anchor-label="lengthInMeters" id="944805777%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="length-in-meters.html"><span>length</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Meters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="944805777%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="length-in-meters.html">lengthInMeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The length of this span in meters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="972519409%2FProperties%2F1617540583" anchor-label="noThroughRestrictionsIndexes" id="972519409%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="no-through-restrictions-indexes.html"><span>no</span><wbr></wbr><span>Through</span><wbr></wbr><span>Restrictions</span><wbr></wbr><span><span>Indexes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="972519409%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="no-through-restrictions-indexes.html">noThroughRestrictionsIndexes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of indexes to <a href="../-section/no-through-restrictions.html">com.here.sdk.routing.Section.noThroughRestrictions</a> the parent section owns. In case the list is not empty, the user must judge all the indexed sdk routing noThroughRestriction's carefully before proceeding.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1911700940%2FProperties%2F1617540583" anchor-label="noticeIndexes" id="1911700940%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="notice-indexes.html"><span>notice</span><wbr></wbr><span><span>Indexes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1911700940%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="notice-indexes.html">noticeIndexes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of indexes to <a href="../-section/section-notices.html">com.here.sdk.routing.Section.sectionNotices</a> the parent section owns. In case the list is not empty, the user must judge all the indexed <a href="../-section-notice/index.html">com.here.sdk.routing.SectionNotice</a>s carefully before proceeding.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1759936054%2FProperties%2F1617540583" anchor-label="roadNumbers" id="-1759936054%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="road-numbers.html"><span>road</span><wbr></wbr><span><span>Numbers</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1759936054%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="road-numbers.html">roadNumbers</a><span class="token operator">: </span><a href="../-localized-road-numbers/index.html">LocalizedRoadNumbers</a></div><div class="brief "><p class="paragraph">The road numbers on the span enriched with information specific to <i>route numbers</i> of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (<code class="lang-kotlin">RouteType</code>).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1697337556%2FProperties%2F1617540583" anchor-label="scooterAttributes" id="-1697337556%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="scooter-attributes.html"><span>scooter</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1697337556%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="scooter-attributes.html">scooterAttributes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-access-attributes/index.html">AccessAttributes</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of scooter access attributes on the span.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-94467300%2FProperties%2F1617540583" anchor-label="sectionPolylineOffset" id="-94467300%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="section-polyline-offset.html"><span>section</span><wbr></wbr><span>Polyline</span><wbr></wbr><span><span>Offset</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-94467300%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="section-polyline-offset.html">sectionPolylineOffset</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief "><p class="paragraph">The position of the span inside the section's geometry, given as an offset. The span geometry starts from this offset and ends on the offset of the next span, both start offset point and end offset point being included in the span, because the spans' geometry share a point in the section's geometry.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2076173842%2FProperties%2F1617540583" anchor-label="segmentReference" id="-2076173842%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="segment-reference.html"><span>segment</span><wbr></wbr><span><span>Reference</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2076173842%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="segment-reference.html">segmentReference</a><span class="token operator">: </span><a href="../-segment-reference/index.html">SegmentReference</a></div><div class="brief "><p class="paragraph">The segment reference of this span.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="152064902%2FProperties%2F1617540583" anchor-label="speedLimitInMetersPerSecond" id="152064902%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="speed-limit-in-meters-per-second.html"><span>speed</span><wbr></wbr><span>Limit</span><wbr></wbr><span>In</span><wbr></wbr><span>Meters</span><wbr></wbr><span>Per</span><wbr></wbr><span><span>Second</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="152064902%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="speed-limit-in-meters-per-second.html">speedLimitInMetersPerSecond</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The speed limit in meters per second on the span.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1157753098%2FProperties%2F1617540583" anchor-label="stateCode" id="-1157753098%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="state-code.html"><span>state</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1157753098%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="state-code.html">stateCode</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The state code of the span. State code is available in some countries to denote principal subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio. The format of state code can vary for different countries, take the United States as example, it consists of two alphabet letters. The value is <code class="lang-kotlin">null</code> when no data is available.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1663346636%2FProperties%2F1617540583" anchor-label="streetAttributes" id="1663346636%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="street-attributes.html"><span>street</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1663346636%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="street-attributes.html">streetAttributes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-street-attributes/index.html">StreetAttributes</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of street attributes on the span.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="556196911%2FProperties%2F1617540583" anchor-label="streetNames" id="556196911%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="street-names.html"><span>street</span><wbr></wbr><span><span>Names</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="556196911%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="street-names.html">streetNames</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-localized-texts/index.html">LocalizedTexts</a></div><div class="brief "><p class="paragraph">The street names on the span.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-781835627%2FProperties%2F1617540583" anchor-label="trafficIncidentIndexes" id="-781835627%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="traffic-incident-indexes.html"><span>traffic</span><wbr></wbr><span>Incident</span><wbr></wbr><span><span>Indexes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-781835627%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="traffic-incident-indexes.html">trafficIncidentIndexes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The indexes of traffic incidents from the field <a href="../-section/traffic-incidents.html">com.here.sdk.routing.Section.trafficIncidents</a> of the parent <a href="../-section/index.html">com.here.sdk.routing.Section</a>. Each matching incident takes at least a whole <a href="geometry.html">com.here.sdk.routing.Span.geometry</a>. The same incident can take other spans and an area out of the built route as well.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="948727742%2FProperties%2F1617540583" anchor-label="truckAttributes" id="948727742%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="truck-attributes.html"><span>truck</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="948727742%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="truck-attributes.html">truckAttributes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-access-attributes/index.html">AccessAttributes</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of truck access attributes on the span.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1206644358%2FProperties%2F1617540583" anchor-label="walkAttributes" id="1206644358%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="walk-attributes.html"><span>walk</span><wbr></wbr><span><span>Attributes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1206644358%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="walk-attributes.html">walkAttributes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-walk-attributes/index.html">WalkAttributes</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The list of walk attributes on the span.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="1259075217%2FFunctions%2F1617540583" anchor-label="getShieldText" id="1259075217%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-shield-text.html"><span>get</span><wbr></wbr><span>Shield</span><wbr></wbr><span><span>Text</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1259075217%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-shield-text.html"><span class="token function">getShieldText</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">roadNumber<span class="token operator">: </span><a href="../-localized-road-number/index.html">LocalizedRoadNumber</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Converts full route number to the value to be displayed on the road shield. The results are based on country code and state code of <code class="lang-kotlin">Span</code> object and route type of passed <code class="lang-kotlin">road_number</code> argument.</p></div></div></div>
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
