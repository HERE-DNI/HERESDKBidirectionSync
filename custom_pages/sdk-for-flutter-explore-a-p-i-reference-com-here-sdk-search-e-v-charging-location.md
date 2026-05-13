---
title: "EVChargingLocation"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>EVChargingLocation</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.search/EVChargingLocation///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.search</a><span class="delimiter">/</span><span class="current">EVChargingLocation</span></div>
  <div class="cover ">
    <h1 class="cover"><span>EVCharging</span><wbr></wbr><span><span>Location</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">EVChargingLocation</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">An electric vehicle (EV) charging location.</p><p class="paragraph">The semantics generally follow the OCPI 2.2.1 standard.</p><p class="paragraph">Known EV-specific acronyms:</p><ul><li><p class="paragraph">EV: Electric Vehicle</p></li><li><p class="paragraph">OCPI: Open Charge Point Interface (a standard with a rather wide adoption worldwide, https://evroaming.org/)</p></li><li><p class="paragraph">CPO: Charge Point Operator (company that runs the EV charging location)</p></li><li><p class="paragraph">eMSP: e-Mobility Service Provider (customer-facing company)</p></li><li><p class="paragraph">EVSE: Electric Vehicle Supply Equipment (the actual charger that can charge one car at a time)</p></li></ul><p class="paragraph">A charging location includes a collection of one or more EV supply equipment (EVSE) instances. Typically, the charging location is the exact location of the group of EVSEs, simplified to a single point, but it can also be the entrance of a parking structure which contains these EVSEs. Each EVSE supports more precise position, where applicable.</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-1043925606%2FClasslikes%2F1617540583" anchor-label="Companion" id="-1043925606%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1043925606%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="433304178%2FProperties%2F1617540583" anchor-label="connectorGroups" id="433304178%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="connector-groups.html"><span>connector</span><wbr></wbr><span><span>Groups</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="433304178%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="connector-groups.html">connectorGroups</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-e-v-charging-connector-group/index.html">EVChargingConnectorGroup</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Connector groups for the location. Provides an overview of the charging connectors in the location by type and power. Available only if <code class="lang-kotlin">EVChargingLocationFeature.CONNECTOR_GROUPS</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise empty.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1523729334%2FProperties%2F1617540583" anchor-label="cpoID" id="1523729334%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="cpo-i-d.html"><span>cpo</span><wbr></wbr><span><span>ID</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1523729334%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="cpo-i-d.html">cpoID</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">CPO's own ID for the location. This ID may be relevant for some clients to map the charging location data to their own or 3rd party systems. Available only if <code class="lang-kotlin">EVChargingLocationFeature.LOCATION_INFO</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1383176138%2FProperties%2F1617540583" anchor-label="eMobilityServiceProviders" id="-1383176138%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="e-mobility-service-providers.html"><span>e</span><wbr></wbr><span>Mobility</span><wbr></wbr><span>Service</span><wbr></wbr><span><span>Providers</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1383176138%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="e-mobility-service-providers.html">eMobilityServiceProviders</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-e-v-charging-operator/index.html">EVChargingOperator</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">eMSPs with a roaming agreement enabling access to the EV charging location. Available only if <code class="lang-kotlin">EVChargingLocationFeature.EMSPS</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise empty.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="259115039%2FProperties%2F1617540583" anchor-label="energyMix" id="259115039%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="energy-mix.html"><span>energy</span><wbr></wbr><span><span>Mix</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="259115039%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="energy-mix.html">energyMix</a><span class="token operator">: </span><a href="../-energy-mix/index.html">EnergyMix</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Details on the energy supplied at the charging location. Available only if <code class="lang-kotlin">EVChargingLocationFeature.LOCATION_INFO</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-39566943%2FProperties%2F1617540583" anchor-label="evChargingOperator" id="-39566943%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="ev-charging-operator.html"><span>ev</span><wbr></wbr><span>Charging</span><wbr></wbr><span><span>Operator</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-39566943%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="ev-charging-operator.html">evChargingOperator</a><span class="token operator">: </span><a href="../-e-v-charging-operator/index.html">EVChargingOperator</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Operator of the charging point, if available.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1573346767%2FProperties%2F1617540583" anchor-label="evChargingSubOperator" id="-1573346767%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="ev-charging-sub-operator.html"><span>ev</span><wbr></wbr><span>Charging</span><wbr></wbr><span>Sub</span><wbr></wbr><span><span>Operator</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1573346767%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="ev-charging-sub-operator.html">evChargingSubOperator</a><span class="token operator">: </span><a href="../-e-v-charging-operator/index.html">EVChargingOperator</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Suboperator of the charging point, if available.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1290589373%2FProperties%2F1617540583" anchor-label="evses" id="-1290589373%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="evses.html"><span><span>evses</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1290589373%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="evses.html">evses</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-e-v-s-e-info/index.html">EVSEInfo</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">List of EVSEs at the charging station. Available only if <code class="lang-kotlin">EVChargingLocationFeature.EVSES</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise empty.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="745002621%2FProperties%2F1617540583" anchor-label="facilityTypes" id="745002621%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="facility-types.html"><span>facility</span><wbr></wbr><span><span>Types</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="745002621%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="facility-types.html">facilityTypes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-facility-type/index.html">FacilityType</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Facilities available at the charging location, for example hotel, wifi, parking lot etc. Available only if <code class="lang-kotlin">EVChargingLocationFeature.NEARBY</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise empty.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-138717396%2FProperties%2F1617540583" anchor-label="id" id="-138717396%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="id.html"><span><span>id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-138717396%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@get:</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-name/index.html"><span class="token annotation builtin">JvmName</span></a><span class="token punctuation">(</span><span>name<span class="token operator"> = </span><span class="breakable-word"><span class="token string">&quot;getID&quot;</span></span></span><wbr></wbr><span class="token punctuation">)</span></div></div><span class="token keyword">val </span><a href="id.html">id</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">A unique identifier of the charging location.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="737838396%2FProperties%2F1617540583" anchor-label="name" id="737838396%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="name.html"><span><span>name</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="737838396%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="name.html">name</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Display name of the charging location, if available.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2138619216%2FProperties%2F1617540583" anchor-label="openingHours" id="-2138619216%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="opening-hours.html"><span>opening</span><wbr></wbr><span><span>Hours</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2138619216%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="opening-hours.html">openingHours</a><span class="token operator">: </span><a href="../-e-v-charging-opening-hours/index.html">EVChargingOpeningHours</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The times when the EVSEs at the charging location can be accessed for charging. Available only if <code class="lang-kotlin">EVChargingLocationFeature.LOCATION_INFO</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="407401473%2FProperties%2F1617540583" anchor-label="parkingType" id="407401473%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="parking-type.html"><span>parking</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="407401473%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="parking-type.html">parkingType</a><span class="token operator">: </span><a href="../-parking-type/index.html">ParkingType</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The type of parking at the charging location. Available only if <code class="lang-kotlin">EVChargingLocationFeature.LOCATION_INFO</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-687515872%2FProperties%2F1617540583" anchor-label="restrictions" id="-687515872%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="restrictions.html"><span><span>restrictions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-687515872%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="restrictions.html">restrictions</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-e-v-access-restriction-reason/index.html">EVAccessRestrictionReason</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Reason(s) for restricted access.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1120513630%2FProperties%2F1617540583" anchor-label="supportedVehicles" id="1120513630%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="supported-vehicles.html"><span>supported</span><wbr></wbr><span><span>Vehicles</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1120513630%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="supported-vehicles.html">supportedVehicles</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-e-v-charging-vehicle-category/index.html">EVChargingVehicleCategory</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">List of vehicle categories this charging location can support. For example, the same location can be suitable for charging passenger cars and motorcycles. There may be some further restrictions specified in other attributes, for example the available connector types may not be suitable for all vehicles in the supported category.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1548036575%2FProperties%2F1617540583" anchor-label="supportPhoneNumber" id="1548036575%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="support-phone-number.html"><span>support</span><wbr></wbr><span>Phone</span><wbr></wbr><span><span>Number</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1548036575%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="support-phone-number.html">supportPhoneNumber</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The phone number that EV drivers should call when need assistance at the charge location, in E.164 format. Available only if <code class="lang-kotlin">EVChargingLocationFeature.LOCATION_INFO</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1427292956%2FProperties%2F1617540583" anchor-label="tariffs" id="-1427292956%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="tariffs.html"><span><span>tariffs</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1427292956%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="tariffs.html">tariffs</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-e-v-charging-tariff/index.html">EVChargingTariff</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">List of tariffs or price plans for the connectors of the charging station. Tariffs are typically connector-type specific. Hence, they are always linked with connectors and/or connector groups, by indexes to this list.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="897292910%2FProperties%2F1617540583" anchor-label="timeZone" id="897292910%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="time-zone.html"><span>time</span><wbr></wbr><span><span>Zone</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="897292910%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="time-zone.html">timeZone</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The time zone of the charging location. Based on IANA tzdata's TZ-values. Available only if <code class="lang-kotlin">EVChargingLocationFeature.LOCATION_INFO</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="471475437%2FProperties%2F1617540583" anchor-label="truckRestrictions" id="471475437%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="truck-restrictions.html"><span>truck</span><wbr></wbr><span><span>Restrictions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="471475437%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="truck-restrictions.html">truckRestrictions</a><span class="token operator">: </span><a href="../-e-v-charging-truck-restriction/index.html">EVChargingTruckRestriction</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Access restrictions for trucks and light commercial vehicles. Restricted, only available to customers having a specific contract with HERE and if requested by including <code class="lang-kotlin">EVChargingLocationFeature.TRUCK_RESTRICTIONS</code> in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
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
