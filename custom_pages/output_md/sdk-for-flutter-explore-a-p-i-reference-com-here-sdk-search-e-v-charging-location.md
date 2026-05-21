---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.search/EVChargingLocation///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search/EVChargingLocation</div>
<div class="cover">
<h1 class="cover">EVCharging<wbr/>Location</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">An electric vehicle (EV) charging location.</p><p class="paragraph">The semantics generally follow the OCPI 2.2.1 standard.</p><p class="paragraph">Known EV-specific acronyms:</p><ul><li><p class="paragraph">EV: Electric Vehicle</p></li><li><p class="paragraph">OCPI: Open Charge Point Interface (a standard with a rather wide adoption worldwide, https://evroaming.org/)</p></li><li><p class="paragraph">CPO: Charge Point Operator (company that runs the EV charging location)</p></li><li><p class="paragraph">eMSP: e-Mobility Service Provider (customer-facing company)</p></li><li><p class="paragraph">EVSE: Electric Vehicle Supply Equipment (the actual charger that can charge one car at a time)</p></li></ul><p class="paragraph">A charging location includes a collection of one or more EV supply equipment (EVSE) instances. Typically, the charging location is the exact location of the group of EVSEs, simplified to a single point, but it can also be the entrance of a parking structure which contains these EVSEs. Each EVSE supports more precise position, where applicable.</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-1043925606%2FClasslikes%2F1617540583" id="-1043925606%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="connectorGroups" data-filterable-set=":modules:dokkaHtml/release" data-name="433304178%2FProperties%2F1617540583" id="433304178%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-connector-groups</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-connector-groups: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-connector-group&gt;</div><div class="brief"><p class="paragraph">Connector groups for the location. Provides an overview of the charging connectors in the location by type and power. Available only if <code class="lang-kotlin">EVChargingLocationFeature.CONNECTOR_GROUPS</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise empty.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="cpoID" data-filterable-set=":modules:dokkaHtml/release" data-name="1523729334%2FProperties%2F1617540583" id="1523729334%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-cpo-i-d</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-cpo-i-d: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">CPO's own ID for the location. This ID may be relevant for some clients to map the charging location data to their own or 3rd party systems. Available only if <code class="lang-kotlin">EVChargingLocationFeature.LOCATION_INFO</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="eMobilityServiceProviders" data-filterable-set=":modules:dokkaHtml/release" data-name="-1383176138%2FProperties%2F1617540583" id="-1383176138%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-e-mobility-service-providers</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-e-mobility-service-providers: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-operator&gt;</div><div class="brief"><p class="paragraph">eMSPs with a roaming agreement enabling access to the EV charging location. Available only if <code class="lang-kotlin">EVChargingLocationFeature.EMSPS</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise empty.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="energyMix" data-filterable-set=":modules:dokkaHtml/release" data-name="259115039%2FProperties%2F1617540583" id="259115039%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-energy-mix</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-energy-mix: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-energy-mix?</div><div class="brief"><p class="paragraph">Details on the energy supplied at the charging location. Available only if <code class="lang-kotlin">EVChargingLocationFeature.LOCATION_INFO</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="evChargingOperator" data-filterable-set=":modules:dokkaHtml/release" data-name="-39566943%2FProperties%2F1617540583" id="-39566943%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-ev-charging-operator</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-ev-charging-operator: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-operator?</div><div class="brief"><p class="paragraph">Operator of the charging point, if available.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="evChargingSubOperator" data-filterable-set=":modules:dokkaHtml/release" data-name="-1573346767%2FProperties%2F1617540583" id="-1573346767%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-ev-charging-sub-operator</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-ev-charging-sub-operator: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-operator?</div><div class="brief"><p class="paragraph">Suboperator of the charging point, if available.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="evses" data-filterable-set=":modules:dokkaHtml/release" data-name="-1290589373%2FProperties%2F1617540583" id="-1290589373%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-evses</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-evses: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-s-e-info&gt;</div><div class="brief"><p class="paragraph">List of EVSEs at the charging station. Available only if <code class="lang-kotlin">EVChargingLocationFeature.EVSES</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise empty.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="facilityTypes" data-filterable-set=":modules:dokkaHtml/release" data-name="745002621%2FProperties%2F1617540583" id="745002621%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-facility-types</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-facility-types: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-facility-type&gt;</div><div class="brief"><p class="paragraph">Facilities available at the charging location, for example hotel, wifi, parking lot etc. Available only if <code class="lang-kotlin">EVChargingLocationFeature.NEARBY</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise empty.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="id" data-filterable-set=":modules:dokkaHtml/release" data-name="-138717396%2FProperties%2F1617540583" id="-138717396%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-id</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@get:<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-name/index.html">JvmName</a>(name = "getID"<wbr/>)</div></div>val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-id: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief"><p class="paragraph">A unique identifier of the charging location.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="name" data-filterable-set=":modules:dokkaHtml/release" data-name="737838396%2FProperties%2F1617540583" id="737838396%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-name</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-name: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">Display name of the charging location, if available.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="openingHours" data-filterable-set=":modules:dokkaHtml/release" data-name="-2138619216%2FProperties%2F1617540583" id="-2138619216%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-opening-hours</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-opening-hours: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-opening-hours?</div><div class="brief"><p class="paragraph">The times when the EVSEs at the charging location can be accessed for charging. Available only if <code class="lang-kotlin">EVChargingLocationFeature.LOCATION_INFO</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="parkingType" data-filterable-set=":modules:dokkaHtml/release" data-name="407401473%2FProperties%2F1617540583" id="407401473%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-parking-type</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-parking-type: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-parking-type?</div><div class="brief"><p class="paragraph">The type of parking at the charging location. Available only if <code class="lang-kotlin">EVChargingLocationFeature.LOCATION_INFO</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="restrictions" data-filterable-set=":modules:dokkaHtml/release" data-name="-687515872%2FProperties%2F1617540583" id="-687515872%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-restrictions</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-restrictions: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-access-restriction-reason&gt;</div><div class="brief"><p class="paragraph">Reason(s) for restricted access.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="supportedVehicles" data-filterable-set=":modules:dokkaHtml/release" data-name="1120513630%2FProperties%2F1617540583" id="1120513630%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-supported-vehicles</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-supported-vehicles: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-vehicle-category&gt;</div><div class="brief"><p class="paragraph">List of vehicle categories this charging location can support. For example, the same location can be suitable for charging passenger cars and motorcycles. There may be some further restrictions specified in other attributes, for example the available connector types may not be suitable for all vehicles in the supported category.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="supportPhoneNumber" data-filterable-set=":modules:dokkaHtml/release" data-name="1548036575%2FProperties%2F1617540583" id="1548036575%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-support-phone-number</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-support-phone-number: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">The phone number that EV drivers should call when need assistance at the charge location, in E.164 format. Available only if <code class="lang-kotlin">EVChargingLocationFeature.LOCATION_INFO</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="tariffs" data-filterable-set=":modules:dokkaHtml/release" data-name="-1427292956%2FProperties%2F1617540583" id="-1427292956%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-tariffs</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-tariffs: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-tariff&gt;</div><div class="brief"><p class="paragraph">List of tariffs or price plans for the connectors of the charging station. Tariffs are typically connector-type specific. Hence, they are always linked with connectors and/or connector groups, by indexes to this list.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="timeZone" data-filterable-set=":modules:dokkaHtml/release" data-name="897292910%2FProperties%2F1617540583" id="897292910%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-time-zone</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-time-zone: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">The time zone of the charging location. Based on IANA tzdata's TZ-values. Available only if <code class="lang-kotlin">EVChargingLocationFeature.LOCATION_INFO</code> is included in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="truckRestrictions" data-filterable-set=":modules:dokkaHtml/release" data-name="471475437%2FProperties%2F1617540583" id="471475437%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-truck-restrictions</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-location-truck-restrictions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-e-v-charging-truck-restriction?</div><div class="brief"><p class="paragraph">Access restrictions for trucks and light commercial vehicles. Restricted, only available to customers having a specific contract with HERE and if requested by including <code class="lang-kotlin">EVChargingLocationFeature.TRUCK_RESTRICTIONS</code> in <code class="lang-kotlin">EVSearchOptions.additional_features</code>, otherwise <code class="lang-kotlin">null</code>.</p></div></div></div>
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
