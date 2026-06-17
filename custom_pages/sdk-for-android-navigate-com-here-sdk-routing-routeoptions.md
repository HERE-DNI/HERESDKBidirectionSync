---
title: "RouteOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-routeoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RouteOptions.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.RouteOptions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RouteOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>The options to specify how the route will be calculated.</p></div>
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
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#alternatives">alternatives</a></code></div>
<div class="col-last even-row-color">
<div class="block">Maximum number of alternative routes that will be calculated, in addition
 to the best one.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#arrivalTime">arrivalTime</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional time when travel is expected to end.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#departureTime">departureTime</a></code></div>
<div class="col-last even-row-color">
<div class="block">Optional time when travel is expected to start.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#enableRouteHandle">enableRouteHandle</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A flag that indicates whether the resulting route should contain a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#enableRouteLabels">enableRouteLabels</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies whether route labels should be included in the route response.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#enableTolls">enableTolls</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A flag that indicates whether the resulting route <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-section#getTolls()"><code>Section.getTolls()</code></a> properties should contain
 tolls data.</div>
</div>
<div class="col-first even-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#optimizationMode">optimizationMode</a></code></div>
<div class="col-last even-row-color">
<div class="block">The optimization mode to be used for route calculation.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#optimizeWaypointsOrder">optimizeWaypointsOrder</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#speedCapInMetersPerSecond">speedCapInMetersPerSecond</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies the maximum speed in meters per second, which the user wishes not to exceed.</div>
</div>
<div class="col-first odd-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode">trafficOptimizationMode</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The traffic optimization mode to be used for route calculation.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E()">RouteOptions</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.routing.OptimizationMode)">RouteOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int)">RouteOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date)">RouteOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date)">RouteOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double)">RouteOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean)">RouteOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode)">RouteOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean)">RouteOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode,
 boolean enableTolls)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean,boolean)">RouteOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode,
 boolean enableTolls,
 boolean optimizeWaypointsOrder)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean,boolean,boolean)">RouteOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode,
 boolean enableTolls,
 boolean optimizeWaypointsOrder,
 boolean enableRouteLabels)</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>
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
<section class="detail" id="optimizationMode">
<h3>optimizationMode</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a></span> <span class="element-name">optimizationMode</span></div>
<div class="block"><p>The optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="alternatives">
<h3>alternatives</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">alternatives</span></div>
<div class="block"><p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></div>
</section>
</li>
<li>
<section class="detail" id="departureTime">
<h3>departureTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">departureTime</span></div>
<div class="block"><p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="arrivalTime">
<h3>arrivalTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">arrivalTime</span></div>
<div class="block"><p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="speedCapInMetersPerSecond">
<h3>speedCapInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">speedCapInMetersPerSecond</span></div>
<div class="block"><p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></div>
</section>
</li>
<li>
<section class="detail" id="enableRouteHandle">
<h3>enableRouteHandle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableRouteHandle</span></div>
<div class="block"><p>A flag that indicates whether the resulting route should contain a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.
 Defaults to <code>false</code>.
 Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</p></div>
</section>
</li>
<li>
<section class="detail" id="trafficOptimizationMode">
<h3>trafficOptimizationMode</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a></span> <span class="element-name">trafficOptimizationMode</span></div>
<div class="block"><p>The traffic optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode#TIME_DEPENDENT"><code>TrafficOptimizationMode.TIME_DEPENDENT</code></a>, which enables traffic-aware routing.</p></div>
</section>
</li>
<li>
<section class="detail" id="enableTolls">
<h3>enableTolls</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableTolls</span></div>
<div class="block"><p>A flag that indicates whether the resulting route <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-section#getTolls()"><code>Section.getTolls()</code></a> properties should contain
 tolls data. Defaults to <code>false</code>.
 </p><p><strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
 Consult your HERE representative to get more information on the related pricing schemes.
 </p><p><strong>Note:</strong> For users of the <code>OfflineRoutingEngine</code> this is a beta release of this feature,
 so there could be a few bugs and unexpected behaviors. The <code>OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code>RoutingEngine</code> the feature is stable.</p></div>
</section>
</li>
<li>
<section class="detail" id="optimizeWaypointsOrder">
<h3>optimizeWaypointsOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">optimizeWaypointsOrder</span></div>
<div class="block"><p>A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
 The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-e-g-optimizationmode" title="enum class in com.here.sdk.routing"><code>OptimizationMode</code></a>.
 The starting and destination <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing"><code>Waypoint</code></a> are not reordered.
 If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize).
 The resulting order of waypoints can be identified by their waypoint indices in the route sections
 (see <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route#getSections()"><code>Route.getSections()</code></a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-section#getDeparturePlace()"><code>Section.getDeparturePlace()</code></a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-section#getArrivalPlace()"><code>Section.getArrivalPlace()</code></a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routeplace#waypointIndex"><code>RoutePlace.waypointIndex</code></a>).
 Currently, the waypoints order optimization is available only when using the <code>OfflineRoutingEngine</code> (only available for the Navigate license).
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="enableRouteLabels">
<h3>enableRouteLabels</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableRouteLabels</span></div>
<div class="block"><p>Specifies whether route labels should be included in the route response.
 Route labels identify major highways or road names along the route.
 By default, this is set to <code>false</code>.</p></div>
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
<h3>RouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RouteOptions</span>()</div>
<div class="block"><p>Creates a new instance.</p></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode)">
<h3>RouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int)">
<h3>RouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date)">
<h3>RouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date)">
<h3>RouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double)">
<h3>RouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>speedCapInMetersPerSecond</code> - <p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean)">
<h3>RouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>speedCapInMetersPerSecond</code> - <p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></dd>
<dd><code>enableRouteHandle</code> - <p>A flag that indicates whether the resulting route should contain a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.
 Defaults to <code>false</code>.
 Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode)">
<h3>RouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>speedCapInMetersPerSecond</code> - <p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></dd>
<dd><code>enableRouteHandle</code> - <p>A flag that indicates whether the resulting route should contain a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.
 Defaults to <code>false</code>.
 Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</p></dd>
<dd><code>trafficOptimizationMode</code> - <p>The traffic optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode#TIME_DEPENDENT"><code>TrafficOptimizationMode.TIME_DEPENDENT</code></a>, which enables traffic-aware routing.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean)">
<h3>RouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode,
 boolean enableTolls)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>speedCapInMetersPerSecond</code> - <p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></dd>
<dd><code>enableRouteHandle</code> - <p>A flag that indicates whether the resulting route should contain a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.
 Defaults to <code>false</code>.
 Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</p></dd>
<dd><code>trafficOptimizationMode</code> - <p>The traffic optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode#TIME_DEPENDENT"><code>TrafficOptimizationMode.TIME_DEPENDENT</code></a>, which enables traffic-aware routing.</p></dd>
<dd><code>enableTolls</code> - <p>A flag that indicates whether the resulting route <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-section#getTolls()"><code>Section.getTolls()</code></a> properties should contain
 tolls data. Defaults to <code>false</code>.
 </p><p><strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
 Consult your HERE representative to get more information on the related pricing schemes.
 </p><p><strong>Note:</strong> For users of the <code>OfflineRoutingEngine</code> this is a beta release of this feature,
 so there could be a few bugs and unexpected behaviors. The <code>OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code>RoutingEngine</code> the feature is stable.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean,boolean)">
<h3>RouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode,
 boolean enableTolls,
 boolean optimizeWaypointsOrder)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>speedCapInMetersPerSecond</code> - <p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></dd>
<dd><code>enableRouteHandle</code> - <p>A flag that indicates whether the resulting route should contain a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.
 Defaults to <code>false</code>.
 Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</p></dd>
<dd><code>trafficOptimizationMode</code> - <p>The traffic optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode#TIME_DEPENDENT"><code>TrafficOptimizationMode.TIME_DEPENDENT</code></a>, which enables traffic-aware routing.</p></dd>
<dd><code>enableTolls</code> - <p>A flag that indicates whether the resulting route <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-section#getTolls()"><code>Section.getTolls()</code></a> properties should contain
 tolls data. Defaults to <code>false</code>.
 </p><p><strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
 Consult your HERE representative to get more information on the related pricing schemes.
 </p><p><strong>Note:</strong> For users of the <code>OfflineRoutingEngine</code> this is a beta release of this feature,
 so there could be a few bugs and unexpected behaviors. The <code>OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code>RoutingEngine</code> the feature is stable.</p></dd>
<dd><code>optimizeWaypointsOrder</code> - <p>A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
 The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-e-g-optimizationmode" title="enum class in com.here.sdk.routing"><code>OptimizationMode</code></a>.
 The starting and destination <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing"><code>Waypoint</code></a> are not reordered.
 If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize).
 The resulting order of waypoints can be identified by their waypoint indices in the route sections
 (see <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route#getSections()"><code>Route.getSections()</code></a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-section#getDeparturePlace()"><code>Section.getDeparturePlace()</code></a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-section#getArrivalPlace()"><code>Section.getArrivalPlace()</code></a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routeplace#waypointIndex"><code>RoutePlace.waypointIndex</code></a>).
 Currently, the waypoints order optimization is available only when using the <code>OfflineRoutingEngine</code> (only available for the Navigate license).
 Defaults to <code>false</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean,boolean,boolean)">
<h3>RouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode,
 int alternatives,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> departureTime,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> arrivalTime,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond,
 boolean enableRouteHandle,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode,
 boolean enableTolls,
 boolean optimizeWaypointsOrder,
 boolean enableRouteLabels)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optimizationMode</code> - <p>The optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>.</p></dd>
<dd><code>alternatives</code> - <p>Maximum number of alternative routes that will be calculated, in addition
 to the best one. The provided value must be in the range [0, 6].
 Alternative routes can be unavailable, thus they are not guaranteed to be returned.
 The order of routes is from the best to the worst, as evaluated by the route calculation
 algorithm and according to the given input parameters.
 Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
 Must be 0 for isoline calculation.</p></dd>
<dd><code>departureTime</code> - <p>Optional time when travel is expected to start. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, i.e. now.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both departure time and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#arrivalTime"><code>arrivalTime</code></a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>arrivalTime</code> - <p>Optional time when travel is expected to end. Traffic speed and
 incidents shall be taken into account in the calculation of the route, per <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#trafficOptimizationMode"><code>trafficOptimizationMode</code></a>.
 By default, the time is not set.
 If the time is not set, the current time will be used internally, to predict the arrival time.
 Therefore, by default, a time-aware route request is initiated including traffic.
 </p><p><strong>Note</strong>:
 <ul>
<li>Both <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#departureTime"><code>departureTime</code></a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
 when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul></p></dd>
<dd><code>speedCapInMetersPerSecond</code> - <p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
 The valid range is [1, 70] meters per second. Note that it is valid only for <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a> and <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-transportmode#SCOOTER"><code>TransportMode.SCOOTER</code></a> transport modes.
 For car, truck and scooter transport modes, it will affect <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a> of
 the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
 which means that no speed cap is set.</p></dd>
<dd><code>enableRouteHandle</code> - <p>A flag that indicates whether the resulting route should contain a <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.
 Defaults to <code>false</code>.
 Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</p></dd>
<dd><code>trafficOptimizationMode</code> - <p>The traffic optimization mode to be used for route calculation. By default, it is <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficoptimizationmode#TIME_DEPENDENT"><code>TrafficOptimizationMode.TIME_DEPENDENT</code></a>, which enables traffic-aware routing.</p></dd>
<dd><code>enableTolls</code> - <p>A flag that indicates whether the resulting route <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-section#getTolls()"><code>Section.getTolls()</code></a> properties should contain
 tolls data. Defaults to <code>false</code>.
 </p><p><strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
 Consult your HERE representative to get more information on the related pricing schemes.
 </p><p><strong>Note:</strong> For users of the <code>OfflineRoutingEngine</code> this is a beta release of this feature,
 so there could be a few bugs and unexpected behaviors. The <code>OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code>RoutingEngine</code> the feature is stable.</p></dd>
<dd><code>optimizeWaypointsOrder</code> - <p>A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
 The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-e-g-optimizationmode" title="enum class in com.here.sdk.routing"><code>OptimizationMode</code></a>.
 The starting and destination <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing"><code>Waypoint</code></a> are not reordered.
 If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize).
 The resulting order of waypoints can be identified by their waypoint indices in the route sections
 (see <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route#getSections()"><code>Route.getSections()</code></a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-section#getDeparturePlace()"><code>Section.getDeparturePlace()</code></a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-section#getArrivalPlace()"><code>Section.getArrivalPlace()</code></a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routeplace#waypointIndex"><code>RoutePlace.waypointIndex</code></a>).
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
