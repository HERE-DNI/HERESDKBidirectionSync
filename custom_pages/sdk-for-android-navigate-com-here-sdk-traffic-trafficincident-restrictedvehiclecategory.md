---
title: "TrafficIncident.RestrictedVehicleCategory (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrafficIncident.RestrictedVehicleCategory.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.traffic</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>&gt;
<div className="inheritance">com.here.sdk.traffic.TrafficIncident.RestrictedVehicleCategory</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident" title="class in com.here.sdk.traffic">TrafficIncident</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static enum </span><span className="element-name type-name-label">TrafficIncident.RestrictedVehicleCategory</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>&gt;</span></div>
<div className="block"><p>The vehicle categories that can be restricted.
 Note, a vehicle can belong to several categories (e.g. a passenger motor car
 belongs to <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#CAR"><code>CAR</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#MOTOR_VEHICLE"><code>MOTOR_VEHICLE</code></a>, and <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#ALL"><code>ALL</code></a>).
 A vehicle is restricted if it belongs to the category presented in the map <a href="sdk-for-android-navigate-trafficincident#getVehicleRestrictions()"><code>TrafficIncident.getVehicleRestrictions()</code></a>
 and at least one of the vehicle properties is under the matching <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-vehiclerestriction" title="class in com.here.sdk.traffic"><code>TrafficIncident.VehicleRestriction</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="inherited-list">

<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section className="constants-summary" id="enum-constant-summary">

<div className="caption"><span>Enum Constants</span></div>
<div className="summary-table two-column-summary">


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#ALL">ALL</a></code></div>
<div className="col-last even-row-color">
<div className="block">All the vehicles are applicable for this category.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#BUS">BUS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Bus.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#CAR">CAR</a></code></div>
<div className="col-last even-row-color">
<div className="block">Car.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#HEAVY_GOODS_VEHICLE">HEAVY_GOODS_VEHICLE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Heavy goods vehicle (or large goods vehicle).</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#MOTOR_VEHICLE">MOTOR_VEHICLE</a></code></div>
<div className="col-last even-row-color">
<div className="block">Motor vehicle.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#MOTORCYCLE">MOTORCYCLE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Motorcycle.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#OTHER">OTHER</a></code></div>
<div className="col-last even-row-color">
<div className="block">Other vehicles.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#TAXI">TAXI</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Taxi.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#TRAIN">TRAIN</a></code></div>
<div className="col-last even-row-color">
<div className="block">Train.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#TRANSPORTING_ABNORMAL_SIZE_LOAD">TRANSPORTING_ABNORMAL_SIZE_LOAD</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Transporting an abnormal size load.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#TRANSPORTING_HAZARDOUS_GOODS">TRANSPORTING_HAZARDOUS_GOODS</a></code></div>
<div className="col-last even-row-color">
<div className="block">Transporting hazardous goods.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#TRUCK">TRUCK</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Truck.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory#VEHICLE_WITH_TRAILER">VEHICLE_WITH_TRAILER</a></code></div>
<div className="col-last even-row-color">
<div className="block">Vehicle with trailer.</div>
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
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section className="constant-details" id="enum-constant-detail">

<ul className="member-list">
<li>
<section className="detail" id="BUS">
<h3>BUS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">BUS</span></div>
<div className="block"><p>Bus.</p></div>
</section>
</li>
<li>
<section className="detail" id="CAR">
<h3>CAR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">CAR</span></div>
<div className="block"><p>Car.</p></div>
</section>
</li>
<li>
<section className="detail" id="HEAVY_GOODS_VEHICLE">
<h3>HEAVY_GOODS_VEHICLE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">HEAVY_GOODS_VEHICLE</span></div>
<div className="block"><p>Heavy goods vehicle (or large goods vehicle).
 In the European Union heavy goods vehicle is any truck with a gross combination mass (GCM) of over 3,500 kg.</p></div>
</section>
</li>
<li>
<section className="detail" id="TRUCK">
<h3>TRUCK</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">TRUCK</span></div>
<div className="block"><p>Truck.</p></div>
</section>
</li>
<li>
<section className="detail" id="MOTORCYCLE">
<h3>MOTORCYCLE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">MOTORCYCLE</span></div>
<div className="block"><p>Motorcycle.</p></div>
</section>
</li>
<li>
<section className="detail" id="MOTOR_VEHICLE">
<h3>MOTOR_VEHICLE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">MOTOR_VEHICLE</span></div>
<div className="block"><p>Motor vehicle. Definition: it is a self-propelled vehicle,
 that does not operate on rails and is used for the transportation of people or cargo.</p></div>
</section>
</li>
<li>
<section className="detail" id="TAXI">
<h3>TAXI</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">TAXI</span></div>
<div className="block"><p>Taxi.</p></div>
</section>
</li>
<li>
<section className="detail" id="TRAIN">
<h3>TRAIN</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">TRAIN</span></div>
<div className="block"><p>Train.</p></div>
</section>
</li>
<li>
<section className="detail" id="TRANSPORTING_ABNORMAL_SIZE_LOAD">
<h3>TRANSPORTING_ABNORMAL_SIZE_LOAD</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">TRANSPORTING_ABNORMAL_SIZE_LOAD</span></div>
<div className="block"><p>Transporting an abnormal size load. See rules of the exact country that describe the exact parameters.</p></div>
</section>
</li>
<li>
<section className="detail" id="TRANSPORTING_HAZARDOUS_GOODS">
<h3>TRANSPORTING_HAZARDOUS_GOODS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">TRANSPORTING_HAZARDOUS_GOODS</span></div>
<div className="block"><p>Transporting hazardous goods.</p></div>
</section>
</li>
<li>
<section className="detail" id="VEHICLE_WITH_TRAILER">
<h3>VEHICLE_WITH_TRAILER</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">VEHICLE_WITH_TRAILER</span></div>
<div className="block"><p>Vehicle with trailer.</p></div>
</section>
</li>
<li>
<section className="detail" id="OTHER">
<h3>OTHER</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">OTHER</span></div>
<div className="block"><p>Other vehicles.</p></div>
</section>
</li>
<li>
<section className="detail" id="ALL">
<h3>ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">ALL</span></div>
<div className="block"><p>All the vehicles are applicable for this category.</p></div>
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
<section className="detail" id="values()">
<h3>values</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>[]</span> <span className="element-name">values</span>()</div>
<div className="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
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
