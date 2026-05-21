---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.search/EVChargingStation///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search/EVChargingStation</div>
<div class="cover">
<h1 class="cover">EVCharging<wbr/>Station</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station</div><p class="paragraph">Group of connectors for electric vehicles (EVs), defined by a common charging connector type and maximum power level.</p><p class="paragraph">Use /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-place-category-companion-b-u-s-i-n-e-s-s-a-n-d-s-e-r-v-i-c-e-s-e-v-c-h-a-r-g-i-n-g-s-t-a-t-i-o-n to find stations. In the <code class="lang-kotlin">Details</code> of a <code class="lang-kotlin">Place</code> result you can find the list of found pools containing stations, if any.</p><p class="paragraph">For offline EV rich attributes, enable /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-e-v in /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options-layer-configuration.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="EVChargingStation" data-filterable-set=":modules:dokkaHtml/release" data-name="1216456618%2FConstructors%2F1617540583" id="1216456618%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-e-v-charging-station</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Creates a new instance.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="availableConnectorCount" data-filterable-set=":modules:dokkaHtml/release" data-name="67831601%2FProperties%2F1617540583" id="67831601%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-available-connector-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-available-connector-count: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Number of available physical connectors at the charging station. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="chargingMode" data-filterable-set=":modules:dokkaHtml/release" data-name="1382032106%2FProperties%2F1617540583" id="1382032106%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-charging-mode</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-charging-mode: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">Charging mode of the charging station. For more information, see https://en.wikipedia.org/w/index.php?title=Charging_station&amp;oldid=1013010605#IEC-61851-1_Charging_Modes standard. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="connectorCount" data-filterable-set=":modules:dokkaHtml/release" data-name="1424889180%2FProperties%2F1617540583" id="1424889180%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-connector-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-connector-count: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Number of physical connectors at the charging station. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="connectorTypeId" data-filterable-set=":modules:dokkaHtml/release" data-name="237065562%2FProperties%2F1617540583" id="237065562%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-connector-type-id</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-connector-type-id: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">ID of the connector type. For more information on the current connector types, see https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="connectorTypeName" data-filterable-set=":modules:dokkaHtml/release" data-name="1088008170%2FProperties%2F1617540583" id="1088008170%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-connector-type-name</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-connector-type-name: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">Name of the connector type. For more information on the current connector types, see https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html May include customer-facing names. In such cases, a 'customer names' label is present. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="currentRangeInAmperes" data-filterable-set=":modules:dokkaHtml/release" data-name="445926182%2FProperties%2F1617540583" id="445926182%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-current-range-in-amperes</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-current-range-in-amperes: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">Current range provided by the charging station, in amperes. Values are alphanumeric represented by the Ampere value followed by an 'A', for example '12A-80A'. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hasFixedCable" data-filterable-set=":modules:dokkaHtml/release" data-name="1363363193%2FProperties%2F1617540583" id="1363363193%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-has-fixed-cable</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-has-fixed-cable: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>?</div><div class="brief"><p class="paragraph">Indicates that the cable is fixed or not fixed for a specific Connector Type on the charge station. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="lastUpdated" data-filterable-set=":modules:dokkaHtml/release" data-name="1275923863%2FProperties%2F1617540583" id="1275923863%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-last-updated</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-last-updated: <a href="https://developer.android.com/reference/kotlin/java/util/Date.html">Date</a>?</div><div class="brief"><p class="paragraph">Last update of the <code class="lang-kotlin">available_connector_count</code> and <code class="lang-kotlin">occupied_connector_count</code> fields. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxPowerInKilowatts" data-filterable-set=":modules:dokkaHtml/release" data-name="-385057094%2FProperties%2F1617540583" id="-385057094%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-max-power-in-kilowatts</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-max-power-in-kilowatts: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>?</div><div class="brief"><p class="paragraph">Maximum charge power of connectors in kW. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="occupiedConnectorCount" data-filterable-set=":modules:dokkaHtml/release" data-name="-1719041058%2FProperties%2F1617540583" id="-1719041058%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-occupied-connector-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-occupied-connector-count: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Number of occupied physical connectors at the charging station. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="outOfServiceConnectorCount" data-filterable-set=":modules:dokkaHtml/release" data-name="-575544180%2FProperties%2F1617540583" id="-575544180%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-out-of-service-connector-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-out-of-service-connector-count: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Number of physical connectors that are out of service at the charging station. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="phaseCount" data-filterable-set=":modules:dokkaHtml/release" data-name="-1567383926%2FProperties%2F1617540583" id="-1567383926%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-phase-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-phase-count: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Number of phases used by the charging station. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="physicalReference" data-filterable-set=":modules:dokkaHtml/release" data-name="-1776026040%2FProperties%2F1617540583" id="-1776026040%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-physical-reference</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-physical-reference: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">Printed on the outside of the EVSE for visual identification. Available only in offline search. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="powerFeedTypeId" data-filterable-set=":modules:dokkaHtml/release" data-name="-2073922908%2FProperties%2F1617540583" id="-2073922908%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-power-feed-type-id</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-power-feed-type-id: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">ID of the power feed type, as defined by the https://en.wikipedia.org/wiki/SAE_J1772#Charging standard. No data in case of offline search. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="powerFeedTypeName" data-filterable-set=":modules:dokkaHtml/release" data-name="726180532%2FProperties%2F1617540583" id="726180532%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-power-feed-type-name</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-power-feed-type-name: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">Name of the power feed type, as defined by the https://en.wikipedia.org/wiki/SAE_J1772#Charging standard. Provides the customer information on the charge level of the specific Connector Type. Also, can describe level that is used in North America and Australia. In that case label 'North America (Australia)' is present. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="reservedConnectorCount" data-filterable-set=":modules:dokkaHtml/release" data-name="315831316%2FProperties%2F1617540583" id="315831316%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-reserved-connector-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-reserved-connector-count: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Number of physical connectors that are reserved at the charging station. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online searches using the <code class="lang-kotlin">SearchEngine</code>, it may be <code class="lang-kotlin">null</code> if the data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="supplierName" data-filterable-set=":modules:dokkaHtml/release" data-name="-1028324985%2FProperties%2F1617540583" id="-1028324985%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-supplier-name</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-supplier-name: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">The EV charging station operator. This field is always <code class="lang-kotlin">null</code> for offline search using the <code class="lang-kotlin">OfflineSearchEngine</code>. For online search using the <code class="lang-kotlin">SearchEngine</code>, it can be null if data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="voltageRangeInVolts" data-filterable-set=":modules:dokkaHtml/release" data-name="-2111492850%2FProperties%2F1617540583" id="-2111492850%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-voltage-range-in-volts</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-voltage-range-in-volts: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">Voltage range of the charge provided by the charging station, in volts. Values are alphanumeric represented by the voltage range followed by 'V' and by the current type 'AC' or 'DC', for example: '100-120V AC'. This field can be <code class="lang-kotlin">null</code> if data is unavailable.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="1765123235%2FFunctions%2F1617540583" id="1765123235%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="1907044579%2FFunctions%2F1617540583" id="1907044579%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-station-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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
<a class="footer--button footer--button_go-to-top" href="#content" id="go-to-top-link"></a>
© 2026 Copyright

Generated by 
<a class="footer--link footer--link_external" href="https://github.com/Kotlin/dokka">
dokka
</a>

</div>
</div>

</div>

</div>
`
}</HTMLBlock>
