---
title: "TransitRouteOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TransitRouteOptions.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.TransitRouteOptions</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TransitRouteOptions</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>All the options to specify how a public transit route should be calculated.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions#alternatives">alternatives</a></code></div>
<div className="col-last even-row-color">
<div className="block">Number of alternative routes to return aside from the optimal route.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions#arrivalTime">arrivalTime</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Optional time when travel is expected to end.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions#changes">changes</a></code></div>
<div className="col-last even-row-color">
<div className="block">Maximum number of changes or transfers allowed in a route.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions#departureTime">departureTime</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Optional time when travel is expected to start.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-transitmodefilter" title="enum class in com.here.sdk.routing">TransitModeFilter</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions#modeFilter">modeFilter</a></code></div>
<div className="col-last even-row-color">
<div className="block">Defines inclusion or exclusion of transit modes for route calculation.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-transitmode" title="enum class in com.here.sdk.routing">TransitMode</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions#modes">modes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">This list is used to determine which transit modes should be used for route calculation,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions#modeFilter"><code>modeFilter</code></a> specifies whether this list is an inclusion or an exclusion.</div>
</div>
<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions#pedestrianMaxDistanceInMeters">pedestrianMaxDistanceInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">Maximum allowed walking distance in meters (e.g.</div>
</div>
<div className="col-first odd-row-color"><code>double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions#pedestrianSpeedInMetersPerSecond">pedestrianSpeedInMetersPerSecond</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Walking speed in meters per second.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing">RouteTextOptions</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions#textOptions">textOptions</a></code></div>
<div className="col-last even-row-color">
<div className="block">Customize textual content returned from the route calculation, such
 as localization, format, and unit system.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions#%3Cinit%3E()">TransitRouteOptions</a>()</code></div>
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
<section className="detail" id="departureTime">
<h3>departureTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">departureTime</span></div>
<div className="block"><p>Optional time when travel is expected to start.
 If it is not specified, it is set to the current time.</p></div>
</section>
</li>
<li>
<section className="detail" id="arrivalTime">
<h3>arrivalTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">arrivalTime</span></div>
<div className="block"><p>Optional time when travel is expected to end.</p></div>
</section>
</li>
<li>
<section className="detail" id="alternatives">
<h3>alternatives</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">alternatives</span></div>
<div className="block"><p>Number of alternative routes to return aside from the optimal route.
 The provided value must be in the range [0, 6].
 By default, it is 0 and only one route is calculated.</p></div>
</section>
</li>
<li>
<section className="detail" id="changes">
<h3>changes</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">changes</span></div>
<div className="block"><p>Maximum number of changes or transfers allowed in a route.
 When it is not set, unlimited number of changes is permitted.
 The provided value must be in the range [0, 6].</p></div>
</section>
</li>
<li>
<section className="detail" id="modeFilter">
<h3>modeFilter</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-transitmodefilter" title="enum class in com.here.sdk.routing">TransitModeFilter</a></span> <span className="element-name">modeFilter</span></div>
<div className="block"><p>Defines inclusion or exclusion of transit modes for route calculation.
 By default, the inclusion mode is used.</p></div>
</section>
</li>
<li>
<section className="detail" id="modes">
<h3>modes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-transitmode" title="enum class in com.here.sdk.routing">TransitMode</a>&gt;</span> <span className="element-name">modes</span></div>
<div className="block"><p>This list is used to determine which transit modes should be used for route calculation,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions#modeFilter"><code>modeFilter</code></a> specifies whether this list is an inclusion or an exclusion.
 For example, specifying subway and bus transit modes with the include filter, returns only subway
 and bus transit modes, and with the exclude filter, returns all the transit modes except subway
 and bus. When not set, all the supported transit modes are permitted.
 By default, this list is empty.</p></div>
</section>
</li>
<li>
<section className="detail" id="pedestrianSpeedInMetersPerSecond">
<h3>pedestrianSpeedInMetersPerSecond</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">pedestrianSpeedInMetersPerSecond</span></div>
<div className="block"><p>Walking speed in meters per second. Influences the duration of walking segments from origin to a station,
 from a station to destination and in-between the stations (e.g. if transfer is needed).
 The provided value must be in the range [0.5, 2.0].
 The default value is 1.0 mps.</p></div>
</section>
</li>
<li>
<section className="detail" id="pedestrianMaxDistanceInMeters">
<h3>pedestrianMaxDistanceInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">pedestrianMaxDistanceInMeters</span></div>
<div className="block"><p>Maximum allowed walking distance in meters (e.g. when looking for nearest stations).
 The provided value must be in the range [0, 6000].
 The default value is 2000 meters.</p></div>
</section>
</li>
<li>
<section className="detail" id="textOptions">
<h3>textOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing">RouteTextOptions</a></span> <span className="element-name">textOptions</span></div>
<div className="block"><p>Customize textual content returned from the route calculation, such
 as localization, format, and unit system.</p></div>
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
<h3>TransitRouteOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TransitRouteOptions</span>()</div>
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
<li>
<section className="detail" id="fromDefaultParameterConfiguration()">
<h3>fromDefaultParameterConfiguration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions" title="class in com.here.sdk.routing">TransitRouteOptions</a></span> <span className="element-name">fromDefaultParameterConfiguration</span>()</div>
<div className="block"><p>Returns TransitRouteOptions instance with default values used in SDK.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>An <a href="sdk-for-android-navigate-com-here-sdk-routing-transitrouteoptions" title="class in com.here.sdk.routing"><code>TransitRouteOptions</code></a> instance with default values used in SDK.</p></dd>
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
