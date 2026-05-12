---
title: "EVChargingStation Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-evchargingstation"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVChargingStation.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingStation"></a>
<a title="EVChargingStation Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVChargingStation Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct EVChargingStation : Hashable</code></pre>
</div>
</div>
<p>Group of connectors for electric vehicles (EVs), defined by a common charging connector type and
maximum power level.</p>
<p>Use <code><a href="../Classes/PlaceCategory.html#/s:7heresdk13PlaceCategoryC36businessAndServicesEvChargingStationSSvpZ">PlaceCategory.businessAndServicesEvChargingStation</a></code> to find stations.
In the <code><a href="../Structs/Details.html">Details</a></code> of a <code><a href="../Classes/Place.html">Place</a></code> result you can find the list of found pools containing stations,
if any.</p>
<p>For offline EV rich attributes, enable <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">LayerConfiguration.Feature.ev</a></code>
in <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV12supplierNameSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/supplierName"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV12supplierNameSSSgvp">supplierName</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The EV charging station operator.
This field is always <code>nil</code> for offline search using the <code>OfflineSearchEngine</code>. For online search using the <code><a href="../Classes/SearchEngine.html">SearchEngine</a></code>, it can be null if data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var supplierName: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV17connectorTypeNameSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectorTypeName"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV17connectorTypeNameSSSgvp">connectorTypeName</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Name of the connector type.
For more information on the current connector types, see
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html</a>
May include customer-facing names. In such cases, a ‘customer names’ label is present.
This field can be <code>nil</code> if data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var connectorTypeName: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV15connectorTypeIdSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectorTypeId"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV15connectorTypeIdSSSgvp">connectorTypeId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>ID of the connector type.
For more information on the current connector types, see
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html</a>
This field is always <code>nil</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code><a href="../Classes/SearchEngine.html">SearchEngine</a></code>, it may be <code>nil</code> if the data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var connectorTypeId: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV17powerFeedTypeNameSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/powerFeedTypeName"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV17powerFeedTypeNameSSSgvp">powerFeedTypeName</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Name of the power feed type, as defined by the
<a href="https://en.wikipedia.org/wiki/SAE_J1772#Charging">https://en.wikipedia.org/wiki/SAE_J1772#Charging</a> standard.
Provides the customer information on the charge level of the specific Connector Type.
Also, can describe level that is used in North America and Australia.
In that case label ‘North America (Australia)’ is present.
This field can be <code>nil</code> if data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var powerFeedTypeName: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV15powerFeedTypeIdSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/powerFeedTypeId"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV15powerFeedTypeIdSSSgvp">powerFeedTypeId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>ID of the power feed type, as defined by the
<a href="https://en.wikipedia.org/wiki/SAE_J1772#Charging">https://en.wikipedia.org/wiki/SAE_J1772#Charging</a> standard.
No data in case of offline search.
This field is always <code>nil</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code><a href="../Classes/SearchEngine.html">SearchEngine</a></code>, it may be <code>nil</code> if the data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var powerFeedTypeId: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV19maxPowerInKilowattsSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxPowerInKilowatts"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV19maxPowerInKilowattsSdSgvp">maxPowerInKilowatts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum charge power of connectors in kW.
This field can be <code>nil</code> if data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var maxPowerInKilowatts: Double?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV14connectorCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectorCount"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV14connectorCounts5Int32VSgvp">connectorCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of physical connectors at the charging station.
This field can be <code>nil</code> if data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var connectorCount: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV23availableConnectorCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/availableConnectorCount"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV23availableConnectorCounts5Int32VSgvp">availableConnectorCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of available physical connectors at the charging station.
This field is always <code>nil</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code><a href="../Classes/SearchEngine.html">SearchEngine</a></code>, it may be <code>nil</code> if the data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var availableConnectorCount: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV22occupiedConnectorCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/occupiedConnectorCount"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV22occupiedConnectorCounts5Int32VSgvp">occupiedConnectorCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of occupied physical connectors at the charging station.
This field is always <code>nil</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code><a href="../Classes/SearchEngine.html">SearchEngine</a></code>, it may be <code>nil</code> if the data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var occupiedConnectorCount: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV26outOfServiceConnectorCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/outOfServiceConnectorCount"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV26outOfServiceConnectorCounts5Int32VSgvp">outOfServiceConnectorCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of physical connectors that are out of service at the charging station.
This field is always <code>nil</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code><a href="../Classes/SearchEngine.html">SearchEngine</a></code>, it may be <code>nil</code> if the data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var outOfServiceConnectorCount: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV22reservedConnectorCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/reservedConnectorCount"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV22reservedConnectorCounts5Int32VSgvp">reservedConnectorCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of physical connectors that are reserved at the charging station.
This field is always <code>nil</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code><a href="../Classes/SearchEngine.html">SearchEngine</a></code>, it may be <code>nil</code> if the data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var reservedConnectorCount: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV11lastUpdated10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastUpdated"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV11lastUpdated10Foundation4DateVSgvp">lastUpdated</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Last update of the <code>available_connector_count</code> and <code>occupied_connector_count</code> fields.
This field is always <code>nil</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code><a href="../Classes/SearchEngine.html">SearchEngine</a></code>, it may be <code>nil</code> if the data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var lastUpdated: Date?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV12chargingModeSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/chargingMode"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV12chargingModeSSSgvp">chargingMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Charging mode of the charging station. For more information, see
<a href="https://en.wikipedia.org/w/index.php?title=Charging_station&amp;oldid=1013010605#IEC-61851-1_Charging_Modes">https://en.wikipedia.org/w/index.php?title=Charging_station&amp;oldid=1013010605#IEC-61851-1_Charging_Modes</a> standard.
This field can be <code>nil</code> if data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var chargingMode: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV19voltageRangeInVoltsSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/voltageRangeInVolts"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV19voltageRangeInVoltsSSSgvp">voltageRangeInVolts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Voltage range of the charge provided by the charging station, in volts.
Values are alphanumeric represented by the voltage range followed by ‘V’ and
by the current type ‘AC’ or ‘DC’, for example: ‘100-120V AC’.
This field can be <code>nil</code> if data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var voltageRangeInVolts: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV21currentRangeInAmperesSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currentRangeInAmperes"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV21currentRangeInAmperesSSSgvp">currentRangeInAmperes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Current range provided by the charging station, in amperes.
Values are alphanumeric represented by the Ampere value followed by an ‘A’,
for example ‘12A-80A’.
This field can be <code>nil</code> if data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var currentRangeInAmperes: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV10phaseCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/phaseCount"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV10phaseCounts5Int32VSgvp">phaseCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of phases used by the charging station.
This field can be <code>nil</code> if data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var phaseCount: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV13hasFixedCableSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hasFixedCable"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV13hasFixedCableSbSgvp">hasFixedCable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates that the cable is fixed or not fixed for a specific
Connector Type on the charge station.
This field can be <code>nil</code> if data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var hasFixedCable: Bool?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV17physicalReferenceSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/physicalReference"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV17physicalReferenceSSSgvp">physicalReference</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Printed on the outside of the EVSE for visual identification.
Available only in offline search.
This field can be <code>nil</code> if data is unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var physicalReference: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EVChargingStationV12supplierName013connectorTypeE00fG2Id09powerFeedgE00ijgH019maxPowerInKilowatts0F5Count018availableConnectorO008occupiedqO0012outOfServiceqO008reservedqO011lastUpdated12chargingMode012voltageRangeM5Volts012currentRangeM7Amperes05phaseO013hasFixedCable17physicalReferenceACSSSg_A4VSdSgs5Int32VSgA4Z10Foundation4DateVSgA3vZSbSgAVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(supplierName:connectorTypeName:connectorTypeId:powerFeedTypeName:powerFeedTypeId:maxPowerInKilowatts:connectorCount:availableConnectorCount:occupiedConnectorCount:outOfServiceConnectorCount:reservedConnectorCount:lastUpdated:chargingMode:voltageRangeInVolts:currentRangeInAmperes:phaseCount:hasFixedCable:physicalReference:)"></a>
<a class="token" href="#/s:7heresdk17EVChargingStationV12supplierName013connectorTypeE00fG2Id09powerFeedgE00ijgH019maxPowerInKilowatts0F5Count018availableConnectorO008occupiedqO0012outOfServiceqO008reservedqO011lastUpdated12chargingMode012voltageRangeM5Volts012currentRangeM7Amperes05phaseO013hasFixedCable17physicalReferenceACSSSg_A4VSdSgs5Int32VSgA4Z10Foundation4DateVSgA3vZSbSgAVtcfc">init(supplierName:<wbr/>connectorTypeName:<wbr/>connectorTypeId:<wbr/>powerFeedTypeName:<wbr/>powerFeedTypeId:<wbr/>maxPowerInKilowatts:<wbr/>connectorCount:<wbr/>availableConnectorCount:<wbr/>occupiedConnectorCount:<wbr/>outOfServiceConnectorCount:<wbr/>reservedConnectorCount:<wbr/>lastUpdated:<wbr/>chargingMode:<wbr/>voltageRangeInVolts:<wbr/>currentRangeInAmperes:<wbr/>phaseCount:<wbr/>hasFixedCable:<wbr/>physicalReference:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(supplierName: String? = nil, connectorTypeName: String? = nil, connectorTypeId: String? = nil, powerFeedTypeName: String? = nil, powerFeedTypeId: String? = nil, maxPowerInKilowatts: Double? = nil, connectorCount: Int32? = nil, availableConnectorCount: Int32? = nil, occupiedConnectorCount: Int32? = nil, outOfServiceConnectorCount: Int32? = nil, reservedConnectorCount: Int32? = nil, lastUpdated: Date? = nil, chargingMode: String? = nil, voltageRangeInVolts: String? = nil, currentRangeInAmperes: String? = nil, phaseCount: Int32? = nil, hasFixedCable: Bool? = nil, physicalReference: String? = nil)</code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>



</div>
`
}</HTMLBlock>
