---
title: "ChargingConnectorAttributes (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-chargingconnectorattributes"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ChargingConnectorAttributes.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.ChargingConnectorAttributes</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">ChargingConnectorAttributes</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Details of the connector that is suggested to be used in the section's
 <a href="sdk-for-android-navigate-com-here-sdk-routing-postaction" title="class in com.here.sdk.routing"><code>PostAction</code></a>'s for charging.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectorattributes#connectorType">connectorType</a></code></div>
<div className="col-last even-row-color">
<div className="block">Suggested connector for charging at this station.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectorattributes#currentInAmperes">currentInAmperes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Current of the suggested connector in Amperes.</div>
</div>
<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectorattributes#powerInKilowatts">powerInKilowatts</a></code></div>
<div className="col-last even-row-color">
<div className="block">Power supplied by the suggested connector in kW.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-chargingsupplytype" title="enum class in com.here.sdk.routing">ChargingSupplyType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectorattributes#supplyType">supplyType</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Supply type of the suggested connector.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectorattributes#voltageInVolts">voltageInVolts</a></code></div>
<div className="col-last even-row-color">
<div className="block">Voltage of the suggested connector in Volts.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectorattributes#%3Cinit%3E(double,java.lang.Double,java.lang.Double,com.here.sdk.routing.ChargingSupplyType,com.here.sdk.routing.ChargingConnectorType)">ChargingConnectorAttributes</a><wbr/>(double powerInKilowatts,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> currentInAmperes,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> voltageInVolts,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingsupplytype" title="enum class in com.here.sdk.routing">ChargingSupplyType</a> supplyType,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a> connectorType)</code></div>
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
<section className="detail" id="powerInKilowatts">
<h3>powerInKilowatts</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">powerInKilowatts</span></div>
<div className="block"><p>Power supplied by the suggested connector in kW.</p></div>
</section>
</li>
<li>
<section className="detail" id="currentInAmperes">
<h3>currentInAmperes</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">currentInAmperes</span></div>
<div className="block"><p>Current of the suggested connector in Amperes.</p></div>
</section>
</li>
<li>
<section className="detail" id="voltageInVolts">
<h3>voltageInVolts</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">voltageInVolts</span></div>
<div className="block"><p>Voltage of the suggested connector in Volts.</p></div>
</section>
</li>
<li>
<section className="detail" id="supplyType">
<h3>supplyType</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-chargingsupplytype" title="enum class in com.here.sdk.routing">ChargingSupplyType</a></span> <span className="element-name">supplyType</span></div>
<div className="block"><p>Supply type of the suggested connector.</p></div>
</section>
</li>
<li>
<section className="detail" id="connectorType">
<h3>connectorType</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a></span> <span className="element-name">connectorType</span></div>
<div className="block"><p>Suggested connector for charging at this station.</p></div>
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
<section className="detail" id="&lt;init&gt;(double,java.lang.Double,java.lang.Double,com.here.sdk.routing.ChargingSupplyType,com.here.sdk.routing.ChargingConnectorType)">
<h3>ChargingConnectorAttributes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ChargingConnectorAttributes</span><wbr/><span className="parameters">(double powerInKilowatts,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> currentInAmperes,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> voltageInVolts,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingsupplytype" title="enum class in com.here.sdk.routing">ChargingSupplyType</a> supplyType,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a> connectorType)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>powerInKilowatts</code> - <p>Power supplied by the suggested connector in kW.</p></dd>
<dd><code>currentInAmperes</code> - <p>Current of the suggested connector in Amperes.</p></dd>
<dd><code>voltageInVolts</code> - <p>Voltage of the suggested connector in Volts.</p></dd>
<dd><code>supplyType</code> - <p>Supply type of the suggested connector.</p></dd>
<dd><code>connectorType</code> - <p>Suggested connector for charging at this station.</p></dd>
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
