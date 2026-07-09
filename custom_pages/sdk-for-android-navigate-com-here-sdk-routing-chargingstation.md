---
title: "ChargingStation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-chargingstation"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ChargingStation.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.ChargingStation</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">ChargingStation</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Data for an electric vehicle charging station.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#brand">brand</a></code></div>
<div className="col-last even-row-color">
<div className="block">Charging station brand.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#chargePointOperator">chargePointOperator</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Charging station charge-point-operator.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#connectorAttributes">connectorAttributes</a></code></div>
<div className="col-last even-row-color">
<div className="block">Details of the connector suggested to be used.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#id">id</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Identifier of this charging station.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#matchingEMobilityServiceProviders">matchingEMobilityServiceProviders</a></code></div>
<div className="col-last even-row-color">
<div className="block">List of matched E-Mobility Service Providers.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#name">name</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Human readable name of this charging station.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#%3Cinit%3E(java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes)">ChargingStation</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a> connectorAttributes)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#%3Cinit%3E(java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes,com.here.sdk.core.NameID,com.here.sdk.core.NameID,java.util.List)">ChargingStation</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a> connectorAttributes,
 <a href="sdk-for-android-navigate-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a> brand,
 <a href="sdk-for-android-navigate-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a> chargePointOperator,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a>&gt; matchingEMobilityServiceProviders)</code></div>
<div className="col-last odd-row-color">
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
<section className="detail" id="id">
<h3>id</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">id</span></div>
<div className="block"><p>Identifier of this charging station. It can only be null when custom charging
 stations from non-HERE datasets have been injected on the HERE platform.
 By default, with HERE datasets it is guranteed to be not null.</p></div>
</section>
</li>
<li>
<section className="detail" id="name">
<h3>name</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">name</span></div>
<div className="block"><p>Human readable name of this charging station. It can be null when there is no
 name associated with the station.</p></div>
</section>
</li>
<li>
<section className="detail" id="connectorAttributes">
<h3>connectorAttributes</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a></span> <span className="element-name">connectorAttributes</span></div>
<div className="block"><p>Details of the connector suggested to be used.</p></div>
</section>
</li>
<li>
<section className="detail" id="brand">
<h3>brand</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a></span> <span className="element-name">brand</span></div>
<div className="block"><p>Charging station brand.
 <a href="sdk-for-android-navigate-nameid#name"><code>NameID.name</code></a> reflect to charging station brand name.
 <a href="sdk-for-android-navigate-nameid#id"><code>NameID.id</code></a> reflect to charging station brand unique ID.</p></div>
</section>
</li>
<li>
<section className="detail" id="chargePointOperator">
<h3>chargePointOperator</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a></span> <span className="element-name">chargePointOperator</span></div>
<div className="block"><p>Charging station charge-point-operator.
 <a href="sdk-for-android-navigate-nameid#name"><code>NameID.name</code></a> reflect to charge-point-operator name.
 <a href="sdk-for-android-navigate-nameid#id"><code>NameID.id</code></a> reflect to charge-point-operator ID.</p></div>
</section>
</li>
<li>
<section className="detail" id="matchingEMobilityServiceProviders">
<h3>matchingEMobilityServiceProviders</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a>&gt;</span> <span className="element-name">matchingEMobilityServiceProviders</span></div>
<div className="block"><p>List of matched E-Mobility Service Providers.
 Populated only when <a href="sdk-for-android-navigate-electricvehicleoptions#evMobilityServiceProviderPreferences"><code>ElectricVehicleOptions.evMobilityServiceProviderPreferences</code></a> was set.
 This list reflects the subset of E-Mobility Service Providers supported by the charging station,
 from the list specified in the request parameter <a href="sdk-for-android-navigate-electricvehicleoptions#evMobilityServiceProviderPreferences"><code>ElectricVehicleOptions.evMobilityServiceProviderPreferences</code></a>.
 <a href="sdk-for-android-navigate-nameid#name"><code>NameID.name</code></a> in each list item reflect to E-Mobility Service Provider name.
 <a href="sdk-for-android-navigate-nameid#id"><code>NameID.id</code></a> in each list item reflect to E-Mobility Service Provider id.</p></div>
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
<section className="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes)">
<h3>ChargingStation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ChargingStation</span><wbr/><span className="parameters">(@Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a> connectorAttributes)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - <p>Identifier of this charging station. It can only be null when custom charging
 stations from non-HERE datasets have been injected on the HERE platform.
 By default, with HERE datasets it is guranteed to be not null.</p></dd>
<dd><code>name</code> - <p>Human readable name of this charging station. It can be null when there is no
 name associated with the station.</p></dd>
<dd><code>connectorAttributes</code> - <p>Details of the connector suggested to be used.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes,com.here.sdk.core.NameID,com.here.sdk.core.NameID,java.util.List)">
<h3>ChargingStation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ChargingStation</span><wbr/><span className="parameters">(@Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a> connectorAttributes,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a> brand,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a> chargePointOperator,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a>&gt; matchingEMobilityServiceProviders)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - <p>Identifier of this charging station. It can only be null when custom charging
 stations from non-HERE datasets have been injected on the HERE platform.
 By default, with HERE datasets it is guranteed to be not null.</p></dd>
<dd><code>name</code> - <p>Human readable name of this charging station. It can be null when there is no
 name associated with the station.</p></dd>
<dd><code>connectorAttributes</code> - <p>Details of the connector suggested to be used.</p></dd>
<dd><code>brand</code> - <p>Charging station brand.
 <a href="sdk-for-android-navigate-nameid#name"><code>NameID.name</code></a> reflect to charging station brand name.
 <a href="sdk-for-android-navigate-nameid#id"><code>NameID.id</code></a> reflect to charging station brand unique ID.</p></dd>
<dd><code>chargePointOperator</code> - <p>Charging station charge-point-operator.
 <a href="sdk-for-android-navigate-nameid#name"><code>NameID.name</code></a> reflect to charge-point-operator name.
 <a href="sdk-for-android-navigate-nameid#id"><code>NameID.id</code></a> reflect to charge-point-operator ID.</p></dd>
<dd><code>matchingEMobilityServiceProviders</code> - <p>List of matched E-Mobility Service Providers.
 Populated only when <a href="sdk-for-android-navigate-electricvehicleoptions#evMobilityServiceProviderPreferences"><code>ElectricVehicleOptions.evMobilityServiceProviderPreferences</code></a> was set.
 This list reflects the subset of E-Mobility Service Providers supported by the charging station,
 from the list specified in the request parameter <a href="sdk-for-android-navigate-electricvehicleoptions#evMobilityServiceProviderPreferences"><code>ElectricVehicleOptions.evMobilityServiceProviderPreferences</code></a>.
 <a href="sdk-for-android-navigate-nameid#name"><code>NameID.name</code></a> in each list item reflect to E-Mobility Service Provider name.
 <a href="sdk-for-android-navigate-nameid#id"><code>NameID.id</code></a> in each list item reflect to E-Mobility Service Provider id.</p></dd>
</dl>
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
