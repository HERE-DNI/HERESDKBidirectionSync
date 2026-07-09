---
title: "RouteOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-routeoptions"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RouteOptions.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.RouteOptions</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RouteOptions</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>The options to specify how the route will be calculated.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#alternatives">alternatives</a></code></div>
<div className="col-last even-row-color">
<div className="block">Maximum number of alternative routes that will be calculated, in addition
 to the best one.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#arrivalTime">arrivalTime</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Optional time when travel is expected to end.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#departureTime">departureTime</a></code></div>
<div className="col-last even-row-color">
<div className="block">Optional time when travel is expected to start.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#enableRouteHandle">enableRouteHandle</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A flag that indicates whether the resulting route should contain a <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#enableRouteLabels">enableRouteLabels</a></code></div>
<div className="col-last even-row-color">
<div className="block">Specifies whether route labels should be included in the route response.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#enableTolls">enableTolls</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A flag that indicates whether the resulting route <a href="sdk-for-android-navigate-section#getTolls()"><code>Section.getTolls()</code></a> properties should contain
 tolls data.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#optimizationMode">optimizationMode</a></code></div>
<div className="col-last even-row-color">
<div className="block">The optimization mode to be used for route calculation.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#optimizeWaypointsOrder">optimizeWaypointsOrder</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#speedCapInMetersPerSecond">speedCapInMetersPerSecond</a></code></div>
<div className="col-last even-row-color">
<div className="block">Specifies the maximum speed in meters per second, which the user wishes not to exceed.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode">trafficOptimizationMode</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The traffic optimization mode to be used for route calculation.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#%3Cinit%3E()">RouteOptions</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#%3Cinit%3E(com.here.sdk.routing.OptimizationMode)">RouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int)">RouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date)">RouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date)">RouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double)">RouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean)">RouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode)">RouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean)">RouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode,
 boolean enableTolls)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean,boolean)">RouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode,
 boolean enableTolls,
 boolean optimizeWaypointsOrder)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean,boolean,boolean)">RouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode,
 boolean enableTolls,
 boolean optimizeWaypointsOrder,
 boolean enableRouteLabels)</code></div>
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
<section className="detail" id="optimizationMode">
<h3>optimizationMode</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a></span> <span className="element-name">optimizationMode</span></div>
<div className="block"><p>The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="alternatives">
<h3>alternatives</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">alternatives</span></div>
<div className="block"><p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></div>
</section>
</li>
<li>
<section className="detail" id="departureTime">
<h3>departureTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">departureTime</span></div>
<div className="block"><p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="arrivalTime">
<h3>arrivalTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">arrivalTime</span></div>
<div className="block"><p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="speedCapInMetersPerSecond">
<h3>speedCapInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">speedCapInMetersPerSecond</span></div>
<div className="block"><p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></div>
</section>
</li>
<li>
<section className="detail" id="enableRouteHandle">
<h3>enableRouteHandle</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">enableRouteHandle</span></div>
<div className="block"><p>A flag that indicates whether the resulting route should contain a <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.
 Defaults to <code>false</code>.
 Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</p></div>
</section>
</li>
<li>
<section className="detail" id="trafficOptimizationMode">
<h3>trafficOptimizationMode</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a></span> <span className="element-name">trafficOptimizationMode</span></div>
<div className="block"><p>The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-trafficoptimizationmode#TIME_DEPENDENT"><code>TrafficOptimizationMode.TIME_DEPENDENT</code></a>, which enables traffic-aware routing.</p></div>
</section>
</li>
<li>
<section className="detail" id="enableTolls">
<h3>enableTolls</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">enableTolls</span></div>
<div className="block"><p>A flag that indicates whether the resulting route <a href="sdk-for-android-navigate-section#getTolls()"><code>Section.getTolls()</code></a> properties should contain
 tolls data. Defaults to <code>false</code>.
 <strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
 Consult your HERE representative to get more information on the related pricing schemes.
 <strong>Note:</strong> For users of the <code>OfflineRoutingEngine</code> this is a beta release of this feature,
 so there could be a few bugs and unexpected behaviors. The <code>OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code>RoutingEngine</code> the feature is stable.</p></div>
</section>
</li>
<li>
<section className="detail" id="optimizeWaypointsOrder">
<h3>optimizeWaypointsOrder</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">optimizeWaypointsOrder</span></div>
<div className="block"><p>A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
 The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing"><code>OptimizationMode</code></a>.
 The starting and destination <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing"><code>Waypoint</code></a> are not reordered.
 If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize).
 The resulting order of waypoints can be identified by their waypoint indices in the route sections
 (see <a href="sdk-for-android-navigate-route#getSections()"><code>Route.getSections()</code></a>, <a href="sdk-for-android-navigate-section#getDeparturePlace()"><code>Section.getDeparturePlace()</code></a>, <a href="sdk-for-android-navigate-section#getArrivalPlace()"><code>Section.getArrivalPlace()</code></a>, <a href="sdk-for-android-navigate-routeplace#waypointIndex"><code>RoutePlace.waypointIndex</code></a>).
 Currently, the waypoints order optimization is available only when using the <code>OfflineRoutingEngine</code> (only available for the Navigate license).
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="enableRouteLabels">
<h3>enableRouteLabels</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">enableRouteLabels</span></div>
<div className="block"><p>Specifies whether route labels should be included in the route response.
 Route labels identify major highways or road names along the route.
 By default, this is set to <code>false</code>.</p></div>
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
<h3>RouteOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteOptions</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode)">
<h3>RouteOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int)">
<h3>RouteOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date)">
<h3>RouteOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date)">
<h3>RouteOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double)">
<h3>RouteOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>speedCapInMetersPerSecond</code> - <p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean)">
<h3>RouteOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>speedCapInMetersPerSecond</code> - <p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></dd>
<dd><code>enableRouteHandle</code> - <p>A flag that indicates whether the resulting route should contain a <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.
 Defaults to <code>false</code>.
 Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode)">
<h3>RouteOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>speedCapInMetersPerSecond</code> - <p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></dd>
<dd><code>enableRouteHandle</code> - <p>A flag that indicates whether the resulting route should contain a <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.
 Defaults to <code>false</code>.
 Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</p></dd>
<dd><code>trafficOptimizationMode</code> - <p>The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-trafficoptimizationmode#TIME_DEPENDENT"><code>TrafficOptimizationMode.TIME_DEPENDENT</code></a>, which enables traffic-aware routing.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean)">
<h3>RouteOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode,
 boolean enableTolls)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>speedCapInMetersPerSecond</code> - <p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></dd>
<dd><code>enableRouteHandle</code> - <p>A flag that indicates whether the resulting route should contain a <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.
 Defaults to <code>false</code>.
 Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</p></dd>
<dd><code>trafficOptimizationMode</code> - <p>The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-trafficoptimizationmode#TIME_DEPENDENT"><code>TrafficOptimizationMode.TIME_DEPENDENT</code></a>, which enables traffic-aware routing.</p></dd>
<dd><code>enableTolls</code> - <p>A flag that indicates whether the resulting route <a href="sdk-for-android-navigate-section#getTolls()"><code>Section.getTolls()</code></a> properties should contain
 tolls data. Defaults to <code>false</code>.
 <strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
 Consult your HERE representative to get more information on the related pricing schemes.
 <strong>Note:</strong> For users of the <code>OfflineRoutingEngine</code> this is a beta release of this feature,
 so there could be a few bugs and unexpected behaviors. The <code>OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code>RoutingEngine</code> the feature is stable.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean,boolean)">
<h3>RouteOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode,
 boolean enableTolls,
 boolean optimizeWaypointsOrder)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>speedCapInMetersPerSecond</code> - <p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></dd>
<dd><code>enableRouteHandle</code> - <p>A flag that indicates whether the resulting route should contain a <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.
 Defaults to <code>false</code>.
 Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</p></dd>
<dd><code>trafficOptimizationMode</code> - <p>The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-trafficoptimizationmode#TIME_DEPENDENT"><code>TrafficOptimizationMode.TIME_DEPENDENT</code></a>, which enables traffic-aware routing.</p></dd>
<dd><code>enableTolls</code> - <p>A flag that indicates whether the resulting route <a href="sdk-for-android-navigate-section#getTolls()"><code>Section.getTolls()</code></a> properties should contain
 tolls data. Defaults to <code>false</code>.
 <strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
 Consult your HERE representative to get more information on the related pricing schemes.
 <strong>Note:</strong> For users of the <code>OfflineRoutingEngine</code> this is a beta release of this feature,
 so there could be a few bugs and unexpected behaviors. The <code>OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code>RoutingEngine</code> the feature is stable.</p></dd>
<dd><code>optimizeWaypointsOrder</code> - <p>A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
 The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing"><code>OptimizationMode</code></a>.
 The starting and destination <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing"><code>Waypoint</code></a> are not reordered.
 If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize).
 The resulting order of waypoints can be identified by their waypoint indices in the route sections
 (see <a href="sdk-for-android-navigate-route#getSections()"><code>Route.getSections()</code></a>, <a href="sdk-for-android-navigate-section#getDeparturePlace()"><code>Section.getDeparturePlace()</code></a>, <a href="sdk-for-android-navigate-section#getArrivalPlace()"><code>Section.getArrivalPlace()</code></a>, <a href="sdk-for-android-navigate-routeplace#waypointIndex"><code>RoutePlace.waypointIndex</code></a>).
 Currently, the waypoints order optimization is available only when using the <code>OfflineRoutingEngine</code> (only available for the Navigate license).
 Defaults to <code>false</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean,boolean,boolean)">
<h3>RouteOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode,
 boolean enableTolls,
 boolean optimizeWaypointsOrder,
 boolean enableRouteLabels)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 <strong>Note</strong>:
 <ul>
<li>Both <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>speedCapInMetersPerSecond</code> - <p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></dd>
<dd><code>enableRouteHandle</code> - <p>A flag that indicates whether the resulting route should contain a <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.
 Defaults to <code>false</code>.
 Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</p></dd>
<dd><code>trafficOptimizationMode</code> - <p>The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-navigate-trafficoptimizationmode#TIME_DEPENDENT"><code>TrafficOptimizationMode.TIME_DEPENDENT</code></a>, which enables traffic-aware routing.</p></dd>
<dd><code>enableTolls</code> - <p>A flag that indicates whether the resulting route <a href="sdk-for-android-navigate-section#getTolls()"><code>Section.getTolls()</code></a> properties should contain
 tolls data. Defaults to <code>false</code>.
 <strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
 Consult your HERE representative to get more information on the related pricing schemes.
 <strong>Note:</strong> For users of the <code>OfflineRoutingEngine</code> this is a beta release of this feature,
 so there could be a few bugs and unexpected behaviors. The <code>OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code>RoutingEngine</code> the feature is stable.</p></dd>
<dd><code>optimizeWaypointsOrder</code> - <p>A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
 The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing"><code>OptimizationMode</code></a>.
 The starting and destination <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing"><code>Waypoint</code></a> are not reordered.
 If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize).
 The resulting order of waypoints can be identified by their waypoint indices in the route sections
 (see <a href="sdk-for-android-navigate-route#getSections()"><code>Route.getSections()</code></a>, <a href="sdk-for-android-navigate-section#getDeparturePlace()"><code>Section.getDeparturePlace()</code></a>, <a href="sdk-for-android-navigate-section#getArrivalPlace()"><code>Section.getArrivalPlace()</code></a>, <a href="sdk-for-android-navigate-routeplace#waypointIndex"><code>RoutePlace.waypointIndex</code></a>).
 Currently, the waypoints order optimization is available only when using the <code>OfflineRoutingEngine</code> (only available for the Navigate license).
 Defaults to <code>false</code>.</p></dd>
<dd><code>enableRouteLabels</code> - <p>Specifies whether route labels should be included in the route response.
 Route labels identify major highways or road names along the route.
 By default, this is set to <code>false</code>.</p></dd>
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
