---
title: "VehicleProfile (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VehicleProfile.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.transport</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.transport.VehicleProfile</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public final class </span><span className="element-name type-name-label">VehicleProfile</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use <code>sdk.transport.TransportSpecification</code> instead.</p></div>
</div>
<div className="block"><p>A vehicle profile describes the vehicle being used with the HSDK.
 The profile is planned to be used as single source of information describing the vehicle.
 Current modules that use this profile:
 <ul>
<li>Navigation: Tracking mode for truck related vehicle restrictions.</li>
</ul>
<strong>Note:</strong> This is a beta release of this vehicle profile, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases or even become unsupported, without a
 deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile#axleCount">axleCount</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Defines total number of axles in the vehicle.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile#grossWeightInKilograms">grossWeightInKilograms</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Vehicle weight including trailers and shipped goods in kilograms.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile#hazardousMaterials">hazardousMaterials</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Specifies a list of hazardous materials shipped in the vehicle.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile#heightInCentimeters">heightInCentimeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Vehicle height in centimeters.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile#lengthInCentimeters">lengthInCentimeters</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Vehicle length in centimeters.</div>
</div>
<div className="col-first odd-row-color"><code>int</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile#trailerCount">trailerCount</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Defines number of trailers attached to the vehicle.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile#truckCategory">truckCategory</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Defines the truck category.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile#tunnelCategory">tunnelCategory</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Specifies the tunnel categories to restrict certain route links.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-vehicletype" title="enum class in com.here.sdk.transport">VehicleType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile#vehicleType">vehicleType</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Defines the vehicle type.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile#weightPerAxleInKilograms">weightPerAxleInKilograms</a></code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Vehicle weight per axle in kilograms.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile#widthInCentimeters">widthInCentimeters</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block">Vehicle width in centimeters.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile#%3Cinit%3E(com.here.sdk.transport.VehicleType)">VehicleProfile</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-transport-vehicletype" title="enum class in com.here.sdk.transport">VehicleType</a> vehicleType)</code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span></div>
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
<section className="detail" id="vehicleType">
<h3>vehicleType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-vehicletype" title="enum class in com.here.sdk.transport">VehicleType</a></span> <span className="element-name">vehicleType</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Defines the vehicle type.</p></div>
</section>
</li>
<li>
<section className="detail" id="truckCategory">
<h3>truckCategory</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></span> <span className="element-name">truckCategory</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Defines the truck category.
 Only used when the <a href="sdk-for-android-navigate-com-here-sdk-transport-vehicleprofile#vehicleType"><code>vehicleType</code></a> is <a href="sdk-for-android-navigate-vehicletype#TRUCK"><code>VehicleType.TRUCK</code></a>
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="trailerCount">
<h3>trailerCount</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">trailerCount</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Defines number of trailers attached to the vehicle. The provided value must be in the range
 [0, 255]. When not set, possible trailer count restrictions will not be taken into consideration
 for route calculation. By default, it is 0.</p></div>
</section>
</li>
<li>
<section className="detail" id="hazardousMaterials">
<h3>hazardousMaterials</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt;</span> <span className="element-name">hazardousMaterials</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Specifies a list of hazardous materials shipped in the vehicle.
 Refer to <a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport"><code>HazardousMaterial</code></a> for the available options.</p></div>
</section>
</li>
<li>
<section className="detail" id="tunnelCategory">
<h3>tunnelCategory</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></span> <span className="element-name">tunnelCategory</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Specifies the tunnel categories to restrict certain route links.
 The route will pass only through tunnels of a less strict category.
 Refer to <a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport"><code>TunnelCategory</code></a> for the available options.</p></div>
</section>
</li>
<li>
<section className="detail" id="axleCount">
<h3>axleCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">axleCount</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Defines total number of axles in the vehicle. The provided value must be greater than or
 equal to 2. When not set, possible axle count restrictions will not be taken into
 consideration for route calculation. By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="grossWeightInKilograms">
<h3>grossWeightInKilograms</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">grossWeightInKilograms</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Vehicle weight including trailers and shipped goods in kilograms.
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="heightInCentimeters">
<h3>heightInCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">heightInCentimeters</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Vehicle height in centimeters. The provided value must be in the range [0, 5000].
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="lengthInCentimeters">
<h3>lengthInCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">lengthInCentimeters</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Vehicle length in centimeters. The provided value must be in the range [0, 30000].
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="widthInCentimeters">
<h3>widthInCentimeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">widthInCentimeters</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Vehicle width in centimeters. The provided value must be in the range [0, 5000].
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section className="detail" id="weightPerAxleInKilograms">
<h3>weightPerAxleInKilograms</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">weightPerAxleInKilograms</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Vehicle weight per axle in kilograms. The provided value must be greater or equal to 0.
 When not set, possible weight per axle restrictions will not be taken into
 consideration for route calculation. By default, it is not set.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.transport.VehicleType)">
<h3>VehicleProfile</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">VehicleProfile</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-transport-vehicletype" title="enum class in com.here.sdk.transport">VehicleType</a> vehicleType)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>vehicleType</code> - <p>Defines the vehicle type.</p></dd>
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
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
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
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span></div>
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
