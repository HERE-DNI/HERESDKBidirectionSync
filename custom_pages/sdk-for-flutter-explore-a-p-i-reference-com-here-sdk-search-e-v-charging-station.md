---
title: "EVChargingStation"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>EVChargingStation</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.search/EVChargingStation///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.search</a><span class="delimiter">/</span><span class="current">EVChargingStation</span></div>
  <div class="cover ">
    <h1 class="cover"><span>EVCharging</span><wbr></wbr><span><span>Station</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">EVChargingStation</a></div><p class="paragraph">Group of connectors for electric vehicles (EVs), defined by a common charging connector type and maximum power level.</p><p class="paragraph">Use <a href="../-place-category/-companion/-b-u-s-i-n-e-s-s_-a-n-d_-s-e-r-v-i-c-e-s_-e-v_-c-h-a-r-g-i-n-g_-s-t-a-t-i-o-n.html">com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_EV_CHARGING_STATION</a> to find stations. In the <code class="lang-kotlin">Details</code> of a <code class="lang-kotlin">Place</code> result you can find the list of found pools containing stations, if any.</p><p class="paragraph">For offline EV rich attributes, enable <a href="../../com.here.sdk.core.engine/-layer-configuration/-feature/-e-v/index.html">com.here.sdk.core.engine.LayerConfiguration.Feature.EV</a> in <a href="../../com.here.sdk.core.engine/-s-d-k-options/layer-configuration.html">com.here.sdk.core.engine.SDKOptions.layerConfiguration</a>.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="1216456618%2FConstructors%2F1617540583" anchor-label="EVChargingStation" id="1216456618%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-v-charging-station.html"><span>EVCharging</span><wbr></wbr><span><span>Station</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1216456618%2FConstructors%2F1617540583"></span>
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
        <div class="table"><a data-name="67831601%2FProperties%2F1617540583" anchor-label="availableConnectorCount" id="67831601%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="available-connector-count.html"><span>available</span><wbr></wbr><span>Connector</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="67831601%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="available-connector-count.html">availableConnectorCount</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Number of available physical connectors at the charging station. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1382032106%2FProperties%2F1617540583" anchor-label="chargingMode" id="1382032106%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="charging-mode.html"><span>charging</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1382032106%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="charging-mode.html">chargingMode</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Charging mode of the charging station. For more information, see https://en.wikipedia.org/w/index.php?title=Charging_station&oldid=1013010605#IEC-61851-1_Charging_Modes standard. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1424889180%2FProperties%2F1617540583" anchor-label="connectorCount" id="1424889180%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="connector-count.html"><span>connector</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1424889180%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="connector-count.html">connectorCount</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Number of physical connectors at the charging station. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="237065562%2FProperties%2F1617540583" anchor-label="connectorTypeId" id="237065562%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="connector-type-id.html"><span>connector</span><wbr></wbr><span>Type</span><wbr></wbr><span><span>Id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="237065562%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="connector-type-id.html">connectorTypeId</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">ID of the connector type. For more information on the current connector types, see https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1088008170%2FProperties%2F1617540583" anchor-label="connectorTypeName" id="1088008170%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="connector-type-name.html"><span>connector</span><wbr></wbr><span>Type</span><wbr></wbr><span><span>Name</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1088008170%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="connector-type-name.html">connectorTypeName</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Name of the connector type. For more information on the current connector types, see https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html May include customer-facing names. In such cases, a 'customer names' label is present. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="445926182%2FProperties%2F1617540583" anchor-label="currentRangeInAmperes" id="445926182%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="current-range-in-amperes.html"><span>current</span><wbr></wbr><span>Range</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Amperes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="445926182%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="current-range-in-amperes.html">currentRangeInAmperes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Current range provided by the charging station, in amperes. Values are alphanumeric represented by the Ampere value followed by an 'A', for example '12A-80A'. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1363363193%2FProperties%2F1617540583" anchor-label="hasFixedCable" id="1363363193%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="has-fixed-cable.html"><span>has</span><wbr></wbr><span>Fixed</span><wbr></wbr><span><span>Cable</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1363363193%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="has-fixed-cable.html">hasFixedCable</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Indicates that the cable is fixed or not fixed for a specific Connector Type on the charge station. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1275923863%2FProperties%2F1617540583" anchor-label="lastUpdated" id="1275923863%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="last-updated.html"><span>last</span><wbr></wbr><span><span>Updated</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1275923863%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="last-updated.html">lastUpdated</a><span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Last update of the <code class="lang-kotlin">available_connector_count</code> and <code class="lang-kotlin">occupied_connector_count</code> fields. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-385057094%2FProperties%2F1617540583" anchor-label="maxPowerInKilowatts" id="-385057094%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="max-power-in-kilowatts.html"><span>max</span><wbr></wbr><span>Power</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilowatts</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-385057094%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="max-power-in-kilowatts.html">maxPowerInKilowatts</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Maximum charge power of connectors in kW. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1719041058%2FProperties%2F1617540583" anchor-label="occupiedConnectorCount" id="-1719041058%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="occupied-connector-count.html"><span>occupied</span><wbr></wbr><span>Connector</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1719041058%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="occupied-connector-count.html">occupiedConnectorCount</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Number of occupied physical connectors at the charging station. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-575544180%2FProperties%2F1617540583" anchor-label="outOfServiceConnectorCount" id="-575544180%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="out-of-service-connector-count.html"><span>out</span><wbr></wbr><span>Of</span><wbr></wbr><span>Service</span><wbr></wbr><span>Connector</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-575544180%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="out-of-service-connector-count.html">outOfServiceConnectorCount</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Number of physical connectors that are out of service at the charging station. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1567383926%2FProperties%2F1617540583" anchor-label="phaseCount" id="-1567383926%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="phase-count.html"><span>phase</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1567383926%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="phase-count.html">phaseCount</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Number of phases used by the charging station. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1776026040%2FProperties%2F1617540583" anchor-label="physicalReference" id="-1776026040%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="physical-reference.html"><span>physical</span><wbr></wbr><span><span>Reference</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1776026040%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="physical-reference.html">physicalReference</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Printed on the outside of the EVSE for visual identification. Available only in offline search. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2073922908%2FProperties%2F1617540583" anchor-label="powerFeedTypeId" id="-2073922908%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="power-feed-type-id.html"><span>power</span><wbr></wbr><span>Feed</span><wbr></wbr><span>Type</span><wbr></wbr><span><span>Id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2073922908%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="power-feed-type-id.html">powerFeedTypeId</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">ID of the power feed type, as defined by the https://en.wikipedia.org/wiki/SAE_J1772#Charging standard. No data in case of offline search. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="726180532%2FProperties%2F1617540583" anchor-label="powerFeedTypeName" id="726180532%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="power-feed-type-name.html"><span>power</span><wbr></wbr><span>Feed</span><wbr></wbr><span>Type</span><wbr></wbr><span><span>Name</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="726180532%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="power-feed-type-name.html">powerFeedTypeName</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Name of the power feed type, as defined by the https://en.wikipedia.org/wiki/SAE_J1772#Charging standard. Provides the customer information on the charge level of the specific Connector Type. Also, can describe level that is used in North America and Australia. In that case label 'North America (Australia)' is present. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="315831316%2FProperties%2F1617540583" anchor-label="reservedConnectorCount" id="315831316%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="reserved-connector-count.html"><span>reserved</span><wbr></wbr><span>Connector</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="315831316%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="reserved-connector-count.html">reservedConnectorCount</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Number of physical connectors that are reserved at the charging station. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1028324985%2FProperties%2F1617540583" anchor-label="supplierName" id="-1028324985%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="supplier-name.html"><span>supplier</span><wbr></wbr><span><span>Name</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1028324985%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="supplier-name.html">supplierName</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The EV charging station operator. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online search using the <code class="lang-kotlin">SearchEngine</code>, it can be null if data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2111492850%2FProperties%2F1617540583" anchor-label="voltageRangeInVolts" id="-2111492850%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="voltage-range-in-volts.html"><span>voltage</span><wbr></wbr><span>Range</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Volts</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2111492850%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="voltage-range-in-volts.html">voltageRangeInVolts</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Voltage range of the charge provided by the charging station, in volts. Values are alphanumeric represented by the voltage range followed by 'V' and by the current type 'AC' or 'DC', for example: '100-120V AC'. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="1765123235%2FFunctions%2F1617540583" anchor-label="equals" id="1765123235%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="equals.html"><span><span>equals</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1765123235%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">operator override </span><span class="token keyword">fun </span><a href="equals.html"><span class="token function">equals</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">other<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1907044579%2FFunctions%2F1617540583" anchor-label="hashCode" id="1907044579%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="hash-code.html"><span>hash</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1907044579%2FFunctions%2F1617540583"></span>
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
