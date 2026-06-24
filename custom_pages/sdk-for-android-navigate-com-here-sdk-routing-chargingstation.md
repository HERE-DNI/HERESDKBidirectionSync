---
title: "ChargingStation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-chargingstation"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- ChargingStation.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.ChargingStation</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">ChargingStation</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Data for an electric vehicle charging station.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-nameid" title="class in com.here.sdk.core">NameID</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#brand">brand</a></code></div>
<div class="col-last even-row-color">
<div class="block">Charging station brand.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-nameid" title="class in com.here.sdk.core">NameID</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#chargePointOperator">chargePointOperator</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Charging station charge-point-operator.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#connectorAttributes">connectorAttributes</a></code></div>
<div class="col-last even-row-color">
<div class="block">Details of the connector suggested to be used.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#id">id</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Identifier of this charging station.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-nameid" title="class in com.here.sdk.core">NameID</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#matchingEMobilityServiceProviders">matchingEMobilityServiceProviders</a></code></div>
<div class="col-last even-row-color">
<div class="block">List of matched E-Mobility Service Providers.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#name">name</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Human readable name of this charging station.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#%3Cinit%3E(java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes)">ChargingStation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-navigate-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a> connectorAttributes)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#%3Cinit%3E(java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes,com.here.sdk.core.NameID,com.here.sdk.core.NameID,java.util.List)">ChargingStation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-navigate-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a> connectorAttributes,
 <a href="sdk-for-android-navigate-nameid" title="class in com.here.sdk.core">NameID</a> brand,
 <a href="sdk-for-android-navigate-nameid" title="class in com.here.sdk.core">NameID</a> chargePointOperator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-nameid" title="class in com.here.sdk.core">NameID</a>&gt; matchingEMobilityServiceProviders)</code></div>
<div class="col-last odd-row-color">
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation#hashCode()">hashCode</a>()</code></div>

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
<section class="detail" id="id">
<h3>id</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">id</span></div>
<div class="block"><p>Identifier of this charging station. It can only be null when custom charging
 stations from non-HERE datasets have been injected on the HERE platform.
 By default, with HERE datasets it is guranteed to be not null.</p></div>
</section>
</li>
<li>
<section class="detail" id="name">
<h3>name</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">name</span></div>
<div class="block"><p>Human readable name of this charging station. It can be null when there is no
 name associated with the station.</p></div>
</section>
</li>
<li>
<section class="detail" id="connectorAttributes">
<h3>connectorAttributes</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a></span> <span class="element-name">connectorAttributes</span></div>
<div class="block"><p>Details of the connector suggested to be used.</p></div>
</section>
</li>
<li>
<section class="detail" id="brand">
<h3>brand</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-nameid" title="class in com.here.sdk.core">NameID</a></span> <span class="element-name">brand</span></div>
<div class="block"><p>Charging station brand.
 <a href="sdk-for-android-navigate-nameid#name"><code>NameID.name</code></a> reflect to charging station brand name.
 <a href="sdk-for-android-navigate-nameid#id"><code>NameID.id</code></a> reflect to charging station brand unique ID.</p></div>
</section>
</li>
<li>
<section class="detail" id="chargePointOperator">
<h3>chargePointOperator</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-nameid" title="class in com.here.sdk.core">NameID</a></span> <span class="element-name">chargePointOperator</span></div>
<div class="block"><p>Charging station charge-point-operator.
 <a href="sdk-for-android-navigate-nameid#name"><code>NameID.name</code></a> reflect to charge-point-operator name.
 <a href="sdk-for-android-navigate-nameid#id"><code>NameID.id</code></a> reflect to charge-point-operator ID.</p></div>
</section>
</li>
<li>
<section class="detail" id="matchingEMobilityServiceProviders">
<h3>matchingEMobilityServiceProviders</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-nameid" title="class in com.here.sdk.core">NameID</a>&gt;</span> <span class="element-name">matchingEMobilityServiceProviders</span></div>
<div class="block"><p>List of matched E-Mobility Service Providers.
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
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes)">
<h3>ChargingStation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ChargingStation</span><wbr/><span class="parameters">(@Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @Nullable
 <a href="sdk-for-android-navigate-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a> connectorAttributes)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes,com.here.sdk.core.NameID,com.here.sdk.core.NameID,java.util.List)">
<h3>ChargingStation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ChargingStation</span><wbr/><span class="parameters">(@Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @Nullable
 <a href="sdk-for-android-navigate-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a> connectorAttributes,
 @Nullable
 <a href="sdk-for-android-navigate-nameid" title="class in com.here.sdk.core">NameID</a> brand,
 @Nullable
 <a href="sdk-for-android-navigate-nameid" title="class in com.here.sdk.core">NameID</a> chargePointOperator,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-nameid" title="class in com.here.sdk.core">NameID</a>&gt; matchingEMobilityServiceProviders)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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
