---
title: "TruckSpecifications (API Reference)"
slug: "sdk-for-android-navigate-truckspecifications"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TruckSpecifications.html -->
<!DOCTYPE HTML>






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
<div class="inheritance">com.here.sdk.transport.TruckSpecifications</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">TruckSpecifications</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use <code>TransportSpecification</code> instead.</p></div>
</div>
<div class="block"><p>Truck specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count.
 Only the fields that are set are considered for restriction handling.</p></div>
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
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#axleCount">axleCount</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Defines total number of axles in the vehicle.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#currentWeightInKilograms">currentWeightInKilograms</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Current truck weight, including trailers and shipped goods currently loaded, specified in
 kilograms.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#grossWeightInKilograms">grossWeightInKilograms</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
 kilograms.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#heightInCentimeters">heightInCentimeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Truck height in centimeters.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isTruckLight">isTruckLight</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#lengthInCentimeters">lengthInCentimeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Truck length in centimeters.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#payloadCapacityInKilograms">payloadCapacityInKilograms</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Allowed payload capacity, including trailers, specified in kilograms.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#trailerAxleCount">trailerAxleCount</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Defines total number of axles across all the trailers attached to the vehicle.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#trailerCount">trailerCount</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Defines number of trailers attached to the vehicle.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-trucktype" title="enum class in com.here.sdk.transport">TruckType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#truckType">truckType</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Defines the type of truck.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-weightperaxlegroup" title="class in com.here.sdk.transport">WeightPerAxleGroup</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#weightPerAxleGroup">weightPerAxleGroup</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Allows specification of axle weights in a more fine-grained way than <code>weight_per_axle_in_kilograms</code>.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#weightPerAxleInKilograms">weightPerAxleInKilograms</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Heaviest weight per axle, regardless of axle type or axle group.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#widthInCentimeters">widthInCentimeters</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Truck width in centimeters.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TruckSpecifications</a>()</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
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
<section class="detail" id="grossWeightInKilograms">
<h3>grossWeightInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">grossWeightInKilograms</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
 kilograms. The provided value must be greater than or equal to 0. If unspecified,
 it will default to <a href="#currentWeightInKilograms"><code>currentWeightInKilograms</code></a>. By default, it is not set.</p></div>
</section>
</li>
<li>
<section class="detail" id="currentWeightInKilograms">
<h3>currentWeightInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">currentWeightInKilograms</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Current truck weight, including trailers and shipped goods currently loaded, specified in
 kilograms. The provided value must be greater than or equal to 0. If unspecified,
 it will default to <a href="#grossWeightInKilograms"><code>grossWeightInKilograms</code></a>. By default, it is not set.</p></div>
</section>
</li>
<li>
<section class="detail" id="weightPerAxleInKilograms">
<h3>weightPerAxleInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">weightPerAxleInKilograms</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Heaviest weight per axle, regardless of axle type or axle group.
 It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
 The provided value must be greater or equal to 0.
 By default, it is not set.
 <strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
 When available for your edition, if both attributes are set, during online RoutingEngine an [sdk.routing.RoutingError.INVALID_PARAMETER] error is generated.
 Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</p></div>
</section>
</li>
<li>
<section class="detail" id="weightPerAxleGroup">
<h3>weightPerAxleGroup</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-weightperaxlegroup" title="class in com.here.sdk.transport">WeightPerAxleGroup</a></span> <span class="element-name">weightPerAxleGroup</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Allows specification of axle weights in a more fine-grained way than <code>weight_per_axle_in_kilograms</code>.
 This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden.
 By default is not set.
 <strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
 When available for your edition, if both attributes are set, during online RoutingEngine an [sdk.routing.RoutingError.INVALID_PARAMETER] error is generated.
 Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</p></div>
</section>
</li>
<li>
<section class="detail" id="heightInCentimeters">
<h3>heightInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">heightInCentimeters</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Truck height in centimeters. The provided value must be in the range [0, 5000].
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section class="detail" id="widthInCentimeters">
<h3>widthInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">widthInCentimeters</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Truck width in centimeters. The provided value must be in the range [0, 5000].
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section class="detail" id="lengthInCentimeters">
<h3>lengthInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">lengthInCentimeters</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Truck length in centimeters. The provided value must be in the range [0, 30000].
 By default, it is not set.</p></div>
</section>
</li>
<li>
<section class="detail" id="axleCount">
<h3>axleCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">axleCount</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Defines total number of axles in the vehicle. The provided value must be greater than or
 equal to 2. By default, it is not set.
 Route calculation: When not set, possible axle count restrictions will not be
 taken into consideration.
 Rendering <code>sdk.mapview.TruckProfile</code>: When set, truck restriction icons for an axle count
 greater than <a href="#axleCount"><code>axleCount</code></a> will not be displayed.
 When specifying <a href="#trailerAxleCount"><code>trailerAxleCount</code></a>, then <a href="#axleCount"><code>axleCount</code></a> is required and must be greater than <a href="#trailerAxleCount"><code>trailerAxleCount</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="trailerCount">
<h3>trailerCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">trailerCount</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Defines number of trailers attached to the vehicle. The provided value must be in the range
 [0, 255]. By default, it is not set.
 When specifying <a href="#trailerAxleCount"><code>trailerAxleCount</code></a>, then <a href="#trailerCount"><code>trailerCount</code></a> is required and must be greater than 0.</p></div>
</section>
</li>
<li>
<section class="detail" id="truckType">
<h3>truckType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trucktype" title="enum class in com.here.sdk.transport">TruckType</a></span> <span class="element-name">truckType</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Defines the type of truck. By default, it is <a href="sdk-for-android-navigate-trucktype#STRAIGHT"><code>TruckType.STRAIGHT</code></a>.
 Rendering <code>sdk.mapview.TruckProfile</code>: <a href="#truckType"><code>truckType</code></a> is ignored and has no effect.</p></div>
</section>
</li>
<li>
<section class="detail" id="isTruckLight">
<h3>isTruckLight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTruckLight</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.
 The flag should not be set to <code>true</code> in other countries than Japan. The flag defaults to <code>false</code>.
 </p><p>A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets
 the vehicle can access, which access restrictions apply, and which speed limits are applicable.
 Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will
 not always overwrite these settings: Make sure to not exceed the specifications that classify a truck as light.
 </p><p>In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to true,
 you will get, for example, the same speed limits as for cars. Make sure to set the flag only to true, when
 a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.
 </p><p>When <code>TruckSpecifications</code> are set as part of <code>MapContentSettings</code>, then this flag will be ignored and
 has no effect.
 </p><p><strong>Note:</strong>
 This flag and the concept of light trucks are supported only in Japan as beta and are considered to be
 experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.
 Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases with a deprecation process.</p></div>
</section>
</li>
<li>
<section class="detail" id="payloadCapacityInKilograms">
<h3>payloadCapacityInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">payloadCapacityInKilograms</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Allowed payload capacity, including trailers, specified in kilograms. The provided value
 must be greater then or equal to 0. By default, it is not set.</p></div>
</section>
</li>
<li>
<section class="detail" id="trailerAxleCount">
<h3>trailerAxleCount</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">trailerAxleCount</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Defines total number of axles across all the trailers attached to the vehicle.
 This number is included in <a href="#axleCount"><code>axleCount</code></a>, hence <a href="#trailerAxleCount"><code>trailerAxleCount</code></a> must be less than <a href="#axleCount"><code>axleCount</code></a>
 and greater than or equal to 1. <a href="#axleCount"><code>axleCount</code></a> and <a href="#trailerCount"><code>trailerCount</code></a> are required to specify <a href="#trailerAxleCount"><code>trailerAxleCount</code></a>.
 By default, it is not set.
 Note: This parameter is currently used only for the calculation of tolls in regions where it is applicable.</p></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>TruckSpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TruckSpecifications</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Creates a new instance.</p></div>
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
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
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
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
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



</div>
`
}</HTMLBlock>
