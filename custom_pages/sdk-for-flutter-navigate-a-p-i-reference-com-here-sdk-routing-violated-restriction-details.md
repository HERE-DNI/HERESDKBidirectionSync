---
title: "Details"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-routing-violated-restriction-details"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>Details</title>
    <link href="../../../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../../../";</script>
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
<script type="text/javascript" src="../../../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../../../styles/style.css" rel="Stylesheet">
<link href="../../../../styles/main.css" rel="Stylesheet">
<link href="../../../../styles/prism.css" rel="Stylesheet">
<link href="../../../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
</head>
<body>
    <div class="root">
    <nav class="navigation theme-dark" id="navigation-wrapper">
            <a class="library-name--link" href="../../../../index.html">
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.routing/ViolatedRestriction.Details///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../../index.html">com.here.sdk.routing</a><span class="delimiter">/</span><a href="../index.html">ViolatedRestriction</a><span class="delimiter">/</span><span class="current">Details</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Details</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">Details</a></div><p class="paragraph">Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set. For example, if the vehicle violates the maximum allowed height during the trip, then the member <code class="lang-kotlin">max_height_in_centimeters</code> will be set with the maximum allowed height value.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-2052023910%2FConstructors%2F1617540583" anchor-label="Details" id="-2052023910%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-details.html"><span><span>Details</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2052023910%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="970598488%2FProperties%2F1617540583" anchor-label="forbiddenAxleCount" id="970598488%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="forbidden-axle-count.html"><span>forbidden</span><wbr></wbr><span>Axle</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="970598488%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="forbidden-axle-count.html">forbiddenAxleCount</a><span class="token operator">: </span><a href="../../../com.here.sdk.core/-integer-range/index.html">IntegerRange</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The restriction to trucks with axles number within specified range during the trip. This property will be set if the <a href="../../../com.here.sdk.transport/-vehicle-specification/axle-count.html">com.here.sdk.transport.VehicleSpecification.axleCount</a> is within this range.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="894386056%2FProperties%2F1617540583" anchor-label="forbiddenHazardousGoods" id="894386056%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="forbidden-hazardous-goods.html"><span>forbidden</span><wbr></wbr><span>Hazardous</span><wbr></wbr><span><span>Goods</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="894386056%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="forbidden-hazardous-goods.html">forbiddenHazardousGoods</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../../../com.here.sdk.transport/-hazardous-material/index.html">HazardousMaterial</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used for the route calculation provided using <a href="../../../com.here.sdk.transport/-vehicle-specification/hazardous-materials.html">com.here.sdk.transport.VehicleSpecification.hazardousMaterials</a> from <a href="../../../com.here.sdk.transport/-transport-specification/vehicle-specification.html">com.here.sdk.transport.TransportSpecification.vehicleSpecification</a> from <a href="../../-routing-options/transport-specification.html">com.here.sdk.routing.RoutingOptions.transportSpecification</a>. This property is the intersection of the two lists.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="641498791%2FProperties%2F1617540583" anchor-label="forbiddenTrailerCount" id="641498791%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="forbidden-trailer-count.html"><span>forbidden</span><wbr></wbr><span>Trailer</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="641498791%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="forbidden-trailer-count.html">forbiddenTrailerCount</a><span class="token operator">: </span><a href="../../../com.here.sdk.core/-integer-range/index.html">IntegerRange</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Constrains the restriction to trucks with number of trailer within specified range during the trip. This property will be set if the <a href="../../../com.here.sdk.transport/-vehicle-specification/trailer-count.html">com.here.sdk.transport.VehicleSpecification.trailerCount</a> is within this range.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-330865254%2FProperties%2F1617540583" anchor-label="forbiddenTruckCategory" id="-330865254%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="forbidden-truck-category.html"><span>forbidden</span><wbr></wbr><span>Truck</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-330865254%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="forbidden-truck-category.html">forbiddenTruckCategory</a><span class="token operator">: </span><a href="../../../com.here.sdk.transport/-truck-category/index.html">TruckCategory</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">This property will be set if a restriction applies to the value of <a href="../../../com.here.sdk.transport/-truck-category/index.html">com.here.sdk.transport.TruckCategory</a> parameter used for route calculation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1954711273%2FProperties%2F1617540583" anchor-label="forbiddenTruckRoadTypes" id="1954711273%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="forbidden-truck-road-types.html"><span>forbidden</span><wbr></wbr><span>Truck</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Types</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1954711273%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="forbidden-truck-road-types.html">forbiddenTruckRoadTypes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../../../com.here.sdk.transport/-truck-road-type/index.html">TruckRoadType</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Contains violated restrictions for truck road types.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1237324894%2FProperties%2F1617540583" anchor-label="forbiddenTruckType" id="1237324894%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="forbidden-truck-type.html"><span>forbidden</span><wbr></wbr><span>Truck</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1237324894%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="forbidden-truck-type.html"><strike>forbiddenTruckType</strike></a><span class="token operator">: </span><a href="../../../com.here.sdk.transport/-truck-type/index.html">TruckType</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">This property will be set if a restriction applies to the value of <a href="../../../com.here.sdk.transport/-truck-type/index.html">com.here.sdk.transport.TruckType</a> parameter used for route calculation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2116903997%2FProperties%2F1617540583" anchor-label="maxHeightInCentimeters" id="-2116903997%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="max-height-in-centimeters.html"><span>max</span><wbr></wbr><span>Height</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Centimeters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2116903997%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="max-height-in-centimeters.html">maxHeightInCentimeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Max permitted height during the trip, in centimeters. This property will be set if the <a href="../../../com.here.sdk.transport/-vehicle-specification/height-in-centimeters.html">com.here.sdk.transport.VehicleSpecification.heightInCentimeters</a> exceeds this value.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1206095340%2FProperties%2F1617540583" anchor-label="maxKingpinToRearAxleDistanceInCentimeters" id="-1206095340%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="max-kingpin-to-rear-axle-distance-in-centimeters.html"><span>max</span><wbr></wbr><span>Kingpin</span><wbr></wbr><span>To</span><wbr></wbr><span>Rear</span><wbr></wbr><span>Axle</span><wbr></wbr><span>Distance</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Centimeters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1206095340%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="max-kingpin-to-rear-axle-distance-in-centimeters.html">maxKingpinToRearAxleDistanceInCentimeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Contains the maximum permitted distance from kingpin to the rear axle in centimeters. This property will be set if the <a href="../../../com.here.sdk.transport/-vehicle-specification/kingpin-to-rear-axle-distance-in-centimeters.html">com.here.sdk.transport.VehicleSpecification.kingpinToRearAxleDistanceInCentimeters</a> exceeds the specified value.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1541013058%2FProperties%2F1617540583" anchor-label="maxLengthInCentimeters" id="1541013058%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="max-length-in-centimeters.html"><span>max</span><wbr></wbr><span>Length</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Centimeters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1541013058%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="max-length-in-centimeters.html">maxLengthInCentimeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Max permitted length during the trip, in centimeters. This property will be set if the <a href="../../../com.here.sdk.transport/-vehicle-specification/length-in-centimeters.html">com.here.sdk.transport.VehicleSpecification.lengthInCentimeters</a> exceeds this value.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="969840343%2FProperties%2F1617540583" anchor-label="maxNumberOfTires" id="969840343%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="max-number-of-tires.html"><span>max</span><wbr></wbr><span>Number</span><wbr></wbr><span>Of</span><wbr></wbr><span><span>Tires</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="969840343%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="max-number-of-tires.html">maxNumberOfTires</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Contains the maximum permitted number of tires. This property will be set if the <a href="../../../com.here.sdk.transport/-vehicle-specification/tires-count.html">com.here.sdk.transport.VehicleSpecification.tiresCount</a> exceeds the specified value.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="922942186%2FProperties%2F1617540583" anchor-label="maxPayloadCapacityInKilograms" id="922942186%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="max-payload-capacity-in-kilograms.html"><span>max</span><wbr></wbr><span>Payload</span><wbr></wbr><span>Capacity</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilograms</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="922942186%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="max-payload-capacity-in-kilograms.html">maxPayloadCapacityInKilograms</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Max permitted payload capacity during the trip, in kilograms. This property will be set if the <a href="../../../com.here.sdk.transport/-vehicle-specification/payload-capacity-in-kilograms.html">com.here.sdk.transport.VehicleSpecification.payloadCapacityInKilograms</a> exceeds this value.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1440761358%2FProperties%2F1617540583" anchor-label="maxTunnelCategory" id="-1440761358%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="max-tunnel-category.html"><span>max</span><wbr></wbr><span>Tunnel</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1440761358%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="max-tunnel-category.html">maxTunnelCategory</a><span class="token operator">: </span><a href="../../../com.here.sdk.transport/-tunnel-category/index.html">TunnelCategory</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Tunnel category to restrict transport of specific goods during the trip. This property will be set if the <a href="../../../com.here.sdk.transport/-vehicle-specification/tunnel-category.html">com.here.sdk.transport.VehicleSpecification.tunnelCategory</a> from <a href="../../../com.here.sdk.transport/-transport-specification/vehicle-specification.html">com.here.sdk.transport.TransportSpecification.vehicleSpecification</a> from <a href="../../-routing-options/transport-specification.html">com.here.sdk.routing.RoutingOptions.transportSpecification</a> exceeds this value.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1822752832%2FProperties%2F1617540583" anchor-label="maxWeight" id="1822752832%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="max-weight.html"><span>max</span><wbr></wbr><span><span>Weight</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1822752832%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="max-weight.html">maxWeight</a><span class="token operator">: </span><a href="../../-vehicle-restriction-max-weight/index.html">VehicleRestrictionMaxWeight</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction. This property will be set if the <a href="../../../com.here.sdk.transport/-vehicle-specification/gross-weight-in-kilograms.html">com.here.sdk.transport.VehicleSpecification.grossWeightInKilograms</a> parameter used for route calculation exceeds this value.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-663192298%2FProperties%2F1617540583" anchor-label="maxWeightPerAxleGroupInKilograms" id="-663192298%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="max-weight-per-axle-group-in-kilograms.html"><span>max</span><wbr></wbr><span>Weight</span><wbr></wbr><span>Per</span><wbr></wbr><span>Axle</span><wbr></wbr><span>Group</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilograms</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-663192298%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="max-weight-per-axle-group-in-kilograms.html">maxWeightPerAxleGroupInKilograms</a><span class="token operator">: </span><a href="../../-max-axle-group-weight/index.html">MaxAxleGroupWeight</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Max permitted weight per axle group during the trip, in kilograms. This property will be set if the <a href="../../../com.here.sdk.transport/-vehicle-specification/weight-per-axle-group.html">com.here.sdk.transport.VehicleSpecification.weightPerAxleGroup</a> exceeds this value.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1960102953%2FProperties%2F1617540583" anchor-label="maxWeightPerAxleInKilograms" id="-1960102953%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="max-weight-per-axle-in-kilograms.html"><span>max</span><wbr></wbr><span>Weight</span><wbr></wbr><span>Per</span><wbr></wbr><span>Axle</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilograms</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1960102953%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="max-weight-per-axle-in-kilograms.html">maxWeightPerAxleInKilograms</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Max permitted weight per axle during the trip, in kilograms. This property will be set if the <a href="../../../com.here.sdk.transport/-vehicle-specification/weight-per-axle-in-kilograms.html">com.here.sdk.transport.VehicleSpecification.weightPerAxleInKilograms</a> exceeds this value.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="245393592%2FProperties%2F1617540583" anchor-label="maxWidthInCentimeters" id="245393592%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="max-width-in-centimeters.html"><span>max</span><wbr></wbr><span>Width</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Centimeters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="245393592%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="max-width-in-centimeters.html">maxWidthInCentimeters</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Max permitted width during the trip, in centimeters. This property will be set if the <a href="../../../com.here.sdk.transport/-vehicle-specification/width-in-centimeters.html">com.here.sdk.transport.VehicleSpecification.widthInCentimeters</a> exceeds this value.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1901480795%2FProperties%2F1617540583" anchor-label="routingZoneReference" id="-1901480795%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="routing-zone-reference.html"><span>routing</span><wbr></wbr><span>Zone</span><wbr></wbr><span><span>Reference</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1901480795%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="routing-zone-reference.html">routingZoneReference</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Contains the restricted routing zone reference This property will be set if the <a href="../../-avoidance-options/zone-categories.html">com.here.sdk.routing.AvoidanceOptions.zoneCategories</a> is not empty</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-849809771%2FProperties%2F1617540583" anchor-label="timeRule" id="-849809771%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="time-rule.html"><span>time</span><wbr></wbr><span><span>Rule</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-849809771%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="time-rule.html">timeRule</a><span class="token operator">: </span><a href="../../../com.here.sdk.core/-time-rule/index.html">TimeRule</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Time intervals during which restrictions are enforced.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-806092957%2FFunctions%2F1617540583" anchor-label="equals" id="-806092957%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="equals.html"><span><span>equals</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-806092957%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">operator override </span><span class="token keyword">fun </span><a href="equals.html"><span class="token function">equals</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">other<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1243069987%2FFunctions%2F1617540583" anchor-label="hashCode" id="1243069987%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="hash-code.html"><span>hash</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1243069987%2FFunctions%2F1617540583"></span>
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
