---
title: "ChargingStop (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-chargingstop"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- ChargingStop.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.ChargingStop</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">ChargingStop</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>The options to specify a user-planned charging stop.
 <strong>Note:</strong>
 In order to specify this <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, it is also required to set
 [sdk.routing.BatterySpecifications.total_capacity_in_kilowatt_hours], [sdk.routing.BatterySpecifications.initial_charge_in_kilowatt_hours],
 and [sdk.routing.BatterySpecifications.charging_curve].
 Without all of them, the route calculation will fail as an invalid parameter error.</p></div>
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
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#currentInAmperes">currentInAmperes</a></code></div>
<div class="col-last even-row-color">
<div class="block">The value of rated current of the connector (in A).</div>
</div>
<div class="col-first odd-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#maxDuration">maxDuration</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The maximum duration the user plans to charge at the station,
 including <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-batteryspecifications#chargingSetupDuration"><code>BatterySpecifications.chargingSetupDuration</code></a>.</div>
</div>
<div class="col-first even-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#minDuration">minDuration</a></code></div>
<div class="col-last even-row-color">
<div class="block">The minimum duration the user expects to charge at the station,
 including <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-batteryspecifications#chargingSetupDuration"><code>BatterySpecifications.chargingSetupDuration</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#powerInKilowatts">powerInKilowatts</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The value of rated power of the connector (in kW).</div>
</div>
<div class="col-first even-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-chargingsupplytype" title="enum class in com.here.sdk.routing">ChargingSupplyType</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#supplyType">supplyType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Supply type of the suggested connector.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#voltageInVolts">voltageInVolts</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The value of rated voltage of the connector (in V).</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#%3Cinit%3E()">ChargingStop</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#%3Cinit%3E(double,double,double,com.here.sdk.routing.ChargingSupplyType,com.here.time.Duration,com.here.time.Duration)">ChargingStop</a><wbr/>(double powerInKilowatts,
 double currentInAmperes,
 double voltageInVolts,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-chargingsupplytype" title="enum class in com.here.sdk.routing">ChargingSupplyType</a> supplyType,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-duration" title="class in com.here.time">Duration</a> minDuration,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-duration" title="class in com.here.time">Duration</a> maxDuration)</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#hashCode()">hashCode</a>()</code></div>
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
<section class="detail" id="powerInKilowatts">
<h3>powerInKilowatts</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">powerInKilowatts</span></div>
<div class="block"><p>The value of rated power of the connector (in kW).</p></div>
</section>
</li>
<li>
<section class="detail" id="currentInAmperes">
<h3>currentInAmperes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">currentInAmperes</span></div>
<div class="block"><p>The value of rated current of the connector (in A).</p></div>
</section>
</li>
<li>
<section class="detail" id="voltageInVolts">
<h3>voltageInVolts</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">voltageInVolts</span></div>
<div class="block"><p>The value of rated voltage of the connector (in V).</p></div>
</section>
</li>
<li>
<section class="detail" id="supplyType">
<h3>supplyType</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-chargingsupplytype" title="enum class in com.here.sdk.routing">ChargingSupplyType</a></span> <span class="element-name">supplyType</span></div>
<div class="block"><p>Supply type of the suggested connector.</p></div>
</section>
</li>
<li>
<section class="detail" id="minDuration">
<h3>minDuration</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">minDuration</span></div>
<div class="block"><p>The minimum duration the user expects to charge at the station,
 including <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-batteryspecifications#chargingSetupDuration"><code>BatterySpecifications.chargingSetupDuration</code></a>.
 <strong>Note:</strong>
 At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
 For most use cases, providing at least <code>min_duration</code> is recommended.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxDuration">
<h3>maxDuration</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">maxDuration</span></div>
<div class="block"><p>The maximum duration the user plans to charge at the station,
 including <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-batteryspecifications#chargingSetupDuration"><code>BatterySpecifications.chargingSetupDuration</code></a>.
 <strong>Note:</strong>
 At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
 For most use cases, providing at least <code>min_duration</code> is recommended.</p></div>
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
<h3>ChargingStop</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ChargingStop</span>()</div>
<div class="block"><p>Creates a new instance.</p></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double,double,com.here.sdk.routing.ChargingSupplyType,com.here.time.Duration,com.here.time.Duration)">
<h3>ChargingStop</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ChargingStop</span><wbr/><span class="parameters">(double powerInKilowatts,
 double currentInAmperes,
 double voltageInVolts,
 @Nullable
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-chargingsupplytype" title="enum class in com.here.sdk.routing">ChargingSupplyType</a> supplyType,
 @Nullable
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-duration" title="class in com.here.time">Duration</a> minDuration,
 @Nullable
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-duration" title="class in com.here.time">Duration</a> maxDuration)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>powerInKilowatts</code> - <p>The value of rated power of the connector (in kW).</p></dd>
<dd><code>currentInAmperes</code> - <p>The value of rated current of the connector (in A).</p></dd>
<dd><code>voltageInVolts</code> - <p>The value of rated voltage of the connector (in V).</p></dd>
<dd><code>supplyType</code> - <p>Supply type of the suggested connector.</p></dd>
<dd><code>minDuration</code> - <p>The minimum duration the user expects to charge at the station,
 including <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-batteryspecifications#chargingSetupDuration"><code>BatterySpecifications.chargingSetupDuration</code></a>.
 <strong>Note:</strong>
 At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
 For most use cases, providing at least <code>min_duration</code> is recommended.</p></dd>
<dd><code>maxDuration</code> - <p>The maximum duration the user plans to charge at the station,
 including <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-batteryspecifications#chargingSetupDuration"><code>BatterySpecifications.chargingSetupDuration</code></a>.
 <strong>Note:</strong>
 At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
 For most use cases, providing at least <code>min_duration</code> is recommended.</p></dd>
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
</main>





</div>
`
}</HTMLBlock>
