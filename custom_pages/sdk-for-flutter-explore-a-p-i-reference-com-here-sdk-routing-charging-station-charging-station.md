---
title: "Charging Station"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-station-charging-station"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -charging-station.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.routing/ChargingStation/ChargingStation/#kotlin.String?#kotlin.String?#com.here.sdk.routing.ChargingConnectorAttributes?/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-station/ChargingStation</div>
<div class="cover">
<h1 class="cover">Charging<wbr/>Station</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(id: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?, name: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?, connectorAttributes: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-connector-attributes?)</div><p class="paragraph">Creates a new instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>id</u></div></div><div><div class="title"><p class="paragraph">Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>name</u></div></div><div><div class="title"><p class="paragraph">Human readable name of this charging station. It can be null when there is no name associated with the station.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>connector<wbr/>Attributes</u></div></div><div><div class="title"><p class="paragraph">Details of the connector suggested to be used.</p></div></div></div></div></div><hr/><div class="symbol monospace">constructor(id: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?, name: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?, connectorAttributes: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-connector-attributes?, brand: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-name-i-d?, chargePointOperator: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-name-i-d?, matchingEMobilityServiceProviders: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-name-i-d&gt;)</div><p class="paragraph">Creates a new instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>id</u></div></div><div><div class="title"><p class="paragraph">Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>name</u></div></div><div><div class="title"><p class="paragraph">Human readable name of this charging station. It can be null when there is no name associated with the station.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>connector<wbr/>Attributes</u></div></div><div><div class="title"><p class="paragraph">Details of the connector suggested to be used.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>brand</u></div></div><div><div class="title"><p class="paragraph">Charging station brand. /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-name-i-d-name reflect to charging station brand name. /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-name-i-d-id reflect to charging station brand unique ID.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>charge<wbr/>Point<wbr/>Operator</u></div></div><div><div class="title"><p class="paragraph">Charging station charge-point-operator. /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-name-i-d-name reflect to charge-point-operator name. /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-name-i-d-id reflect to charge-point-operator ID.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>matching<wbr/>EMobility<wbr/>Service<wbr/>Providers</u></div></div><div><div class="title"><p class="paragraph">List of matched E-Mobility Service Providers. Populated only when /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-electric-vehicle-options-ev-mobility-service-provider-preferences was set. This list reflects the subset of E-Mobility Service Providers supported by the charging station, from the list specified in the request parameter /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-electric-vehicle-options-ev-mobility-service-provider-preferences. /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-name-i-d-name in each list item reflect to E-Mobility Service Provider name. /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-name-i-d-id in each list item reflect to E-Mobility Service Provider id.</p></div></div></div></div></div></div></div>
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
