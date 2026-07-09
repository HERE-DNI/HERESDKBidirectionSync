---
title: "LaneAccess (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-laneaccess"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LaneAccess.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.LaneAccess</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">LaneAccess</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A class which identifies the vehicle type(s) allowed to
 access a lane.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#automobiles">automobiles</a></code></div>
<div className="col-last even-row-color">
<div className="block">Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive
 on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#buses">buses</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Buses that are used for public transportation.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#carpools">carpools</a></code></div>
<div className="col-last even-row-color">
<div className="block">Represents the sharing of car journeys so that more than one person travels in a car, and
 prevents the need for others to have to drive to a location themselves.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#deliveryVehicles">deliveryVehicles</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Delivery <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#trucks"><code>trucks</code></a> that are permitted to enter the city proper
 to unload goods at businesses.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#emergencyVehicles">emergencyVehicles</a></code></div>
<div className="col-last even-row-color">
<div className="block">Any vehicle that is designated and authorized to respond to an emergency in a
 life-threatening situation.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#motorcycles">motorcycles</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Motorized two-wheeled passenger vehicles.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#pedestrians">pedestrians</a></code></div>
<div className="col-last even-row-color">
<div className="block">Persons traveling on foot, whether walking or running.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#taxis">taxis</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Four-wheel vehicles that are usually fitted with a taximeter, that may be hired,
 along with their driver, to carry passengers to any specified destination.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#throughTraffic">throughTraffic</a></code></div>
<div className="col-last even-row-color">
<div className="block">Passenger vehicles (i.e., those defined as passenger car/automobiles) that are
 allowed to access roads that have traffic restrictions.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#trucks">trucks</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Large vehicles that range from medium to heavy duty trucks.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#%3Cinit%3E(boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">LaneAccess</a><wbr/>(boolean automobiles,
 boolean buses,
 boolean taxis,
 boolean carpools,
 boolean pedestrians,
 boolean trucks,
 boolean throughTraffic,
 boolean deliveryVehicles,
 boolean emergencyVehicles,
 boolean motorcycles)</code></div>
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
<section className="detail" id="automobiles">
<h3>automobiles</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">automobiles</span></div>
<div className="block"><p>Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive
 on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.</p></div>
</section>
</li>
<li>
<section className="detail" id="buses">
<h3>buses</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">buses</span></div>
<div className="block"><p>Buses that are used for public transportation.</p></div>
</section>
</li>
<li>
<section className="detail" id="taxis">
<h3>taxis</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">taxis</span></div>
<div className="block"><p>Four-wheel vehicles that are usually fitted with a taximeter, that may be hired,
 along with their driver, to carry passengers to any specified destination.</p></div>
</section>
</li>
<li>
<section className="detail" id="carpools">
<h3>carpools</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">carpools</span></div>
<div className="block"><p>Represents the sharing of car journeys so that more than one person travels in a car, and
 prevents the need for others to have to drive to a location themselves.</p></div>
</section>
</li>
<li>
<section className="detail" id="pedestrians">
<h3>pedestrians</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">pedestrians</span></div>
<div className="block"><p>Persons traveling on foot, whether walking or running.</p></div>
</section>
</li>
<li>
<section className="detail" id="trucks">
<h3>trucks</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">trucks</span></div>
<div className="block"><p>Large vehicles that range from medium to heavy duty trucks.</p></div>
</section>
</li>
<li>
<section className="detail" id="throughTraffic">
<h3>throughTraffic</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">throughTraffic</span></div>
<div className="block"><p>Passenger vehicles (i.e., those defined as passenger car/automobiles) that are
 allowed to access roads that have traffic restrictions.</p></div>
</section>
</li>
<li>
<section className="detail" id="deliveryVehicles">
<h3>deliveryVehicles</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">deliveryVehicles</span></div>
<div className="block"><p>Delivery <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#trucks"><code>trucks</code></a> that are permitted to enter the city proper
 to unload goods at businesses.</p></div>
</section>
</li>
<li>
<section className="detail" id="emergencyVehicles">
<h3>emergencyVehicles</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">emergencyVehicles</span></div>
<div className="block"><p>Any vehicle that is designated and authorized to respond to an emergency in a
 life-threatening situation.</p></div>
</section>
</li>
<li>
<section className="detail" id="motorcycles">
<h3>motorcycles</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">motorcycles</span></div>
<div className="block"><p>Motorized two-wheeled passenger vehicles. Generally, mopeds are considered
 motorcycles.</p></div>
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
<section className="detail" id="&lt;init&gt;(boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>LaneAccess</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">LaneAccess</span><wbr/><span className="parameters">(boolean automobiles,
 boolean buses,
 boolean taxis,
 boolean carpools,
 boolean pedestrians,
 boolean trucks,
 boolean throughTraffic,
 boolean deliveryVehicles,
 boolean emergencyVehicles,
 boolean motorcycles)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
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
<dd><code>deliveryVehicles</code> - <p>Delivery <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess#trucks"><code>trucks</code></a> that are permitted to enter the city proper
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
