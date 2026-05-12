---
title: "PhysicalConsumptionModel (API Reference)"
slug: "sdk-for-android-explore-physicalconsumptionmodel"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PhysicalConsumptionModel.html -->
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
<li><a href="sdk-for-android-explore-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-help-doc#class">Help</a></li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.PhysicalConsumptionModel</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">PhysicalConsumptionModel</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Defines the physical consumption model for electric vehicles,
 using vehicle-specific parameters to calculate energy consumption along a route.
 <strong>Note:</strong> [sdk.transport.VehicleSpecification.current_weight_in_kilograms] must be set.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#airDragCoefficient">airDragCoefficient</a></code></div>
<div class="col-last even-row-color">
<div class="block">The drag coefficient of an vehicle defines the way the vehicle is expected to pass through the surrounding air.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#auxiliaryPowerConsumptionInWatts">auxiliaryPowerConsumptionInWatts</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Power (in W) consumed by the vehicle's auxiliary systems (for example, air conditioning, lights).</div>
</div>
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#driveTrainEfficiency">driveTrainEfficiency</a></code></div>
<div class="col-last even-row-color">
<div class="block">The proportion of the energy drawn from the battery that is used to move the vehicle.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#frontalAreaInSquareMeters">frontalAreaInSquareMeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters.</div>
</div>
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#recuperationEfficiency">recuperationEfficiency</a></code></div>
<div class="col-last even-row-color">
<div class="block">The proportion of the energy gained when braking or going downhill that can be recuperated and restored as battery charge.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#rollingResistanceCoefficient">rollingResistanceCoefficient</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Rolling resistance refers to the resistance experienced by your vehicle tire as it rolls over a surface.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PhysicalConsumptionModel</a>()</code></div>
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
<section class="detail" id="driveTrainEfficiency">
<h3>driveTrainEfficiency</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">driveTrainEfficiency</span></div>
<div class="block"><p>The proportion of the energy drawn from the battery that is used to move the vehicle.
 (This is to factor in energy losses through heat in the motors, for example.)
 Supported range from 0 to 1</p></div>
</section>
</li>
<li>
<section class="detail" id="recuperationEfficiency">
<h3>recuperationEfficiency</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">recuperationEfficiency</span></div>
<div class="block"><p>The proportion of the energy gained when braking or going downhill that can be recuperated and restored as battery charge.
 <p>Supported range from 0 to 1</p></p></div>
</section>
</li>
<li>
<section class="detail" id="auxiliaryPowerConsumptionInWatts">
<h3>auxiliaryPowerConsumptionInWatts</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">auxiliaryPowerConsumptionInWatts</span></div>
<div class="block"><p>Power (in W) consumed by the vehicle's auxiliary systems (for example, air conditioning, lights).
 <p>The provided value must be greater than or equal to 0.</p></p></div>
</section>
</li>
<li>
<section class="detail" id="frontalAreaInSquareMeters">
<h3>frontalAreaInSquareMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">frontalAreaInSquareMeters</span></div>
<div class="block"><p>Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters.
 Physical consumption model is using this value in combination with <code>airDragCoefficient</code> to calculate the consumption caused by air resistance.
 As fallback <a href="sdk-for-android-explore-transport-vehiclespecification#widthInCentimeters"><code>VehicleSpecification.widthInCentimeters</code></a> and <a href="sdk-for-android-explore-transport-vehiclespecification#heightInCentimeters"><code>VehicleSpecification.heightInCentimeters</code></a> are used.
 <p>This parameter is used to provide a more accurate consumption prediction for electric vehicles.
 <p>In the range from 0.5 to 50</p></p></p></div>
</section>
</li>
<li>
<section class="detail" id="rollingResistanceCoefficient">
<h3>rollingResistanceCoefficient</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">rollingResistanceCoefficient</span></div>
<div class="block"><p>Rolling resistance refers to the resistance experienced by your vehicle tire as it rolls over a surface.
 The main causes of this resistance are tire deformation, wing drag, and friction with the ground.
 The coefficient of rolling resistance is a numerical value indicating the severity of this factor.
 <p>This parameter is used to provide a more accurate consumption prediction for electric vehicles.
 <p>Supported range from 0 to 1</p></p></p></div>
</section>
</li>
<li>
<section class="detail" id="airDragCoefficient">
<h3>airDragCoefficient</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">airDragCoefficient</span></div>
<div class="block"><p>The drag coefficient of an vehicle defines the way the vehicle is expected to pass through the surrounding air.
 More streamlined vehicles are more aerodynamic and therefore have smaller drag coefficient.
 <p>This parameter is used to provide a more accurate consumption prediction for electric vehicles.
 <p>Supported range from 0 to 1</p></p></p></div>
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
<h3>PhysicalConsumptionModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PhysicalConsumptionModel</span>()</div>
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
