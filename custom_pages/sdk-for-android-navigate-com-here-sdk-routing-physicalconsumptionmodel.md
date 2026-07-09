---
title: "PhysicalConsumptionModel (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-physicalconsumptionmodel"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PhysicalConsumptionModel.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.PhysicalConsumptionModel</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">PhysicalConsumptionModel</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Defines the physical consumption model for electric vehicles,
 using vehicle-specific parameters to calculate energy consumption along a route.
 <strong>Note:</strong> [sdk.transport.VehicleSpecification.current_weight_in_kilograms] must be set.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-physicalconsumptionmodel#airDragCoefficient">airDragCoefficient</a></code></div>
<div className="col-last even-row-color">
<div className="block">The drag coefficient of an vehicle defines the way the vehicle is expected to pass through the surrounding air.</div>
</div>
<div className="col-first odd-row-color"><code>double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-physicalconsumptionmodel#auxiliaryPowerConsumptionInWatts">auxiliaryPowerConsumptionInWatts</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Power (in W) consumed by the vehicle's auxiliary systems (for example, air conditioning, lights).</div>
</div>
<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-physicalconsumptionmodel#driveTrainEfficiency">driveTrainEfficiency</a></code></div>
<div className="col-last even-row-color">
<div className="block">The proportion of the energy drawn from the battery that is used to move the vehicle.</div>
</div>
<div className="col-first odd-row-color"><code>double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-physicalconsumptionmodel#frontalAreaInSquareMeters">frontalAreaInSquareMeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters.</div>
</div>
<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-physicalconsumptionmodel#recuperationEfficiency">recuperationEfficiency</a></code></div>
<div className="col-last even-row-color">
<div className="block">The proportion of the energy gained when braking or going downhill that can be recuperated and restored as battery charge.</div>
</div>
<div className="col-first odd-row-color"><code>double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-physicalconsumptionmodel#rollingResistanceCoefficient">rollingResistanceCoefficient</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Rolling resistance refers to the resistance experienced by your vehicle tire as it rolls over a surface.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-physicalconsumptionmodel#%3Cinit%3E()">PhysicalConsumptionModel</a>()</code></div>
<div className="col-last even-row-color">
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
<section className="detail" id="driveTrainEfficiency">
<h3>driveTrainEfficiency</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">driveTrainEfficiency</span></div>
<div className="block"><p>The proportion of the energy drawn from the battery that is used to move the vehicle.
 (This is to factor in energy losses through heat in the motors, for example.)
 Supported range from 0 to 1</p></div>
</section>
</li>
<li>
<section className="detail" id="recuperationEfficiency">
<h3>recuperationEfficiency</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">recuperationEfficiency</span></div>
<div className="block"><p>The proportion of the energy gained when braking or going downhill that can be recuperated and restored as battery charge.
 Supported range from 0 to 1</p></div>
</section>
</li>
<li>
<section className="detail" id="auxiliaryPowerConsumptionInWatts">
<h3>auxiliaryPowerConsumptionInWatts</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">auxiliaryPowerConsumptionInWatts</span></div>
<div className="block"><p>Power (in W) consumed by the vehicle's auxiliary systems (for example, air conditioning, lights).
 The provided value must be greater than or equal to 0.</p></div>
</section>
</li>
<li>
<section className="detail" id="frontalAreaInSquareMeters">
<h3>frontalAreaInSquareMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">frontalAreaInSquareMeters</span></div>
<div className="block"><p>Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters.
 Physical consumption model is using this value in combination with <code>airDragCoefficient</code> to calculate the consumption caused by air resistance.
 As fallback <a href="sdk-for-android-navigate-vehiclespecification#widthInCentimeters"><code>VehicleSpecification.widthInCentimeters</code></a> and <a href="sdk-for-android-navigate-vehiclespecification#heightInCentimeters"><code>VehicleSpecification.heightInCentimeters</code></a> are used.
 This parameter is used to provide a more accurate consumption prediction for electric vehicles.
 In the range from 0.5 to 50</p></div>
</section>
</li>
<li>
<section className="detail" id="rollingResistanceCoefficient">
<h3>rollingResistanceCoefficient</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">rollingResistanceCoefficient</span></div>
<div className="block"><p>Rolling resistance refers to the resistance experienced by your vehicle tire as it rolls over a surface.
 The main causes of this resistance are tire deformation, wing drag, and friction with the ground.
 The coefficient of rolling resistance is a numerical value indicating the severity of this factor.
 This parameter is used to provide a more accurate consumption prediction for electric vehicles.
 Supported range from 0 to 1</p></div>
</section>
</li>
<li>
<section className="detail" id="airDragCoefficient">
<h3>airDragCoefficient</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">airDragCoefficient</span></div>
<div className="block"><p>The drag coefficient of an vehicle defines the way the vehicle is expected to pass through the surrounding air.
 More streamlined vehicles are more aerodynamic and therefore have smaller drag coefficient.
 This parameter is used to provide a more accurate consumption prediction for electric vehicles.
 Supported range from 0 to 1</p></div>
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
<section className="detail" id="&lt;init&gt;()">
<h3>PhysicalConsumptionModel</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">PhysicalConsumptionModel</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
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
