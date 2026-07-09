---
title: "EVChargingStation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-evchargingstation"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- EVChargingStation.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.search.EVChargingStation</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">EVChargingStation</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Group of connectors for electric vehicles (EVs), defined by a common charging connector type and
 maximum power level.
 Use <a href="sdk-for-android-navigate-placecategory#BUSINESS_AND_SERVICES_EV_CHARGING_STATION"><code>PlaceCategory.BUSINESS_AND_SERVICES_EV_CHARGING_STATION</code></a> to find stations.
 In the <code>Details</code> of a <code>Place</code> result you can find the list of found pools containing stations,
 if any.
 For offline EV rich attributes, enable <a href="sdk-for-android-navigate-layerconfiguration-feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#availableConnectorCount">availableConnectorCount</a></code></div>
<div className="col-last even-row-color">
<div className="block">Number of available physical connectors at the charging station.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#chargingMode">chargingMode</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Charging mode of the charging station.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#connectorCount">connectorCount</a></code></div>
<div className="col-last even-row-color">
<div className="block">Number of physical connectors at the charging station.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#connectorTypeId">connectorTypeId</a></code></div>
<div className="col-last odd-row-color">
<div className="block">ID of the connector type.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#connectorTypeName">connectorTypeName</a></code></div>
<div className="col-last even-row-color">
<div className="block">Name of the connector type.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#currentRangeInAmperes">currentRangeInAmperes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Current range provided by the charging station, in amperes.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#hasFixedCable">hasFixedCable</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates that the cable is fixed or not fixed for a specific
 Connector Type on the charge station.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#lastUpdated">lastUpdated</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Last update of the <code>available_connector_count</code> and <code>occupied_connector_count</code> fields.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#maxPowerInKilowatts">maxPowerInKilowatts</a></code></div>
<div className="col-last even-row-color">
<div className="block">Maximum charge power of connectors in kW.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#occupiedConnectorCount">occupiedConnectorCount</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Number of occupied physical connectors at the charging station.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#outOfServiceConnectorCount">outOfServiceConnectorCount</a></code></div>
<div className="col-last even-row-color">
<div className="block">Number of physical connectors that are out of service at the charging station.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#phaseCount">phaseCount</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Number of phases used by the charging station.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#physicalReference">physicalReference</a></code></div>
<div className="col-last even-row-color">
<div className="block">Printed on the outside of the EVSE for visual identification.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#powerFeedTypeId">powerFeedTypeId</a></code></div>
<div className="col-last odd-row-color">
<div className="block">ID of the power feed type, as defined by the
 https://en.wikipedia.org/wiki/SAE_J1772#Charging standard.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#powerFeedTypeName">powerFeedTypeName</a></code></div>
<div className="col-last even-row-color">
<div className="block">Name of the power feed type, as defined by the
 https://en.wikipedia.org/wiki/SAE_J1772#Charging standard.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#reservedConnectorCount">reservedConnectorCount</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Number of physical connectors that are reserved at the charging station.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#supplierName">supplierName</a></code></div>
<div className="col-last even-row-color">
<div className="block">The EV charging station operator.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#voltageRangeInVolts">voltageRangeInVolts</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Voltage range of the charge provided by the charging station, in volts.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#%3Cinit%3E()">EVChargingStation</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="supplierName">
<h3>supplierName</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">supplierName</span></div>
<div className="block"><p>The EV charging station operator.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online search using the <code>SearchEngine</code>, it can be null if data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="connectorTypeName">
<h3>connectorTypeName</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">connectorTypeName</span></div>
<div className="block"><p>Name of the connector type.
 For more information on the current connector types, see
 https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html
 May include customer-facing names. In such cases, a 'customer names' label is present.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="connectorTypeId">
<h3>connectorTypeId</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">connectorTypeId</span></div>
<div className="block"><p>ID of the connector type.
 For more information on the current connector types, see
 https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="powerFeedTypeName">
<h3>powerFeedTypeName</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">powerFeedTypeName</span></div>
<div className="block"><p>Name of the power feed type, as defined by the
 https://en.wikipedia.org/wiki/SAE_J1772#Charging standard.
 Provides the customer information on the charge level of the specific Connector Type.
 Also, can describe level that is used in North America and Australia.
 In that case label 'North America (Australia)' is present.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="powerFeedTypeId">
<h3>powerFeedTypeId</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">powerFeedTypeId</span></div>
<div className="block"><p>ID of the power feed type, as defined by the
 https://en.wikipedia.org/wiki/SAE_J1772#Charging standard.
 No data in case of offline search.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="maxPowerInKilowatts">
<h3>maxPowerInKilowatts</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">maxPowerInKilowatts</span></div>
<div className="block"><p>Maximum charge power of connectors in kW.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="connectorCount">
<h3>connectorCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">connectorCount</span></div>
<div className="block"><p>Number of physical connectors at the charging station.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="availableConnectorCount">
<h3>availableConnectorCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">availableConnectorCount</span></div>
<div className="block"><p>Number of available physical connectors at the charging station.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="occupiedConnectorCount">
<h3>occupiedConnectorCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">occupiedConnectorCount</span></div>
<div className="block"><p>Number of occupied physical connectors at the charging station.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="outOfServiceConnectorCount">
<h3>outOfServiceConnectorCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">outOfServiceConnectorCount</span></div>
<div className="block"><p>Number of physical connectors that are out of service at the charging station.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="reservedConnectorCount">
<h3>reservedConnectorCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">reservedConnectorCount</span></div>
<div className="block"><p>Number of physical connectors that are reserved at the charging station.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="lastUpdated">
<h3>lastUpdated</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">lastUpdated</span></div>
<div className="block"><p>Last update of the <code>available_connector_count</code> and <code>occupied_connector_count</code> fields.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="chargingMode">
<h3>chargingMode</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">chargingMode</span></div>
<div className="block"><p>Charging mode of the charging station. For more information, see
 https://en.wikipedia.org/w/index.php?title=Charging_station&amp;oldid=1013010605#IEC-61851-1_Charging_Modes standard.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="voltageRangeInVolts">
<h3>voltageRangeInVolts</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">voltageRangeInVolts</span></div>
<div className="block"><p>Voltage range of the charge provided by the charging station, in volts.
 Values are alphanumeric represented by the voltage range followed by 'V' and
 by the current type 'AC' or 'DC', for example: '100-120V AC'.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="currentRangeInAmperes">
<h3>currentRangeInAmperes</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">currentRangeInAmperes</span></div>
<div className="block"><p>Current range provided by the charging station, in amperes.
 Values are alphanumeric represented by the Ampere value followed by an 'A',
 for example '12A-80A'.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="phaseCount">
<h3>phaseCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">phaseCount</span></div>
<div className="block"><p>Number of phases used by the charging station.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="hasFixedCable">
<h3>hasFixedCable</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span className="element-name">hasFixedCable</span></div>
<div className="block"><p>Indicates that the cable is fixed or not fixed for a specific
 Connector Type on the charge station.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="physicalReference">
<h3>physicalReference</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">physicalReference</span></div>
<div className="block"><p>Printed on the outside of the EVSE for visual identification.
 Available only in offline search.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>EVChargingStation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">EVChargingStation</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
