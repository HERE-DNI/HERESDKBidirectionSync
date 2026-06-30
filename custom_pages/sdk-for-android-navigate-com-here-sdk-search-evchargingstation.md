---
title: "EVChargingStation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-evchargingstation"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- EVChargingStation.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.search.EVChargingStation</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">EVChargingStation</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Group of connectors for electric vehicles (EVs), defined by a common charging connector type and
 maximum power level.
 Use <a href="sdk-for-android-navigate-placecategory#BUSINESS_AND_SERVICES_EV_CHARGING_STATION"><code>PlaceCategory.BUSINESS_AND_SERVICES_EV_CHARGING_STATION</code></a> to find stations.
 In the <code>Details</code> of a <code>Place</code> result you can find the list of found pools containing stations,
 if any.
 For offline EV rich attributes, enable <a href="sdk-for-android-navigate-layerconfiguration.feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#availableConnectorCount">availableConnectorCount</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of available physical connectors at the charging station.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#chargingMode">chargingMode</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Charging mode of the charging station.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#connectorCount">connectorCount</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of physical connectors at the charging station.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#connectorTypeId">connectorTypeId</a></code></div>
<div class="col-last odd-row-color">
<div class="block">ID of the connector type.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#connectorTypeName">connectorTypeName</a></code></div>
<div class="col-last even-row-color">
<div class="block">Name of the connector type.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#currentRangeInAmperes">currentRangeInAmperes</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Current range provided by the charging station, in amperes.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#hasFixedCable">hasFixedCable</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the cable is fixed or not fixed for a specific
 Connector Type on the charge station.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#lastUpdated">lastUpdated</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Last update of the <code>available_connector_count</code> and <code>occupied_connector_count</code> fields.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#maxPowerInKilowatts">maxPowerInKilowatts</a></code></div>
<div class="col-last even-row-color">
<div class="block">Maximum charge power of connectors in kW.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#occupiedConnectorCount">occupiedConnectorCount</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of occupied physical connectors at the charging station.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#outOfServiceConnectorCount">outOfServiceConnectorCount</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of physical connectors that are out of service at the charging station.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#phaseCount">phaseCount</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of phases used by the charging station.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#physicalReference">physicalReference</a></code></div>
<div class="col-last even-row-color">
<div class="block">Printed on the outside of the EVSE for visual identification.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#powerFeedTypeId">powerFeedTypeId</a></code></div>
<div class="col-last odd-row-color">
<div class="block">ID of the power feed type, as defined by the
 https://en.wikipedia.org/wiki/SAE_J1772#Charging standard.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#powerFeedTypeName">powerFeedTypeName</a></code></div>
<div class="col-last even-row-color">
<div class="block">Name of the power feed type, as defined by the
 https://en.wikipedia.org/wiki/SAE_J1772#Charging standard.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#reservedConnectorCount">reservedConnectorCount</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of physical connectors that are reserved at the charging station.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#supplierName">supplierName</a></code></div>
<div class="col-last even-row-color">
<div class="block">The EV charging station operator.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#voltageRangeInVolts">voltageRangeInVolts</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Voltage range of the charge provided by the charging station, in volts.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#%3Cinit%3E()">EVChargingStation</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-evchargingstation#hashCode()">hashCode</a>()</code></div>

</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="supplierName">
<h3>supplierName</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">supplierName</span></div>
<div class="block"><p>The EV charging station operator.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online search using the <code>SearchEngine</code>, it can be null if data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="connectorTypeName">
<h3>connectorTypeName</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">connectorTypeName</span></div>
<div class="block"><p>Name of the connector type.
 For more information on the current connector types, see
 https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html
 May include customer-facing names. In such cases, a 'customer names' label is present.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="connectorTypeId">
<h3>connectorTypeId</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">connectorTypeId</span></div>
<div class="block"><p>ID of the connector type.
 For more information on the current connector types, see
 https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="powerFeedTypeName">
<h3>powerFeedTypeName</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">powerFeedTypeName</span></div>
<div class="block"><p>Name of the power feed type, as defined by the
 https://en.wikipedia.org/wiki/SAE_J1772#Charging standard.
 Provides the customer information on the charge level of the specific Connector Type.
 Also, can describe level that is used in North America and Australia.
 In that case label 'North America (Australia)' is present.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="powerFeedTypeId">
<h3>powerFeedTypeId</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">powerFeedTypeId</span></div>
<div class="block"><p>ID of the power feed type, as defined by the
 https://en.wikipedia.org/wiki/SAE_J1772#Charging standard.
 No data in case of offline search.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxPowerInKilowatts">
<h3>maxPowerInKilowatts</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">maxPowerInKilowatts</span></div>
<div class="block"><p>Maximum charge power of connectors in kW.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="connectorCount">
<h3>connectorCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">connectorCount</span></div>
<div class="block"><p>Number of physical connectors at the charging station.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="availableConnectorCount">
<h3>availableConnectorCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">availableConnectorCount</span></div>
<div class="block"><p>Number of available physical connectors at the charging station.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="occupiedConnectorCount">
<h3>occupiedConnectorCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">occupiedConnectorCount</span></div>
<div class="block"><p>Number of occupied physical connectors at the charging station.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="outOfServiceConnectorCount">
<h3>outOfServiceConnectorCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">outOfServiceConnectorCount</span></div>
<div class="block"><p>Number of physical connectors that are out of service at the charging station.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="reservedConnectorCount">
<h3>reservedConnectorCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">reservedConnectorCount</span></div>
<div class="block"><p>Number of physical connectors that are reserved at the charging station.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="lastUpdated">
<h3>lastUpdated</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">lastUpdated</span></div>
<div class="block"><p>Last update of the <code>available_connector_count</code> and <code>occupied_connector_count</code> fields.
 This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="chargingMode">
<h3>chargingMode</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">chargingMode</span></div>
<div class="block"><p>Charging mode of the charging station. For more information, see
 https://en.wikipedia.org/w/index.php?title=Charging_station&amp;oldid=1013010605#IEC-61851-1_Charging_Modes standard.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="voltageRangeInVolts">
<h3>voltageRangeInVolts</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">voltageRangeInVolts</span></div>
<div class="block"><p>Voltage range of the charge provided by the charging station, in volts.
 Values are alphanumeric represented by the voltage range followed by 'V' and
 by the current type 'AC' or 'DC', for example: '100-120V AC'.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="currentRangeInAmperes">
<h3>currentRangeInAmperes</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">currentRangeInAmperes</span></div>
<div class="block"><p>Current range provided by the charging station, in amperes.
 Values are alphanumeric represented by the Ampere value followed by an 'A',
 for example '12A-80A'.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="phaseCount">
<h3>phaseCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">phaseCount</span></div>
<div class="block"><p>Number of phases used by the charging station.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="hasFixedCable">
<h3>hasFixedCable</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">hasFixedCable</span></div>
<div class="block"><p>Indicates that the cable is fixed or not fixed for a specific
 Connector Type on the charge station.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="physicalReference">
<h3>physicalReference</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">physicalReference</span></div>
<div class="block"><p>Printed on the outside of the EVSE for visual identification.
 Available only in offline search.
 This field can be <code>null</code> if data is unavailable.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>EVChargingStation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EVChargingStation</span>()</div>
<div class="block"><p>Creates a new instance.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
`
}</HTMLBlock>
