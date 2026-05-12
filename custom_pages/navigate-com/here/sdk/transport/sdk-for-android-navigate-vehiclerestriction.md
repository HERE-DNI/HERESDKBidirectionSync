---
title: "VehicleRestriction (API Reference)"
slug: "sdk-for-android-navigate-vehiclerestriction"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VehicleRestriction.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li><a href="#field-summary">Field</a> | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#field-detail">Field</a> | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.transport</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.transport.VehicleRestriction</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">VehicleRestriction</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents a vehicle restriction.
 <p>Any non <code>null</code> field adds more details to the restriction.
 A general truck restriction is represented with <code>null</code> values for
 fields <code>restriction</code> and
 <code>hazmatRestriction</code>.
 <p><strong>Note:</strong> This is a beta release of this feature.
 Related APIs may change for new releases without a deprecation process.</p></p></p></div>
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
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#appliesToDelivery">appliesToDelivery</a></code></div>
<div class="col-last even-row-color">
<div class="block">Flag indicating whether this restriction applies to delivery vehicles.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#axleCount">axleCount</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The axle count for which the current restriction applies.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#axleCountInGroup">axleCountInGroup</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of axles in a group for which the current restriction applies.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-hazardousmaterialrestriction" title="class in com.here.sdk.transport">HazardousMaterialRestriction</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#hazmatRestriction">hazmatRestriction</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Restriction on transport of hazardous materials and max allowed tunnel category.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-specificrestriction" title="class in com.here.sdk.transport">SpecificRestriction</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#restriction">restriction</a></code></div>
<div class="col-last even-row-color">
<div class="block">A <code>SpecificRestriction</code> defines what type of restriction applies (weight, height, etc.)
 and the range of allowed values.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-timerestriction" title="class in com.here.sdk.transport">TimeRestriction</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#timeRestriction">timeRestriction</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Restriction applies during specific time.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#trailerCount">trailerCount</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of trailers for which the restriction applies.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#truckCategory">truckCategory</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Restriction applies to a specific truck category.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#weather">weather</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type of weather in which restriction applies.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">VehicleRestriction</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an uncoditional general restriction.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.transport.SpecificRestriction)">VehicleRestriction</a><wbr/>(<a href="sdk-for-android-navigate-specificrestriction" title="class in com.here.sdk.transport">SpecificRestriction</a> restriction)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates an unconditional restriction.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="restriction">
<h3>restriction</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-specificrestriction" title="class in com.here.sdk.transport">SpecificRestriction</a></span> <span class="element-name">restriction</span></div>
<div class="block"><p>A <code>SpecificRestriction</code> defines what type of restriction applies (weight, height, etc.)
 and the range of allowed values.</p></div>
</section>
</li>
<li>
<section class="detail" id="hazmatRestriction">
<h3>hazmatRestriction</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-hazardousmaterialrestriction" title="class in com.here.sdk.transport">HazardousMaterialRestriction</a></span> <span class="element-name">hazmatRestriction</span></div>
<div class="block"><p>Restriction on transport of hazardous materials and max allowed tunnel category.
 For example, (FLAMMABLE, TunnelCategory.D) means, a restriction applying for trucks
 carrying flammable materials are not allowed to enter tunnels category D and E -
 (TunnelCategory.B and TunnelCategory.C allowed).</p></div>
</section>
</li>
<li>
<section class="detail" id="timeRestriction">
<h3>timeRestriction</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-timerestriction" title="class in com.here.sdk.transport">TimeRestriction</a></span> <span class="element-name">timeRestriction</span></div>
<div class="block"><p>Restriction applies during specific time.</p></div>
</section>
</li>
<li>
<section class="detail" id="appliesToDelivery">
<h3>appliesToDelivery</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">appliesToDelivery</span></div>
<div class="block"><p>Flag indicating whether this restriction applies to delivery vehicles.
 <ul>
<li><code>false</code> means delivery is allowed into this restricted street.</li>
<li><code>true</code> means delivery is NOT allowed into this restricted street.</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="weather">
<h3>weather</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-navigation-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></span> <span class="element-name">weather</span></div>
<div class="block"><p>Type of weather in which restriction applies.</p></div>
</section>
</li>
<li>
<section class="detail" id="truckCategory">
<h3>truckCategory</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-truckcategory" title="enum class in com.here.sdk.transport">TruckCategory</a></span> <span class="element-name">truckCategory</span></div>
<div class="block"><p>Restriction applies to a specific truck category.</p></div>
</section>
</li>
<li>
<section class="detail" id="trailerCount">
<h3>trailerCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">trailerCount</span></div>
<div class="block"><p>Number of trailers for which the restriction applies.</p></div>
</section>
</li>
<li>
<section class="detail" id="axleCount">
<h3>axleCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">axleCount</span></div>
<div class="block"><p>The axle count for which the current restriction applies.
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
<section class="detail" id="axleCountInGroup">
<h3>axleCountInGroup</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span class="element-name">axleCountInGroup</span></div>
<div class="block"><p>Number of axles in a group for which the current restriction applies.
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
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.transport.SpecificRestriction)">
<h3>VehicleRestriction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VehicleRestriction</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-specificrestriction" title="class in com.here.sdk.transport">SpecificRestriction</a> restriction)</span></div>
<div class="block"><p>Creates an unconditional restriction.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>restriction</code> - <p>A <code>SpecificRestriction</code> defines what type of restriction applies (weight, height, etc.)
 and the range of allowed values.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>VehicleRestriction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VehicleRestriction</span>()</div>
<div class="block"><p>Creates an uncoditional general restriction.</p></div>
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
</main>
</div>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>
