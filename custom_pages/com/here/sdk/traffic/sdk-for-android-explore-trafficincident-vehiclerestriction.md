---
title: "TrafficIncident.VehicleRestriction (API Reference)"
slug: "sdk-for-android-explore-trafficincident-vehiclerestriction"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrafficIncident.VehicleRestriction.html -->
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.traffic</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.traffic.TrafficIncident.VehicleRestriction</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-explore-trafficincident" title="class in com.here.sdk.traffic">TrafficIncident</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">TrafficIncident.VehicleRestriction</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>The vehicle restriction representing a vehicle category and relevant restriction rules.</p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isCaravanRestricted">isCaravanRestricted</a></code></div>
<div class="col-last even-row-color">
<div class="block">The flag indicating if a driving with a caravan is restricted for vehicles of the matching category.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isDestinationInIncidentAreaRestricted">isDestinationInIncidentAreaRestricted</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The flag indicating if a traffic destination in the incident area is restricted for vehicles of the matching category.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isDieselFuelRestricted">isDieselFuelRestricted</a></code></div>
<div class="col-last even-row-color">
<div class="block">The flag indicating if diesel fuel is restricted for vehicles of the matching category.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isDrivingWithoutSnowChainsRestricted">isDrivingWithoutSnowChainsRestricted</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The flag indicating if a driving without snow chains is restricted for vehicles of the matching category.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isDrivingWithoutWinterTyresRestricted">isDrivingWithoutWinterTyresRestricted</a></code></div>
<div class="col-last even-row-color">
<div class="block">The flag indicating if a driving without winter tyres is restricted for vehicles of the matching category.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isEuro3EmissionStandardRestricted">isEuro3EmissionStandardRestricted</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The flag indicating if euro3 and weaker emission standards are restricted for vehicles of the matching category.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isEuro4EmissionStandardRestricted">isEuro4EmissionStandardRestricted</a></code></div>
<div class="col-last even-row-color">
<div class="block">The flag indicating if euro4 and weaker emission standards are restricted for vehicles of the matching category.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isEuro5EmissionStandardRestricted">isEuro5EmissionStandardRestricted</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The flag indicating if euro5 and weaker emission standards are restricted for vehicles of the matching category.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isEvenNumberPlateRestricted">isEvenNumberPlateRestricted</a></code></div>
<div class="col-last even-row-color">
<div class="block">The flag indicating if a plate with even number is restricted for vehicles of the matching category.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isLpgFuelRestricted">isLpgFuelRestricted</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The flag indicating if LPG fuel is restricted for vehicles of the matching category.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isOddNumberPlateRestricted">isOddNumberPlateRestricted</a></code></div>
<div class="col-last even-row-color">
<div class="block">The flag indicating if a plate with odd number is restricted for vehicles of the matching category.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isPetrolFuelRestricted">isPetrolFuelRestricted</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The flag indicating if petrol fuel is restricted for vehicles of the matching category.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isResidentsTrafficRestricted">isResidentsTrafficRestricted</a></code></div>
<div class="col-last even-row-color">
<div class="block">The flag indicating if a residents traffic is restricted for vehicles of the matching category.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isRestrictedAlways">isRestrictedAlways</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The flag indicating if vehicles of the matching category are restricted anyway (not depending on any vehicle parameter).</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isThroughTrafficRestricted">isThroughTrafficRestricted</a></code></div>
<div class="col-last even-row-color">
<div class="block">The flag indicating if a through traffic is restricted for vehicles of the matching category.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isTrailerRestricted">isTrailerRestricted</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The flag indicating if a driving with a trailer is restricted for vehicles of the matching category.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#restrictedIfAxleWeightLessThanInKilograms">restrictedIfAxleWeightLessThanInKilograms</a></code></div>
<div class="col-last even-row-color">
<div class="block">Vehicles of the matching category are restricted if the vehicle weight per axle is less than the weight in kilograms.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#restrictedIfAxleWeightMoreThanInKilograms">restrictedIfAxleWeightMoreThanInKilograms</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Vehicles of the matching category are restricted if the vehicle weight per axle is more than the weight in kilograms.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#restrictedIfGrossWeightLessThanInKilograms">restrictedIfGrossWeightLessThanInKilograms</a></code></div>
<div class="col-last even-row-color">
<div class="block">Vehicles of the matching category are restricted if the vehicle gross weight is less than the weight in kilograms.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#restrictedIfGrossWeightMoreThanInKilograms">restrictedIfGrossWeightMoreThanInKilograms</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Vehicles of the matching category are restricted if the vehicle gross weight is more than the weight in kilograms.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#restrictedIfHigherThanInCentimeters">restrictedIfHigherThanInCentimeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Vehicles of the matching category are restricted if the vehicle is higher than the height in centimeters.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#restrictedIfLongerThanInCentimeters">restrictedIfLongerThanInCentimeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Vehicles of the matching category are restricted if the vehicle is longer than the length in centimeters.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#restrictedIfLowerThanInCentimeters">restrictedIfLowerThanInCentimeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Vehicles of the matching category are restricted if the vehicle is lower than the height in centimeters.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#restrictedIfNarrowerThanInCentimeters">restrictedIfNarrowerThanInCentimeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Vehicles of the matching category are restricted if the vehicle is narrower than the width in centimeters.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#restrictedIfOccupantsFewerThan">restrictedIfOccupantsFewerThan</a></code></div>
<div class="col-last even-row-color">
<div class="block">Vehicles of the matching category are restricted if the occupants number is fewer than the value.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#restrictedIfOccupantsMoreThan">restrictedIfOccupantsMoreThan</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Vehicles of the matching category are restricted if the occupants number is more than the value.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#restrictedIfShorterThanInCentimeters">restrictedIfShorterThanInCentimeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Vehicles of the matching category are restricted if the vehicle is shorter than the length in centimeters.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#restrictedIfWiderThanInCentimeters">restrictedIfWiderThanInCentimeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Vehicles of the matching category are restricted if the vehicle is wider than the width in centimeters.</div>
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
<div class="block">Creates a new instance with default values.</div>
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
<section class="detail" id="isRestrictedAlways">
<h3>isRestrictedAlways</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRestrictedAlways</span></div>
<div class="block"><p>The flag indicating if vehicles of the matching category are restricted anyway (not depending on any vehicle parameter).</p></div>
</section>
</li>
<li>
<section class="detail" id="isDieselFuelRestricted">
<h3>isDieselFuelRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDieselFuelRestricted</span></div>
<div class="block"><p>The flag indicating if diesel fuel is restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isPetrolFuelRestricted">
<h3>isPetrolFuelRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPetrolFuelRestricted</span></div>
<div class="block"><p>The flag indicating if petrol fuel is restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isLpgFuelRestricted">
<h3>isLpgFuelRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLpgFuelRestricted</span></div>
<div class="block"><p>The flag indicating if LPG fuel is restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isCaravanRestricted">
<h3>isCaravanRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCaravanRestricted</span></div>
<div class="block"><p>The flag indicating if a driving with a caravan is restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isTrailerRestricted">
<h3>isTrailerRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTrailerRestricted</span></div>
<div class="block"><p>The flag indicating if a driving with a trailer is restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isDrivingWithoutSnowChainsRestricted">
<h3>isDrivingWithoutSnowChainsRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDrivingWithoutSnowChainsRestricted</span></div>
<div class="block"><p>The flag indicating if a driving without snow chains is restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isDrivingWithoutWinterTyresRestricted">
<h3>isDrivingWithoutWinterTyresRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDrivingWithoutWinterTyresRestricted</span></div>
<div class="block"><p>The flag indicating if a driving without winter tyres is restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isEvenNumberPlateRestricted">
<h3>isEvenNumberPlateRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEvenNumberPlateRestricted</span></div>
<div class="block"><p>The flag indicating if a plate with even number is restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isOddNumberPlateRestricted">
<h3>isOddNumberPlateRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOddNumberPlateRestricted</span></div>
<div class="block"><p>The flag indicating if a plate with odd number is restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isThroughTrafficRestricted">
<h3>isThroughTrafficRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isThroughTrafficRestricted</span></div>
<div class="block"><p>The flag indicating if a through traffic is restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isResidentsTrafficRestricted">
<h3>isResidentsTrafficRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isResidentsTrafficRestricted</span></div>
<div class="block"><p>The flag indicating if a residents traffic is restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isDestinationInIncidentAreaRestricted">
<h3>isDestinationInIncidentAreaRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDestinationInIncidentAreaRestricted</span></div>
<div class="block"><p>The flag indicating if a traffic destination in the incident area is restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isEuro3EmissionStandardRestricted">
<h3>isEuro3EmissionStandardRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEuro3EmissionStandardRestricted</span></div>
<div class="block"><p>The flag indicating if euro3 and weaker emission standards are restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isEuro4EmissionStandardRestricted">
<h3>isEuro4EmissionStandardRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEuro4EmissionStandardRestricted</span></div>
<div class="block"><p>The flag indicating if euro4 and weaker emission standards are restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="isEuro5EmissionStandardRestricted">
<h3>isEuro5EmissionStandardRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEuro5EmissionStandardRestricted</span></div>
<div class="block"><p>The flag indicating if euro5 and weaker emission standards are restricted for vehicles of the matching category.</p></div>
</section>
</li>
<li>
<section class="detail" id="restrictedIfGrossWeightMoreThanInKilograms">
<h3>restrictedIfGrossWeightMoreThanInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfGrossWeightMoreThanInKilograms</span></div>
<div class="block"><p>Vehicles of the matching category are restricted if the vehicle gross weight is more than the weight in kilograms.
 If the value is <code>null</code> the upper gross weight bound is not specified.</p></div>
</section>
</li>
<li>
<section class="detail" id="restrictedIfGrossWeightLessThanInKilograms">
<h3>restrictedIfGrossWeightLessThanInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfGrossWeightLessThanInKilograms</span></div>
<div class="block"><p>Vehicles of the matching category are restricted if the vehicle gross weight is less than the weight in kilograms.
 If the value is <code>null</code> the lower gross weight bound is not specified.</p></div>
</section>
</li>
<li>
<section class="detail" id="restrictedIfAxleWeightMoreThanInKilograms">
<h3>restrictedIfAxleWeightMoreThanInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfAxleWeightMoreThanInKilograms</span></div>
<div class="block"><p>Vehicles of the matching category are restricted if the vehicle weight per axle is more than the weight in kilograms.
 If the value is <code>null</code> the upper weight per axle bound is not specified.</p></div>
</section>
</li>
<li>
<section class="detail" id="restrictedIfAxleWeightLessThanInKilograms">
<h3>restrictedIfAxleWeightLessThanInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfAxleWeightLessThanInKilograms</span></div>
<div class="block"><p>Vehicles of the matching category are restricted if the vehicle weight per axle is less than the weight in kilograms.
 If the value is <code>null</code> the lower weight per axle bound is not specified.</p></div>
</section>
</li>
<li>
<section class="detail" id="restrictedIfLongerThanInCentimeters">
<h3>restrictedIfLongerThanInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfLongerThanInCentimeters</span></div>
<div class="block"><p>Vehicles of the matching category are restricted if the vehicle is longer than the length in centimeters.
 If the value is <code>null</code> the upper length bound is not specified.</p></div>
</section>
</li>
<li>
<section class="detail" id="restrictedIfShorterThanInCentimeters">
<h3>restrictedIfShorterThanInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfShorterThanInCentimeters</span></div>
<div class="block"><p>Vehicles of the matching category are restricted if the vehicle is shorter than the length in centimeters.
 If the value is <code>null</code> the lower length bound is not specified.</p></div>
</section>
</li>
<li>
<section class="detail" id="restrictedIfHigherThanInCentimeters">
<h3>restrictedIfHigherThanInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfHigherThanInCentimeters</span></div>
<div class="block"><p>Vehicles of the matching category are restricted if the vehicle is higher than the height in centimeters.
 If the value is <code>null</code> the upper height bound is not specified.</p></div>
</section>
</li>
<li>
<section class="detail" id="restrictedIfLowerThanInCentimeters">
<h3>restrictedIfLowerThanInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfLowerThanInCentimeters</span></div>
<div class="block"><p>Vehicles of the matching category are restricted if the vehicle is lower than the height in centimeters.
 If the value is <code>null</code> the lower height bound is not specified.</p></div>
</section>
</li>
<li>
<section class="detail" id="restrictedIfWiderThanInCentimeters">
<h3>restrictedIfWiderThanInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfWiderThanInCentimeters</span></div>
<div class="block"><p>Vehicles of the matching category are restricted if the vehicle is wider than the width in centimeters.
 If the value is <code>null</code> the upper width bound is not specified.</p></div>
</section>
</li>
<li>
<section class="detail" id="restrictedIfNarrowerThanInCentimeters">
<h3>restrictedIfNarrowerThanInCentimeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfNarrowerThanInCentimeters</span></div>
<div class="block"><p>Vehicles of the matching category are restricted if the vehicle is narrower than the width in centimeters.
 If the value is <code>null</code> the lower width bound is not specified.</p></div>
</section>
</li>
<li>
<section class="detail" id="restrictedIfOccupantsMoreThan">
<h3>restrictedIfOccupantsMoreThan</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfOccupantsMoreThan</span></div>
<div class="block"><p>Vehicles of the matching category are restricted if the occupants number is more than the value.
 If the value is <code>null</code> the upper occupants bound is not specified.</p></div>
</section>
</li>
<li>
<section class="detail" id="restrictedIfOccupantsFewerThan">
<h3>restrictedIfOccupantsFewerThan</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">restrictedIfOccupantsFewerThan</span></div>
<div class="block"><p>Vehicles of the matching category are restricted if the occupants number is fewer than the value.
 If the value is <code>null</code> the lower occupants bound is not specified.</p></div>
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
<h3>VehicleRestriction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VehicleRestriction</span>()</div>
<div class="block"><p>Creates a new instance with default values.</p></div>
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
