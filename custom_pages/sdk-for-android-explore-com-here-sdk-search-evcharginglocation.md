---
title: "EVChargingLocation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-evcharginglocation"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- EVChargingLocation.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.search.EVChargingLocation</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">EVChargingLocation</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>An electric vehicle (EV) charging location.
 </p><p>The semantics generally follow the OCPI 2.2.1 standard.
 </p><p>Known EV-specific acronyms:
 <ul>
<li>EV: Electric Vehicle</li>
<li>OCPI: Open Charge Point Interface (a standard with a rather wide adoption worldwide, https://evroaming.org/)</li>
<li>CPO: Charge Point Operator (company that runs the EV charging location)</li>
<li>eMSP: e-Mobility Service Provider (customer-facing company)</li>
<li>EVSE: Electric Vehicle Supply Equipment (the actual charger that can charge one car at a time)</li>
</ul>
</p><p>A charging location includes a collection of one or more EV supply equipment (EVSE) instances.
 Typically, the charging location is the exact location of the group of EVSEs,
 simplified to a single point, but it can also be the entrance of a parking structure
 which contains these EVSEs.
 Each EVSE supports more precise position, where applicable.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-evchargingconnectorgroup" title="class in com.here.sdk.search">EVChargingConnectorGroup</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getConnectorGroups()">getConnectorGroups</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the connector groups for the location.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getCpoID()">getCpoID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the CPO's own ID for the location.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-evchargingoperator" title="class in com.here.sdk.search">EVChargingOperator</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getEMobilityServiceProviders()">getEMobilityServiceProviders</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of eMSPs with a roaming agreement enabling access to the EV charging location.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-energymix" title="class in com.here.sdk.search">EnergyMix</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getEnergyMix()">getEnergyMix</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the details on the energy supplied at the charging location.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-evchargingoperator" title="class in com.here.sdk.search">EVChargingOperator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getEvChargingOperator()">getEvChargingOperator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the operator of the charging point, if available.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-evchargingoperator" title="class in com.here.sdk.search">EVChargingOperator</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getEvChargingSubOperator()">getEvChargingSubOperator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the suboperator of the charging point, if available.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-evseinfo" title="class in com.here.sdk.search">EVSEInfo</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getEvses()">getEvses</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of EVSEs at the charging station.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-facilitytype" title="enum class in com.here.sdk.search">FacilityType</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getFacilityTypes()">getFacilityTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of facilities available at the charging location, for example
 hotel, wifi, parking lot etc.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getID()">getID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the unique identifier of the charging location.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the display name of the charging location, if available.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-evchargingopeninghours" title="class in com.here.sdk.search">EVChargingOpeningHours</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getOpeningHours()">getOpeningHours</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the times when the EVSEs at the charging location can be accessed for charging.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-parkingtype" title="enum class in com.here.sdk.search">ParkingType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getParkingType()">getParkingType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the type of parking at the charging location.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-evaccessrestrictionreason" title="enum class in com.here.sdk.search">EVAccessRestrictionReason</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getRestrictions()">getRestrictions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of restrictions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-evchargingvehiclecategory" title="enum class in com.here.sdk.search">EVChargingVehicleCategory</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getSupportedVehicles()">getSupportedVehicles</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of vehicle categories this charging location can support.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getSupportPhoneNumber()">getSupportPhoneNumber</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the phone number that EV drivers should call when need assistance at the charge location.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-evchargingtariff" title="class in com.here.sdk.search">EVChargingTariff</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getTariffs()">getTariffs</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of tariffs or price plans for the connectors of the charging station.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getTimeZone()">getTimeZone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the time zone of the charging location.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-evchargingtruckrestriction" title="class in com.here.sdk.search">EVChargingTruckRestriction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-evcharginglocation#getTruckRestrictions()">getTruckRestrictions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the access restrictions for trucks and light commercial vehicles.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<div class="block"><p>Gets the unique identifier of the charging location.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A unique identifier of the charging location.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block"><p>Gets the display name of the charging location, if available.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Display name of the charging location, if available.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCpoID()">
<h3>getCpoID</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCpoID</span>()</div>
<div class="block"><p>Gets the CPO's own ID for the location.
 </p><p>This ID may be relevant for some clients to map the charging location data to their own
 or 3rd party systems.
 Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>CPO's own ID for the location.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEvChargingOperator()">
<h3>getEvChargingOperator</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-evchargingoperator" title="class in com.here.sdk.search">EVChargingOperator</a></span> <span class="element-name">getEvChargingOperator</span>()</div>
<div class="block"><p>Gets the operator of the charging point, if available.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Operator of the charging point, if available.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEvChargingSubOperator()">
<h3>getEvChargingSubOperator</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-evchargingoperator" title="class in com.here.sdk.search">EVChargingOperator</a></span> <span class="element-name">getEvChargingSubOperator</span>()</div>
<div class="block"><p>Gets the suboperator of the charging point, if available.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Suboperator of the charging point, if available.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEMobilityServiceProviders()">
<h3>getEMobilityServiceProviders</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-evchargingoperator" title="class in com.here.sdk.search">EVChargingOperator</a>&gt;</span> <span class="element-name">getEMobilityServiceProviders</span>()</div>
<div class="block"><p>Gets the list of eMSPs with a roaming agreement enabling access to the EV charging location.
 </p><p>Available only if <code>EVChargingLocationFeature.EMSPS</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise empty.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>eMSPs with a roaming agreement enabling access to the EV charging location.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFacilityTypes()">
<h3>getFacilityTypes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-facilitytype" title="enum class in com.here.sdk.search">FacilityType</a>&gt;</span> <span class="element-name">getFacilityTypes</span>()</div>
<div class="block"><p>Gets the list of facilities available at the charging location, for example
 hotel, wifi, parking lot etc.
 </p><p>Available only if <code>EVChargingLocationFeature.NEARBY</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise empty.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Facilities available at the charging location, for example hotel, wifi, parking lot etc.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParkingType()">
<h3>getParkingType</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-parkingtype" title="enum class in com.here.sdk.search">ParkingType</a></span> <span class="element-name">getParkingType</span>()</div>
<div class="block"><p>Gets the type of parking at the charging location.
 </p><p>Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The type of parking at the charging location.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnergyMix()">
<h3>getEnergyMix</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-energymix" title="class in com.here.sdk.search">EnergyMix</a></span> <span class="element-name">getEnergyMix</span>()</div>
<div class="block"><p>Gets the details on the energy supplied at the charging location.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Details on the energy supplied at the charging location.
     Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
     <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEvses()">
<h3>getEvses</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-evseinfo" title="class in com.here.sdk.search">EVSEInfo</a>&gt;</span> <span class="element-name">getEvses</span>()</div>
<div class="block"><p>Gets the list of EVSEs at the charging station.
 </p><p>Available only if <code>EVChargingLocationFeature.EVSES</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise empty.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>List of EVSEs at the charging station.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTariffs()">
<h3>getTariffs</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-evchargingtariff" title="class in com.here.sdk.search">EVChargingTariff</a>&gt;</span> <span class="element-name">getTariffs</span>()</div>
<div class="block"><p>Gets the list of tariffs or price plans for the connectors of the charging station.
 </p><p>Tariffs are typically connector-type specific. Hence, they are always linked with connectors
 and/or connector groups, by indexes to this list.
 </p><p>This property is set only when data is available and when <code>EVSearchOptions.additional_features</code>
 include either <code>EVChargingLocationFeature.EVSES</code> or <code>EVChargingLocationFeature.CONNECTOR_GROUPS</code>.
 </p><p>By default, the list includes tariffs for ad-hoc charging, per connector type,
 for EVSEs that accept payment without registering.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>List of tariffs or price plans for the connectors of the charging station.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectorGroups()">
<h3>getConnectorGroups</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-evchargingconnectorgroup" title="class in com.here.sdk.search">EVChargingConnectorGroup</a>&gt;</span> <span class="element-name">getConnectorGroups</span>()</div>
<div class="block"><p>Gets the connector groups for the location.
 </p><p>Provides an overview of the charging connectors in the location by type and power.
 Available only if <code>EVChargingLocationFeature.CONNECTOR_GROUPS</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise empty.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Connector groups for the location.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupportedVehicles()">
<h3>getSupportedVehicles</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-evchargingvehiclecategory" title="enum class in com.here.sdk.search">EVChargingVehicleCategory</a>&gt;</span> <span class="element-name">getSupportedVehicles</span>()</div>
<div class="block"><p>Gets the list of vehicle categories this charging location can support. For example,
 the same location can be suitable for charging passenger cars and motorcycles.
 </p><p>There may be some further restrictions specified in other attributes, for example the available
 connector types may not be suitable for all vehicles in the supported category.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>List of vehicle categories this charging location can support. For example, the same location
     can be suitable for charging passenger cars and motorcycles.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTruckRestrictions()">
<h3>getTruckRestrictions</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-evchargingtruckrestriction" title="class in com.here.sdk.search">EVChargingTruckRestriction</a></span> <span class="element-name">getTruckRestrictions</span>()</div>
<div class="block"><p>Gets the access restrictions for trucks and light commercial vehicles.
 </p><p>Restricted, only available to customers having a specific contract with HERE
 and if requested by including <code>EVChargingLocationFeature.TRUCK_RESTRICTIONS</code> in
 <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Access restrictions for trucks and light commercial vehicles.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOpeningHours()">
<h3>getOpeningHours</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-evchargingopeninghours" title="class in com.here.sdk.search">EVChargingOpeningHours</a></span> <span class="element-name">getOpeningHours</span>()</div>
<div class="block"><p>Gets the times when the EVSEs at the charging location can be accessed for charging.
 </p><p>Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The times when the EVSEs at the charging location can be accessed for charging.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRestrictions()">
<h3>getRestrictions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-evaccessrestrictionreason" title="enum class in com.here.sdk.search">EVAccessRestrictionReason</a>&gt;</span> <span class="element-name">getRestrictions</span>()</div>
<div class="block"><p>Gets the list of restrictions.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Reason(s) for restricted access.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupportPhoneNumber()">
<h3>getSupportPhoneNumber</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSupportPhoneNumber</span>()</div>
<div class="block"><p>Gets the phone number that EV drivers should call when need assistance at the charge location.
 </p><p>Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The phone number that EV drivers should call when need assistance at the charge location, in E.164 format.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTimeZone()">
<h3>getTimeZone</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTimeZone</span>()</div>
<div class="block"><p>Gets the time zone of the charging location. Based on IANA tzdata's TZ-values.
 </p><p>Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The time zone of the charging location. Based on IANA tzdata's TZ-values.</p></dd>
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
