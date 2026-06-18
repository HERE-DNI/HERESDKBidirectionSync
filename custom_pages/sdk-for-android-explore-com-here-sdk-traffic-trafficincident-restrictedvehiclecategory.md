---
title: "TrafficIncident.RestrictedVehicleCategory (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrafficIncident.RestrictedVehicleCategory.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-traffic-package-summary">com.here.sdk.traffic</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>&gt;
<div class="inheritance">com.here.sdk.traffic.TrafficIncident.RestrictedVehicleCategory</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-explore-trafficincident" title="class in com.here.sdk.traffic">TrafficIncident</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static enum </span><span class="element-name type-name-label">TrafficIncident.RestrictedVehicleCategory</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>&gt;</span></div>
<div class="block"><p>The vehicle categories that can be restricted.
 Note, a vehicle can belong to several categories (e.g. a passenger motor car
 belongs to <a href="sdk-for-android-explore-index#CAR"><code>CAR</code></a>, <a href="sdk-for-android-explore-index#MOTOR_VEHICLE"><code>MOTOR_VEHICLE</code></a>, and <a href="sdk-for-android-explore-index#ALL"><code>ALL</code></a>).
 A vehicle is restricted if it belongs to the category presented in the map <a href="sdk-for-android-explore-trafficincident#getVehicleRestrictions()"><code>TrafficIncident.getVehicleRestrictions()</code></a>
 and at least one of the vehicle properties is under the matching <a href="sdk-for-android-explore-trafficincident.vehiclerestriction" title="class in com.here.sdk.traffic"><code>TrafficIncident.VehicleRestriction</code></a>.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="inherited-list">

<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section class="constants-summary" id="enum-constant-summary">

<div class="caption"><span>Enum Constants</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Enum Constant</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#ALL">ALL</a></code></div>
<div class="col-last even-row-color">
<div class="block">All the vehicles are applicable for this category.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#BUS">BUS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Bus.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#CAR">CAR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Car.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#HEAVY_GOODS_VEHICLE">HEAVY_GOODS_VEHICLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Heavy goods vehicle (or large goods vehicle).</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#MOTOR_VEHICLE">MOTOR_VEHICLE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Motor vehicle.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#MOTORCYCLE">MOTORCYCLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Motorcycle.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#OTHER">OTHER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Other vehicles.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#TAXI">TAXI</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Taxi.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#TRAIN">TRAIN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Train.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#TRANSPORTING_ABNORMAL_SIZE_LOAD">TRANSPORTING_ABNORMAL_SIZE_LOAD</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Transporting an abnormal size load.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#TRANSPORTING_HAZARDOUS_GOODS">TRANSPORTING_HAZARDOUS_GOODS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Transporting hazardous goods.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#TRUCK">TRUCK</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Truck.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#VEHICLE_WITH_TRAILER">VEHICLE_WITH_TRAILER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Vehicle with trailer.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#values()">values</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section class="constant-details" id="enum-constant-detail">

<ul class="member-list">
<li>
<section class="detail" id="BUS">
<h3>BUS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">BUS</span></div>
<div class="block"><p>Bus.</p></div>
</section>
</li>
<li>
<section class="detail" id="CAR">
<h3>CAR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">CAR</span></div>
<div class="block"><p>Car.</p></div>
</section>
</li>
<li>
<section class="detail" id="HEAVY_GOODS_VEHICLE">
<h3>HEAVY_GOODS_VEHICLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">HEAVY_GOODS_VEHICLE</span></div>
<div class="block"><p>Heavy goods vehicle (or large goods vehicle).
 In the European Union heavy goods vehicle is any truck with a gross combination mass (GCM) of over 3,500 kg.</p></div>
</section>
</li>
<li>
<section class="detail" id="TRUCK">
<h3>TRUCK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">TRUCK</span></div>
<div class="block"><p>Truck.</p></div>
</section>
</li>
<li>
<section class="detail" id="MOTORCYCLE">
<h3>MOTORCYCLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">MOTORCYCLE</span></div>
<div class="block"><p>Motorcycle.</p></div>
</section>
</li>
<li>
<section class="detail" id="MOTOR_VEHICLE">
<h3>MOTOR_VEHICLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">MOTOR_VEHICLE</span></div>
<div class="block"><p>Motor vehicle. Definition: it is a self-propelled vehicle,
 that does not operate on rails and is used for the transportation of people or cargo.</p></div>
</section>
</li>
<li>
<section class="detail" id="TAXI">
<h3>TAXI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">TAXI</span></div>
<div class="block"><p>Taxi.</p></div>
</section>
</li>
<li>
<section class="detail" id="TRAIN">
<h3>TRAIN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">TRAIN</span></div>
<div class="block"><p>Train.</p></div>
</section>
</li>
<li>
<section class="detail" id="TRANSPORTING_ABNORMAL_SIZE_LOAD">
<h3>TRANSPORTING_ABNORMAL_SIZE_LOAD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">TRANSPORTING_ABNORMAL_SIZE_LOAD</span></div>
<div class="block"><p>Transporting an abnormal size load. See rules of the exact country that describe the exact parameters.</p></div>
</section>
</li>
<li>
<section class="detail" id="TRANSPORTING_HAZARDOUS_GOODS">
<h3>TRANSPORTING_HAZARDOUS_GOODS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">TRANSPORTING_HAZARDOUS_GOODS</span></div>
<div class="block"><p>Transporting hazardous goods.</p></div>
</section>
</li>
<li>
<section class="detail" id="VEHICLE_WITH_TRAILER">
<h3>VEHICLE_WITH_TRAILER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">VEHICLE_WITH_TRAILER</span></div>
<div class="block"><p>Vehicle with trailer.</p></div>
</section>
</li>
<li>
<section class="detail" id="OTHER">
<h3>OTHER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">OTHER</span></div>
<div class="block"><p>Other vehicles.</p></div>
</section>
</li>
<li>
<section class="detail" id="ALL">
<h3>ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">ALL</span></div>
<div class="block"><p>All the vehicles are applicable for this category.</p></div>
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
<section class="detail" id="values()">
<h3>values</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>[]</span> <span class="element-name">values</span>()</div>
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-trafficincident.restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
