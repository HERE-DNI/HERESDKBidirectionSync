---
title: "VehicleRestriction"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-transport-vehicle-restriction"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>VehicleRestriction</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.transport/VehicleRestriction///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.transport</a><span class="delimiter">/</span><span class="current">VehicleRestriction</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Vehicle</span><wbr></wbr><span><span>Restriction</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">VehicleRestriction</a></div><p class="paragraph">Represents a vehicle restriction.</p><p class="paragraph">Any non <code class="lang-kotlin">null</code> field adds more details to the restriction. A general truck restriction is represented with <code class="lang-kotlin">null</code> values for fields <code class="lang-kotlin">restriction</code> and <code class="lang-kotlin">hazmatRestriction</code>.</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="1548307431%2FConstructors%2F1617540583" anchor-label="VehicleRestriction" id="1548307431%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-vehicle-restriction.html"><span>Vehicle</span><wbr></wbr><span><span>Restriction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1548307431%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">restriction<span class="token operator">: </span><a href="../-specific-restriction/index.html">SpecificRestriction</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates an unconditional restriction.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates an uncoditional general restriction.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="2074228966%2FProperties%2F1617540583" anchor-label="appliesToDelivery" id="2074228966%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="applies-to-delivery.html"><span>applies</span><wbr></wbr><span>To</span><wbr></wbr><span><span>Delivery</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2074228966%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="applies-to-delivery.html">appliesToDelivery</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Flag indicating whether this restriction applies to delivery vehicles.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="372081570%2FProperties%2F1617540583" anchor-label="axleCount" id="372081570%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="axle-count.html"><span>axle</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="372081570%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="axle-count.html">axleCount</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-integer-range/index.html">IntegerRange</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The axle count for which the current restriction applies. Can be used in conjunction with <a href="../-restriction-type/-w-e-i-g-h-t_-p-e-r_-a-x-l-e_-c-o-u-n-t/index.html">com.here.sdk.transport.RestrictionType.WEIGHT_PER_AXLE_COUNT</a> to specify restriction based on weight per number of axles. The <code class="lang-kotlin">axleCount</code> considers total number of axles on the whole vehicle (truck + trailers). This can be used to limit the weight per axle for the whole truck. If <code class="lang-kotlin">axleCount</code> is null, the restriction is general and applies regardless of axle count. If the upper limit of the <code class="lang-kotlin">axleCount</code> range is 0 or <code class="lang-kotlin">null</code> then it means the restriction applies for values >= lower limit, i.e. the upper limit of range if infinite or unbound. When a user taps the icon, the allowed <code class="lang-kotlin">axleCount</code> range can be retrieved directly from <code class="lang-kotlin">VehicleRestriction.axleCount</code>. Examples:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-110568130%2FProperties%2F1617540583" anchor-label="axleCountInGroup" id="-110568130%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="axle-count-in-group.html"><span>axle</span><wbr></wbr><span>Count</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Group</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-110568130%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="axle-count-in-group.html">axleCountInGroup</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-integer-range/index.html">IntegerRange</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Number of axles in a group for which the current restriction applies. <code class="lang-kotlin">axleCountInGroup</code> is a set of axles close together: single, tandem (2), triple (3), etc. Can be used in conjunction with <a href="../-restriction-type/-w-e-i-g-h-t_-p-e-r_-a-x-l-e_-g-r-o-u-p/index.html">com.here.sdk.transport.RestrictionType.WEIGHT_PER_AXLE_GROUP</a> to specify restriction based on weight per axle group. The <code class="lang-kotlin">axleCountInGroup</code> considers number of axles in a specific axle group (usually rear axles on the truck or trailer). This can be used to limit weight for a tandem/triple rear axle group. If the upper limit of the <code class="lang-kotlin">axleCountInGroup</code> range is 0 or <code class="lang-kotlin">null</code> then it means the restriction applies for values >= lower limit, i.e. the upper limit of range if infinite or unbound. Examples:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2074689332%2FProperties%2F1617540583" anchor-label="hazmatRestriction" id="2074689332%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="hazmat-restriction.html"><span>hazmat</span><wbr></wbr><span><span>Restriction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2074689332%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="hazmat-restriction.html">hazmatRestriction</a><span class="token operator">: </span><a href="../-hazardous-material-restriction/index.html">HazardousMaterialRestriction</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Restriction on transport of hazardous materials and max allowed tunnel category. For example, (FLAMMABLE, TunnelCategory.D) means, a restriction applying for trucks carrying flammable materials are not allowed to enter tunnels category D and E - (TunnelCategory.B and TunnelCategory.C allowed).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="897777269%2FProperties%2F1617540583" anchor-label="restriction" id="897777269%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="restriction.html"><span><span>restriction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="897777269%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="restriction.html">restriction</a><span class="token operator">: </span><a href="../-specific-restriction/index.html">SpecificRestriction</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">A <code class="lang-kotlin">SpecificRestriction</code> defines what type of restriction applies (weight, height, etc.) and the range of allowed values.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-522354462%2FProperties%2F1617540583" anchor-label="timeRestriction" id="-522354462%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="time-restriction.html"><span>time</span><wbr></wbr><span><span>Restriction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-522354462%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="time-restriction.html">timeRestriction</a><span class="token operator">: </span><a href="../-time-restriction/index.html">TimeRestriction</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Restriction applies during specific time.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1366759651%2FProperties%2F1617540583" anchor-label="trailerCount" id="-1366759651%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="trailer-count.html"><span>trailer</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1366759651%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="trailer-count.html">trailerCount</a><span class="token operator">: </span><a href="../../com.here.sdk.core/-integer-range/index.html">IntegerRange</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Number of trailers for which the restriction applies.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1837632484%2FProperties%2F1617540583" anchor-label="truckCategory" id="1837632484%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="truck-category.html"><span>truck</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1837632484%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="truck-category.html">truckCategory</a><span class="token operator">: </span><a href="../-truck-category/index.html">TruckCategory</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Restriction applies to a specific truck category.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2125035853%2FProperties%2F1617540583" anchor-label="weather" id="2125035853%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="weather.html"><span><span>weather</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2125035853%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="weather.html">weather</a><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-weather-type/index.html">WeatherType</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Type of weather in which restriction applies.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1196381592%2FFunctions%2F1617540583" anchor-label="equals" id="-1196381592%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="equals.html"><span><span>equals</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1196381592%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">operator override </span><span class="token keyword">fun </span><a href="equals.html"><span class="token function">equals</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">other<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-686904962%2FFunctions%2F1617540583" anchor-label="hashCode" id="-686904962%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="hash-code.html"><span>hash</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-686904962%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">fun </span><a href="hash-code.html"><span class="token function">hashCode</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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
