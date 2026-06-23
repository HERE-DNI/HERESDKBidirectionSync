---
title: "LaneAccess (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-laneaccess"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LaneAccess.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.LaneAccess</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">LaneAccess</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A class which identifies the vehicle type(s) allowed to
 access a lane.</p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#automobiles">automobiles</a></code></div>
<div class="col-last even-row-color">
<div class="block">Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive
 on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#buses">buses</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Buses that are used for public transportation.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#carpools">carpools</a></code></div>
<div class="col-last even-row-color">
<div class="block">Represents the sharing of car journeys so that more than one person travels in a car, and
 prevents the need for others to have to drive to a location themselves.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#deliveryVehicles">deliveryVehicles</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Delivery <a href="sdk-for-android-navigate-index#trucks"><code>trucks</code></a> that are permitted to enter the city proper
 to unload goods at businesses.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#emergencyVehicles">emergencyVehicles</a></code></div>
<div class="col-last even-row-color">
<div class="block">Any vehicle that is designated and authorized to respond to an emergency in a
 life-threatening situation.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#motorcycles">motorcycles</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Motorized two-wheeled passenger vehicles.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#pedestrians">pedestrians</a></code></div>
<div class="col-last even-row-color">
<div class="block">Persons traveling on foot, whether walking or running.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#taxis">taxis</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Four-wheel vehicles that are usually fitted with a taximeter, that may be hired,
 along with their driver, to carry passengers to any specified destination.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#throughTraffic">throughTraffic</a></code></div>
<div class="col-last even-row-color">
<div class="block">Passenger vehicles (i.e., those defined as passenger car/automobiles) that are
 allowed to access roads that have traffic restrictions.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#trucks">trucks</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Large vehicles that range from medium to heavy duty trucks.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">LaneAccess</a><wbr/>(boolean automobiles,
 boolean buses,
 boolean taxis,
 boolean carpools,
 boolean pedestrians,
 boolean trucks,
 boolean throughTraffic,
 boolean deliveryVehicles,
 boolean emergencyVehicles,
 boolean motorcycles)</code></div>
<div class="col-last even-row-color">
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>

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
<section class="detail" id="automobiles">
<h3>automobiles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">automobiles</span></div>
<div class="block"><p>Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive
 on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.</p></div>
</section>
</li>
<li>
<section class="detail" id="buses">
<h3>buses</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">buses</span></div>
<div class="block"><p>Buses that are used for public transportation.</p></div>
</section>
</li>
<li>
<section class="detail" id="taxis">
<h3>taxis</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">taxis</span></div>
<div class="block"><p>Four-wheel vehicles that are usually fitted with a taximeter, that may be hired,
 along with their driver, to carry passengers to any specified destination.</p></div>
</section>
</li>
<li>
<section class="detail" id="carpools">
<h3>carpools</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">carpools</span></div>
<div class="block"><p>Represents the sharing of car journeys so that more than one person travels in a car, and
 prevents the need for others to have to drive to a location themselves.</p></div>
</section>
</li>
<li>
<section class="detail" id="pedestrians">
<h3>pedestrians</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">pedestrians</span></div>
<div class="block"><p>Persons traveling on foot, whether walking or running.</p></div>
</section>
</li>
<li>
<section class="detail" id="trucks">
<h3>trucks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">trucks</span></div>
<div class="block"><p>Large vehicles that range from medium to heavy duty trucks.</p></div>
</section>
</li>
<li>
<section class="detail" id="throughTraffic">
<h3>throughTraffic</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">throughTraffic</span></div>
<div class="block"><p>Passenger vehicles (i.e., those defined as passenger car/automobiles) that are
 allowed to access roads that have traffic restrictions.</p></div>
</section>
</li>
<li>
<section class="detail" id="deliveryVehicles">
<h3>deliveryVehicles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">deliveryVehicles</span></div>
<div class="block"><p>Delivery <a href="sdk-for-android-navigate-index#trucks"><code>trucks</code></a> that are permitted to enter the city proper
 to unload goods at businesses.</p></div>
</section>
</li>
<li>
<section class="detail" id="emergencyVehicles">
<h3>emergencyVehicles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">emergencyVehicles</span></div>
<div class="block"><p>Any vehicle that is designated and authorized to respond to an emergency in a
 life-threatening situation.</p></div>
</section>
</li>
<li>
<section class="detail" id="motorcycles">
<h3>motorcycles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">motorcycles</span></div>
<div class="block"><p>Motorized two-wheeled passenger vehicles. Generally, mopeds are considered
 motorcycles.</p></div>
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
<section class="detail" id="&lt;init&gt;(boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>LaneAccess</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LaneAccess</span><wbr/><span class="parameters">(boolean automobiles,
 boolean buses,
 boolean taxis,
 boolean carpools,
 boolean pedestrians,
 boolean trucks,
 boolean throughTraffic,
 boolean deliveryVehicles,
 boolean emergencyVehicles,
 boolean motorcycles)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>automobiles</code> - <p>Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive
 on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.</p></dd>
<dd><code>buses</code> - <p>Buses that are used for public transportation.</p></dd>
<dd><code>taxis</code> - <p>Four-wheel vehicles that are usually fitted with a taximeter, that may be hired,
 along with their driver, to carry passengers to any specified destination.</p></dd>
<dd><code>carpools</code> - <p>Represents the sharing of car journeys so that more than one person travels in a car, and
 prevents the need for others to have to drive to a location themselves.</p></dd>
<dd><code>pedestrians</code> - <p>Persons traveling on foot, whether walking or running.</p></dd>
<dd><code>trucks</code> - <p>Large vehicles that range from medium to heavy duty trucks.</p></dd>
<dd><code>throughTraffic</code> - <p>Passenger vehicles (i.e., those defined as passenger car/automobiles) that are
 allowed to access roads that have traffic restrictions.</p></dd>
<dd><code>deliveryVehicles</code> - <p>Delivery <a href="sdk-for-android-navigate-index#trucks"><code>trucks</code></a> that are permitted to enter the city proper
 to unload goods at businesses.</p></dd>
<dd><code>emergencyVehicles</code> - <p>Any vehicle that is designated and authorized to respond to an emergency in a
 life-threatening situation.</p></dd>
<dd><code>motorcycles</code> - <p>Motorized two-wheeled passenger vehicles. Generally, mopeds are considered
 motorcycles.</p></dd>
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
