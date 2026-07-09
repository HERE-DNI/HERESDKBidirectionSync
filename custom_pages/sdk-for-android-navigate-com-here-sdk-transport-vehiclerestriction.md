---
title: "VehicleRestriction (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VehicleRestriction.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.transport</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.transport.VehicleRestriction</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">VehicleRestriction</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents a vehicle restriction.
 Any non <code>null</code> field adds more details to the restriction.
 A general truck restriction is represented with <code>null</code> values for
 fields <code>restriction</code> and
 <code>hazmatRestriction</code>.
 <strong>Note:</strong> This is a beta release of this feature.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#appliesToDelivery">appliesToDelivery</a></code></div>
<div className="col-last even-row-color">
<div className="block">Flag indicating whether this restriction applies to delivery vehicles.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#axleCount">axleCount</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The axle count for which the current restriction applies.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#axleCountInGroup">axleCountInGroup</a></code></div>
<div className="col-last even-row-color">
<div className="block">Number of axles in a group for which the current restriction applies.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterialrestriction" title="class in com.here.sdk.transport">HazardousMaterialRestriction</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#hazmatRestriction">hazmatRestriction</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Restriction on transport of hazardous materials and max allowed tunnel category.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-specificrestriction" title="class in com.here.sdk.transport">SpecificRestriction</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#restriction">restriction</a></code></div>
<div className="col-last even-row-color">
<div className="block">A <code>SpecificRestriction</code> defines what type of restriction applies (weight, height, etc.)
 and the range of allowed values.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-timerestriction" title="class in com.here.sdk.transport">TimeRestriction</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#timeRestriction">timeRestriction</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Restriction applies during specific time.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#trailerCount">trailerCount</a></code></div>
<div className="col-last even-row-color">
<div className="block">Number of trailers for which the restriction applies.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#truckCategory">truckCategory</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Restriction applies to a specific truck category.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#weather">weather</a></code></div>
<div className="col-last even-row-color">
<div className="block">Type of weather in which restriction applies.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#%3Cinit%3E()">VehicleRestriction</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates an uncoditional general restriction.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-transport-vehiclerestriction#%3Cinit%3E(com.here.sdk.transport.SpecificRestriction)">VehicleRestriction</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-transport-specificrestriction" title="class in com.here.sdk.transport">SpecificRestriction</a> restriction)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates an unconditional restriction.</div>
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
<section className="detail" id="restriction">
<h3>restriction</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-specificrestriction" title="class in com.here.sdk.transport">SpecificRestriction</a></span> <span className="element-name">restriction</span></div>
<div className="block"><p>A <code>SpecificRestriction</code> defines what type of restriction applies (weight, height, etc.)
 and the range of allowed values.</p></div>
</section>
</li>
<li>
<section className="detail" id="hazmatRestriction">
<h3>hazmatRestriction</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterialrestriction" title="class in com.here.sdk.transport">HazardousMaterialRestriction</a></span> <span className="element-name">hazmatRestriction</span></div>
<div className="block"><p>Restriction on transport of hazardous materials and max allowed tunnel category.
 For example, (FLAMMABLE, TunnelCategory.D) means, a restriction applying for trucks
 carrying flammable materials are not allowed to enter tunnels category D and E -
 (TunnelCategory.B and TunnelCategory.C allowed).</p></div>
</section>
</li>
<li>
<section className="detail" id="timeRestriction">
<h3>timeRestriction</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-timerestriction" title="class in com.here.sdk.transport">TimeRestriction</a></span> <span className="element-name">timeRestriction</span></div>
<div className="block"><p>Restriction applies during specific time.</p></div>
</section>
</li>
<li>
<section className="detail" id="appliesToDelivery">
<h3>appliesToDelivery</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">appliesToDelivery</span></div>
<div className="block"><p>Flag indicating whether this restriction applies to delivery vehicles.
 <ul>
<li><code>false</code> means delivery is allowed into this restricted street.</li>
<li><code>true</code> means delivery is NOT allowed into this restricted street.</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="weather">
<h3>weather</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></span> <span className="element-name">weather</span></div>
<div className="block"><p>Type of weather in which restriction applies.</p></div>
</section>
</li>
<li>
<section className="detail" id="truckCategory">
<h3>truckCategory</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></span> <span className="element-name">truckCategory</span></div>
<div className="block"><p>Restriction applies to a specific truck category.</p></div>
</section>
</li>
<li>
<section className="detail" id="trailerCount">
<h3>trailerCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span className="element-name">trailerCount</span></div>
<div className="block"><p>Number of trailers for which the restriction applies.</p></div>
</section>
</li>
<li>
<section className="detail" id="axleCount">
<h3>axleCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span className="element-name">axleCount</span></div>
<div className="block"><p>The axle count for which the current restriction applies.
 Can be used in conjunction with <a href="sdk-for-android-navigate-restrictiontype#WEIGHT_PER_AXLE_COUNT"><code>RestrictionType.WEIGHT_PER_AXLE_COUNT</code></a>
 to specify restriction based on weight per number of axles.
 The <code>axleCount</code> considers total number of axles on the whole vehicle (truck + trailers).
 This can be used to limit the weight per axle for the whole truck.
 If <code>axleCount</code> is null, the restriction is general and applies regardless of axle count.
 If the upper limit of the <code>axleCount</code> range is 0 or <code>null</code> then it means the restriction applies
 for values &gt;= lower limit, i.e. the upper limit of range if infinite or unbound.
 When a user taps the icon, the allowed <code>axleCount</code> range can be retrieved directly
 from <code>VehicleRestriction.axleCount</code>.
 Examples:
 <ul>
<li>(2,2) → Restriction applies to vehicles with exactly 2 axles.</li>
<li>(2,4) → Restriction applies to vehicles with 2, 3, or 4 axles.</li>
<li>(2, 0) → Restriction applies to vehicles with 2 or more axles (equivalent to 2...∞)</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="axleCountInGroup">
<h3>axleCountInGroup</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span className="element-name">axleCountInGroup</span></div>
<div className="block"><p>Number of axles in a group for which the current restriction applies.
 <code>axleCountInGroup</code> is a set of axles close together: single, tandem (2), triple (3), etc.
 Can be used in conjunction with <a href="sdk-for-android-navigate-restrictiontype#WEIGHT_PER_AXLE_GROUP"><code>RestrictionType.WEIGHT_PER_AXLE_GROUP</code></a>
 to specify restriction based on weight per axle group.
 The <code>axleCountInGroup</code> considers number of axles in a specific axle group (usually rear axles on the truck or trailer).
 This can be used to limit weight for a tandem/triple rear axle group.
 If the upper limit of the <code>axleCountInGroup</code> range is 0 or <code>null</code> then it means the restriction applies
 for values &gt;= lower limit, i.e. the upper limit of range if infinite or unbound.
 Examples:
 <ul>
<li>(1,1) → Restriction applies to single axle group.</li>
<li>(2,2) → Restriction applies to tandem axle group.</li>
<li>(2,4) → Restriction applies to any axle group from 2 to 4 axles.</li>
<li>(2,0) → Restriction applies to axle groups with 2 or more axles.</li>
</ul></p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.transport.SpecificRestriction)">
<h3>VehicleRestriction</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">VehicleRestriction</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-transport-specificrestriction" title="class in com.here.sdk.transport">SpecificRestriction</a> restriction)</span></div>
<div className="block"><p>Creates an unconditional restriction.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>restriction</code> - <p>A <code>SpecificRestriction</code> defines what type of restriction applies (weight, height, etc.)
 and the range of allowed values.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>VehicleRestriction</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">VehicleRestriction</span>()</div>
<div className="block"><p>Creates an uncoditional general restriction.</p></div>
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
