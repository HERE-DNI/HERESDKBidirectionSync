---
title: "VehicleProfileRestriction (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-vehicleprofilerestriction"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VehicleProfileRestriction.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapdata.VehicleProfileRestriction</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">VehicleProfileRestriction</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Physical and cargo profile of a vehicle that triggers a regulation.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-hazardousmaterialtype" title="enum class in com.here.sdk.mapdata">HazardousMaterialType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicleprofilerestriction#hazardousMaterial">hazardousMaterial</a></code></div>
<div className="col-last even-row-color">
<div className="block">Hazardous material condition associated with this profile.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicletypecondition" title="enum class in com.here.sdk.mapdata">VehicleTypeCondition</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicleprofilerestriction#requestedVehicleType">requestedVehicleType</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Vehicle type to which this restriction applies.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicleprofilerestriction#requiredAmountOfTrailers">requiredAmountOfTrailers</a></code></div>
<div className="col-last even-row-color">
<div className="block">Trailer count limits.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicleprofilerestriction#requiredGrossWeightInKilograms">requiredGrossWeightInKilograms</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Gross weight limits in kilograms.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicleprofilerestriction#requiredWeightInKilograms">requiredWeightInKilograms</a></code></div>
<div className="col-last even-row-color">
<div className="block">Weight limits in kilograms.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicleprofilerestriction#%3Cinit%3E(com.here.sdk.core.IntegerRange,com.here.sdk.core.IntegerRange,com.here.sdk.core.IntegerRange,com.here.sdk.mapdata.HazardousMaterialType)">VehicleProfileRestriction</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a> requiredWeightInKilograms,
 <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a> requiredGrossWeightInKilograms,
 <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a> requiredAmountOfTrailers,
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-hazardousmaterialtype" title="enum class in com.here.sdk.mapdata">HazardousMaterialType</a> hazardousMaterial)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance with specified parameters.</div>
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
<section className="detail" id="requestedVehicleType">
<h3>requestedVehicleType</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehicletypecondition" title="enum class in com.here.sdk.mapdata">VehicleTypeCondition</a></span> <span className="element-name">requestedVehicleType</span></div>
<div className="block"><p>Vehicle type to which this restriction applies.</p></div>
</section>
</li>
<li>
<section className="detail" id="requiredWeightInKilograms">
<h3>requiredWeightInKilograms</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span className="element-name">requiredWeightInKilograms</span></div>
<div className="block"><p>Weight limits in kilograms.</p></div>
</section>
</li>
<li>
<section className="detail" id="requiredGrossWeightInKilograms">
<h3>requiredGrossWeightInKilograms</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span className="element-name">requiredGrossWeightInKilograms</span></div>
<div className="block"><p>Gross weight limits in kilograms.</p></div>
</section>
</li>
<li>
<section className="detail" id="requiredAmountOfTrailers">
<h3>requiredAmountOfTrailers</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span className="element-name">requiredAmountOfTrailers</span></div>
<div className="block"><p>Trailer count limits.</p></div>
</section>
</li>
<li>
<section className="detail" id="hazardousMaterial">
<h3>hazardousMaterial</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-hazardousmaterialtype" title="enum class in com.here.sdk.mapdata">HazardousMaterialType</a></span> <span className="element-name">hazardousMaterial</span></div>
<div className="block"><p>Hazardous material condition associated with this profile.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.IntegerRange,com.here.sdk.core.IntegerRange,com.here.sdk.core.IntegerRange,com.here.sdk.mapdata.HazardousMaterialType)">
<h3>VehicleProfileRestriction</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">VehicleProfileRestriction</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a> requiredWeightInKilograms,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a> requiredGrossWeightInKilograms,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a> requiredAmountOfTrailers,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-hazardousmaterialtype" title="enum class in com.here.sdk.mapdata">HazardousMaterialType</a> hazardousMaterial)</span></div>
<div className="block"><p>Creates a new instance with specified parameters.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>requiredWeightInKilograms</code> - <p>Weight limits in kilograms.</p></dd>
<dd><code>requiredGrossWeightInKilograms</code> - <p>Gross weight limits in kilograms.</p></dd>
<dd><code>requiredAmountOfTrailers</code> - <p>Trailer count limits.</p></dd>
<dd><code>hazardousMaterial</code> - <p>Hazardous material condition associated with this profile.</p></dd>
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
