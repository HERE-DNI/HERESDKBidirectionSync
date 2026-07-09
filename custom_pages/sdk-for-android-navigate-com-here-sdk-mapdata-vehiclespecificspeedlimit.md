---
title: "VehicleSpecificSpeedLimit (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-vehiclespecificspeedlimit"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VehicleSpecificSpeedLimit.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapdata.VehicleSpecificSpeedLimit</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">VehicleSpecificSpeedLimit</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Speed limit regulation specific to a vehicle type.
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



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclespecificspeedlimit#builtUpAreaMaxOverrideSpeedInMetersPerSecond">builtUpAreaMaxOverrideSpeedInMetersPerSecond</a></code></div>
<div className="col-last even-row-color">
<div className="block">Max Override Speed indicates the maximum speed a commercial vehicle may travel within a BUA.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclerestrictioncondition" title="class in com.here.sdk.mapdata">VehicleRestrictionCondition</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclespecificspeedlimit#condition">condition</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Conditions under which this speed limit is active.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclespecificspeedlimit#isAdvisory">isAdvisory</a></code></div>
<div className="col-last even-row-color">
<div className="block">If true, this speed limit is advisory rather than legally enforced.</div>
</div>
<div className="col-first odd-row-color"><code>double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclespecificspeedlimit#speedLimitInMetersPerSecond">speedLimitInMetersPerSecond</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Maximum permitted speed in meters per second.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclespecificspeedlimit#%3Cinit%3E(double,boolean,com.here.sdk.mapdata.VehicleRestrictionCondition)">VehicleSpecificSpeedLimit</a><wbr/>(double speedLimitInMetersPerSecond,
 boolean isAdvisory,
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclerestrictioncondition" title="class in com.here.sdk.mapdata">VehicleRestrictionCondition</a> condition)</code></div>
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
<section className="detail" id="speedLimitInMetersPerSecond">
<h3>speedLimitInMetersPerSecond</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">speedLimitInMetersPerSecond</span></div>
<div className="block"><p>Maximum permitted speed in meters per second.</p></div>
</section>
</li>
<li>
<section className="detail" id="isAdvisory">
<h3>isAdvisory</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isAdvisory</span></div>
<div className="block"><p>If true, this speed limit is advisory rather than legally enforced.</p></div>
</section>
</li>
<li>
<section className="detail" id="builtUpAreaMaxOverrideSpeedInMetersPerSecond">
<h3>builtUpAreaMaxOverrideSpeedInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">builtUpAreaMaxOverrideSpeedInMetersPerSecond</span></div>
<div className="block"><p>Max Override Speed indicates the maximum speed a commercial vehicle may travel within a BUA.
 Could be 0 if unlimited.
 A <code>null</code> value means the speed limit is not affected by the BUA override or not present.</p></div>
</section>
</li>
<li>
<section className="detail" id="condition">
<h3>condition</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclerestrictioncondition" title="class in com.here.sdk.mapdata">VehicleRestrictionCondition</a></span> <span className="element-name">condition</span></div>
<div className="block"><p>Conditions under which this speed limit is active.</p></div>
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
<section className="detail" id="&lt;init&gt;(double,boolean,com.here.sdk.mapdata.VehicleRestrictionCondition)">
<h3>VehicleSpecificSpeedLimit</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">VehicleSpecificSpeedLimit</span><wbr/><span className="parameters">(double speedLimitInMetersPerSecond,
 boolean isAdvisory,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-vehiclerestrictioncondition" title="class in com.here.sdk.mapdata">VehicleRestrictionCondition</a> condition)</span></div>
<div className="block"><p>Creates a new instance with specified parameters.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>speedLimitInMetersPerSecond</code> - <p>Maximum permitted speed in meters per second.</p></dd>
<dd><code>isAdvisory</code> - <p>If true, this speed limit is advisory rather than legally enforced.</p></dd>
<dd><code>condition</code> - <p>Conditions under which this speed limit is active.</p></dd>
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
