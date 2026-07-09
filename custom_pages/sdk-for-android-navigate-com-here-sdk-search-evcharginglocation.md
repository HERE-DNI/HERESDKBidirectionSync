---
title: "EVChargingLocation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-evcharginglocation"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- EVChargingLocation.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.search.EVChargingLocation</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">EVChargingLocation</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>An electric vehicle (EV) charging location.
 The semantics generally follow the OCPI 2.2.1 standard.
 Known EV-specific acronyms:
 <ul>
<li>EV: Electric Vehicle</li>
<li>OCPI: Open Charge Point Interface (a standard with a rather wide adoption worldwide, https://evroaming.org/)</li>
<li>CPO: Charge Point Operator (company that runs the EV charging location)</li>
<li>eMSP: e-Mobility Service Provider (customer-facing company)</li>
<li>EVSE: Electric Vehicle Supply Equipment (the actual charger that can charge one car at a time)</li>
</ul>
A charging location includes a collection of one or more EV supply equipment (EVSE) instances.
 Typically, the charging location is the exact location of the group of EVSEs,
 simplified to a single point, but it can also be the entrance of a parking structure
 which contains these EVSEs.
 Each EVSE supports more precise position, where applicable.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getID()">
<h3>getID</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getID</span>()</div>
<div className="block"><p>Gets the unique identifier of the charging location.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>A unique identifier of the charging location.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getName()">
<h3>getName</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getName</span>()</div>
<div className="block"><p>Gets the display name of the charging location, if available.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Display name of the charging location, if available.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCpoID()">
<h3>getCpoID</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getCpoID</span>()</div>
<div className="block"><p>Gets the CPO's own ID for the location.
 This ID may be relevant for some clients to map the charging location data to their own
 or 3rd party systems.
 Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>CPO's own ID for the location.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getEvChargingOperator()">
<h3>getEvChargingOperator</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evchargingoperator" title="class in com.here.sdk.search">EVChargingOperator</a></span> <span className="element-name">getEvChargingOperator</span>()</div>
<div className="block"><p>Gets the operator of the charging point, if available.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Operator of the charging point, if available.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getEvChargingSubOperator()">
<h3>getEvChargingSubOperator</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evchargingoperator" title="class in com.here.sdk.search">EVChargingOperator</a></span> <span className="element-name">getEvChargingSubOperator</span>()</div>
<div className="block"><p>Gets the suboperator of the charging point, if available.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Suboperator of the charging point, if available.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getEMobilityServiceProviders()">
<h3>getEMobilityServiceProviders</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evchargingoperator" title="class in com.here.sdk.search">EVChargingOperator</a>&gt;</span> <span className="element-name">getEMobilityServiceProviders</span>()</div>
<div className="block"><p>Gets the list of eMSPs with a roaming agreement enabling access to the EV charging location.
 Available only if <code>EVChargingLocationFeature.EMSPS</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise empty.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>eMSPs with a roaming agreement enabling access to the EV charging location.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getFacilityTypes()">
<h3>getFacilityTypes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-facilitytype" title="enum class in com.here.sdk.search">FacilityType</a>&gt;</span> <span className="element-name">getFacilityTypes</span>()</div>
<div className="block"><p>Gets the list of facilities available at the charging location, for example
 hotel, wifi, parking lot etc.
 Available only if <code>EVChargingLocationFeature.NEARBY</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise empty.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Facilities available at the charging location, for example hotel, wifi, parking lot etc.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getParkingType()">
<h3>getParkingType</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-parkingtype" title="enum class in com.here.sdk.search">ParkingType</a></span> <span className="element-name">getParkingType</span>()</div>
<div className="block"><p>Gets the type of parking at the charging location.
 Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The type of parking at the charging location.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getEnergyMix()">
<h3>getEnergyMix</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-energymix" title="class in com.here.sdk.search">EnergyMix</a></span> <span className="element-name">getEnergyMix</span>()</div>
<div className="block"><p>Gets the details on the energy supplied at the charging location.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Details on the energy supplied at the charging location.
     Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
     <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getEvses()">
<h3>getEvses</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evseinfo" title="class in com.here.sdk.search">EVSEInfo</a>&gt;</span> <span className="element-name">getEvses</span>()</div>
<div className="block"><p>Gets the list of EVSEs at the charging station.
 Available only if <code>EVChargingLocationFeature.EVSES</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise empty.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>List of EVSEs at the charging station.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTariffs()">
<h3>getTariffs</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evchargingtariff" title="class in com.here.sdk.search">EVChargingTariff</a>&gt;</span> <span className="element-name">getTariffs</span>()</div>
<div className="block"><p>Gets the list of tariffs or price plans for the connectors of the charging station.
 Tariffs are typically connector-type specific. Hence, they are always linked with connectors
 and/or connector groups, by indexes to this list.
 This property is set only when data is available and when <code>EVSearchOptions.additional_features</code>
 include either <code>EVChargingLocationFeature.EVSES</code> or <code>EVChargingLocationFeature.CONNECTOR_GROUPS</code>.
 By default, the list includes tariffs for ad-hoc charging, per connector type,
 for EVSEs that accept payment without registering.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>List of tariffs or price plans for the connectors of the charging station.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getConnectorGroups()">
<h3>getConnectorGroups</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evchargingconnectorgroup" title="class in com.here.sdk.search">EVChargingConnectorGroup</a>&gt;</span> <span className="element-name">getConnectorGroups</span>()</div>
<div className="block"><p>Gets the connector groups for the location.
 Provides an overview of the charging connectors in the location by type and power.
 Available only if <code>EVChargingLocationFeature.CONNECTOR_GROUPS</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise empty.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Connector groups for the location.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSupportedVehicles()">
<h3>getSupportedVehicles</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evchargingvehiclecategory" title="enum class in com.here.sdk.search">EVChargingVehicleCategory</a>&gt;</span> <span className="element-name">getSupportedVehicles</span>()</div>
<div className="block"><p>Gets the list of vehicle categories this charging location can support. For example,
 the same location can be suitable for charging passenger cars and motorcycles.
 There may be some further restrictions specified in other attributes, for example the available
 connector types may not be suitable for all vehicles in the supported category.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>List of vehicle categories this charging location can support. For example, the same location
     can be suitable for charging passenger cars and motorcycles.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTruckRestrictions()">
<h3>getTruckRestrictions</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evchargingtruckrestriction" title="class in com.here.sdk.search">EVChargingTruckRestriction</a></span> <span className="element-name">getTruckRestrictions</span>()</div>
<div className="block"><p>Gets the access restrictions for trucks and light commercial vehicles.
 Restricted, only available to customers having a specific contract with HERE
 and if requested by including <code>EVChargingLocationFeature.TRUCK_RESTRICTIONS</code> in
 <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Access restrictions for trucks and light commercial vehicles.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOpeningHours()">
<h3>getOpeningHours</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evchargingopeninghours" title="class in com.here.sdk.search">EVChargingOpeningHours</a></span> <span className="element-name">getOpeningHours</span>()</div>
<div className="block"><p>Gets the times when the EVSEs at the charging location can be accessed for charging.
 Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The times when the EVSEs at the charging location can be accessed for charging.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRestrictions()">
<h3>getRestrictions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-evaccessrestrictionreason" title="enum class in com.here.sdk.search">EVAccessRestrictionReason</a>&gt;</span> <span className="element-name">getRestrictions</span>()</div>
<div className="block"><p>Gets the list of restrictions.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Reason(s) for restricted access.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSupportPhoneNumber()">
<h3>getSupportPhoneNumber</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getSupportPhoneNumber</span>()</div>
<div className="block"><p>Gets the phone number that EV drivers should call when need assistance at the charge location.
 Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The phone number that EV drivers should call when need assistance at the charge location, in E.164 format.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTimeZone()">
<h3>getTimeZone</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getTimeZone</span>()</div>
<div className="block"><p>Gets the time zone of the charging location. Based on IANA tzdata's TZ-values.
 Available only if <code>EVChargingLocationFeature.LOCATION_INFO</code> is included in
 <code>EVSearchOptions.additional_features</code>, otherwise <code>null</code>.</p></div>
<dl className="notes">
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
</div>



</div>
`
}</HTMLBlock>
