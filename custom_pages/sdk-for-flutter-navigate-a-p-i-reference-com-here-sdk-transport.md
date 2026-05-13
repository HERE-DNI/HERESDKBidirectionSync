---
title: "com.here.sdk.transport"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-transport"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>com.here.sdk.transport</title>
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
<div class="main-content" data-page-type="package" id="content" pageIds="API Reference::com.here.sdk.transport////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../index.html">API Reference</a><span class="delimiter">/</span><span class="current">com.here.sdk.transport</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Package-level</span></span> <span><span>declarations</span></span></h1>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="TYPE">Types</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="847547980%2FClasslikes%2F1617540583" anchor-label="BusSpecifications" id="847547980%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-bus-specifications/index.html"><span>Bus</span><wbr></wbr><span><span>Specifications</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="847547980%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-bus-specifications/index.html"><strike>BusSpecifications</strike></a></div><div class="brief "><p class="paragraph">Bus specifications contain vehicle related attributes. Examples: height, weight, width. Only the fields that are set are considered for restriction handling.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-431458696%2FClasslikes%2F1617540583" anchor-label="CarSpecifications" id="-431458696%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-car-specifications/index.html"><span>Car</span><wbr></wbr><span><span>Specifications</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-431458696%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-car-specifications/index.html"><strike>CarSpecifications</strike></a></div><div class="brief "><p class="paragraph">Car specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1234016714%2FClasslikes%2F1617540583" anchor-label="FuelAdditiveType" id="1234016714%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-fuel-additive-type/index.html"><span>Fuel</span><wbr></wbr><span>Additive</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1234016714%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-fuel-additive-type/index.html">FuelAdditiveType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-fuel-additive-type/index.html">FuelAdditiveType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Defines possible fuel additives that a fuel could contain.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1256239414%2FClasslikes%2F1617540583" anchor-label="FuelType" id="1256239414%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-fuel-type/index.html"><span>Fuel</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1256239414%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-fuel-type/index.html">FuelType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-fuel-type/index.html">FuelType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Defines possible fuel types provided by a fuel station.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1103349921%2FClasslikes%2F1617540583" anchor-label="GeneralVehicleSpeedLimits" id="1103349921%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-general-vehicle-speed-limits/index.html"><span>General</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span>Speed</span><wbr></wbr><span><span>Limits</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1103349921%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-general-vehicle-speed-limits/index.html">GeneralVehicleSpeedLimits</a></div><div class="brief "><p class="paragraph">Contains the speed limits for vehicles in a country / state.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1493370042%2FClasslikes%2F1617540583" anchor-label="HazardousMaterial" id="1493370042%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-hazardous-material/index.html"><span>Hazardous</span><wbr></wbr><span><span>Material</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1493370042%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-hazardous-material/index.html">HazardousMaterial</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-hazardous-material/index.html">HazardousMaterial</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Identifiers for different types of hazardous materials which can be shipped by the truck.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-230103588%2FClasslikes%2F1617540583" anchor-label="HazardousMaterialRestriction" id="-230103588%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-hazardous-material-restriction/index.html"><span>Hazardous</span><wbr></wbr><span>Material</span><wbr></wbr><span><span>Restriction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-230103588%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-hazardous-material-restriction/index.html">HazardousMaterialRestriction</a></div><div class="brief "><p class="paragraph">Represents restriction on transport of hazardous materials. A generic restriction, applying to any hazardous material, is encoded with empty member variables.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1620609548%2FClasslikes%2F1617540583" anchor-label="PedestrianSpecification" id="-1620609548%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-pedestrian-specification/index.html"><span>Pedestrian</span><wbr></wbr><span><span>Specification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1620609548%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-pedestrian-specification/index.html">PedestrianSpecification</a></div><div class="brief "><p class="paragraph">Pedestrian specific settings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1666218218%2FClasslikes%2F1617540583" anchor-label="RestrictionType" id="-1666218218%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-restriction-type/index.html"><span>Restriction</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1666218218%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-restriction-type/index.html">RestrictionType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-restriction-type/index.html">RestrictionType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Type of vehicle restriction.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1053406068%2FClasslikes%2F1617540583" anchor-label="ScooterSpecification" id="1053406068%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-scooter-specification/index.html"><span>Scooter</span><wbr></wbr><span><span>Specification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1053406068%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-scooter-specification/index.html">ScooterSpecification</a></div><div class="brief "><p class="paragraph">Scooter specific settings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="492632578%2FClasslikes%2F1617540583" anchor-label="SpecificRestriction" id="492632578%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-specific-restriction/index.html"><span>Specific</span><wbr></wbr><span><span>Restriction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="492632578%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-specific-restriction/index.html">SpecificRestriction</a></div><div class="brief "><p class="paragraph">Represents a specific vehicle restriction. A <code class="lang-kotlin">SpecificRestriction</code> defines what type of restriction applies (weight, height, etc.) and the range of allowed values. It is always used as part of a <code class="lang-kotlin">VehicleRestriction</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-475812137%2FClasslikes%2F1617540583" anchor-label="TaxiSpecification" id="-475812137%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-taxi-specification/index.html"><span>Taxi</span><wbr></wbr><span><span>Specification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-475812137%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-taxi-specification/index.html">TaxiSpecification</a></div><div class="brief "><p class="paragraph">Taxi specific settings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-403861603%2FClasslikes%2F1617540583" anchor-label="TimeRestriction" id="-403861603%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-time-restriction/index.html"><span>Time</span><wbr></wbr><span><span>Restriction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-403861603%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-time-restriction/index.html">TimeRestriction</a></div><div class="brief "><p class="paragraph">Represents restriction based on time.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1857282384%2FClasslikes%2F1617540583" anchor-label="TransportMode" id="1857282384%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transport-mode/index.html"><span>Transport</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1857282384%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-transport-mode/index.html">TransportMode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-transport-mode/index.html">TransportMode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies the mode of transport used for route calculalation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1265083756%2FClasslikes%2F1617540583" anchor-label="TransportSpecification" id="1265083756%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transport-specification/index.html"><span>Transport</span><wbr></wbr><span><span>Specification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1265083756%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-transport-specification/index.html">TransportSpecification</a></div><div class="brief "><p class="paragraph">Contains transport attributes details related to the transport mode. <strong>Notes</strong></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1478872167%2FClasslikes%2F1617540583" anchor-label="TransportType" id="-1478872167%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-transport-type/index.html"><span>Transport</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1478872167%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-transport-type/index.html">TransportType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-transport-type/index.html">TransportType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies types of transportation for which access/restriction rules apply.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="922779743%2FClasslikes%2F1617540583" anchor-label="TruckCategory" id="922779743%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-truck-category/index.html"><span>Truck</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="922779743%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-truck-category/index.html">TruckCategory</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-truck-category/index.html">TruckCategory</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies the truck category. <strong>Note:</strong> This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-889213491%2FClasslikes%2F1617540583" anchor-label="TruckClass" id="-889213491%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-truck-class/index.html"><span>Truck</span><wbr></wbr><span><span>Class</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-889213491%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-truck-class/index.html">TruckClass</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-truck-class/index.html">TruckClass</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Defines truck class based on weight. Note: This is a BETA feature and thus subject to change.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-553559155%2FClasslikes%2F1617540583" anchor-label="TruckFuelType" id="-553559155%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-truck-fuel-type/index.html"><span>Truck</span><wbr></wbr><span>Fuel</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-553559155%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-truck-fuel-type/index.html">TruckFuelType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-truck-fuel-type/index.html">TruckFuelType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Define possible fuel types for trucks provided by a fuel station. Note: This is a BETA feature and thus subject to change.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="989081187%2FClasslikes%2F1617540583" anchor-label="TruckRoadType" id="989081187%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-truck-road-type/index.html"><span>Truck</span><wbr></wbr><span>Road</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="989081187%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-truck-road-type/index.html">TruckRoadType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-truck-road-type/index.html">TruckRoadType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies Truck road type</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1655632691%2FClasslikes%2F1617540583" anchor-label="TruckSpecifications" id="-1655632691%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-truck-specifications/index.html"><span>Truck</span><wbr></wbr><span><span>Specifications</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1655632691%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-truck-specifications/index.html"><strike>TruckSpecifications</strike></a></div><div class="brief "><p class="paragraph">Truck specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1672216669%2FClasslikes%2F1617540583" anchor-label="TruckType" id="-1672216669%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-truck-type/index.html"><span>Truck</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1672216669%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-truck-type/index.html"><strike>TruckType</strike></a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-truck-type/index.html">TruckType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies the type of truck.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1487933120%2FClasslikes%2F1617540583" anchor-label="TunnelCategory" id="1487933120%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-tunnel-category/index.html"><span>Tunnel</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1487933120%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-tunnel-category/index.html">TunnelCategory</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-tunnel-category/index.html">TunnelCategory</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Specifies the tunnel categories.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1980461239%2FClasslikes%2F1617540583" anchor-label="VehicleProfile" id="-1980461239%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-vehicle-profile/index.html"><span>Vehicle</span><wbr></wbr><span><span>Profile</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1980461239%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-vehicle-profile/index.html"><strike>VehicleProfile</strike></a></div><div class="brief "><p class="paragraph">A vehicle profile describes the vehicle being used with the HSDK.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-866096634%2FClasslikes%2F1617540583" anchor-label="VehicleRestriction" id="-866096634%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-vehicle-restriction/index.html"><span>Vehicle</span><wbr></wbr><span><span>Restriction</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-866096634%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-vehicle-restriction/index.html">VehicleRestriction</a></div><div class="brief "><p class="paragraph">Represents a vehicle restriction.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-109202321%2FClasslikes%2F1617540583" anchor-label="VehicleSpecification" id="-109202321%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-vehicle-specification/index.html"><span>Vehicle</span><wbr></wbr><span><span>Specification</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-109202321%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-vehicle-specification/index.html">VehicleSpecification</a></div><div class="brief "><p class="paragraph">Contains vehicle related attributes. Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-249715402%2FClasslikes%2F1617540583" anchor-label="VehicleType" id="-249715402%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-vehicle-type/index.html"><span>Vehicle</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-249715402%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-vehicle-type/index.html"><strike>VehicleType</strike></a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-vehicle-type/index.html">VehicleType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Defines the type of the vehicle.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-504293412%2FClasslikes%2F1617540583" anchor-label="WeightPerAxleGroup" id="-504293412%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-weight-per-axle-group/index.html"><span>Weight</span><wbr></wbr><span>Per</span><wbr></wbr><span>Axle</span><wbr></wbr><span><span>Group</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-504293412%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-weight-per-axle-group/index.html">WeightPerAxleGroup</a></div><div class="brief "><p class="paragraph">Struct which defines the weight of the different axle groups of a vehicle. The provided value must be greater or equal to 0.</p></div></div></div>
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
